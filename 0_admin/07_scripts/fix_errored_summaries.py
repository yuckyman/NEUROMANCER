#!/usr/bin/env python3
"""
Fix Errored Summaries Script for NEUROMANCER
Regenerates summaries for files that have Ollama API 404 errors.
"""

import os
import re
import requests
import json
from pathlib import Path
from glob import glob

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")

def generate_summary(text_content: str, title: str = "", source: str = "") -> str:
    """Generates a summary of the given text content using an LLM via Ollama."""
    print(f"Generating summary using Ollama model '{OLLAMA_MODEL}'...")
    
    prompt = f"Please provide a concise summary of the following article:\n\n{text_content}\n\nSummary:"
    
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.3
        }
    }

    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        response.raise_for_status()
        
        response_data = response.json()
        summary = response_data.get("response", "No summary generated.").strip()
        return summary

    except requests.exceptions.RequestException as e:
        return f"Error communicating with Ollama API: {e}"
    except json.JSONDecodeError:
        return "Error decoding JSON response from Ollama API"
    except Exception as e:
        return f"An unexpected error occurred during summary generation: {e}"

def fix_errored_summaries():
    """Find and fix all files with errored summaries."""
    ideas_dir = Path("/home/ian/NEUROMANCER/1_ideas")

    fixed_count = 0
    error_count = 0

    # Find all markdown files
    md_files = list(ideas_dir.glob("*.md"))

    for file_path in md_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check if file has the error pattern
            if "Error communicating with Ollama API: 404 Client Error: Not Found for url:" in content:
                print(f"Processing: {file_path.name}")

                # Parse frontmatter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        frontmatter = parts[1]
                        body = parts[2].strip()

                        # Extract title from frontmatter
                        title_match = re.search(r'title:\s*(.+)', frontmatter)
                        title = title_match.group(1).strip("'\"") if title_match else ""

                        # Generate new summary
                        new_summary = generate_summary(body, title)

                        # Replace the error summary (handle multi-line)
                        error_start = "summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:"
                        
                        # Find the start and end of the error summary
                        start_idx = frontmatter.find(error_start)
                        if start_idx != -1:
                            # Find the closing quote
                            remaining = frontmatter[start_idx + len(error_start):]
                            end_idx = remaining.find("'")
                            if end_idx != -1:
                                full_error = error_start + remaining[:end_idx] + "'"
                                new_frontmatter = frontmatter.replace(full_error, f"summary: '{new_summary}'")
                            else:
                                print(f"  ✗ Could not find end of error summary in {file_path.name}")
                                error_count += 1
                                continue
                        else:
                            print(f"  ✗ Could not find error summary in {file_path.name}")
                            error_count += 1
                            continue

                        # Write back the file
                        new_content = f"---{new_frontmatter}---\n\n{body}"
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)

                        fixed_count += 1
                        print(f"  ✓ Fixed summary for {file_path.name}")
                    else:
                        print(f"  ✗ Could not parse frontmatter in {file_path.name}")
                        error_count += 1
                else:
                    print(f"  ✗ No frontmatter found in {file_path.name}")
                    error_count += 1
            else:
                print(f"  - No error found in {file_path.name}")

        except Exception as e:
            print(f"  ✗ Error processing {file_path.name}: {e}")
            error_count += 1

    print(f"\nSummary: Fixed {fixed_count} files, {error_count} errors")

if __name__ == "__main__":
    fix_errored_summaries()