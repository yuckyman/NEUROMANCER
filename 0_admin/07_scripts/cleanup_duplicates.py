#!/usr/bin/env python3
"""
Duplicate cleanup script for NEUROMANCER vault.
Uses SBP pair analysis to identify and safely remove duplicate files.
"""

import os
import json
import requests
from pathlib import Path
from typing import List, Dict, Tuple
import shutil
from datetime import datetime

# Configuration
SBP_API_URL = "http://localhost:8001"
VAULT_ROOT = "/Users/ian/NEUROMANCER"
BACKUP_DIR = "/Users/ian/NEUROMANCER/0_admin/07_scripts/duplicate_backups"
SIMILARITY_THRESHOLD = 0.95  # Only consider 95%+ similar as duplicates

def call_sbp_api(endpoint: str, data: dict) -> dict:
    """Call the SBP FastAPI server."""
    try:
        response = requests.post(f"{SBP_API_URL}/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error calling SBP API: {e}")
        return {}

def get_duplicate_pairs(directory: str = "1_ideas", threshold: float = 0.95) -> List[Dict]:
    """Get duplicate pairs from SBP analysis."""
    print(f"🔍 Finding duplicates in {directory} with {threshold*100}%+ similarity...")
    
    data = {
        "dir": directory,
        "n_neighbors": 100,  # Get more pairs to analyze
        "threshold": threshold
    }
    
    result = call_sbp_api("pair", data)
    pairs = result.get("pairs", [])
    
    print(f"Found {len(pairs)} pairs with {threshold*100}%+ similarity")
    return pairs

def analyze_duplicates(pairs: List[Dict]) -> Dict[str, List[str]]:
    """Analyze pairs to identify files that appear in multiple duplicate relationships."""
    file_duplicates = {}
    
    for pair in pairs:
        note1 = pair.get("note1", "")
        note2 = pair.get("note2", "")
        similarity = pair.get("similarity", 0)
        
        if not note1 or not note2:
            continue
            
        # Extract just the filename from the full path
        file1 = os.path.basename(note1)
        file2 = os.path.basename(note2)
        
        # Group files that are duplicates of each other
        if file1 not in file_duplicates:
            file_duplicates[file1] = []
        if file2 not in file_duplicates[file1]:
            file_duplicates[file1].append(file2)
            
        # Also add reverse relationship
        if file2 not in file_duplicates:
            file_duplicates[file2] = []
        if file1 not in file_duplicates[file2]:
            file_duplicates[file2].append(file1)
    
    return file_duplicates

