#!/usr/bin/env python3
"""
NEUROMANCER Sync Agent
Tool for pulling #process tagged files from WINTERMUTE to NEUROMANCER ingest

Designed to be called by agents or automation systems
"""

import os
import sys
import json
import shutil
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional
import re

# Configuration
NEUROMANCER_ROOT = Path(__file__).parent.parent.parent
INGEST_DIR = NEUROMANCER_ROOT / "0_admin" / "03_ingest" / "automated"
PROCESSED_DIR = NEUROMANCER_ROOT / "0_admin" / "03_ingest" / "processed"
WINTERMUTE_PATH = Path.home() / "WINTERMUTE"

class SyncAgent:
    def __init__(self, wintermute_path=None):
        self.wintermute_path = Path(wintermute_path) if wintermute_path else WINTERMUTE_PATH
        self.sync_log = []
    
    def find_process_tagged_files(self) -> List[Dict]:
        """Fallback method: search filesystem for #process tagged files"""
        tagged_files = []
        
        if not self.wintermute_path.exists():
            print(f"❌ WINTERMUTE path not found: {self.wintermute_path}")
            return tagged_files
        
        print(f"🔍 Searching {self.wintermute_path} for #process tagged files...")
        
        # Search all markdown files
        for md_file in self.wintermute_path.rglob("*.md"):
            try:
                content = md_file.read_text(encoding='utf-8', errors='ignore')
                
                # Check for #process tag (exact match) in content or frontmatter
                if self._has_process_tag(content) or 'process' in self._extract_frontmatter_tags(content):
                    tagged_files.append({
                        'path': str(md_file),
                        'name': md_file.name,
                        'modified': datetime.fromtimestamp(md_file.stat().st_mtime).isoformat(),
                        'size': md_file.stat().st_size,
                        'content': content[:500] + "..." if len(content) > 500 else content
                    })
                    print(f"  ✅ Found: {md_file.name}")
            except Exception as e:
                print(f"  ⚠️  Error reading {md_file.name}: {e}")
        
        return tagged_files
    
    def _extract_frontmatter_tags(self, content: str) -> List[str]:
        """Extract tags from YAML frontmatter"""
        if not content.startswith('---'):
            return []
        
        try:
            # Extract frontmatter section
            end_marker = content.find('---', 3)
            if end_marker == -1:
                return []
            
            frontmatter = content[3:end_marker]
            
            # Look for tags line
            for line in frontmatter.split('\n'):
                if line.strip().startswith('tags:'):
                    # Parse tags array/list
                    tags_match = re.search(r'tags:\s*\[(.*?)\]', line)
                    if tags_match:
                        tags_str = tags_match.group(1)
                        return [tag.strip().strip('"\'') for tag in tags_str.split(',')]
            
            return []
        except:
            return []
    
    def _has_process_tag(self, content: str) -> bool:
        """Check if content contains exactly #process tag (not #processing, #processcommand, etc.)"""
        # Use word boundary regex to match #process exactly
        import re
        pattern = r'#process\b'
        return bool(re.search(pattern, content.lower()))
    
    
    def copy_files_to_ingest(self, files: List[Dict]) -> Dict:
        """Copy found files to neuromancer ingest directory"""
        results = {
            'success': [],
            'errors': [],
            'skipped': []
        }
        
        # Ensure ingest directory exists
        INGEST_DIR.mkdir(parents=True, exist_ok=True)
        
        for file_info in files:
            try:
                source_path = Path(file_info['path'])
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                dest_name = f"{timestamp}_{source_path.stem}.md"
                dest_path = INGEST_DIR / dest_name
                
                # Check if already processed recently
                if dest_path.exists():
                    results['skipped'].append(file_info['name'])
                    continue
                
                # Copy file with metadata preservation
                shutil.copy2(source_path, dest_path)
                
                # Add processing metadata to file
                self._add_processing_metadata(dest_path, file_info)
                
                results['success'].append({
                    'name': file_info['name'],
                    'dest': str(dest_path),
                    'modified': file_info['modified']
                })
                
                print(f"  📋 Copied: {file_info['name']} → {dest_name}")
                
            except Exception as e:
                results['errors'].append({
                    'name': file_info['name'], 
                    'error': str(e)
                })
                print(f"  ❌ Error copying {file_info['name']}: {e}")
        
        return results
    
    def _add_processing_metadata(self, dest_path: Path, file_info: Dict):
        """Add neuromancer processing metadata to copied file"""
        try:
            content = dest_path.read_text(encoding='utf-8')
            
            # Check if already has frontmatter
            if content.startswith('---'):
                # Insert processing metadata into existing frontmatter
                end_marker = content.find('---', 3)
                if end_marker != -1:
                    frontmatter = content[3:end_marker]
                    body = content[end_marker + 3:]
                    
                    processing_meta = f"\nsync_imported: {datetime.now().isoformat()}\nsource_path: {file_info['path']}\nprocessing_status: pending"
                    
                    new_content = f"---{frontmatter}{processing_meta}\n---{body}"
                    dest_path.write_text(new_content, encoding='utf-8')
            else:
                # Add new frontmatter
                processing_meta = f"""---
sync_imported: {datetime.now().isoformat()}
source_path: {file_info['path']}
processing_status: pending
type: imported
category: automated
tags: [imported, process]
---

{content}"""
                dest_path.write_text(processing_meta, encoding='utf-8')
        
        except Exception as e:
            print(f"  ⚠️  Could not add metadata to {dest_path.name}: {e}")
    
    def create_sync_report(self, results: Dict) -> Path:
        """Create detailed sync report"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = NEUROMANCER_ROOT / "0_admin" / "01_inbox" / f"sync_report_{timestamp}.md"
        
        report = f"""---
