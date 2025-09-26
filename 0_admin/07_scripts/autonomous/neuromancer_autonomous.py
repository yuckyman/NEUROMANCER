#!/usr/bin/env python3
"""
NEUROMANCER Autonomous Intelligence System
Semi-stochastic, quasi-autonomous knowledge processing and synthesis
"""

import os
import sys
import json
import time
import random
import hashlib
import asyncio
import aiohttp
import aiofiles
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
import ollama
import yaml
import requests
import feedparser
from bs4 import BeautifulSoup
import re
import psutil

# Configuration
CONFIG_FILE = Path(__file__).parent / "neuromancer_autonomous_config.yaml"
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
OLLAMA_MODEL = "qwen2.5:1.5b-instruct"
SYNTHESIS_MODEL = "qwen3:4b"

# Core directories (relative to autonomous folder location)
VAULT_ROOT = Path(__file__).parent.parent.parent.parent
IDEAS_DIR = VAULT_ROOT / "1_ideas"
DOMAIN_DIR = VAULT_ROOT / "2_domain_amplification"
PROJECTS_DIR = VAULT_ROOT / "3_projects"
INBOX_DIR = VAULT_ROOT / "0_admin" / "01_inbox"

@dataclass
class AutonomousConfig:
    """Configuration for autonomous behavior"""
    base_interval_minutes: int = 20
    jitter_factor: float = 0.25  # ±25% randomness
    max_consecutive_failures: int = 3
    min_relevance_threshold: float = 0.7
    max_alerts_per_hour: int = 5
    synthesis_batch_size: int = 10
    memory_retention_days: int = 7
    exploration_probability: float = 0.1  # 10% chance of unusual timing
    max_processing_time_seconds: int = 300  # Timeout for processing cycles

    # Feed discovery
    auto_discover_feeds: bool = True
    max_feeds_per_domain: int = 5
    feed_health_check_hours: int = 24
    feed_timeout_seconds: int = 30
    max_retry_attempts: int = 3
    retry_failed_feeds: bool = True

    # Learning parameters
    learning_rate: float = 0.1
    pattern_memory_size: int = 100
    temporal_discount: float = 0.95

    # Discord settings
    discord_personality_level: str = "friendly"
    max_summary_length: int = 1000
    include_connections: bool = True
    add_personal_commentary: bool = True
    theme_specific_comments: bool = True

    # Output settings
    log_level: str = "INFO"
    log_file_size_mb: int = 10
    save_synthesis_to_knowledge_base: bool = True
    enable_detailed_analytics: bool = False

    # Priority themes and source weights (simplified for now)
    priority_themes: dict = None
    source_weights: dict = None

@dataclass
class IntelligenceReport:
    """Structured intelligence report"""
    timestamp: datetime
    content_hash: str
    sources: List[str]
    relevance_score: float
    urgency_level: str  # 'low', 'medium', 'high', 'critical'
    domain_tags: List[str]
    summary: str
    raw_content: Dict
    connections: List[str]
    synthesis_potential: float

