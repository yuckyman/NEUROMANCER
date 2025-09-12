#!/usr/bin/env python3
"""
Check which vault the REST API is currently serving
"""

import requests
import json

API_BASE = "http://127.0.0.1:27123"
API_KEY = "332636bd56cb244f8535ce6f5dfcc38f6ab5a5b36855fc013f23813764a77b38"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def check_active_vault():
    try:
        # Get vault structure
        response = requests.get(f"{API_BASE}/vault/", headers=headers)
        if response.status_code == 200:
            files = response.json().get("files", [])
            
            # Check for wintermute indicators
            wintermute_indicators = [
                "0_admin",  # both have this
                "1_life",   # wintermute specific structure
                "2_domain_amplification",
                "sync.ffs_db"  # wintermute specific file
            ]
            
            # Check for neuromancer indicators  
            neuromancer_indicators = [
                "3_projects/repos",  # neuromancer specific
                "README.md"  # likely neuromancer's readme
            ]
            
            print(f"📁 Current vault files: {files}")
            
            # Try to detect vault by checking for specific files
            if "sync.ffs_db" in files:
                print("🧠 WINTERMUTE vault is active!")
                return "wintermute"
            elif any("repos" in str(f) for f in files):
                print("🤖 NEUROMANCER vault is active!")  
                return "neuromancer"
            else:
                print("❓ Cannot determine which vault is active")
                return "unknown"
                
        else:
            print(f"❌ Failed to get vault info: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"❌ Error checking vault: {e}")
        return None

if __name__ == "__main__":
    print("Checking which vault is currently served by REST API...")
    vault = check_active_vault()
    
    if vault == "wintermute":
        print("\n✅ Perfect! We can now search for #process tagged notes in WINTERMUTE")
    elif vault == "neuromancer":
        print("\n⚠️  Need to focus WINTERMUTE window to access its content")
        print("   Try clicking on the WINTERMUTE obsidian window and run this again")
    else:
        print("\n❓ Could not determine vault - check obsidian windows")