type: sync_report
category: admin
created: {datetime.now().isoformat()}
tags: [sync, automation, report]
status: completed
---

# sync agent report - {timestamp}

## summary
- **files found**: {len(results['success']) + len(results['errors']) + len(results['skipped'])}
- **successfully synced**: {len(results['success'])}
- **skipped (already synced)**: {len(results['skipped'])}
- **errors**: {len(results['errors'])}

## successfully synced files
"""
        
        for file in results['success']:
            report += f"- ✅ **{file['name']}** → `{Path(file['dest']).name}`\n"
        
        if results['skipped']:
            report += f"\n## skipped files\n"
            for name in results['skipped']:
                report += f"- ⏭️  **{name}** (already processed recently)\n"
        
        if results['errors']:
            report += f"\n## errors\n"
            for error in results['errors']:
                report += f"- ❌ **{error['name']}**: {error['error']}\n"
        
        report += f"\n## next steps\n"
        if results['success']:
            report += "- review imported files in `0_admin/03_ingest/automated/`\n"
            report += "- run processing agent to analyze content\n"
            report += "- check generated insights in appropriate domain folders\n"
        else:
            report += "- no new files to process\n"
            report += "- consider checking if files are properly tagged with #process\n"
        
        report_path.write_text(report, encoding='utf-8')
        return report_path
    
    def run_sync(self) -> Dict:
        """Main sync operation"""
        print("🚀 NEUROMANCER Sync Agent Starting...")
        print("📡 Using filesystem search method")
        
        # Find tagged files
        tagged_files = self.find_process_tagged_files()
        
        print(f"🔍 Found {len(tagged_files)} #process tagged files")
        
        if not tagged_files:
            print("💤 No files to sync")
            return {'files_found': 0, 'results': None}
        
        # Copy files to ingest
        results = self.copy_files_to_ingest(tagged_files)
        
        # Create report
        report_path = self.create_sync_report(results)
        print(f"📊 Sync report created: {report_path.name}")
        
        print("✅ Sync complete!")
        return {
            'files_found': len(tagged_files),
            'results': results,
            'report': str(report_path)
        }

def main():
    parser = argparse.ArgumentParser(description='NEUROMANCER Sync Agent')
    parser.add_argument('--wintermute-path', help='Custom WINTERMUTE vault path')
    parser.add_argument('--dry-run', action='store_true', 
                       help='Show what would be synced without copying')
    
    args = parser.parse_args()
    
    agent = SyncAgent(wintermute_path=args.wintermute_path)
    
    if args.dry_run:
        print("🧪 DRY RUN MODE - No files will be copied")
        files = agent.find_process_tagged_files()
        
        print(f"Would sync {len(files)} files:")
        for file_info in files:
            print(f"  - {file_info['name']} ({file_info['size']} bytes)")
    else:
        result = agent.run_sync()
        return 0 if result['files_found'] >= 0 else 1

if __name__ == "__main__":
    sys.exit(main())