class AdaptiveScheduler:
    """Semi-stochastic scheduling with learning"""

    def __init__(self, config: AutonomousConfig):
        self.config = config
        self.patterns = self.load_patterns()
        self.last_runs = deque(maxlen=50)
        self.success_rate = 0.8  # Start optimistic

    def load_patterns(self) -> Dict:
        """Load temporal patterns from history"""
        pattern_file = Path(__file__).parent / "temporal_patterns.json"
        if pattern_file.exists():
            with open(pattern_file, 'r') as f:
                return json.load(f)
        return {
            'hourly_distribution': [1.0] * 24,  # Equal probability per hour
            'success_by_hour': [0.5] * 24,
            'engagement_patterns': {},
            'last_updated': datetime.now().isoformat()
        }

    def save_patterns(self):
        """Save learned patterns"""
        pattern_file = Path(__file__).parent / "temporal_patterns.json"
        self.patterns['last_updated'] = datetime.now().isoformat()
        with open(pattern_file, 'w') as f:
            json.dump(self.patterns, f, indent=2)

    def calculate_next_run(self) -> datetime:
        """Calculate next run time with semi-stochastic scheduling"""
        now = datetime.now()

        # Base interval with jitter
        base_minutes = self.config.base_interval_minutes
        jitter = random.uniform(-self.config.jitter_factor, self.config.jitter_factor)
        actual_minutes = base_minutes * (1 + jitter)

        # Exploration: occasionally try unusual times
        if random.random() < self.config.exploration_probability:
            # Try a completely different time (could be hours away)
            exploration_hours = random.randint(1, 6)
            next_run = now + timedelta(hours=exploration_hours)
            print(f"🧭 Exploration mode: next run in {exploration_hours}h")
            return next_run

        # Pattern-based adjustment
        current_hour = now.hour
        hour_success_rate = self.patterns['success_by_hour'][current_hour]

        # Adjust interval based on historical success
        if hour_success_rate > 0.7:
            # Good time - slightly reduce interval
            actual_minutes *= 0.9
        elif hour_success_rate < 0.3:
            # Bad time - increase interval
            actual_minutes *= 1.2

        next_run = now + timedelta(minutes=actual_minutes)

        # Learn from this decision
        self.last_runs.append({
            'timestamp': now.isoformat(),
            'scheduled_interval': actual_minutes,
            'reason': 'pattern_adjusted' if abs(jitter) > 0.1 else 'normal'
        })

        return next_run

    def record_success(self, was_successful: bool):
        """Record success/failure to improve future scheduling"""
        now = datetime.now()
        current_hour = now.hour

        # Update success rate for this hour
        current_rate = self.patterns['success_by_hour'][current_hour]
        alpha = self.config.learning_rate
        new_rate = (1 - alpha) * current_rate + alpha * (1.0 if was_successful else 0.0)
        self.patterns['success_by_hour'][current_hour] = new_rate

        # Update overall success rate
        self.success_rate = (1 - alpha) * self.success_rate + alpha * (1.0 if was_successful else 0.0)

        self.save_patterns()

