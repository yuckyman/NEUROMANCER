#!/usr/bin/env python3
"""
NEUROMANCER Learning Agent
Learns from your behavior and sends increasingly relevant alerts
"""

import os
import sys
import json
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import ollama
import yaml
import requests
from collections import defaultdict, Counter

# Configuration
CONFIG_FILE = Path(__file__).parent / "neuromancer_learning_config.yaml"
DISCORD_WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")
OLLAMA_MODEL = "gemma3:4b"

class NeuromancerLearningAgent:
    def __init__(self):
        self.config = self.load_config()
        self.learning_data = self.load_learning_data()
        self.alert_history = self.load_alert_history()
        
    def load_config(self) -> Dict:
        """Load configuration"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                return yaml.safe_load(f)
        else:
            # Create default config
            default_config = {
                "learning": {
                    "enabled": True,
                    "min_data_points": 10,
                    "learning_rate": 0.1,
                    "decay_factor": 0.95
                },
                "alerting": {
                    "discord_webhook": DISCORD_WEBHOOK,
                    "adaptive_threshold": True,
                    "base_relevance_threshold": 0.7,
                    "max_alerts_per_day": 5
                },
                "personality": {
                    "name": "NEUROMANCER",
                    "voice": "casual, curious, analytical",
                    "learning_style": "iterative, evidence-based",
                    "communication_style": "unbiased, factual, engaging"
                }
            }
            
            with open(CONFIG_FILE, 'w') as f:
                yaml.dump(default_config, f, default_flow_style=False)
            return default_config
    
    def load_learning_data(self) -> Dict:
        """Load learning data from previous interactions"""
        learning_file = Path(__file__).parent / "neuromancer_learning.json"
        if learning_file.exists():
            with open(learning_file, 'r') as f:
                return json.load(f)
        return {
            "interests": defaultdict(float),
            "keywords": defaultdict(float),
            "sources": defaultdict(float),
            "time_patterns": defaultdict(int),
            "alert_responses": [],
            "synthesis_quality": [],
            "learning_iterations": 0
        }
    
    def save_learning_data(self):
        """Save learning data"""
        learning_file = Path(__file__).parent / "neuromancer_learning.json"
        with open(learning_file, 'w') as f:
            json.dump(self.learning_data, f, indent=2)
    
    def load_alert_history(self) -> List[Dict]:
        """Load alert history"""
        history_file = Path(__file__).parent / "neuromancer_alerts.json"
        if history_file.exists():
            with open(history_file, 'r') as f:
                return json.load(f)
        return []
    
    def save_alert_history(self):
        """Save alert history"""
        history_file = Path(__file__).parent / "neuromancer_alerts.json"
        # Keep only last 30 days
        cutoff = datetime.now() - timedelta(days=30)
        recent_alerts = [
            alert for alert in self.alert_history
            if datetime.fromisoformat(alert['timestamp']) > cutoff
        ]
        with open(history_file, 'w') as f:
            json.dump(recent_alerts, f, indent=2)
    
    def analyze_vault_activity(self) -> Dict:
        """Analyze recent vault activity to learn from your behavior"""
        vault_path = Path("/Users/ian/NEUROMANCER")
        
        # Analyze recently modified files
        recent_files = []
        for md_file in vault_path.rglob("*.md"):
            if md_file.stat().st_mtime > (time.time() - 86400 * 7):  # Last 7 days
                recent_files.append(md_file)
        
        # Extract keywords and topics from recent activity
        keywords = Counter()
        topics = Counter()
        
        for file_path in recent_files[:50]:  # Limit to 50 most recent
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract keywords (simple approach)
                words = content.lower().split()
                for word in words:
                    if len(word) > 4 and word.isalpha():
                        keywords[word] += 1
                
                # Extract topics from file path and content
                if "computational" in content.lower() or "neuroscience" in content.lower():
                    topics["computational_neuroscience"] += 1
                if "ai" in content.lower() or "artificial" in content.lower():
                    topics["ai_ml"] += 1
                if "privacy" in content.lower() or "self-hosted" in content.lower():
                    topics["privacy"] += 1
                if "eeg" in content.lower() or "bci" in content.lower():
                    topics["bci_research"] += 1
                
            except Exception as e:
                continue
        
        return {
            "keywords": dict(keywords.most_common(20)),
            "topics": dict(topics),
            "files_analyzed": len(recent_files)
        }
    
    def learn_from_synthesis_quality(self):
        """Learn from the quality of synthesized content"""
        synthesis_dir = Path("/Users/ian/NEUROMANCER/2_domain_amplification/synthesized")
        
        if not synthesis_dir.exists():
            return
        
        # Analyze recent synthesis files
        recent_synthesis = []
        for synth_file in synthesis_dir.rglob("*.md"):
            if synth_file.stat().st_mtime > (time.time() - 86400 * 3):  # Last 3 days
                recent_synthesis.append(synth_file)
        
        # Simple quality metrics (could be enhanced)
        for synth_file in recent_synthesis[:10]:
            try:
                with open(synth_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Basic quality indicators
                quality_score = 0
                if len(content) > 500:  # Substantial content
                    quality_score += 0.3
                if "##" in content:  # Well structured
                    quality_score += 0.2
                if "http" in content:  # Contains references
                    quality_score += 0.2
                if "example" in content.lower():  # Practical
                    quality_score += 0.3
                
                self.learning_data["synthesis_quality"].append({
                    "file": str(synth_file),
                    "score": quality_score,
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                continue
    
    def calculate_adaptive_relevance_threshold(self) -> float:
        """Calculate adaptive relevance threshold based on learning"""
        if not self.config["alerting"]["adaptive_threshold"]:
            return self.config["alerting"]["base_relevance_threshold"]
        
        # Analyze recent alert responses
        recent_responses = [
            resp for resp in self.learning_data["alert_responses"]
            if datetime.fromisoformat(resp["timestamp"]) > datetime.now() - timedelta(days=7)
        ]
        
        if len(recent_responses) < 5:
            return self.config["alerting"]["base_relevance_threshold"]
        
        # Calculate average engagement
        avg_engagement = sum(resp["engagement"] for resp in recent_responses) / len(recent_responses)
        
        # Adjust threshold based on engagement
        if avg_engagement > 0.7:  # High engagement
            return max(0.6, self.config["alerting"]["base_relevance_threshold"] - 0.1)
        elif avg_engagement < 0.3:  # Low engagement
            return min(0.9, self.config["alerting"]["base_relevance_threshold"] + 0.1)
        else:
            return self.config["alerting"]["base_relevance_threshold"]
    
    def create_learning_aware_alert(self, item: Dict, relevance_score: float, reason: str) -> Dict:
        """Create an alert that incorporates learning insights"""
        
        # Get current learning insights
        vault_activity = self.analyze_vault_activity()
        
        # Determine alert style based on learning
        if self.learning_data["learning_iterations"] > 10:
            style = "experienced"
        else:
            style = "learning"
        
        # Create personalized message
        if style == "experienced":
            greeting = "hey ian! neuromancer's been learning from your patterns and found something that aligns with your recent focus areas:"
        else:
            greeting = "hey ian! neuromancer found something that might interest you (still learning your preferences):"
        
        # Add learning insights to the alert
        learning_insights = []
        if vault_activity["topics"]:
            top_topic = max(vault_activity["topics"], key=vault_activity["topics"].get)
            learning_insights.append(f"this relates to your recent focus on {top_topic}")
        
        if self.learning_data["synthesis_quality"]:
            recent_quality = [q["score"] for q in self.learning_data["synthesis_quality"][-5:]]
            avg_quality = sum(recent_quality) / len(recent_quality)
            if avg_quality > 0.7:
                learning_insights.append("high-quality synthesis pattern detected")
        
        # Build embed with learning context
        embed = {
            "title": "🧠 NEUROMANCER Intelligence Alert",
            "description": f"**{item['title']}**",
            "url": item['url'],
            "color": 0x00ff00 if relevance_score > 0.8 else 0xffaa00,
            "fields": [
                {
                    "name": "Relevance Score",
                    "value": f"{relevance_score:.1f}/1.0",
                    "inline": True
                },
                {
                    "name": "Source",
                    "value": item['source'].replace('_', ' ').title(),
                    "inline": True
                },
                {
                    "name": "Why This Matters",
                    "value": reason,
                    "inline": False
                }
            ],
            "footer": {
                "text": f"NEUROMANCER • Learning Iteration {self.learning_data['learning_iterations']} • {datetime.now().strftime('%Y-%m-%d %H:%M')}"
            }
        }
        
        # Add learning insights if available
        if learning_insights:
            embed["fields"].append({
                "name": "🎯 Learning Insights",
                "value": "• " + "\n• ".join(learning_insights),
                "inline": False
            })
        
        # Add confidence level based on learning
        confidence = min(0.9, 0.5 + (self.learning_data["learning_iterations"] * 0.05))
        embed["fields"].append({
            "name": "Confidence",
            "value": f"{confidence:.1%} (based on {self.learning_data['learning_iterations']} learning cycles)",
            "inline": True
        })
        
        return {
            "content": greeting,
            "embeds": [embed]
        }
    
    def update_learning_from_alert(self, item: Dict, alert_sent: bool, engagement_score: float = 0.5):
        """Update learning data based on alert outcome"""
        
        # Update interest weights based on item content
        content_keywords = item['title'].lower().split()
        for keyword in content_keywords:
            if len(keyword) > 3:
                self.learning_data["interests"][keyword] += engagement_score * 0.1
        
        # Update source preferences
        self.learning_data["sources"][item['source']] += engagement_score * 0.1
        
        # Record alert response
        self.learning_data["alert_responses"].append({
            "timestamp": datetime.now().isoformat(),
            "item_id": item.get('id', ''),
            "engagement": engagement_score,
            "alert_sent": alert_sent,
            "source": item['source']
        })
        
        # Increment learning iterations
        self.learning_data["learning_iterations"] += 1
        
        # Apply decay to prevent old data from dominating
        decay_factor = self.config["learning"]["decay_factor"]
        for key in ["interests", "keywords", "sources"]:
            for subkey in self.learning_data[key]:
                self.learning_data[key][subkey] *= decay_factor
    
    def process_learning_cycle(self):
        """Main learning and alerting cycle"""
        print(f"🧠 NEUROMANCER learning agent starting cycle {self.learning_data['learning_iterations'] + 1}...")
        
        # Learn from recent vault activity
        vault_activity = self.analyze_vault_activity()
        print(f"📊 Analyzed {vault_activity['files_analyzed']} recent files")
        
        # Learn from synthesis quality
        self.learn_from_synthesis_quality()
        
        # Calculate adaptive threshold
        threshold = self.calculate_adaptive_relevance_threshold()
        print(f"🎯 Adaptive relevance threshold: {threshold:.2f}")
        
        # Import and use social monitor
        try:
            from social_monitor import SocialMonitor
            monitor = SocialMonitor()
            
            # Override threshold with learning-based threshold
            monitor.config['alerting']['min_relevance_score'] = threshold
            
            # Process items
            items = []
            items.extend(monitor.get_hacker_news_items())
            items.extend(monitor.get_reddit_items())
            
            alerts_sent = 0
            
            for item in items:
                # Analyze relevance with learning context
                relevance_score, reason = monitor.analyze_relevance(item)
                
                if relevance_score >= threshold:
                    print(f"High relevance item: {item['title'][:50]}... (score: {relevance_score:.2f})")
                    
                    # Create learning-aware alert
                    alert_data = self.create_learning_aware_alert(item, relevance_score, reason)
                    
                    # Send alert
                    if monitor.send_discord_alert(alert_data):
                        print(f"✅ Learning-aware alert sent for: {item['title'][:50]}...")
                        alerts_sent += 1
                        
                        # Update learning data
                        self.update_learning_from_alert(item, True, 0.7)  # Assume good engagement
                    else:
                        print(f"❌ Failed to send alert for: {item['title'][:50]}...")
                        self.update_learning_from_alert(item, False, 0.3)
                
                # Mark as processed
                monitor.processed_items.add(item['id'])
            
            # Save learning data
            self.save_learning_data()
            monitor.save_processed_items()
            
            print(f"🎓 NEUROMANCER learning cycle complete: {alerts_sent} alerts sent")
            return alerts_sent
            
        except ImportError:
            print("❌ Social monitor not available, running in learning-only mode")
            return 0

def main():
    """Main entry point"""
    agent = NeuromancerLearningAgent()
    alerts_sent = agent.process_learning_cycle()
    
    if alerts_sent > 0:
        print(f"🧠 NEUROMANCER delivered {alerts_sent} learning-enhanced intelligence alerts!")
    else:
        print("🔍 NEUROMANCER learning cycle complete - no high-relevance items found")

if __name__ == "__main__":
    main()
