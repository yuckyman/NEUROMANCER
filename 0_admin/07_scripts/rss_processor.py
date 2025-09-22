#!/usr/bin/env python3
"""
RSS Content Processor for NEUROMANCER
Processes raw RSS text files from the inbox and further categorizes/enriches them.
"""

import os
import sys
import re
import hashlib
import yaml
import json
from datetime import datetime
from pathlib import Path
from summary_generator import generate_summary
from domain_classifier import DOMAIN_CONFIG

# Configuration
INBOX_RSS_DIR = Path(__file__).parent.parent / "01_inbox/rss_txt"
IDEAS_DIR = Path(__file__).parent.parent.parent / "1_ideas"
HASH_REGISTRY = Path(__file__).parent / "content_hashes.json"

def load_hash_registry():
    """Load content hash registry for deduplication"""
    if HASH_REGISTRY.exists():
        try:
            with open(HASH_REGISTRY, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
    return {"processed_hashes": {}, "duplicate_count": 0}

def save_hash_registry(registry):
    """Save content hash registry"""
    with open(HASH_REGISTRY, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)

def classify_content(content, title):
    """Classify content based on patterns and keywords"""
    content_lower = content.lower()
    
    for domain, config in DOMAIN_CONFIG.items():
        # Check content patterns
        for pattern in config['patterns']:
            if re.search(pattern, content_lower):
                return domain
    
    return None

def process_rss_entry(filepath: Path):
    """Process a single RSS entry file: summarize, tag, format, and move."""
    print(f"Processing: {filepath.name}")

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title, link, and full content
        content_lines = content.splitlines()
        
        # Parse the RSS file format
        feed_title = "N/A"
        feed_url = "N/A"
        link = "N/A"
        title = filepath.stem.replace("_rss_", "").replace("_", " ")
        
        # Extract metadata from first few lines
        if len(content_lines) >= 3:
            if content_lines[0].startswith("RSS Feed:"):
                feed_title = content_lines[0].replace("RSS Feed:", "").strip()
            if content_lines[1].startswith("Source:"):
                feed_url = content_lines[1].replace("Source:", "").strip()
            if content_lines[2].startswith("Link:"):
                link = content_lines[2].replace("Link:", "").strip()
        
        # Find the title (usually line 4 or 5)
        title_line = ""
        for i, line in enumerate(content_lines):
            if i >= 4 and line.strip() and not line.startswith("by ") and len(line.strip()) > 10:
                title_line = line.strip()
                break
        
        if title_line:
            title = title_line
        
        # Extract article body (everything after the title)
        article_body = ""
        title_found = False
        for line in content_lines:
            if line.strip() == title_line:
                title_found = True
                continue
            if title_found and line.strip():
                article_body += line + "\n"
        
        article_body = article_body.strip()

        if not article_body:
            print(f"Warning: No discernible article body found in {filepath.name}. Skipping summarization and classification.")
            return

        # Generate summary
        summary = generate_summary(article_body, title, feed_title, "", "")
        print(f"  Summary generated: {summary[:100]}...")

        # Classify content to get tags
        target_domain = classify_content(article_body, title)
        tags = DOMAIN_CONFIG.get(target_domain, {}).get('tags', []) if target_domain else ["unclassified"]
        print(f"  Classified tags: {tags}")

        # Generate content hash for deduplication
        full_markdown_content = f"---\ntitle: {title}\nlink: {link}\nsummary: {summary}\ntags: {tags}\n---\n\n{article_body}"
        content_hash = hashlib.sha256(full_markdown_content.encode('utf-8')).hexdigest()

        # Load hash registry and check for duplicates
        hash_registry = load_hash_registry()
        if content_hash in hash_registry['processed_hashes']:
            print(f"  🚫 Duplicate content detected (hash: {content_hash[:8]}). Skipping {filepath.name}.")
            hash_registry['duplicate_count'] += 1
            save_hash_registry(hash_registry)
            # Delete the original raw text file
            os.remove(filepath)
            print(f"  🗑️ Deleted raw file: {filepath.name}")
            return

        # Prepare YAML frontmatter
        frontmatter = {
            "title": title,
            "link": link,
            "summary": summary,
            "tags": tags,
            "content_hash": content_hash,
            "feed_title": feed_title,
            "feed_url": feed_url,
            "date_processed": datetime.now().isoformat()
        }
        if target_domain:
            frontmatter["category"] = target_domain.replace('_', '-')

        # Construct final Markdown content
        markdown_content = f"---\n{yaml.dump(frontmatter, default_flow_style=False, sort_keys=False)}---\n\n{article_body}"

        # Create new Markdown filename
        safe_title = re.sub(r'[^\w\-_\.]', '_', title)[:50]
        md_filename = f"{datetime.now().strftime("%Y%m%d_%H%M%S")}_idea_{safe_title}.md"
        md_filepath = IDEAS_DIR / md_filename
        IDEAS_DIR.mkdir(parents=True, exist_ok=True)

        with open(md_filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"  📝 Created Markdown file: {md_filename}")

        # Update hash registry
        hash_registry['processed_hashes'][content_hash] = {
            "file": str(md_filepath),
            "original_raw_file": str(filepath),
            "processed_date": datetime.now().isoformat(),
            "domain": target_domain
        }
        save_hash_registry(hash_registry)

        # Delete the original raw text file
        os.remove(filepath)
        print(f"  🗑️ Deleted raw file: {filepath.name}")

    except Exception as e:
        print(f"Error processing {filepath.name}: {e}")

def main():
    """Main RSS processing function"""
    print("🧠 NEUROMANCER RSS Processor Starting...")

    if not INBOX_RSS_DIR.exists():
        print(f"Error: Inbox directory not found at {INBOX_RSS_DIR}")
        sys.exit(1)

    processed_count = 0
    for filepath in INBOX_RSS_DIR.iterdir():
        if filepath.is_file() and filepath.suffix == '.txt':
            process_rss_entry(filepath)
            processed_count += 1
    
    print(f"✅ RSS processing complete! Processed {processed_count} entries.")

if __name__ == "__main__":
    main()