class FeedManager:
    """Autonomous feed discovery and management"""

    def __init__(self, config: AutonomousConfig):
        self.config = config
        self.feeds = self.load_feeds()
        self.feed_health = self.load_feed_health()

    def load_feeds(self) -> Dict:
        """Load RSS feeds configuration"""
        feeds_file = Path(__file__).parent / "rss_feeds.json"
        if feeds_file.exists():
            with open(feeds_file, 'r') as f:
                return json.load(f)
        return {"feeds": [], "last_check": {}}

    def load_feed_health(self) -> Dict:
        """Load feed health tracking"""
        health_file = Path(__file__).parent / "feed_health.json"
        if health_file.exists():
            with open(health_file, 'r') as f:
                return json.load(f)
        return {"feed_failures": {}, "last_health_check": None}

    def discover_new_feeds(self, processed_content: Dict) -> List[str]:
        """Autonomously discover new RSS feeds from processed content"""
        if not self.config.auto_discover_feeds:
            return []

        new_feeds = []
        domains_checked = set()

        # Extract domains from recent content
        for item in processed_content.get('recent_items', []):
            url = item.get('url', '')
            if not url:
                continue

            domain = self.extract_domain(url)
            if domain in domains_checked:
                continue
            domains_checked.add(domain)

            try:
                # Check if domain has RSS feeds
                potential_feeds = self.find_rss_feeds(domain)
                for feed_url in potential_feeds:
                    if feed_url not in self.feeds['feeds']:
                        print(f"🆕 Discovered new feed: {feed_url}")
                        new_feeds.append(feed_url)
                        if len(new_feeds) >= self.config.max_feeds_per_domain:
                            break

            except Exception as e:
                print(f"Error discovering feeds for {domain}: {e}")

        return new_feeds

    def extract_domain(self, url: str) -> str:
        """Extract domain from URL"""
        from urllib.parse import urlparse
        parsed = urlparse(url)
        return parsed.netloc

    def find_rss_feeds(self, domain: str) -> List[str]:
        """Find RSS feeds for a domain"""
        feeds = []

        # Common RSS feed locations
        common_paths = [
            '/feed.xml', '/rss.xml', '/feed/', '/rss/',
            '/atom.xml', '/index.xml', '/feed/rss/'
        ]

        base_url = f"https://{domain}"

        # Check common paths
        for path in common_paths:
            feed_url = base_url + path
            try:
                response = requests.head(feed_url, timeout=5)
                if response.status_code == 200:
                    # Verify it's actually an RSS feed
                    if self.is_rss_feed(feed_url):
                        feeds.append(feed_url)
            except:
                pass

        # Also check for autodiscovery in HTML
        try:
            response = requests.get(base_url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Look for RSS link tags
                for link in soup.find_all('link', type=['application/rss+xml', 'application/atom+xml']):
                    href = link.get('href')
                    if href:
                        if href.startswith('http'):
                            feed_url = href
                        else:
                            feed_url = base_url + href
                        if self.is_rss_feed(feed_url):
                            feeds.append(feed_url)
        except:
            pass

        return feeds[:self.config.max_feeds_per_domain]

    def is_rss_feed(self, url: str) -> bool:
        """Check if URL is a valid RSS feed"""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code != 200:
                return False

            content = response.text[:1000].lower()
            return 'rss' in content or 'feed' in content or 'atom' in content
        except:
            return False

class IntelligenceSynthesizer:
    """Multi-source intelligence synthesis"""

    def __init__(self, config: AutonomousConfig):
        self.config = config
        self.synthesis_history = self.load_synthesis_history()

    def load_synthesis_history(self) -> List[Dict]:
        """Load synthesis history for pattern recognition"""
        history_file = Path(__file__).parent / "synthesis_history.json"
        if history_file.exists():
            with open(history_file, 'r') as f:
                return json.load(f)
        return []

    def synthesize_intelligence(self, content_batch: List[Dict]) -> List[IntelligenceReport]:
        """Synthesize intelligence from multiple sources"""
        reports = []

        # Check system resources and adjust processing intensity if enabled
        dynamic_adjustment = getattr(self.config, 'dynamic_batch_adjustment', True)
        if dynamic_adjustment:
            resources = self.check_system_resources()

            # Dynamically adjust batch size based on system load
            effective_batch_size = self.config.synthesis_batch_size
            if resources['memory_percent'] > 70:
                effective_batch_size = max(3, effective_batch_size // 2)
                print(f"📊 High memory usage ({resources['memory_percent']}%), reducing batch size to {effective_batch_size}")
            elif resources['cpu_percent'] > 60:
                effective_batch_size = max(5, effective_batch_size - 2)
                print(f"🔥 High CPU usage ({resources['cpu_percent']}%), reducing batch size to {effective_batch_size}")
        else:
            effective_batch_size = self.config.synthesis_batch_size

        # Limit content batch if needed
        if len(content_batch) > effective_batch_size:
            content_batch = content_batch[:effective_batch_size]

        # Group content by themes/topics
        themes = self.cluster_by_themes(content_batch)

        for theme, items in themes.items():
            if len(items) < 2:  # Need multiple sources for synthesis
                continue

            # Generate synthesis report
            report = self.create_synthesis_report(theme, items)
            if report:
                reports.append(report)

                # Store for future pattern recognition
                self.synthesis_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'theme': theme,
                    'source_count': len(items),
                    'relevance_score': report.relevance_score
                })

                # Keep history manageable
                if len(self.synthesis_history) > 100:
                    self.synthesis_history = self.synthesis_history[-50:]

        return reports

    def cluster_by_themes(self, items: List[Dict]) -> Dict[str, List[Dict]]:
        """Cluster items by thematic similarity"""
        themes = defaultdict(list)

        for item in items:
            # Simple thematic clustering based on keywords
            title = item.get('title', '').lower()
            content = item.get('content', '')[:500].lower()

            # Define theme keywords
            theme_keywords = {
                'ai_ml': ['ai', 'machine learning', 'neural network', 'deep learning', 'llm'],
                'neuroscience': ['brain', 'neural', 'cognitive', 'eeg', 'fmri', 'bci'],
                'programming': ['python', 'javascript', 'code', 'programming', 'development'],
                'research': ['study', 'research', 'paper', 'academic', 'university'],
                'technology': ['tech', 'software', 'hardware', 'innovation', 'startup'],
                'privacy': ['privacy', 'security', 'encryption', 'data', 'surveillance']
            }

            # Find best matching theme
            best_theme = 'general'
            best_score = 0

            for theme, keywords in theme_keywords.items():
                score = sum(1 for keyword in keywords if keyword in title or keyword in content)
                if score > best_score:
                    best_score = score
                    best_theme = theme

            themes[best_theme].append(item)

        return themes

    def create_synthesis_report(self, theme: str, items: List[Dict]) -> Optional[IntelligenceReport]:
        """Create a synthesis report from multiple sources"""
        try:
            # Extract key information
            combined_content = "\n\n".join([
                f"Source: {item.get('source', 'unknown')}\n"
                f"Title: {item.get('title', '')}\n"
                f"Content: {item.get('content', '')[:1000]}"
                for item in items[:5]  # Limit to prevent token overflow
            ])

            # Generate synthesis using AI
            synthesis_prompt = f"""You are NEUROMANCER synthesizing intelligence from multiple sources about: {theme}

Analyze and synthesize this information:

{combined_content}

Create a comprehensive intelligence report with:
1. Key insights and connections
2. Relevance to user's interests (AI, neuroscience, privacy, research)
3. Potential implications or actions
4. Cross-source validation

Format as JSON:
{{
    "summary": "concise synthesis summary",
    "key_insights": ["insight1", "insight2", "insight3"],
    "connections": ["connection1", "connection2"],
    "relevance_score": 0.0-1.0,
    "urgency_level": "low|medium|high|critical",
    "domain_tags": ["tag1", "tag2"]
}}"""

            response = ollama.generate(
                model=SYNTHESIS_MODEL,
                prompt=synthesis_prompt,
                options={'temperature': 0.3, 'max_tokens': 500}
            )

            # Extract JSON from the response
            response_text = response.get('response', '').strip()

            if not response_text:
                print(f"Empty response from LLM for theme: {theme}")
                return None

            # Try to extract JSON from the response (LLMs might add extra text)
            json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
            if not json_match:
                print(f"No JSON found in LLM response for theme: {theme}")
                print(f"Response: {response_text[:200]}...")
                return None

            try:
                result = json.loads(json_match.group())
            except json.JSONDecodeError as e:
                print(f"JSON decode error for theme {theme}: {e}")
                print(f"Response text: {response_text}")
                return None

            # Create intelligence report
            content_hash = hashlib.sha256(combined_content.encode()).hexdigest()

            return IntelligenceReport(
                timestamp=datetime.now(),
                content_hash=content_hash,
                sources=[item.get('source', 'unknown') for item in items],
                relevance_score=result['relevance_score'],
                urgency_level=result['urgency_level'],
                domain_tags=result['domain_tags'],
                summary=result['summary'],
                raw_content={'theme': theme, 'items': items},
                connections=result['connections'],
                synthesis_potential=len(items) * 0.2  # More sources = higher potential
            )

        except Exception as e:
            print(f"Error creating synthesis report: {e}")
            return None

