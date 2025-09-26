#!/usr/bin/env python3
"""
NEUROMANCER Social Media Monitor
Monitors social platforms for relevant content and sends intelligent alerts via Discord
"""

import os
import sys
import json
import time
import requests
import feedparser
from datetime import datetime, timedelta
from pathlib import Path
import hashlib
import re
from typing import Dict, List, Optional, Tuple
import ollama
import yaml
import logging
from logging.handlers import RotatingFileHandler
from bs4 import BeautifulSoup

# Configuration
CONFIG_FILE = Path(__file__).parent / "social_monitor_config.yaml"
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
OLLAMA_MODEL = "qwen2.5:1.5b-instruct"
FALLBACK_DEEP_MODEL = os.getenv('OLLAMA_DEEP_MODEL', 'qwen3:4b')

# Default configuration
DEFAULT_CONFIG = {
    "monitoring": {
        "hacker_news": {
            "enabled": True,
            "api_url": "https://hn.algolia.com/api/v1/search_by_date",
            "query": "computational neuroscience OR brain imaging OR EEG OR BCI OR machine learning OR AI agents",
            "min_score": 10,
            "check_interval": 300  # 5 minutes
        },
        "reddit": {
            "enabled": True,
            "subreddits": [
                "MachineLearning",
                "computational_neuroscience", 
                "BCI",
                "neurotech",
                "artificial",
                "LocalLLaMA",
                "selfhosted",
                "privacy"
            ],
            "min_score": 5,
            "check_interval": 600  # 10 minutes
        },
        "github_trending": {
            "enabled": True,
            "languages": ["python", "javascript", "go", "rust"],
            "check_interval": 1800  # 30 minutes
        }
    },
    "alerting": {
        "discord_webhook": DISCORD_WEBHOOK,
        "min_relevance_score": 0.7,
        "max_alerts_per_hour": 3,
        "cooldown_minutes": 30
    },
    "bias_detection": {
        "enabled": True,
        "check_sentiment": True,
        "neutralize_language": True,
        "fact_check_claims": True
    }
}

