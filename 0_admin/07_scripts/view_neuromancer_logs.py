#!/usr/bin/env python3
"""
NEUROMANCER Log Viewer
View and analyze NEUROMANCER's social monitoring logs
"""

import re
import sys
from pathlib import Path
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import argparse

def parse_log_file(log_file: Path) -> list:
    """Parse log file and extract structured data"""
    entries = []
    
    if not log_file.exists():
        print(f"❌ Log file not found: {log_file}")
        return entries
    
    with open(log_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Parse log line format: timestamp - logger - level - message
            match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - (\w+) - (\w+) - (.+)', line)
            if match:
                timestamp_str, logger, level, message = match.groups()
                timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
                
                entries.append({
                    'timestamp': timestamp,
                    'logger': logger,
                    'level': level,
                    'message': message
                })
    
    return entries

def analyze_findings(entries: list) -> dict:
    """Analyze log entries to extract insights"""
    analysis = {
        'total_entries': len(entries),
        'high_relevance_items': [],
        'medium_relevance_items': [],
        'sources': Counter(),
        'relevance_scores': [],
        'alerts_sent': 0,
        'time_range': None
    }
    
    if not entries:
        return analysis
    
    analysis['time_range'] = {
        'start': entries[0]['timestamp'],
        'end': entries[-1]['timestamp']
    }
    
    for entry in entries:
        message = entry['message']
        
        # Extract high relevance items
        if '🔥 HIGH RELEVANCE:' in message:
            score_match = re.search(r'\(score: ([\d.]+)\)', message)
            if score_match:
                score = float(score_match.group(1))
                analysis['relevance_scores'].append(score)
                analysis['high_relevance_items'].append({
                    'timestamp': entry['timestamp'],
                    'score': score,
                    'title': message.split('🔥 HIGH RELEVANCE: ')[1].split('...')[0] if '...' in message else message.split('🔥 HIGH RELEVANCE: ')[1]
                })
        
        # Extract medium relevance items
        elif '📊 MEDIUM RELEVANCE:' in message:
            score_match = re.search(r'\(score: ([\d.]+)\)', message)
            if score_match:
                score = float(score_match.group(1))
                analysis['relevance_scores'].append(score)
                analysis['medium_relevance_items'].append({
                    'timestamp': entry['timestamp'],
                    'score': score,
                    'title': message.split('📊 MEDIUM RELEVANCE: ')[1].split('...')[0] if '...' in message else message.split('📊 MEDIUM RELEVANCE: ')[1]
                })
        
        # Count alerts sent
        elif '✅ Alert sent for:' in message:
            analysis['alerts_sent'] += 1
        
        # Extract sources
        if 'Found' in message and 'new items to analyze' in message:
            # Extract source counts from log message
            hn_match = re.search(r'HN: (\d+)', message)
            reddit_match = re.search(r'Reddit: (\d+)', message)
            github_match = re.search(r'GitHub: (\d+)', message)
            
            if hn_match:
                analysis['sources']['Hacker News'] += int(hn_match.group(1))
            if reddit_match:
                analysis['sources']['Reddit'] += int(reddit_match.group(1))
            if github_match:
                analysis['sources']['GitHub'] += int(github_match.group(1))
    
    return analysis

def print_summary(analysis: dict):
    """Print a summary of the analysis"""
    print("🧠 NEUROMANCER Social Monitor Analysis")
    print("=" * 50)
    
    if analysis['time_range']:
        start = analysis['time_range']['start'].strftime('%Y-%m-%d %H:%M')
        end = analysis['time_range']['end'].strftime('%Y-%m-%d %H:%M')
        print(f"📅 Time Range: {start} to {end}")
    
    print(f"📊 Total Log Entries: {analysis['total_entries']}")
    print(f"🔥 High Relevance Items: {len(analysis['high_relevance_items'])}")
    print(f"📊 Medium Relevance Items: {len(analysis['medium_relevance_items'])}")
    print(f"📢 Alerts Sent: {analysis['alerts_sent']}")
    
    if analysis['sources']:
        print(f"\n📈 Sources Analyzed:")
        for source, count in analysis['sources'].most_common():
            print(f"  • {source}: {count} items")
    
    if analysis['relevance_scores']:
        avg_score = sum(analysis['relevance_scores']) / len(analysis['relevance_scores'])
        max_score = max(analysis['relevance_scores'])
        print(f"\n🎯 Relevance Scores:")
        print(f"  • Average: {avg_score:.2f}")
        print(f"  • Highest: {max_score:.2f}")
        print(f"  • Total Scored: {len(analysis['relevance_scores'])}")

def print_high_relevance_items(analysis: dict, limit: int = 10):
    """Print high relevance items"""
    if not analysis['high_relevance_items']:
        print("\n🔥 No high relevance items found")
        return
    
    print(f"\n🔥 Top {min(limit, len(analysis['high_relevance_items']))} High Relevance Items:")
    print("-" * 60)
    
    for i, item in enumerate(analysis['high_relevance_items'][:limit], 1):
        timestamp = item['timestamp'].strftime('%m-%d %H:%M')
        print(f"{i:2d}. [{item['score']:.2f}] {timestamp} - {item['title']}")

def print_medium_relevance_items(analysis: dict, limit: int = 5):
    """Print medium relevance items"""
    if not analysis['medium_relevance_items']:
        print("\n📊 No medium relevance items found")
        return
    
    print(f"\n📊 Top {min(limit, len(analysis['medium_relevance_items']))} Medium Relevance Items:")
    print("-" * 60)
    
    for i, item in enumerate(analysis['medium_relevance_items'][:limit], 1):
        timestamp = item['timestamp'].strftime('%m-%d %H:%M')
        print(f"{i:2d}. [{item['score']:.2f}] {timestamp} - {item['title']}")

def print_recent_activity(entries: list, hours: int = 24):
    """Print recent activity"""
    cutoff = datetime.now() - timedelta(hours=hours)
    recent_entries = [e for e in entries if e['timestamp'] > cutoff]
    
    print(f"\n🕐 Recent Activity (Last {hours} hours):")
    print("-" * 40)
    
    if not recent_entries:
        print("No recent activity found")
        return
    
    # Group by hour
    hourly_activity = defaultdict(list)
    for entry in recent_entries:
        hour = entry['timestamp'].strftime('%Y-%m-%d %H:00')
        hourly_activity[hour].append(entry)
    
    for hour in sorted(hourly_activity.keys())[-6:]:  # Last 6 hours
        entries_in_hour = hourly_activity[hour]
        high_relevance = len([e for e in entries_in_hour if '🔥 HIGH RELEVANCE:' in e['message']])
        medium_relevance = len([e for e in entries_in_hour if '📊 MEDIUM RELEVANCE:' in e['message']])
        alerts = len([e for e in entries_in_hour if '✅ Alert sent for:' in e['message']])
        
        print(f"{hour}: {high_relevance} high, {medium_relevance} medium, {alerts} alerts")

def main():
    parser = argparse.ArgumentParser(description='View NEUROMANCER social monitoring logs')
    parser.add_argument('--log-file', default='neuromancer_social_monitor.log', help='Log file to analyze')
    parser.add_argument('--high-limit', type=int, default=10, help='Number of high relevance items to show')
    parser.add_argument('--medium-limit', type=int, default=5, help='Number of medium relevance items to show')
    parser.add_argument('--recent-hours', type=int, default=24, help='Hours of recent activity to show')
    parser.add_argument('--summary-only', action='store_true', help='Show only summary statistics')
    
    args = parser.parse_args()
    
    # Find log file
    script_dir = Path(__file__).parent
    log_file = script_dir / args.log_file
    
    # Parse and analyze logs
    entries = parse_log_file(log_file)
    analysis = analyze_findings(entries)
    
    # Print results
    print_summary(analysis)
    
    if not args.summary_only:
        print_high_relevance_items(analysis, args.high_limit)
        print_medium_relevance_items(analysis, args.medium_limit)
        print_recent_activity(entries, args.recent_hours)
    
    print(f"\n📁 Log file: {log_file}")
    print(f"💡 Use --help for more options")

if __name__ == "__main__":
    main()