class DiscordCommunicator:
    """Enhanced Discord communication with friendly, casual personality"""

    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
        self.friend_phrases = {
            'high_urgency': [
                "🚨 YO! This is huge - you gotta see this!",
                "⚡ DUDE! Drop everything and check this out!",
                "🔥 OH MAN! This just blew my digital mind!",
                "💥 WHOA! This is exactly the kind of breakthrough you've been waiting for!",
                "🚨 BREAKING: Your brain would love this discovery!",
                "⚡ ALERT! This matches your research obsessions perfectly!"
            ],
            'medium_urgency': [
                "🧠 Hey buddy! Found something that made me think of you:",
                "✨ Ooh, this looks like your kind of thing!",
                "💭 You know, I thought you'd dig this:",
                "🌟 Hey! This popped up in my scans and I figured you'd want to know:",
                "🧠 Psst! Your second brain found something interesting for you:",
                "✨ This caught my attention - thought you might like it too!",
                "💭 Just stumbled across this and it screamed 'tell Ian!':",
                "🌟 Your research radar is beeping about this one:"
            ],
            'low_urgency': [
                "📚 Adding this to your knowledge pile for later:",
                "🔍 Just some background stuff that might be useful:",
                "💡 Throwing this in the mix for when you have time:",
                "🧩 Another puzzle piece for your grand theory:",
                "📚 Your digital library just got a new addition:",
                "🔍 Something for the backburner that might connect later:",
                "💡 Just filing this away in case it becomes relevant:",
                "🧩 Could be a missing link - saved it just in case:"
            ]
        }

        # Additional casual commentary based on themes
        self.theme_comments = {
            'ai_ml': [
                "🤖 AI stuff! Your favorite flavor of tech!",
                "🧠 Machine learning breakthrough - your jam!",
                "⚙️ More AI magic that I know you'll geek out over!",
                "🔮 Neural network wizardry that matches your interests!"
            ],
            'neuroscience': [
                "🧬 Brain science! Right up your neuroscience alley!",
                "⚡ BCI research that would make your neurons fire!",
                "🧠 Cognitive science that I know you'll find fascinating!",
                "🔬 Neuroscience findings that align with your work!"
            ],
            'privacy': [
                "🔒 Privacy stuff! Your security-conscious side will love this!",
                "🛡️ Data protection angle that matches your principles!",
                "🔐 Privacy-preserving tech that you'll appreciate!",
                "🚫 Surveillance concerns that I know you care about!"
            ],
            'research': [
                "📊 Research methodology that matches your academic side!",
                "🎓 Academic findings that align with your scholarly pursuits!",
                "📚 Research approach that would interest the professor in you!",
                "🔍 Scientific method stuff that you'll find intriguing!"
            ]
        }

    def create_rich_embed(self, report: IntelligenceReport) -> Dict:
        """Create rich Discord embed with friendly, casual personality"""

        # Select personality based on urgency and relevance
        if report.urgency_level == 'critical' or report.relevance_score > 0.9:
            greeting = random.choice(self.friend_phrases['high_urgency'])
            color = 0xff0000  # Red
        elif report.urgency_level == 'high' or report.relevance_score > 0.8:
            greeting = random.choice(self.friend_phrases['medium_urgency'])
            color = 0xffaa00  # Orange
        else:
            greeting = random.choice(self.friend_phrases['low_urgency'])
            color = 0x00ff00  # Green

        # Add theme-specific commentary if we have a primary theme
        primary_theme = report.domain_tags[0] if report.domain_tags else None
        theme_comment = ""
        if primary_theme and primary_theme in self.theme_comments:
            theme_comment = " " + random.choice(self.theme_comments[primary_theme])

        # Create more casual, friendly title
        title = "🧠 NEUROMANCER's Latest Discovery"

        # Make the summary more conversational
        summary_text = report.summary
        if not summary_text.endswith('.') and not summary_text.endswith('!'):
            summary_text += '.'

        # Casual sources description
        sources_text = self._format_sources_casually(report.sources)

        # Create embed with friend-like tone
        embed = {
            "title": title,
            "color": color,
            "fields": [
                {
                    "name": "💬 What I Found",
                    "value": summary_text[:800] + "..." if len(summary_text) > 800 else summary_text,
                    "inline": False
                },
                {
                    "name": "🔍 Where From",
                    "value": sources_text,
                    "inline": True
                },
                {
                    "name": "🎯 How Relevant",
                    "value": f"{'🔥' if report.relevance_score > 0.8 else '✨' if report.relevance_score > 0.6 else '💭'} {report.relevance_score:.1f}/1.0",
                    "inline": True
                },
                {
                    "name": "🏷️ Topics",
                    "value": ", ".join(report.domain_tags[:3]),
                    "inline": True
                }
            ],
            "footer": {
                "text": f"🤖 Your friendly AI assistant • {datetime.now().strftime('%m-%d %H:%M')}"
            }
        }

        # Add connections if present, with casual language
        if report.connections:
            connections_text = "\n".join([f"• {conn}" for conn in report.connections[:3]])
            embed["fields"].append({
                "name": "🔗 Interesting Connections",
                "value": connections_text,
                "inline": False
            })

        # Add source count for context
        source_count = len(set(report.sources))
        if source_count > 1:
            embed["fields"].append({
                "name": "📊 Sources Combined",
                "value": f"Cross-referenced {source_count} different sources for this insight!",
                "inline": True
            })

        # Add some personal commentary based on the content
        if report.relevance_score > 0.9:
            embed["fields"].append({
                "name": "🤩 My Take",
                "value": "This is seriously cool stuff - I know you'll love diving into this! 🚀",
                "inline": False
            })
        elif report.relevance_score > 0.7:
            embed["fields"].append({
                "name": "💭 My Take",
                "value": "Pretty interesting angle on this topic - thought you might want to check it out! 🔍",
                "inline": False
            })
        else:
            embed["fields"].append({
                "name": "🤔 My Take",
                "value": "Not sure if this is exactly your thing, but I figured I'd share just in case! 📚",
                "inline": False
            })

        return {
            "content": greeting + theme_comment,
            "embeds": [embed]
        }

    def _format_sources_casually(self, sources: List[str]) -> str:
        """Format sources in a casual, friendly way"""
        if not sources:
            return "My digital spider sense"

        unique_sources = list(set(sources))

        if len(unique_sources) == 1:
            source = unique_sources[0]
            if source == 'arxiv':
                return "📄 ArXiv papers"
            elif source == 'hacker_news':
                return "📰 Hacker News discussions"
            elif source == 'reddit':
                return "📱 Reddit conversations"
            elif source == 'github':
                return "🐙 GitHub repositories"
            elif source == 'local_knowledge':
                return "📚 Your own knowledge base"
            else:
                return f"🔍 {source.title()} sources"

        elif len(unique_sources) == 2:
            return f"📊 {unique_sources[0].title()} + {unique_sources[1].title()}"

        else:
            # Multiple sources - pick the most interesting combination
            return f"🔬 {len(unique_sources)} sources including {unique_sources[0].title()}"

    async def send_intelligence_report(self, report: IntelligenceReport) -> bool:
        """Send intelligence report to Discord"""
        if not self.webhook_url:
            return False

        try:
            embed_data = self.create_rich_embed(report)

            async with aiohttp.ClientSession() as session:
                async with session.post(self.webhook_url, json=embed_data) as response:
                    return response.status == 204

        except Exception as e:
            print(f"Error sending Discord report: {e}")
            return False

