#!/usr/bin/env python3
"""
Demo script to show what NEUROMANCER Discord alerts would look like
"""

import json
from datetime import datetime

def create_demo_alert():
    """Create a demo Discord alert to show the format"""
    
    # Simulate a high-relevance item
    item = {
        'title': '[D] Self-Promotion Thread - Share your ML projects and research',
        'url': 'https://www.reddit.com/r/MachineLearning/comments/1n67lft/d_selfpromotion_thread/',
        'source': 'reddit',
        'subreddit': 'MachineLearning'
    }
    
    relevance_score = 0.80
    reason = "The subreddit r/MachineLearning is a broad forum, but the 'Self-Promotion Thread' format immediately suggests a space for sharing research and projects. Given Ian's strong interest in computational neuroscience and BCI research, coupled with his broader interest in machine learning and AI agents, this thread provides a potential venue to share work, seek collaborators, or discuss relevant advancements."
    
    bias_info = {
        'biased': False,
        'issues': []
    }
    
    # Create Discord embed with casual tone
    embed = {
        "title": f"🔥 {item['title']}",
        "url": item['url'],
        "color": 0x00ff00,  # Green for high relevance
        "fields": [
            {
                "name": "why this matters",
                "value": reason,
                "inline": False
            },
            {
                "name": "relevance",
                "value": f"{relevance_score:.1f}/1.0",
                "inline": True
            },
            {
                "name": "source",
                "value": "Hacker News 🔥 HN is going wild about this",
                "inline": True
            },
            {
                "name": "hn score",
                "value": "42 points, 15 comments",
                "inline": True
            }
        ],
        "footer": {
            "text": f"neuromancer • {datetime.now().strftime('%m-%d %H:%M')}"
        }
    }
    
    alert_data = {
        "content": "dude, pause fortnite and check this out:",
        "embeds": [embed]
    }
    
    return alert_data

def main():
    print("🧠 NEUROMANCER Discord Alert Demo")
    print("=" * 50)
    print()
    
    alert = create_demo_alert()
    
    print("📱 Discord Message:")
    print(f"Content: {alert['content']}")
    print()
    
    print("📋 Embed Details:")
    embed = alert['embeds'][0]
    print(f"Title: {embed['title']}")
    print(f"URL: {embed['url']}")
    print(f"Color: #{embed['color']:06x}")
    print()
    
    print("📊 Fields:")
    for field in embed['fields']:
        print(f"  • {field['name']}: {field['value']}")
    
    print()
    print("🎯 This is what you'd see in Discord when NEUROMANCER finds something relevant!")
    print("💡 The system learns from your behavior to improve relevance scoring over time.")
    print("🔥 Now with way more casual, fun messaging - like your actual friend!")
    
    # Save demo to file for reference
    with open('/Users/ian/NEUROMANCER/0_admin/07_scripts/demo_alert.json', 'w') as f:
        json.dump(alert, f, indent=2)
    
    print(f"\n📁 Demo saved to: /Users/ian/NEUROMANCER/0_admin/07_scripts/demo_alert.json")

if __name__ == "__main__":
    main()
