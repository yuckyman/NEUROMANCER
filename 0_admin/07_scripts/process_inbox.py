#!/usr/bin/env python3
"""
Inbox processor for NEUROMANCER
Processes text files from phone shortcuts, adds tags via ollama, converts to markdown
"""

import os
import glob
import json
import subprocess
import datetime
from pathlib import Path

# Paths
INBOX_DIR = "/home/ian/NEUROMANCER/0_admin/01_inbox"
TEMPLATES_DIR = "/home/ian/NEUROMANCER/0_admin/02_templates"
PROCESSED_DIR = "/home/ian/NEUROMANCER/1_ideas"  # Following johnny decimal flow

def get_ollama_tags_and_summary(content):
    """Use ollama to analyze content and generate tags + summary"""

    # Create shorter prompt for faster processing
    content_preview = content[:1000] + "..." if len(content) > 1000 else content

    prompt = f"""Analyze this content briefly and respond ONLY with valid JSON:

Content: {content_preview}

Required JSON format:
{{"title": "short title", "category": "ideas", "tags": ["tag1", "tag2"], "summary": "brief summary", "type": "note"}}

Categories: development, projects, ideas, reference, personal
Common tags: dev-log, project, research, idea, technical, personal, urgent, reference"""

    try:
        result = subprocess.run(
            ["ollama", "run", "qwen2.5:0.5b", prompt],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            print(f"Ollama error: {result.stderr}")
            return default_metadata(content)

        # Parse JSON response
        response = result.stdout.strip()
        # Sometimes ollama adds extra text, try to extract JSON
        if "```json" in response:
            response = response.split("```json")[1].split("```")[0]
        elif "{" in response:
            start = response.find("{")
            end = response.rfind("}") + 1
            response = response[start:end]

        return json.loads(response)

    except (subprocess.TimeoutExpired, json.JSONDecodeError, Exception) as e:
        print(f"Error processing with ollama: {e}")
        return default_metadata(content)

def default_metadata(content):
    """Fallback metadata if ollama fails"""
    title = content.split('\n')[0][:50] if content.strip() else "Inbox Note"
    return {
        "title": title,
        "category": "ideas",
        "tags": ["inbox", "unprocessed"],
        "summary": content[:200] + "..." if len(content) > 200 else content,
        "type": "note"
    }

def create_markdown_file(metadata, content, original_file):
    """Create markdown file with frontmatter"""
    now = datetime.datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M")

    # Create safe filename
    safe_title = "".join(c for c in metadata['title'] if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title.replace(' ', '_')[:50]
    filename = f"{date_str}_{safe_title}.md"

    frontmatter = f"""---
type: {metadata['type']}
category: {metadata['category']}
created: {time_str}
modified: {time_str}
tags: {metadata['tags']}
status: draft
source: inbox_processing
original_file: {os.path.basename(original_file)}
---

# {metadata['title']}

## summary
{metadata['summary']}

## content
{content}

## connections
- processed from phone shortcut
"""

    filepath = os.path.join(PROCESSED_DIR, filename)

    # Ensure unique filename
    counter = 1
    while os.path.exists(filepath):
        base, ext = os.path.splitext(filename)
        filename = f"{base}_{counter:02d}{ext}"
        filepath = os.path.join(PROCESSED_DIR, filename)
        counter += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(frontmatter)

    return filepath

def process_inbox():
    """Main processing function"""
    txt_files = glob.glob(os.path.join(INBOX_DIR, "*.txt"))

    if not txt_files:
        return

    print(f"Processing {len(txt_files)} files...")

    for txt_file in txt_files:
        try:
            # Skip files that don't look like phone shortcut files (numeric names)
            basename = os.path.basename(txt_file)
            if not basename.replace('.txt', '').isdigit():
                print(f"Skipping non-numeric file: {basename}")
                continue

            print(f"Processing {txt_file}")

            # Read content
            with open(txt_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()

            if not content:
                os.remove(txt_file)
                continue

            # Get metadata from ollama
            metadata = get_ollama_tags_and_summary(content)

            # Create markdown file
            md_file = create_markdown_file(metadata, content, txt_file)

            print(f"Created: {md_file}")

            # Remove original text file
            os.remove(txt_file)
            print(f"Removed: {txt_file}")

        except Exception as e:
            print(f"Error processing {txt_file}: {e}")

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    process_inbox()