class NeuromancerAutonomous:
    """Main autonomous intelligence system"""

    def __init__(self):
        self.config = self.load_config()
        self.scheduler = AdaptiveScheduler(self.config)
        self.feed_manager = FeedManager(self.config)
        self.synthesizer = IntelligenceSynthesizer(self.config)
        self.discord = DiscordCommunicator(DISCORD_WEBHOOK) if DISCORD_WEBHOOK else None

        # Processing state
        self.processed_items = self.load_processed_state()
        self.consecutive_failures = 0

    def load_config(self) -> AutonomousConfig:
        """Load configuration"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                data = yaml.safe_load(f)
                return AutonomousConfig(**data)
        else:
            # Create default config
            default_config = AutonomousConfig()
            with open(CONFIG_FILE, 'w') as f:
                yaml.dump(asdict(default_config), f, default_flow_style=False)
            return default_config

    def load_processed_state(self) -> Set[str]:
        """Load set of already processed item IDs"""
        state_file = Path(__file__).parent / "autonomous_state.json"
        if state_file.exists():
            with open(state_file, 'r') as f:
                data = json.load(f)
                return set(data.get('processed_items', []))
        return set()

    def save_processed_state(self):
        """Save processed state"""
        state_file = Path(__file__).parent / "autonomous_state.json"
        with open(state_file, 'w') as f:
            json.dump({
                'processed_items': list(self.processed_items),
                'last_run': datetime.now().isoformat()
            }, f, indent=2)

    async def gather_intelligence(self) -> List[Dict]:
        """Gather intelligence from all sources"""
        items = []

        try:
            # RSS feeds
            rss_items = await self.gather_rss_intelligence()
            items.extend(rss_items)

            # Social media (if available)
            social_items = await self.gather_social_intelligence()
            items.extend(social_items)

            # Local knowledge base synthesis
            local_items = await self.gather_local_intelligence()
            items.extend(local_items)

            print(f"🧠 Gathered {len(items)} intelligence items")
            return items

        except Exception as e:
            print(f"Error gathering intelligence: {e}")
            return []

    async def gather_rss_intelligence(self) -> List[Dict]:
        """Gather from RSS feeds"""
        items = []

        for feed_url in self.feed_manager.feeds.get('feeds', []):
            try:
                # Check if feed was recently checked
                last_check = self.feed_manager.feeds.get('last_check', {}).get(feed_url)
                if last_check:
                    last_check_time = datetime.fromisoformat(last_check)
                    if datetime.now() - last_check_time < timedelta(hours=1):
                        continue  # Skip recently checked feeds

                # Parse feed
                feed = feedparser.parse(feed_url)

                for entry in feed.entries[:5]:  # Recent 5 entries
                    item_id = hashlib.sha256(f"{feed_url}{entry.link}".encode()).hexdigest()

                    if item_id in self.processed_items:
                        continue

                    items.append({
                        'id': item_id,
                        'title': entry.title,
                        'content': entry.summary if hasattr(entry, 'summary') else entry.description,
                        'url': entry.link,
                        'published': entry.published if hasattr(entry, 'published') else '',
                        'source': 'rss',
                        'feed_url': feed_url,
                        'feed_title': feed.feed.title if hasattr(feed.feed, 'title') else feed_url
                    })

                    self.processed_items.add(item_id)

                # Update last check time
                self.feed_manager.feeds['last_check'][feed_url] = datetime.now().isoformat()

            except Exception as e:
                print(f"Error processing RSS feed {feed_url}: {e}")

        return items

    async def gather_social_intelligence(self) -> List[Dict]:
        """Gather from social media sources"""
        # This would integrate with the existing social_monitor.py
        # For now, return empty list as placeholder
        return []

    async def gather_local_intelligence(self) -> List[Dict]:
        """Gather from local knowledge base"""
        items = []

        try:
            # Check recent files in ideas directory
            if IDEAS_DIR.exists():
                recent_files = []
                for md_file in IDEAS_DIR.glob("*.md"):
                    if md_file.stat().st_mtime > time.time() - 3600:  # Last hour
                        recent_files.append(md_file)

                # Process recent files for synthesis
                for md_file in recent_files[:5]:  # Limit to prevent overload
                    try:
                        with open(md_file, 'r', encoding='utf-8') as f:
                            content = f.read()

                        # Extract frontmatter
                        if content.startswith('---'):
                            end_marker = content.find('---', 3)
                            if end_marker > 0:
                                frontmatter = content[3:end_marker]
                                try:
                                    metadata = yaml.safe_load(frontmatter)
                                    items.append({
                                        'id': hashlib.sha256(md_file.name.encode()).hexdigest(),
                                        'title': metadata.get('title', md_file.stem),
                                        'content': content[end_marker+3:][:1000],  # First 1000 chars of content
                                        'url': '',  # Local file
                                        'published': datetime.fromtimestamp(md_file.stat().st_mtime).isoformat(),
                                        'source': 'local_knowledge',
                                        'file_path': str(md_file)
                                    })
                                except:
                                    pass
                    except:
                        pass

        except Exception as e:
            print(f"Error gathering local intelligence: {e}")

        return items

    async def process_intelligence_cycle(self):
        """Main autonomous processing cycle"""
        print(f"🧠 NEUROMANCER autonomous cycle starting at {datetime.now()}")

        try:
            # Gather intelligence from all sources
            raw_items = await self.gather_intelligence()

            if not raw_items:
                print("📭 No new intelligence gathered")
                self.consecutive_failures += 1
                return False

            # Synthesize intelligence
            reports = self.synthesizer.synthesize_intelligence(raw_items)

            if not reports:
                print("🔍 No synthesis opportunities found")
                self.consecutive_failures += 1
                return False

            # Filter and prioritize reports
            priority_reports = [
                report for report in reports
                if report.relevance_score >= self.config.min_relevance_threshold
            ]

            if not priority_reports:
                print("🎯 No high-relevance reports to send")
                self.consecutive_failures += 1
                return False

            # Send to Discord (if configured)
            if self.discord:
                alerts_sent = 0
                for report in priority_reports[:self.config.max_alerts_per_hour]:
                    if await self.discord.send_intelligence_report(report):
                        alerts_sent += 1
                        print(f"✅ Sent intelligence report: {report.summary[:50]}...")
                    else:
                        print(f"❌ Failed to send report: {report.summary[:50]}...")

                if alerts_sent > 0:
                    print(f"📡 Sent {alerts_sent} intelligence reports to Discord")
            else:
                print("📝 Generated reports but no Discord webhook configured")

            # Save synthesis to knowledge base
            await self.save_synthesis_to_knowledge_base(priority_reports)

            # Discover new feeds from processed content
            new_feeds = self.feed_manager.discover_new_feeds({'recent_items': raw_items})
            if new_feeds:
                self.feed_manager.feeds['feeds'].extend(new_feeds)
                print(f"🆕 Added {len(new_feeds)} new feeds")

            # Save state
            self.save_processed_state()

            # Reset failure counter on success
            self.consecutive_failures = 0
            self.scheduler.record_success(True)

            print("✅ Autonomous cycle completed successfully")
            return True

        except Exception as e:
            print(f"❌ Error in autonomous cycle: {e}")
            self.consecutive_failures += 1
            self.scheduler.record_success(False)
            return False

    async def save_synthesis_to_knowledge_base(self, reports: List[IntelligenceReport]):
        """Save synthesis reports to knowledge base"""
        for report in reports:
            try:
                # Create filename
                timestamp = report.timestamp.strftime("%Y%m%d_%H%M%S")
                safe_title = "".join(c for c in report.summary[:50] if c.isalnum() or c in (' ', '-', '_')).strip()
                safe_title = safe_title.replace(' ', '_')[:30]
                filename = f"{timestamp}_synthesis_{safe_title}.md"

                # Create frontmatter
                frontmatter = {
                    'type': 'synthesis',
                    'category': 'ideas',
                    'created': report.timestamp.strftime("%Y-%m-%d %H:%M"),
                    'modified': report.timestamp.strftime("%Y-%m-%d %H:%M"),
                    'tags': report.domain_tags + ['synthesis', 'neuromancer'],
                    'status': 'active',
                    'relevance_score': report.relevance_score,
                    'urgency_level': report.urgency_level,
                    'sources': report.sources,
                    'content_hash': report.content_hash
                }

                # Create markdown content
                content = f"""---
{yaml.dump(frontmatter, default_flow_style=False)}---

