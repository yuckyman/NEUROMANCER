#!/usr/bin/env python3
"""
Quick test to verify REST API is working with authentication
"""

import requests
import json

API_BASE = "http://127.0.0.1:27123"
API_KEY = "332636bd56cb244f8535ce6f5dfcc38f6ab5a5b36855fc013f23813764a77b38"

def test_with_auth():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        # Test basic connection
        response = requests.get(f"{API_BASE}/", headers=headers, timeout=5)
        print(f"✅ Connection successful! Status: {response.status_code}")
        print(f"Response: {response.text[:300]}...")
        
        # Try to get vault info
        vault_response = requests.get(f"{API_BASE}/vault/", headers=headers, timeout=5)
        print(f"\n📁 Vault endpoint: {vault_response.status_code}")
        if vault_response.status_code == 200:
            try:
                vault_data = vault_response.json()
                print(f"Vault info: {json.dumps(vault_data, indent=2)[:300]}...")
            except:
                print(f"Vault response: {vault_response.text[:200]}...")
        
        return True
    except requests.exceptions.ConnectionError:
        print("❌ Connection refused - plugin not running")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("Testing Obsidian REST API with authentication...")
    test_with_auth()