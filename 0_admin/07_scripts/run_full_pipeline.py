#!/usr/bin/env python3
"""
NEUROMANCER Full Pipeline Runner
Orchestrates the complete workflow: RSS → Inbox → Ideas → Domain Classification
"""

import os
import sys
import subprocess
from pathlib import Path

def run_script(script_name, description, timeout=600):
    """Run a script and return success status"""
    script_path = Path(__file__).parent / script_name

    if not script_path.exists():
        print(f"❌ Script not found: {script_path}")
        return False

    print(f"🚀 Running {description}...")

    try:
        result = subprocess.run([sys.executable, str(script_path)],
                              capture_output=True, text=True, timeout=timeout)

        if result.returncode == 0:
            print(f"✅ {description} completed successfully")
            return True
        else:
            print(f"❌ {description} failed:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            return False

    except subprocess.TimeoutExpired:
        print(f"❌ {description} timed out after {timeout} seconds")
        return False
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def main():
    """Run the complete NEUROMANCER pipeline"""
    print("🎯 NEUROMANCER Full Pipeline Starting...")

    # Step 1: RSS Ingestion
    if not run_script("rss_ingestor.py", "RSS Feed Ingestion"):
        print("❌ Pipeline stopped at RSS ingestion")
        return False

    # Step 2: Inbox Processing (automatically calls domain classifier)
    if not run_script("process_inbox.py", "Inbox Processing"):
        print("❌ Pipeline stopped at inbox processing")
        return False

    # Step 3: Domain Classification (should already be called by process_inbox.py)
    # But let's run it again to be safe in case of any issues
    if not run_script("domain_classifier.py", "Domain Classification"):
        print("❌ Pipeline stopped at domain classification")
        return False

    print("🎉 NEUROMANCER Pipeline completed successfully!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)