def create_backup_dir():
    """Create backup directory with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{BACKUP_DIR}_{timestamp}"
    os.makedirs(backup_path, exist_ok=True)
    return backup_path

def backup_file(file_path: str, backup_dir: str) -> str:
    """Backup a file before deletion."""
    if not os.path.exists(file_path):
        return None
        
    filename = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, filename)
    
    # If backup already exists, add timestamp
    if os.path.exists(backup_path):
        name, ext = os.path.splitext(filename)
        timestamp = datetime.now().strftime("%_H%M%S")
        backup_path = os.path.join(backup_dir, f"{name}_{timestamp}{ext}")
    
    shutil.copy2(file_path, backup_path)
    return backup_path

def get_file_info(file_path: str) -> Dict:
    """Get file information for comparison."""
    if not os.path.exists(file_path):
        return {}
        
    stat = os.stat(file_path)
    return {
        "path": file_path,
        "size": stat.st_size,
        "modified": stat.st_mtime,
        "created": stat.st_ctime
    }

def choose_keep_file(files: List[str]) -> str:
    """Choose which file to keep based on heuristics."""
    file_infos = []
    
    for file_path in files:
        full_path = os.path.join(VAULT_ROOT, "1_ideas", file_path)
        info = get_file_info(full_path)
        if info:
            file_infos.append((file_path, info))
    
    if not file_infos:
        return files[0] if files else None
    
    # Heuristics for choosing which file to keep:
    # 1. Prefer files with more descriptive names (longer, more specific)
    # 2. Prefer newer files (higher modification time)
    # 3. Prefer larger files (more content)
    
    def score_file(file_info):
        filename, info = file_info
        name_score = len(filename)  # Longer names often more descriptive
        time_score = info["modified"]  # Newer is better
        size_score = info["size"]  # Larger is better
        
        return (name_score * 0.3 + time_score * 0.4 + size_score * 0.3)
    
    best_file = max(file_infos, key=score_file)
    return best_file[0]

def cleanup_duplicates(directory: str = "1_ideas", dry_run: bool = True):
    """Clean up duplicate files."""
    print(f"🧹 {'DRY RUN: ' if dry_run else ''}Cleaning duplicates in {directory}")
    
    # Get duplicate pairs
    pairs = get_duplicate_pairs(directory, SIMILARITY_THRESHOLD)
    if not pairs:
        print("No duplicates found!")
        return
    
    # Analyze duplicates
    file_duplicates = analyze_duplicates(pairs)
    
    # Group files into duplicate clusters
    clusters = []
    processed = set()
    
    for file1, duplicates in file_duplicates.items():
        if file1 in processed:
            continue
            
        cluster = [file1] + duplicates
        clusters.append(cluster)
        processed.update(cluster)
    
    print(f"\n📊 Found {len(clusters)} duplicate clusters:")
    
    # Create backup directory
    backup_dir = create_backup_dir() if not dry_run else None
    
    deleted_count = 0
    kept_count = 0
    
    for i, cluster in enumerate(clusters, 1):
        print(f"\n--- Cluster {i} ({len(cluster)} files) ---")
        
        # Choose which file to keep
        keep_file = choose_keep_file(cluster)
        files_to_delete = [f for f in cluster if f != keep_file]
        
        print(f"✅ KEEP: {keep_file}")
        kept_count += 1
        
        for file_to_delete in files_to_delete:
            full_path = os.path.join(VAULT_ROOT, "1_ideas", file_to_delete)
            
            if dry_run:
                print(f"🗑️  WOULD DELETE: {file_to_delete}")
            else:
                # Backup before deletion
                backup_path = backup_file(full_path, backup_dir)
                if backup_path:
                    print(f"💾 BACKED UP: {file_to_delete} -> {backup_path}")
                
                # Delete the file
                try:
                    os.remove(full_path)
                    print(f"🗑️  DELETED: {file_to_delete}")
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ ERROR deleting {file_to_delete}: {e}")
    
    print(f"\n📈 Summary:")
    print(f"   Files kept: {kept_count}")
    print(f"   Files {'would be ' if dry_run else ''}deleted: {deleted_count}")
    
    if not dry_run and backup_dir:
        print(f"   Backups saved to: {backup_dir}")
    
    return deleted_count

def main():
    """Main function."""
    print("🔍 NEUROMANCER Duplicate Cleanup Tool")
    print("=" * 50)
    
    # Check if SBP server is running
    try:
        response = requests.get(f"{SBP_API_URL}/status")
        if response.status_code != 200:
            print("❌ SBP server is not running. Please start it first.")
            return
    except:
        print("❌ Cannot connect to SBP server. Please start it first.")
        return
    
    # Run dry run first
    print("\n🔍 Running dry run to show what would be deleted...")
    dry_run_count = cleanup_duplicates("1_ideas", dry_run=True)
    
    if dry_run_count == 0:
        print("\n✅ No duplicates found to clean up!")
        return
    
    # Ask for confirmation
    print("\n" + "=" * 50)
    response = input("Proceed with actual deletion? (yes/no): ").lower().strip()
    
    if response in ['yes', 'y']:
        print("\n🗑️  Proceeding with deletion...")
        deleted_count = cleanup_duplicates("1_ideas", dry_run=False)
        print(f"\n✅ Cleanup complete! Deleted {deleted_count} duplicate files.")
    else:
        print("\n❌ Cleanup cancelled.")

if __name__ == "__main__":
    main()
