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
import re
import requests
from pathlib import Path
import fitz  # PyMuPDF for PDF processing
import docx  # python-docx for Word documents
import mimetypes
from PIL import Image
import pytesseract

# Paths
INBOX_DIR = "/home/ian/NEUROMANCER/0_admin/01_inbox"
TEMPLATES_DIR = "/home/ian/NEUROMANCER/0_admin/02_templates"
PROCESSED_DIR = "/home/ian/NEUROMANCER/1_ideas"  # Following johnny decimal flow

def get_ollama_tags_and_summary(content):
    """Use ollama to analyze content and generate tags + summary"""

    # Create shorter prompt for faster processing
    # Prioritize original content over scraped content for preview
    original_content = content.split('\n\n## Scraped from')[0]
    content_preview = original_content[:1000] + "..." if len(original_content) > 1000 else original_content

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
            timeout=60
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

def extract_urls(content):
    """Extract URLs from text content"""
    url_pattern = r'https?://[^\s<>"\']+'
    return re.findall(url_pattern, content)

def scrape_url(url, timeout=10):
    """Scrape content from a URL"""
    try:
        response = requests.get(url, timeout=timeout, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; InboxProcessor/1.0)'
        })
        response.raise_for_status()

        # Try to get text content, fallback to raw text
        if 'text/html' in response.headers.get('content-type', ''):
            # Simple HTML to text conversion
            text = response.text
            # Remove script and style elements
            text = re.sub(r'<script[^>]*>.*?</script>', '', text, flags=re.DOTALL | re.IGNORECASE)
            text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
            # Remove HTML tags
            text = re.sub(r'<[^>]+>', '', text)
            # Clean up whitespace
            text = re.sub(r'\s+', ' ', text).strip()
            return text[:2000] + "..." if len(text) > 2000 else text
        else:
            return response.text[:2000] + "..." if len(response.text) > 2000 else response.text

    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

def extract_text_from_pdf(file_path):
    """Extract text content from PDF files"""
    try:
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()

        # Clean up excessive whitespace
        text = re.sub(r'\n+', '\n', text)
        text = re.sub(r' +', ' ', text)
        return text.strip()
    except Exception as e:
        return f"Error extracting PDF text: {str(e)}"

def extract_text_from_docx(file_path):
    """Extract text content from Word documents"""
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error extracting DOCX text: {str(e)}"

def extract_text_from_image(file_path):
    """Extract text from images using OCR"""
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"Error extracting image text: {str(e)}"

def extract_file_content(file_path):
    """Extract text content from various file types"""
    mime_type, _ = mimetypes.guess_type(file_path)
    file_extension = os.path.splitext(file_path)[1].lower()

    # Handle different file types
    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension in ['.docx', '.doc']:
        return extract_text_from_docx(file_path)
    elif file_extension in ['.png', '.jpg', '.jpeg', '.tiff', '.bmp']:
        return extract_text_from_image(file_path)
    elif file_extension == '.txt':
        # Handle text files as before
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read().strip()
        except Exception as e:
            return f"Error reading text file: {str(e)}"
    else:
        # For unsupported file types, return file info
        file_size = os.path.getsize(file_path)
        return f"File: {os.path.basename(file_path)}\nType: {mime_type or 'Unknown'}\nSize: {file_size} bytes\n\nNote: This file type is not directly supported for text extraction. Consider converting to PDF or text format."

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

    # Create safe filename - remove URLs from title for cleaner filenames
    title_without_urls = re.sub(r'https?://[^\s]+', '', metadata['title']).strip()
    if not title_without_urls:
        title_without_urls = metadata['title'][:30]  # Fallback if title is only URLs
    safe_title = "".join(c for c in title_without_urls if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_title = safe_title.replace(' ', '_')[:50]
    filename = f"{date_str}_{safe_title}.md"

    # Clean title for display (keep URLs but make it readable)
    display_title = metadata['title']
    if len(display_title) > 80:
        display_title = display_title[:77] + "..."

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

# {display_title}

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
    # Process all supported file types
    supported_patterns = ["*.txt", "*.pdf", "*.docx", "*.doc", "*.png", "*.jpg", "*.jpeg"]
    all_files = []

    for pattern in supported_patterns:
        all_files.extend(glob.glob(os.path.join(INBOX_DIR, pattern)))

    # Also include any file that might be a phone shortcut (numeric names)
    all_files.extend(glob.glob(os.path.join(INBOX_DIR, "*")))
    all_files = list(set(all_files))  # Remove duplicates

    if not all_files:
        return

    print(f"Processing {len(all_files)} files...")

    for file_path in all_files:
        try:
            basename = os.path.basename(file_path)
            file_extension = os.path.splitext(file_path)[1].lower()

            print(f"Processing {file_path}")

            # Extract content based on file type
            content = extract_file_content(file_path)

            if not content or content.strip() == "":
                print(f"No content extracted from {basename}, removing...")
                os.remove(file_path)
                continue

            # Check for URLs and scrape if found (only for text-based content)
            urls = []
            scraped_content = ""
            successful_scrapes = []

            if file_extension in ['.txt', '.pdf', '.docx', '.doc']:
                urls = extract_urls(content)

            if urls:
                print(f"Found {len(urls)} URLs, scraping...")
                for url in urls[:3]:  # Limit to 3 URLs to avoid overload
                    print(f"Scraping: {url}")
                    scraped = scrape_url(url)
                    if scraped and not scraped.startswith("Error"):
                        scraped_content += f"\n\n## Scraped from {url}\n{scraped}\n"
                        successful_scrapes.append(scraped)
                    else:
                        print(f"Failed to scrape: {url}")

            # Combine original content with scraped content
            full_content = content + scraped_content

            # Get metadata from ollama (use original content + truncated scrapes for analysis)
            analysis_content = content
            if successful_scrapes:
                # Truncate each scrape to 200 chars for ollama
                truncated_scrapes = [scrape[:200] + "..." if len(scrape) > 200 else scrape for scrape in successful_scrapes[:2]]
                analysis_content += "\n\nAdditional context from links:\n" + "\n".join(truncated_scrapes)
            metadata = get_ollama_tags_and_summary(analysis_content)

            # Create markdown file
            md_file = create_markdown_file(metadata, full_content, file_path)

            print(f"Created: {md_file}")

            # Remove original file
            os.remove(file_path)
            print(f"Removed: {file_path}")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs(PROCESSED_DIR, exist_ok=True)
    process_inbox()