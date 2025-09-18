#!/usr/bin/env python3
"""
Domain Classifier for NEUROMANCER
Automatically moves articles from 1_ideas to appropriate 2_domain_amplification subfolders
"""

import os
import json
import shutil
import re
import hashlib
from pathlib import Path
from datetime import datetime
import yaml

# Configuration
IDEAS_DIR = Path("/home/ian/NEUROMANCER/1_ideas")
DOMAIN_DIR = Path("/home/ian/NEUROMANCER/2_domain_amplification")
CONFIG_FILE = Path("/home/ian/NEUROMANCER/0_admin/07_scripts/domain_config.json")
HASH_REGISTRY = Path("/home/ian/NEUROMANCER/0_admin/07_scripts/content_hashes.json")

# Domain mapping with keywords and patterns
DOMAIN_CONFIG = {
    "24_computing": {
        "patterns": [
            r"(?i)(computer vision|machine learning|deep learning|neural network|ai|artificial intelligence)",
            r"(?i)(algorithm|data structure|programming|software|code|development)",
            r"(?i)(python|javascript|typescript|rust|golang|java|c\+\+)",
            r"(?i)(gpu|cuda|tensorflow|pytorch|scikit|pandas|numpy)"
        ],
        "tags": ["computer-vision", "machine-learning", "programming", "ai", "software"],
        "description": "Computing, AI, and software development"
    },
    "25_foss": {
        "patterns": [
            r"(?i)(open source|foss|free software|linux|git|github|gitlab)",
            r"(?i)(privacy|security|encryption|p2p|decentralized|blockchain)",
            r"(?i)(self.?hosting|docker|kubernetes|infrastructure|devops)",
            r"(?i)(mesh.?network|nostr|activity.?pub|fediverse|web3)"
        ],
        "tags": ["open-source", "privacy", "selfhosting", "decentralized", "foss"],
        "description": "Free/open source software, privacy, and decentralized systems"
    },
    "26_brain_imaging": {
        "patterns": [
            r"(?i)(fmri|diffusion.?mri|mri|brain.?imaging|neuroimaging)",
            r"(?i)(eeg|meg|brain|neural|cognitive|neurological)",
            r"(?i)(medical.?imaging|tumor|diagnosis|healthcare|clinical)",
            r"(?i)(axon|myelin|cortex|hippocampus|neuroscience)"
        ],
        "tags": ["brain-imaging", "neuroimaging", "neuroscience", "medical-imaging"],
        "description": "Brain imaging, neuroscience, and medical imaging"
    }
}

