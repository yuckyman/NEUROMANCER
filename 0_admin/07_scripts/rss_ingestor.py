#!/usr/bin/env python3
"""
RSS Content Ingestor for NEUROMANCER
Fetches RSS feeds and converts them to inbox items for processing
"""

import os
import sys
import json
import requests
import feedparser
from datetime import datetime, timedelta
from pathlib import Path
import re

# Configuration
INBOX_DIR = Path(__file__).parent.parent / "01_inbox"
FEEDS_CONFIG = Path(__file__).parent / "rss_feeds.json"

# Default RSS feeds to monitor with article limits
DEFAULT_FEEDS = [
    {"url": "https://github.blog/feed/", "limit": 10},
    {"url": "https://opencode.ai/feed.xml", "limit": 10},
    {"url": "https://simonwillison.net/atom/everything/", "limit": 15},
    {"url": "https://www.python.org/blogs/feed/", "limit": 10},
    {"url": "https://realpython.com/atom.xml", "limit": 20},
    {"url": "https://machinelearningmastery.com/feed/", "limit": 10},
    {"url": "https://towardsdatascience.com/feed", "limit": 15},
    {"url": "https://arxiv.org/rss/cs.AI", "limit": 25},
    {"url": "https://arxiv.org/rss/cs.CV", "limit": 25}
]

def load_feeds_config():
    """Load RSS feeds configuration"""
    if FEEDS_CONFIG.exists():
        with open(FEEDS_CONFIG, 'r') as f:
            return json.load(f)
    return {"feeds": DEFAULT_FEEDS, "last_check": {}}

def save_feeds_config(config):
    """Save RSS feeds configuration"""
    with open(FEEDS_CONFIG, 'w') as f:
        json.dump(config, f, indent=2)

def fetch_feed(feed_url, last_check=None, limit=50):
    """Fetch RSS feed and return new entries"""
    try:
        headers = {
            'User-Agent': 'NEUROMANCER-RSS-Ingestor/1.0'
        }
        response = requests.get(feed_url, headers=headers, timeout=30)
        response.raise_for_status()

        feed = feedparser.parse(response.content)

        if feed.bozo:
            print(f"Warning: Malformed feed at {feed_url}")
            return []

        new_entries = []
        # Limit the number of entries to process
        entries_to_process = feed.entries[:limit] if limit > 0 else feed.entries

        for entry in entries_to_process:
            # TODO: Implement date-based filtering for new entries
            # For now, include all entries to avoid type issues

            # Extract content
            title = getattr(entry, 'title', 'No Title')
            link = getattr(entry, 'link', '')

            # Get description/content
            content = ''
            if hasattr(entry, 'description'):
                content = str(entry.description)
            elif hasattr(entry, 'content') and entry.content:
                if isinstance(entry.content, list) and len(entry.content) > 0:
                    content = str(entry.content[0].value) if hasattr(entry.content[0], 'value') else str(entry.content[0])
                else:
                    content = str(entry.content)

            # Clean HTML tags from content
            content = re.sub(r'<[^>]+>', '', content)
            content = re.sub(r'\s+', ' ', content).strip()

            new_entries.append({
                'title': title,
                'link': link,
                'content': content[:1000] + '...' if len(content) > 1000 else content,
                'feed_url': feed_url,
                'feed_title': getattr(feed.feed, 'title', feed_url) if hasattr(feed, 'feed') else feed_url
            })

        return new_entries

    except Exception as e:
        print(f"Error fetching {feed_url}: {e}")
        return []

def create_inbox_file(entry):
    """Create an inbox file from RSS entry"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = re.sub(r'[^\w\-_\.]', '_', entry['title'])[:50]
    filename = f"{timestamp}_rss_{safe_title}.txt"

    content = f"""RSS Feed: {entry['feed_title']}
Source: {entry['feed_url']}
Link: {entry['link']}

{entry['title']}

{entry['content']}
"""

    filepath = INBOX_DIR / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Created inbox file: {filename}")
    return filepath

def main():
    """Main RSS ingestion function"""
    print("🚀 NEUROMANCER RSS Ingestor Starting...")

    # Ensure inbox directory exists
    INBOX_DIR.mkdir(parents=True, exist_ok=True)

    # Load configuration
    config = load_feeds_config()

    # Get custom feed URL from environment (for manual triggers)
    custom_feed = os.getenv('CUSTOM_FEED_URL')
    if custom_feed:
        feeds_to_check = [{"url": custom_feed, "limit": 20}]  # Default limit for custom feeds
    else:
        feeds_to_check = config['feeds']

    total_new_entries = 0

    for feed_config in feeds_to_check:
        if isinstance(feed_config, str):
            # Handle old format for backward compatibility
            feed_url = feed_config
            feed_limit = 50
        else:
            # Handle new format with limits
            feed_url = feed_config['url']
            feed_limit = feed_config.get('limit', 50)
        print(f"📡 Checking feed: {feed_url}")

        # Get last check time
        last_check = None
        if feed_url in config['last_check']:
            try:
                last_check = datetime.fromisoformat(config['last_check'][feed_url])
            except:
                pass

        # Fetch new entries
        new_entries = fetch_feed(feed_url, last_check)

        print(f"  📄 Found {len(new_entries)} new entries")

        # Create inbox files for new entries
        for entry in new_entries:
            create_inbox_file(entry)
            total_new_entries += 1

        # Update last check time
        config['last_check'][feed_url] = datetime.now().isoformat()

    # Save updated configuration
    save_feeds_config(config)

    print(f"✅ RSS ingestion complete! Processed {total_new_entries} new entries")

    if total_new_entries > 0:
        print("📝 New content added to inbox - running inbox processor...")
        # Automatically run inbox processor
        import subprocess
        try:
            result = subprocess.run([sys.executable, str(Path(__file__).parent / "process_inbox.py")],
                                  capture_output=True, text=True, timeout=300)
            if result.returncode == 0:
                print("✅ Inbox processing completed successfully")
                print("🔄 Running domain classifier...")
                # Automatically run domain classifier
                result2 = subprocess.run([sys.executable, str(Path(__file__).parent / "domain_classifier.py")],
                                       capture_output=True, text=True, timeout=300)
                if result2.returncode == 0:
                    print("✅ Domain classification completed successfully")
                else:
                    print(f"❌ Domain classification failed: {result2.stderr}")
            else:
                print(f"❌ Inbox processing failed: {result.stderr}")
        except subprocess.TimeoutExpired:
            print("❌ Processing timeout - run scripts manually")
        except Exception as e:
            print(f"❌ Error in automated processing: {e}")
    else:
        print("📭 No new content to process")

if __name__ == "__main__":
    main()