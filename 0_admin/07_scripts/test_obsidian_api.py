#!/usr/bin/env python3
"""
Test script to explore Obsidian Local REST API endpoints
"""

import requests
import json
from pprint import pprint

API_BASE = "http://127.0.0.1:27123"
API_KEY = "332636bd56cb244f8535ce6f5dfcc38f6ab5a5b36855fc013f23813764a77b38"

def test_connection():
    """Test basic API connection"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.get(f"{API_BASE}/", headers=headers)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        return True
    except requests.RequestException as e:
        print(f"Connection failed: {e}")
        return False

def explore_endpoints():
    """Try common REST API patterns to discover endpoints"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    endpoints_to_try = [
        "/",
        "/vault",
        "/vault/",
        "/notes", 
        "/notes/",
        "/search",
        "/tags",
        "/api",
        "/docs",
        "/vault/0_admin/01_inbox/dev_log.md",  # try getting a specific file
        "/search?query=process",  # try searching
        "/search?query=tag:process"  # try tag search
    ]
    
    for endpoint in endpoints_to_try:
        try:
            response = requests.get(f"{API_BASE}{endpoint}", headers=headers)
            print(f"\n{endpoint}: {response.status_code}")
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"JSON response: {json.dumps(data, indent=2)[:500]}...")
                except:
                    print(f"Text response: {response.text[:200]}...")
            elif response.status_code == 404:
                print("Not found")
            else:
                print(f"Error: {response.text[:100]}")
        except Exception as e:
            print(f"{endpoint}: Error - {e}")

if __name__ == "__main__":
    print("Testing Obsidian Local REST API connection...")
    
    if test_connection():
        print("\nExploring available endpoints...")
        explore_endpoints()
    else:
        print("\nMake sure:")
        print("1. Obsidian is running")
        print("2. Local REST API plugin is installed and enabled")
        print("3. API is configured to run on port 27123")