class SocialMonitor:
    def __init__(self):
        self.config = self.load_config()
        self.processed_items = self.load_processed_items()
        self.alert_history = self.load_alert_history()
        self.setup_logging()
        
        # Load discord webhook from environment
        webhook_url = os.getenv('DISCORD_WEBHOOK_URL')
        if webhook_url:
            self.config['alerting']['discord_webhook'] = webhook_url
            self.logger.info(f"Discord webhook loaded: {webhook_url[:50]}...")
        else:
            self.logger.warning("No DISCORD_WEBHOOK_URL environment variable set")

    def to_second_person_and_cap(self, text: str, max_words: int) -> str:
        """Convert first/third person mentions to second person and cap to max words."""
        if not text:
            return text
        # Normalize whitespace
        cleaned = re.sub(r"\s+", " ", text).strip()
        # Replace common name refs -> you
        replacements = [
            (r"\b[Ii]an\b", "you"),
            (r"\b[Ii]an's\b", "your"),
            (r"\bthe user's\b", "your"),
            (r"\bthe user\b", "you"),
            (r"\btheir interests\b", "your interests"),
            (r"\bhis interests\b", "your interests"),
            (r"\bher interests\b", "your interests"),
            (r"\buser's interests\b", "your interests"),
            (r"\byou’s\b", "your"),
        ]
        for pattern, repl in replacements:
            cleaned = re.sub(pattern, repl, cleaned)
        # Cap words
        words = cleaned.split()
        if len(words) > max_words:
            cleaned = " ".join(words[:max_words]) + "…"
        return cleaned
        
    def setup_logging(self):
        """Setup logging with rotation to prevent log files from growing too large"""
        log_file = Path(__file__).parent / "neuromancer_social_monitor.log"
        
        # Create logger
        self.logger = logging.getLogger('neuromancer_social')
        self.logger.setLevel(logging.DEBUG)  # Enable debug logging
        
        # Remove existing handlers to avoid duplicates
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # Create rotating file handler (max 5MB, keep 3 files)
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=5*1024*1024,  # 5MB
            backupCount=3
        )
        file_handler.setLevel(logging.DEBUG)
        
        # Create console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Keep console at INFO level
        
        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def load_config(self) -> Dict:
        """Load configuration from file or create default"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                return yaml.safe_load(f)
        else:
            # Create default config file
            with open(CONFIG_FILE, 'w') as f:
                yaml.dump(DEFAULT_CONFIG, f, default_flow_style=False)
            return DEFAULT_CONFIG
    
    def load_processed_items(self) -> set:
        """Load set of already processed items to avoid duplicates"""
        processed_file = Path(__file__).parent / "processed_social_items.json"
        if processed_file.exists():
            with open(processed_file, 'r') as f:
                data = json.load(f)
                return set(data.get('processed_ids', []))
        return set()
    
    def save_processed_items(self):
        """Save processed items to avoid duplicates"""
        processed_file = Path(__file__).parent / "processed_social_items.json"
        data = {
            'processed_ids': list(self.processed_items),
            'last_updated': datetime.now().isoformat()
        }
        with open(processed_file, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_alert_history(self) -> List[Dict]:
        """Load alert history to respect rate limits"""
        history_file = Path(__file__).parent / "alert_history.json"
        if history_file.exists():
            with open(history_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_alert_history(self):
        """Save alert history"""
        history_file = Path(__file__).parent / "alert_history.json"
        # Keep only last 24 hours
        cutoff = datetime.now() - timedelta(hours=24)
        recent_alerts = [
            alert for alert in self.alert_history 
            if datetime.fromisoformat(alert['timestamp']) > cutoff
        ]
        with open(history_file, 'w') as f:
            json.dump(recent_alerts, f, indent=2)
    
    def can_send_alert(self) -> bool:
        """Check if we can send an alert based on rate limits"""
        if not self.config['alerting']['discord_webhook']:
            self.logger.debug("No discord webhook configured")
            return False
        
        # Check hourly limit
        hour_ago = datetime.now() - timedelta(hours=1)
        recent_alerts = [
            alert for alert in self.alert_history
            if datetime.fromisoformat(alert['timestamp']) > hour_ago
        ]
        
        self.logger.debug(f"Recent alerts in last hour: {len(recent_alerts)}/{self.config['alerting']['max_alerts_per_hour']}")
        
        if len(recent_alerts) >= self.config['alerting']['max_alerts_per_hour']:
            self.logger.debug("Hourly rate limit reached")
            return False
        
        # Check cooldown
        if recent_alerts:
            last_alert = max(recent_alerts, key=lambda x: x['timestamp'])
            last_alert_time = datetime.fromisoformat(last_alert['timestamp'])
            cooldown = timedelta(minutes=self.config['alerting']['cooldown_minutes'])
            if datetime.now() - last_alert_time < cooldown:
                self.logger.debug(f"Cooldown not met: {datetime.now() - last_alert_time} < {cooldown}")
                return False
        
        self.logger.debug("Alert allowed")
        return True
    
    def get_hacker_news_items(self) -> List[Dict]:
        """Fetch relevant items from Hacker News using iterative deepening"""
        if not self.config['monitoring']['hacker_news']['enabled']:
            return []
        
        try:
            # Iterative deepening: start broad, then narrow down
            query_levels = [
                # Level 1: Broad topics (high volume, lower precision)
                {
                    'queries': ["machine learning", "AI artificial intelligence", "python programming"],
                    'hits_per_page': 15,
                    'min_score': 5
                },
                # Level 2: More specific (medium volume, higher precision)  
                {
                    'queries': ["neuroscience brain", "BCI brain computer", "EEG analysis", "computational neuroscience"],
                    'hits_per_page': 10,
                    'min_score': 8
                },
                # Level 3: Very specific (low volume, highest precision)
                {
                    'queries': ["motor imagery", "brain imaging", "privacy preserving", "local AI", "self-hosted"],
                    'hits_per_page': 5,
                    'min_score': 10
                }
            ]
            
            all_items = []
            seen_ids = set()
            
            for level_idx, level in enumerate(query_levels):
                self.logger.info(f"HN Level {level_idx + 1}: {len(level['queries'])} queries, min_score={level['min_score']}")
                
                for query in level['queries']:
                    # Rate limiting: small delay between requests
                    time.sleep(0.5)
                    
                    params = {
                        'query': query,
                        'tags': 'story',
                        'hitsPerPage': level['hits_per_page'],
                        'numericFilters': f'points>{level["min_score"]}'
                    }
                    
                    try:
                        response = requests.get(
                            self.config['monitoring']['hacker_news']['api_url'],
                            params=params,
                            timeout=10
                        )
                        response.raise_for_status()
                        
                        data = response.json()
                        hits = data.get('hits', [])
                        
                        self.logger.debug(f"Query '{query}': {len(hits)} hits")
                        
                        for hit in hits:
                            item_id = str(hit.get('objectID', ''))
                            if item_id not in seen_ids and item_id not in self.processed_items:
                                seen_ids.add(item_id)
                                all_items.append({
                                    'id': item_id,
                                    'title': hit.get('title', ''),
                                    'url': hit.get('url', f"https://news.ycombinator.com/item?id={item_id}"),
                                    'score': hit.get('points', 0),
                                    'comments': hit.get('num_comments', 0),
                                    'created_at': hit.get('created_at', ''),
                                    'source': 'hacker_news',
                                    'query_level': level_idx + 1,
                                    'query_used': query
                                })
                        
                    except Exception as e:
                        self.logger.warning(f"Error with query '{query}': {e}")
                        continue
                
                # If we found enough items at this level, we can stop early
                if len(all_items) >= 20:
                    self.logger.info(f"Found {len(all_items)} items, stopping at level {level_idx + 1}")
                    break
            
            self.logger.info(f"Hacker News: found {len(all_items)} items using iterative deepening")
            return all_items
            
        except Exception as e:
            self.logger.error(f"Error fetching Hacker News: {e}")
            return []
    
    def get_reddit_items(self) -> List[Dict]:
        """Fetch relevant items from Reddit"""
        if not self.config['monitoring']['reddit']['enabled']:
            return []
        
        # Keywords to filter out (weekly mod posts, etc.)
        filter_keywords = [
            'self-promotion thread',
            '[d] self-promotion thread',  # reddit format
            'weekly discussion',
            'monthly discussion', 
            'daily discussion',
            'ask anything',
            'simple questions',
            'career advice',
            'what should i learn',
            'beginner question',
            'help me choose',
            'which framework',
            'moderator announcement',
            'subreddit rules',
            'community guidelines',
            'share your',
            'promotion thread',
            'weekly thread',
            'monthly thread'
        ]
        
        items = []
        for subreddit in self.config['monitoring']['reddit']['subreddits']:
            try:
                # Use Reddit RSS feed (no API key required)
                rss_url = f"https://www.reddit.com/r/{subreddit}/hot.rss"
                feed = feedparser.parse(rss_url)
                
                for entry in feed.entries[:10]:  # Top 10 from each subreddit
                    # Extract post ID from link
                    post_id = entry.link.split('/')[-1] if '/' in entry.link else entry.link
                    if post_id not in self.processed_items:
                        title = entry.title
                        
                        # Filter out weekly/mod posts (more robust matching)
                        title_lower = title.lower()
                        if any(keyword in title_lower for keyword in filter_keywords):
                            self.logger.debug(f"Filtered out reddit post: {title}")
                            continue
                        
                        # Additional pattern matching for reddit-specific formats
                        if (title_lower.startswith('[d]') and 'promotion' in title_lower) or \
                           (title_lower.startswith('[w]') and 'discussion' in title_lower) or \
                           (title_lower.startswith('[m]') and 'discussion' in title_lower):
                            self.logger.debug(f"Filtered out reddit mod post: {title}")
                            continue
                        
                        items.append({
                            'id': f"reddit_{post_id}",
                            'title': title,
                            'url': entry.link,
                            'subreddit': subreddit,
                            'created_at': entry.get('published', ''),
                            'source': 'reddit'
                        })
                
            except Exception as e:
                self.logger.error(f"Error fetching Reddit r/{subreddit}: {e}")
                continue
        
        self.logger.info(f"Reddit: found {len(items)} items after filtering")
        return items

    def enrich_with_context(self, item: Dict) -> Dict:
        """Fetch article HTML and, if HN, comment text for deeper summary."""
        enriched = dict(item)
        texts: List[str] = []
        try:
            resp = requests.get(item['url'], timeout=15, headers={'User-Agent': 'NEUROMANCER/1.0'})
            if resp.ok:
                soup = BeautifulSoup(resp.text, 'html.parser')
                for tag in soup(['script', 'style', 'noscript']):
                    tag.decompose()
                article_text = ' '.join(t.get_text(' ', strip=True) for t in soup.find_all(['h1','h2','p','li']))
                if article_text:
                    texts.append(article_text[:8000])
        except Exception:
            pass

        if item.get('source') == 'hacker_news' and item.get('id'):
            try:
                r = requests.get(f"https://hn.algolia.com/api/v1/items/{item['id']}", timeout=15)
                if r.ok:
                    data = r.json()
                    def gather(children):
                        out = []
                        for ch in children or []:
                            txt = ch.get('text') or ''
                            if txt:
                                out.append(BeautifulSoup(txt, 'html.parser').get_text(' ', strip=True))
                            out.extend(gather(ch.get('children')))
                        return out
                    comments = gather(data.get('children'))
                    if comments:
                        texts.append(' '.join(comments)[:6000])
            except Exception:
                pass

        enriched['context_text'] = '\n\n'.join(texts)[:10000]
        return enriched

    def second_pass_summary(self, item: Dict) -> str:
        """Use a stronger/smarter model to summarize with context in 100 words, 2nd person."""
        context = item.get('context_text', '')
        if not context:
            return ''
        max_words = int(self.config.get('alerting', {}).get('summary_max_words', 100))
        prompt = (
            "You are Neuromancer. Summarize why this matters to the user in at most "
            f"{max_words} words, second person, casual, friendly, geeky. Focus on: "
            "AI agents, local-first/self-hosting, ML, neuroscience/EEG/BCI when relevant.\n\n"
            f"TITLE: {item.get('title','')}\nURL: {item.get('url','')}\n\nCONTENT:\n{context}\n\n"
            "Return only the summary."
        )
        try:
            resp = ollama.generate(model=FALLBACK_DEEP_MODEL, prompt=prompt, options={'temperature': 0.3, 'max_tokens': 256})
            text = resp.get('response', '').strip()
            return self.to_second_person_and_cap(text, max_words)
        except Exception:
            try:
                resp = ollama.generate(model=OLLAMA_MODEL, prompt=prompt, options={'temperature': 0.3, 'max_tokens': 256})
                text = resp.get('response', '').strip()
                return self.to_second_person_and_cap(text, max_words)
            except Exception:
                return ''
    
    def get_github_trending(self) -> List[Dict]:
        """Fetch trending repositories from GitHub using GitHub API"""
        if not self.config['monitoring']['github_trending']['enabled']:
            return []
        
        items = []
        
        # Use GitHub's search API to find trending repos
        try:
            # Search for recently created repos with good star counts
            for language in self.config['monitoring']['github_trending']['languages']:
                params = {
                    'q': f'language:{language} created:>2025-09-20 stars:>10',
                    'sort': 'stars',
                    'order': 'desc',
                    'per_page': 10
                }
                
                # Use GitHub's search API (no auth required for public repos)
                response = requests.get(
                    'https://api.github.com/search/repositories',
                    params=params,
                    timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    
                    for repo in data.get('items', []):
                        repo_id = str(repo['id'])
                        if repo_id not in self.processed_items:
                            items.append({
                                'id': f"github_{repo_id}",
                                'title': f"{repo['name']}: {repo['description'] or 'No description'}",
                                'url': repo['html_url'],
                                'language': language,
                                'stars': repo['stargazers_count'],
                                'created_at': repo['created_at'],
                                'source': 'github'
                            })
                else:
                    self.logger.warning(f"GitHub API error for {language}: {response.status_code}")
                    
        except Exception as e:
            self.logger.error(f"Error fetching GitHub trending: {e}")
        
        self.logger.info(f"GitHub: found {len(items)} trending repositories")
        return items
    
    def analyze_relevance(self, item: Dict) -> Tuple[float, str]:
        """Analyze item relevance using AI with source penalties"""
        try:
            # Source penalties (reddit gets penalized, github gets slight boost)
            source_penalties = {
                'reddit': 0.75,       # 25% penalty for reddit
                'hacker_news': 0.95,  # slight downweight unless strongly aligned
                'github': 1.10,       # 10% boost for github repos
                'arxiv': 1.12,        # 12% boost for arXiv papers
                'default': 1.0
            }
            
            source_penalty = source_penalties.get(item['source'], source_penalties['default'])
            
            # Create analysis prompt
            prompt = f"""analyze this item for relevance to ian's interests. be strict and conservative; only give high scores if it clearly advances his core areas:

title: {item['title']}
url: {item['url']}
source: {item['source']}

ian's key interests:
- computational neuroscience and BCI research
- local-first AI systems and privacy
- machine learning and AI agents
- research-to-practice methodology
- self-hosted tools and data ownership
- brain imaging and EEG analysis

rate relevance from 0.0 to 1.0 and provide a brief explanation.
respond in format: SCORE: X.X | REASON: brief explanation. keep under 2 sentences.

be unbiased and factual. focus on technical merit and practical value. penalize newsy/meta hype.
consider that {item['source']} content may vary in quality."""
            
            response = ollama.generate(
                model=OLLAMA_MODEL,
                prompt=prompt,
                options={'temperature': 0.3, 'max_tokens': 200}
            )
            
            result = response['response'].strip()
            
            # Parse score and reason
            score_match = re.search(r'SCORE:\s*(\d+\.?\d*)', result)
            reason_match = re.search(r'REASON:\s*(.+)', result)
            
            base_score = float(score_match.group(1)) if score_match else 0.0
            reason = reason_match.group(1).strip() if reason_match else "No reason provided"
            
            # Apply source penalty/boost
            adjusted_score = min(1.0, base_score * source_penalty)
            
            # Add source context to reason
            if source_penalty != 1.0:
                if source_penalty < 1.0:
                    reason += f" (adjusted for {item['source']} source quality)"
                else:
                    reason += f" (boosted for {item['source']} source quality)"
            
            return adjusted_score, reason
            
        except Exception as e:
            self.logger.error(f"Error analyzing relevance: {e}")
            return 0.0, "Analysis failed"
    
    def detect_bias(self, content: str) -> Dict:
        """Detect potential bias in content"""
        if not self.config['bias_detection']['enabled']:
            return {'biased': False, 'issues': []}
        
        try:
            prompt = f"""analyze this content for potential bias or misleading information:

