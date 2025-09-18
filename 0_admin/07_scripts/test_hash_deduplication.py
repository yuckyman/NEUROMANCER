#!/usr/bin/env python3
"""
Test script for SHA-256 hash deduplication functionality
"""

import os
import json
import hashlib
import re
from pathlib import Path

def calculate_content_hash(content):
    """Calculate SHA-256 hash of content for deduplication"""
    # Normalize content for consistent hashing
    normalized = content.strip().lower()
    # Remove extra whitespace
    normalized = re.sub(r'\s+', ' ', normalized)
    return hashlib.sha256(normalized.encode('utf-8')).hexdigest()

def test_hash_functionality():
    """Test the hash deduplication functionality"""
    print("🧪 Testing SHA-256 Hash Deduplication")
    print("=" * 50)

    # Test content normalization
    test_content1 = """
    This is a test article about machine learning.
    It contains information about AI and neural networks.
    """

    test_content2 = """
    THIS IS A TEST ARTICLE ABOUT MACHINE LEARNING.
    IT CONTAINS INFORMATION ABOUT AI AND NEURAL NETWORKS.
    """

    test_content3 = """
    This is a different article about web development.
    It talks about JavaScript and React.
    """

    # Calculate hashes
    hash1 = calculate_content_hash(test_content1)
    hash2 = calculate_content_hash(test_content2)
    hash3 = calculate_content_hash(test_content3)

    print(f"Content 1 hash: {hash1}")
    print(f"Content 2 hash: {hash2}")
    print(f"Content 3 hash: {hash3}")
    print()

    # Test hash consistency (same content should have same hash)
    if hash1 == hash2:
        print("✅ Hash normalization working: Same content produces same hash")
    else:
        print("❌ Hash normalization failed: Different hashes for same content")

    # Test hash uniqueness (different content should have different hashes)
    if hash1 != hash3 and hash2 != hash3:
        print("✅ Hash uniqueness working: Different content produces different hashes")
    else:
        print("❌ Hash uniqueness failed: Same hash for different content")

    print()
    print("📊 Hash Registry Structure:")
    print("-" * 30)

    # Show example registry structure
    example_registry = {
        "processed_hashes": {
            hash1: {
                "file": "2025-09-18_Test_Article.md",
                "date": "2025-09-18T10:30:00",
                "original_file": "test.txt",
                "source": "inbox_processing",
                "domain": "24_computing"
            }
        },
        "duplicate_count": 0
    }

    print(json.dumps(example_registry, indent=2))

    print()
    print("🎯 Deduplication Benefits:")
    print("- Prevents duplicate content across RSS feeds")
    print("- Avoids processing the same article multiple times")
    print("- Maintains content integrity across domains")
    print("- Tracks processing history with timestamps")

if __name__ == "__main__":
    test_hash_functionality()