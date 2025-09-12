#!/usr/bin/env python3
"""
Discover Obsidian REST API endpoints by trying common patterns
"""

import requests
import json

API_BASE = "http://127.0.0.1:27123"
API_KEY = "332636bd56cb244f8535ce6f5dfcc38f6ab5a5b36855fc013f23813764a77b38"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def try_vault_file_access():
    """Try different ways to access files in the vault"""
    
    # Get vault contents first
    vault_resp = requests.get(f"{API_BASE}/vault/", headers=headers)
    if vault_resp.status_code == 200:
        files = vault_resp.json().get("files", [])
        print("Vault files:", files)
    
    # Try accessing specific files with different patterns
    file_patterns = [
        "/vault/0_admin/01_inbox/dev_log.md",
        "/vault/0_admin%2F01_inbox%2Fdev_log.md",  # URL encoded
        "/vault/0_admin/01_inbox/dev_log",  # without .md
        "/files/0_admin/01_inbox/dev_log.md",
        "/content/0_admin/01_inbox/dev_log.md"
    ]
    
    for pattern in file_patterns:
        try:
            resp = requests.get(f"{API_BASE}{pattern}", headers=headers)
            print(f"{pattern}: {resp.status_code}")
            if resp.status_code == 200:
                print(f"Success! Response: {resp.text[:200]}...")
        except Exception as e:
            print(f"{pattern}: Error - {e}")

def try_search_endpoints():
    """Try different search endpoint patterns"""
    search_patterns = [
        "/search?q=process",
        "/search?query=process",
        "/search?text=process", 
        "/search/process",
        "/find?q=process",
        "/query?q=process",
        "/vault/search?q=process"
    ]
    
    for pattern in search_patterns:
        try:
            resp = requests.get(f"{API_BASE}{pattern}", headers=headers)
            print(f"{pattern}: {resp.status_code}")
            if resp.status_code == 200:
                print(f"Search success! Response: {resp.text[:300]}...")
        except Exception as e:
            print(f"{pattern}: Error - {e}")

def try_list_all_files():
    """Try to get a recursive file listing"""
    patterns = [
        "/vault/?recursive=true",
        "/vault/files",
        "/vault/all",
        "/files",
        "/all"
    ]
    
    for pattern in patterns:
        try:
            resp = requests.get(f"{API_BASE}{pattern}", headers=headers)
            print(f"{pattern}: {resp.status_code}")
            if resp.status_code == 200:
                print(f"File listing: {resp.text[:400]}...")
        except Exception as e:
            print(f"{pattern}: Error - {e}")

if __name__ == "__main__":
    print("🔍 Discovering Obsidian API endpoints...")
    
    print("\n📁 Trying vault file access...")
    try_vault_file_access()
    
    print("\n🔎 Trying search endpoints...")
    try_search_endpoints()
    
    print("\n📋 Trying file listings...")
    try_list_all_files()