{content}

check for:
- emotional language that might cloud judgment
- unsubstantiated claims
- political or ideological slant
- sensationalist language
- missing context or nuance

respond with: BIASED: true/false | ISSUES: list of specific issues found

be objective and focus on factual accuracy."""
            
            response = ollama.generate(
                model=OLLAMA_MODEL,
                prompt=prompt,
                options={'temperature': 0.2, 'max_tokens': 150}
            )
            
            result = response['response'].strip()
            
            biased_match = re.search(r'BIASED:\s*(true|false)', result, re.IGNORECASE)
            issues_match = re.search(r'ISSUES:\s*(.+)', result)
            
            is_biased = biased_match.group(1).lower() == 'true' if biased_match else False
            issues = issues_match.group(1).strip() if issues_match else ""
            
            return {
                'biased': is_biased,
                'issues': issues.split(',') if issues else []
            }
            
        except Exception as e:
            print(f"Error detecting bias: {e}")
            return {'biased': False, 'issues': ['Analysis failed']}
    
    def create_discord_alert(self, item: Dict, relevance_score: float, reason: str, bias_info: Dict) -> Dict:
        """Create Discord alert message with casual, fun tone"""
        
        # Casual greetings based on relevance score and time
        casual_greetings = [
            "yo ian! breaking news:",
            "dude, pause fortnite and check this out:",
            "holy shit, this is actually relevant:",
            "okay this is pretty cool:",
            "yo, neuromancer found some good stuff:",
            "dude, this might be up your alley:",
            "wait, this is actually interesting:",
            "okay so neuromancer is freaking out about this:",
            "yo, found something that might blow your mind:",
            "dude, this is exactly the kind of thing you'd love:"
        ]
        
        # Source-specific casual comments
        source_comments = {
            'hacker_news': '🔥 HN is going wild about this',
            'reddit': '📱 reddit actually found something decent',
            'github': '🐙 github trending, looks promising'
        }
        
        # Pick greeting based on relevance score
        if relevance_score > 0.9:
            greeting = casual_greetings[0]  # "breaking news"
        elif relevance_score > 0.8:
            greeting = casual_greetings[1]  # "pause fortnite"
        elif relevance_score > 0.7:
            greeting = casual_greetings[2]  # "holy shit"
        else:
            greeting = casual_greetings[3]  # "pretty cool"
        
        # Determine emoji based on source
        source_emojis = {
            'hacker_news': '🔥',
            'reddit': '📱',
            'github': '🐙'
        }
        
        emoji = source_emojis.get(item['source'], '📰')
        source_comment = source_comments.get(item['source'], '')
        
        # Create casual, fun summary
        if bias_info['biased']:
            warning = "⚠️ *heads up: might be a bit biased*"
        else:
            warning = ""
        
        # Build embed with casual tone (second person POV)
        # Prepare reason in second person with word cap
        max_words = int(self.config.get('alerting', {}).get('summary_max_words', 100))
        reason_2p = self.to_second_person_and_cap(reason, max_words)

        embed = {
            "title": f"{emoji} {item['title']}",
            "url": item['url'],
            "color": 0x00ff00 if relevance_score > 0.8 else 0xffaa00,
            "fields": [
                {
                    "name": "why this matters to you",
                    "value": reason_2p,
                    "inline": False
                },
                {
                    "name": "relevance to you",
                    "value": f"{relevance_score:.1f}/1.0",
                    "inline": True
                },
                {
                    "name": "source",
                    "value": f"{item['source'].replace('_', ' ').title()} {source_comment}",
                    "inline": True
                }
            ],
            "footer": {
                "text": f"neuromancer • {datetime.now().strftime('%m-%d %H:%M')}"
            }
        }

        # Optional deep dive field (if present on item)
        deep_summary = item.get('deep_summary')
        if deep_summary:
            embed["fields"].insert(1, {
                "name": "deep dive (for you)",
                "value": self.to_second_person_and_cap(deep_summary, int(self.config.get('alerting', {}).get('summary_max_words', 100))),
                "inline": False
            })
        
        if bias_info['biased'] and bias_info['issues']:
            embed["fields"].append({
                "name": "⚠️ potential issues",
                "value": "• " + "\n• ".join(bias_info['issues'][:3]),
                "inline": False
            })
        
        if item['source'] == 'hacker_news' and 'score' in item:
            embed["fields"].append({
                "name": "hn score",
                "value": f"{item['score']} points, {item.get('comments', 0)} comments",
                "inline": True
            })
        elif item['source'] == 'reddit' and 'subreddit' in item:
            embed["fields"].append({
                "name": "subreddit",
                "value": f"r/{item['subreddit']}",
                "inline": True
            })
        elif item['source'] == 'github' and 'stars' in item:
            embed["fields"].append({
                "name": "stars",
                "value": f"⭐ {item['stars']}",
                "inline": True
            })
        
        return {
            "content": greeting,
            "embeds": [embed]
        }
    
    def send_discord_alert(self, alert_data: Dict):
        """Send alert to Discord"""
        if not self.config['alerting']['discord_webhook']:
            print("No Discord webhook configured")
            return False
        
        try:
            response = requests.post(
                self.config['alerting']['discord_webhook'],
                json=alert_data,
                timeout=10
            )
            response.raise_for_status()
            
            # Record alert
            self.alert_history.append({
                'timestamp': datetime.now().isoformat(),
                'item_id': alert_data.get('embeds', [{}])[0].get('url', ''),
                'success': True
            })
            
            return True
            
        except Exception as e:
            print(f"Error sending Discord alert: {e}")
            self.alert_history.append({
                'timestamp': datetime.now().isoformat(),
                'item_id': alert_data.get('embeds', [{}])[0].get('url', ''),
                'success': False,
                'error': str(e)
            })
            return False
    
    def process_items(self):
        """Main processing loop"""
        self.logger.info("🔍 NEUROMANCER social monitor starting...")
        
        all_items = []
        
        # Fetch from all sources
        hn_items = self.get_hacker_news_items()
        reddit_items = self.get_reddit_items()
        github_items = self.get_github_trending()
        
        all_items.extend(hn_items)
        all_items.extend(reddit_items)
        all_items.extend(github_items)
        
        self.logger.info(f"Found {len(all_items)} new items to analyze (HN: {len(hn_items)}, Reddit: {len(reddit_items)}, GitHub: {len(github_items)})")
        
        alerts_sent = 0
        high_relevance_items = []
        medium_relevance_items = []
        
        per_run_cap = int(self.config['alerting'].get('max_alerts_per_run', 2))
        for item in all_items:
            # Analyze relevance
            relevance_score, reason = self.analyze_relevance(item)
            
            # Log findings with different levels based on relevance
            if relevance_score >= self.config['alerting']['min_relevance_score']:
                high_relevance_items.append({
                    'item': item,
                    'score': relevance_score,
                    'reason': reason
                })
                self.logger.info(f"🔥 HIGH RELEVANCE: {item['title'][:60]}... (score: {relevance_score:.2f}) - {reason}")
                
                # Check if we can send more alerts
                if not self.can_send_alert():
                    self.logger.warning("Rate limit reached, stopping alerts for now")
                    break
                
                # Detect bias
                bias_info = self.detect_bias(item['title'])

                # Deep context scrape and second-pass summary (best-effort)
                try:
                    item_with_context = self.enrich_with_context(item)
                    deep_summary = self.second_pass_summary(item_with_context)
                    if deep_summary:
                        item['deep_summary'] = deep_summary
                except Exception as _:
                    pass
                
                # Create and send alert
                alert_data = self.create_discord_alert(item, relevance_score, reason, bias_info)
                
                if self.send_discord_alert(alert_data):
                    self.logger.info(f"✅ Alert sent for: {item['title'][:50]}...")
                    alerts_sent += 1
                    if alerts_sent >= per_run_cap:
                        self.logger.info("Per-run alert cap reached, stopping alerts for this run")
                        break
                else:
                    self.logger.error(f"❌ Failed to send alert for: {item['title'][:50]}...")
                    
            elif relevance_score >= 0.5:  # Medium relevance
                medium_relevance_items.append({
                    'item': item,
                    'score': relevance_score,
                    'reason': reason
                })
                self.logger.info(f"📊 MEDIUM RELEVANCE: {item['title'][:60]}... (score: {relevance_score:.2f}) - {reason}")
            else:
                self.logger.debug(f"📉 LOW RELEVANCE: {item['title'][:60]}... (score: {relevance_score:.2f})")
            
            # Mark as processed
            self.processed_items.add(item['id'])
        
        # Log summary
        self.logger.info(f"📈 ANALYSIS SUMMARY:")
        self.logger.info(f"  • Total items analyzed: {len(all_items)}")
        self.logger.info(f"  • High relevance items: {len(high_relevance_items)}")
        self.logger.info(f"  • Medium relevance items: {len(medium_relevance_items)}")
        self.logger.info(f"  • Alerts sent: {alerts_sent}")
        
        # Log top high relevance items for review
        if high_relevance_items:
            self.logger.info("🔥 TOP HIGH RELEVANCE ITEMS:")
            for i, item_data in enumerate(high_relevance_items[:5], 1):
                item = item_data['item']
                score = item_data['score']
                self.logger.info(f"  {i}. [{score:.2f}] {item['title']} - {item['url']}")
        
        # Log top medium relevance items
        if medium_relevance_items and len(high_relevance_items) < 3:
            self.logger.info("📊 TOP MEDIUM RELEVANCE ITEMS:")
            for i, item_data in enumerate(medium_relevance_items[:3], 1):
                item = item_data['item']
                score = item_data['score']
                self.logger.info(f"  {i}. [{score:.2f}] {item['title']} - {item['url']}")
        
        # Save state
        self.save_processed_items()
        self.save_alert_history()
        
        self.logger.info(f"🎯 NEUROMANCER monitoring complete: {alerts_sent} alerts sent")
        return alerts_sent

def main():
    """Main entry point"""
    monitor = SocialMonitor()
    alerts_sent = monitor.process_items()
    
    if alerts_sent > 0:
        monitor.logger.info(f"🧠 NEUROMANCER delivered {alerts_sent} intelligence alerts!")
    else:
        monitor.logger.info("🔍 NEUROMANCER monitoring complete - no high-relevance items found")

if __name__ == "__main__":
    main()
