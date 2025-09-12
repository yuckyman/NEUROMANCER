#!/usr/bin/env python3
"""
WINTERMUTE → NEUROMANCER sync script
Uses Obsidian Local REST API to pull #process tagged notes
"""

import requests
import json
import os
import shutil
from datetime import datetime
from pathlib import Path

# Configuration
OBSIDIAN_API_BASE = "http://localhost:27123"
API_KEY = ""  # Set this in environment or config
NEUROMANCER_ROOT = Path(__file__).parent.parent.parent
INGEST_DIR = NEUROMANCER_ROOT / "0_admin" / "03_ingest" / "automated"
PROCESSED_DIR = NEUROMANCER_ROOT / "0_admin" / "03_ingest" / "processed"

class WintermuteSyncer:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OBSIDIAN_API_KEY")
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def get_vault_notes(self):
        """Get all notes from WINTERMUTE vault"""
        try:
            response = requests.get(
                f"{OBSIDIAN_API_BASE}/vault/",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to get vault notes: {e}")
            return None
    
    def search_process_tagged(self):
        """Search for notes tagged with #process"""
        # This will depend on the actual API endpoints
        # Placeholder for now - need to test API first
        pass
    
    def get_note_content(self, note_path):
        """Get content of a specific note"""
        try:
            response = requests.get(
                f"{OBSIDIAN_API_BASE}/vault/{note_path}",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to get note {note_path}: {e}")
            return None
    
    def sync_tagged_notes(self):
        """Main sync function - pull #process tagged notes"""
        print("Starting WINTERMUTE sync...")
        
        # Test API connection first
        vault_info = self.get_vault_notes()
        if not vault_info:
            print("Cannot connect to Obsidian API")
            return
        
        print(f"Connected to vault: {vault_info}")
        
        # TODO: Implement actual search and sync logic
        # Need to explore API endpoints first
    
    def create_sync_log(self, synced_files):
        """Create log of sync operation"""
        timestamp = datetime.now().isoformat()
        log_entry = {
            "timestamp": timestamp,
            "files_synced": len(synced_files),
            "files": synced_files
        }
        
        log_file = NEUROMANCER_ROOT / "0_admin" / "01_inbox" / "sync_log.json"
        
        # Load existing log or create new
        if log_file.exists():
            with open(log_file, 'r') as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(log_entry)
        
        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)

if __name__ == "__main__":
    syncer = WintermuteSyncer()
    syncer.sync_tagged_notes()