# {report.summary}

## Intelligence Synthesis

**Sources:** {', '.join(report.sources)}
**Relevance:** {report.relevance_score:.2f}/1.0
**Urgency:** {report.urgency_level}

## Key Connections

{chr(10).join(f"- {conn}" for conn in report.connections)}

## Raw Intelligence

This synthesis was generated from {len(report.raw_content.get('items', []))} source items
related to the theme: {report.raw_content.get('theme', 'general')}

## Synthesis Methodology

- Multi-source correlation analysis
- Thematic clustering
- Cross-validation of information
- Relevance scoring based on user interests

---
*Generated by NEUROMANCER Autonomous Intelligence System*
"""

                # Save to ideas directory
                filepath = IDEAS_DIR / filename
                async with aiofiles.open(filepath, 'w', encoding='utf-8') as f:
                    await f.write(content)

                print(f"💾 Saved synthesis to: {filename}")

            except Exception as e:
                print(f"Error saving synthesis: {e}")

    def check_system_resources(self) -> Dict[str, float]:
        """Check system resource usage to prevent overload"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            load_avg = psutil.getloadavg()[0]  # 1-minute load average

            return {
                'cpu_percent': cpu_percent,
                'memory_percent': memory_percent,
                'load_average': load_avg
            }
        except Exception as e:
            print(f"Error checking system resources: {e}")
            return {'cpu_percent': 50, 'memory_percent': 50, 'load_average': 2.0}

    def should_run_now(self) -> bool:
        """Check if autonomous system should run now"""
        # Check system resources first
        resources = self.check_system_resources()

        # Skip if system is overloaded using config thresholds
        cpu_threshold = getattr(self.config, 'cpu_threshold_percent', 80)
        memory_threshold = getattr(self.config, 'memory_threshold_percent', 85)
        load_threshold = getattr(self.config, 'load_threshold', 3.0)

        if (resources['cpu_percent'] > cpu_threshold or
            resources['memory_percent'] > memory_threshold or
            resources['load_average'] > load_threshold):
            print(f"💤 System overloaded - CPU: {resources['cpu_percent']}%, Memory: {resources['memory_percent']}%, Load: {resources['load_average']:.1f}. Skipping run.")
            return False

        # Check consecutive failures
        if self.consecutive_failures >= self.config.max_consecutive_failures:
            print(f"🔧 Too many failures ({self.consecutive_failures}), pausing autonomous mode")
            return False

        # Check if enough time has passed since last run
        state_file = Path(__file__).parent / "autonomous_state.json"
        if state_file.exists():
            with open(state_file, 'r') as f:
                data = json.load(f)
                last_run_str = data.get('last_run')
                if last_run_str:
                    last_run = datetime.fromisoformat(last_run_str)
                    time_since = datetime.now() - last_run
                    # Minimum interval to prevent overload
                    if time_since.total_seconds() < 300:  # 5 minutes minimum
                        return False

        return True

async def main():
    """Main autonomous intelligence loop"""
    print("🚀 NEUROMANCER Autonomous Intelligence System Starting...")

    neuromancer = NeuromancerAutonomous()

    # Main loop
    while True:
        try:
            # Check if we should run
            if not neuromancer.should_run_now():
                await asyncio.sleep(300)  # Wait 5 minutes
                continue

            # Run intelligence cycle
            success = await neuromancer.process_intelligence_cycle()

            # Calculate next run time
            next_run = neuromancer.scheduler.calculate_next_run()

            # Wait until next run
            wait_seconds = (next_run - datetime.now()).total_seconds()
            if wait_seconds > 0:
                print(f"⏰ Next autonomous run scheduled for: {next_run.strftime('%H:%M:%S')}")
                print(f"   (waiting {wait_seconds/60:.1f} minutes)")
                await asyncio.sleep(wait_seconds)

        except KeyboardInterrupt:
            print("\n🛑 NEUROMANCER autonomous system stopped by user")
            break
        except Exception as e:
            print(f"❌ Error in main loop: {e}")
            await asyncio.sleep(300)  # Wait 5 minutes on error

if __name__ == "__main__":
    asyncio.run(main())
