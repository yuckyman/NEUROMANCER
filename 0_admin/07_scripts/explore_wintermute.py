#!/usr/bin/env python3
"""
Explore WINTERMUTE vault content via REST API
"""

import requests
import json
import urllib.parse

API_BASE = "http://127.0.0.1:27123"
API_KEY = "332636bd56cb244f8535ce6f5dfcc38f6ab5a5b36855fc013f23813764a77b38"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_folder_contents(folder_path=""):
    """Get contents of a specific folder"""
    try:
        url = f"{API_BASE}/vault/{folder_path}" if folder_path else f"{API_BASE}/vault/"
        response = requests.get(url, headers=headers)
        print(f"📁 {folder_path or 'root'}: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            files = data.get("files", [])
            print(f"   Contents: {files}")
            return files
        else:
            print(f"   Error: {response.text[:100]}")
            return []
    except Exception as e:
        print(f"   Error: {e}")
        return []

def try_get_file_content(file_path):
    """Try different ways to get file content"""
    patterns = [
        f"/vault/{file_path}",
        f"/vault/{urllib.parse.quote(file_path)}",
        f"/vault/{file_path.replace('.md', '')}",
        f"/content/{file_path}",
        f"/file/{file_path}",
        f"/notes/{file_path}"
    ]
    
    print(f"\n📄 Trying to read: {file_path}")
    for pattern in patterns:
        try:
            response = requests.get(f"{API_BASE}{pattern}", headers=headers)
            print(f"   {pattern}: {response.status_code}")
            
            if response.status_code == 200:
                content = response.text[:300] if len(response.text) > 300 else response.text
                print(f"   ✅ SUCCESS! Content preview: {content}...")
                return response.text
        except Exception as e:
            print(f"   {pattern}: Error - {e}")
    
    print(f"   ❌ Could not read {file_path}")
    return None

def explore_inbox():
    """Explore the inbox folder where new content might be"""
    print("🔍 Exploring 0_admin/01_inbox...")
    inbox_files = get_folder_contents("0_admin/01_inbox")
    
    # Try to read one of the files if any exist
    if inbox_files:
        test_file = inbox_files[0] if inbox_files[0].endswith('.md') else None
        if test_file:
            full_path = f"0_admin/01_inbox/{test_file}"
            try_get_file_content(full_path)

if __name__ == "__main__":
    print("🔍 Exploring WINTERMUTE vault structure...")
    
    # Get root contents
    root_files = get_folder_contents()
    
    # Explore some folders
    if "0_admin" in [f.rstrip('/') for f in root_files]:
        admin_files = get_folder_contents("0_admin")
        if "01_inbox/" in admin_files:
            explore_inbox()
    
    print("\n💡 If we can read files, we can search for #process tags manually by:")
    print("   1. Getting all .md files recursively") 
    print("   2. Reading each file's content")
    print("   3. Searching for #process in the content")