class DomainClassifier:
    def __init__(self):
        self.config = self.load_config()
        self.processed_files = set(self.config.get("processed_files", []))
        self.stats = self.config.get("stats", {"total_processed": 0, "by_domain": {}})
        self.hash_registry = self.load_hash_registry()

    def load_hash_registry(self):
        """Load content hash registry for deduplication"""
        if HASH_REGISTRY.exists():
            try:
                with open(HASH_REGISTRY, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {"processed_hashes": {}, "duplicate_count": 0}

    def load_config(self):
        """Load configuration and processing history"""
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        return {"processed_files": [], "stats": {"total_processed": 0, "by_domain": {}}}

    def save_config(self):
        """Save configuration and processing history"""
        config = {
            "processed_files": list(self.processed_files),
            "stats": self.stats,
            "last_run": datetime.now().isoformat()
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)

        # Save updated hash registry
        with open(HASH_REGISTRY, 'w', encoding='utf-8') as f:
            json.dump(self.hash_registry, f, indent=2)

    def extract_frontmatter(self, file_path):
        """Extract YAML frontmatter from markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if content.startswith('---'):
                end_pos = content.find('---', 3)
                if end_pos != -1:
                    frontmatter_text = content[3:end_pos]
                    return yaml.safe_load(frontmatter_text)
        except Exception as e:
            print(f"Error reading frontmatter from {file_path}: {e}")

        return {}

    def check_content_duplicate(self, file_path):
        """Check if content is a duplicate using hash registry"""
        frontmatter = self.extract_frontmatter(file_path)

        # Check if content_hash exists in frontmatter
        content_hash = frontmatter.get('content_hash')
        if content_hash and content_hash in self.hash_registry['processed_hashes']:
            duplicate_info = self.hash_registry['processed_hashes'][content_hash]
            print(f"⚠️  Content duplicate detected! Hash: {content_hash[:16]}...")
            print(f"   Original file: {duplicate_info['file']}")
            print(f"   Original domain: {duplicate_info.get('domain', 'unknown')}")
            return True

        return False

    def classify_article(self, file_path):
        """Classify article based on content, tags, and patterns"""
        frontmatter = self.extract_frontmatter(file_path)

        # Get content for analysis
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None

        # Extract text after frontmatter for analysis
        if content.startswith('---'):
            end_pos = content.find('---', 3)
            if end_pos != -1:
                content = content[end_pos + 3:]

        # Check tags first (most reliable)
        article_tags = frontmatter.get('tags', [])
        if isinstance(article_tags, str):
            article_tags = [article_tags]

        for domain, config in DOMAIN_CONFIG.items():
            # Check if any article tags match domain tags
            if any(tag in config['tags'] for tag in article_tags):
                return domain

        # Check content patterns
        content_lower = content.lower()
        for domain, config in DOMAIN_CONFIG.items():
            for pattern in config['patterns']:
                if re.search(pattern, content_lower):
                    return domain

        return None

    def move_article(self, source_path, target_domain):
        """Move article to target domain folder"""
        target_dir = DOMAIN_DIR / target_domain
        target_dir.mkdir(exist_ok=True)

        filename = Path(source_path).name
        target_path = target_dir / filename

        # Handle filename conflicts
        counter = 1
        while target_path.exists():
            stem = target_path.stem
            suffix = target_path.suffix
            target_path = target_dir / f"{stem}_{counter:02d}{suffix}"
            counter += 1

        # Move file (destructive)
        shutil.move(source_path, target_path)

        # Update frontmatter with new category
        self.update_frontmatter(target_path, target_domain)

        return target_path

    def update_frontmatter(self, file_path, domain):
        """Update frontmatter with domain-specific category"""
        frontmatter = self.extract_frontmatter(file_path)

        # Update category
        frontmatter['category'] = domain.replace('_', '-')

        # Add domain-specific tags if not present
        if 'tags' not in frontmatter:
            frontmatter['tags'] = []

        if isinstance(frontmatter['tags'], str):
            frontmatter['tags'] = [frontmatter['tags']]

        domain_config = DOMAIN_CONFIG.get(domain, {})
        domain_tags = domain_config.get('tags', [])

        # Add missing domain tags
        for tag in domain_tags:
            if tag not in frontmatter['tags']:
                frontmatter['tags'].append(tag)

        # Reconstruct file with updated frontmatter
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if content.startswith('---'):
                end_pos = content.find('---', 3)
                if end_pos != -1:
                    after_frontmatter = content[end_pos + 3:]

                    # Write updated file
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write('---\n')
                        yaml.dump(frontmatter, f, default_flow_style=False, sort_keys=False)
                        f.write('---\n')
                        f.write(after_frontmatter)

        except Exception as e:
            print(f"Error updating frontmatter for {file_path}: {e}")

    def process_articles(self, dry_run=False, limit=None):
        """Process articles in 1_ideas directory"""
        print("🔍 Scanning 1_ideas directory...")

        # Get all markdown files
        md_files = list(IDEAS_DIR.glob("*.md"))

        if not md_files:
            print("No markdown files found in 1_ideas")
            return

        print(f"📄 Found {len(md_files)} markdown files")

        processed_count = 0
        moved_count = 0

        for file_path in md_files:
            if limit and processed_count >= limit:
                break

            filename = file_path.name

            # Skip if already processed
            if filename in self.processed_files:
                continue

            print(f"🔎 Analyzing: {filename}")

            # Check for content duplicates first
            if self.check_content_duplicate(file_path):
                print(f"  🚫 Skipping duplicate content: {filename}")
                # Mark as processed to avoid rechecking
                self.processed_files.add(filename)
                processed_count += 1
                continue

            # Classify article
            target_domain = self.classify_article(file_path)

            if target_domain:
                print(f"  ✅ Classified as: {target_domain}")

                if not dry_run:
                    try:
                        target_path = self.move_article(file_path, target_domain)
                        print(f"  📁 Moved to: {target_path}")

                        # Update hash registry with domain info
                        frontmatter = self.extract_frontmatter(file_path)
                        content_hash = frontmatter.get('content_hash')
                        if content_hash and content_hash in self.hash_registry['processed_hashes']:
                            self.hash_registry['processed_hashes'][content_hash]['domain'] = target_domain
                            self.hash_registry['processed_hashes'][content_hash]['moved_date'] = datetime.now().isoformat()

                        # Update stats
                        if target_domain not in self.stats["by_domain"]:
                            self.stats["by_domain"][target_domain] = 0
                        self.stats["by_domain"][target_domain] += 1
                        self.stats["total_processed"] += 1
                        moved_count += 1

                    except Exception as e:
                        print(f"  ❌ Error moving {filename}: {e}")
                else:
                    print(f"  📁 Would move to: {DOMAIN_DIR / target_domain / filename}")
                    moved_count += 1
            else:
                print("  🤔 No suitable domain found")

            # Mark as processed
            self.processed_files.add(filename)
            processed_count += 1

        print("\n📊 Processing Summary:")
        print(f"  Total files analyzed: {processed_count}")
        print(f"  Files moved: {moved_count}")
        print(f"  Files skipped: {processed_count - moved_count}")

        if not dry_run:
            self.save_config()

    def show_stats(self):
        """Display processing statistics"""
        print("📈 Domain Classification Statistics:")
        print(f"  Total processed: {self.stats['total_processed']}")
        print("  By domain:")

        for domain, count in self.stats["by_domain"].items():
            description = DOMAIN_CONFIG.get(domain, {}).get('description', 'Unknown')
            print(f"    {domain}: {count} articles ({description})")

def main():
    """Main function"""
    import argparse

    parser = argparse.ArgumentParser(description="Domain Classifier for NEUROMANCER")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--limit", type=int, help="Limit number of files to process")
    parser.add_argument("--stats", action="store_true", help="Show processing statistics")
    parser.add_argument("--reset", action="store_true", help="Reset processing history")

    args = parser.parse_args()

    classifier = DomainClassifier()

    if args.reset:
        print("🔄 Resetting processing history...")
        classifier.processed_files.clear()
        classifier.stats = {"total_processed": 0, "by_domain": {}}
        classifier.save_config()
        print("✅ Processing history reset")
        return

    if args.stats:
        classifier.show_stats()
        return

    print("🚀 NEUROMANCER Domain Classifier Starting...")
    classifier.process_articles(dry_run=args.dry_run, limit=args.limit)

if __name__ == "__main__":
    main()