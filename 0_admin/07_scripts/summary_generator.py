#!/usr/bin/env python3
"""
Summary Generator for NEUROMANCER
Generates summaries of articles using an LLM.
"""

import os
import requests
import json
from pathlib import Path

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:0.5b")

def generate_summary(text_content: str, title: str = "", source: str = "", date_posted: str = "", description: str = "") -> str:
    """Generates a summary of the given text content using an LLM via Ollama.

    Args:
        text_content: The full text content of the article.
        title: The article title.
        source: The source/feed name.
        date_posted: The publication date.
        description: A brief description if available.

    Returns:
        A string containing the generated summary, or a fallback summary if generation fails.
    """
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

    response = None # Initialize response to None
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=120)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        response_data = response.json()
        summary = response_data.get("response", "No summary generated.").strip()
        return summary

    except requests.exceptions.RequestException as e:
        # Generate fallback summary
        fallback = f"This article is titled '{title}'"
        if source:
            fallback += f", posted on {source}"
        if date_posted:
            fallback += f" on {date_posted}"
        fallback += "."
        if description:
            fallback += f" {description}"
        return fallback
    except json.JSONDecodeError:
        if response:
            return f"Error decoding JSON response from Ollama API: {response.text}"
        else:
            return "Error decoding JSON response from Ollama API: No response received."
    except Exception as e:
        return f"An unexpected error occurred during summary generation: {e}"
if __name__ == "__main__":
    # Example usage for testing
    sample_text = """
    Title: The Future of AI
    
    Artificial intelligence is rapidly advancing, with new breakthroughs happening constantly.
    From machine learning to deep neural networks, AI is transforming industries and daily life.
    Ethical considerations and societal impact are key discussion points as AI continues to evolve.
    """
    summary = generate_summary(sample_text)
    print(f"\nGenerated Summary:\n{summary}")
