---
type: implementation-guide
category: photo-organization
created: 2025-09-13
tags: [implementation, photo-organization, vision-models, wintermute]
status: active
---

# photo organization system implementation

step-by-step guide for implementing vision-based photo metadata extraction and organization

## prerequisites

### system setup
- macbook m4 pro with 24gb unified memory ✓
- ollama installed and configured
- python 3.11+ environment
- access to WINTERMUTE photo vault (read-only)
- NEUROMANCER processing space

### model installation
```bash
# install optimal vision model for m4 pro
ollama pull llama3.2-vision:11b

# alternative lightweight option
ollama pull llava:7b

# test vision capability
ollama run llama3.2-vision:11b "describe this image" < test_photo.jpg
```

## phase 1: prototype development

### basic photo processor script
```python
# photo_metadata_processor.py
import json
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime

class PhotoMetadataProcessor:
    def __init__(self, model="llama3.2-vision:11b"):
        self.model = model
        self.processed_count = 0

    def get_file_hash(self, filepath):
        """generate sha256 hash for file integrity"""
        sha256_hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()

    def analyze_photo(self, photo_path):
        """send photo to ollama vision model"""
        prompt = """Analyze this photo and provide:
1. A brief scene description
2. Detailed description for searchability
3. List of objects/subjects present
4. Color palette (dominant colors)
5. Mood/atmosphere
6. Photography style/technique
7. Any text visible in the image
8. Location hints if identifiable
9. Season/weather indicators

Format as JSON with keys: scene, detailed, objects, colors, mood, style, text, location_hints, season_weather"""

        cmd = ["ollama", "run", self.model, prompt]
        with open(photo_path, 'rb') as f:
            result = subprocess.run(cmd, input=f.read(), capture_output=True, text=True)

        return result.stdout.strip()

    def process_photo(self, photo_path, output_dir):
        """process single photo and generate metadata"""
        photo_path = Path(photo_path)
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # generate metadata filename
        metadata_file = output_dir / f"{photo_path.stem}.json"

        # skip if already processed and current
        if metadata_file.exists():
            with open(metadata_file) as f:
                existing = json.load(f)
            if existing.get('file_info', {}).get('hash') == self.get_file_hash(photo_path):
                print(f"Skipping {photo_path.name} - already processed")
                return

        print(f"Processing {photo_path.name}...")

        # analyze photo
        analysis = self.analyze_photo(photo_path)

        # create metadata structure
        metadata = {
            "file_info": {
                "path": str(photo_path),
                "hash": self.get_file_hash(photo_path),
                "size": photo_path.stat().st_size,
                "modified": datetime.fromtimestamp(photo_path.stat().st_mtime).isoformat()
            },
            "vision_analysis": {
                "model": self.model,
                "processed": datetime.now().isoformat(),
                "raw_output": analysis
            }
        }

        # save metadata
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)

        self.processed_count += 1
        print(f"Saved metadata to {metadata_file}")

# usage example
if __name__ == "__main__":
    processor = PhotoMetadataProcessor()
    processor.process_photo("~/WINTERMUTE/photos/sample.jpg", "~/NEUROMANCER/metadata")
```

### test with sample photos
```bash
# create test environment
mkdir -p ~/NEUROMANCER/photo_processing/metadata
mkdir -p ~/NEUROMANCER/photo_processing/logs

# test with a few photos
python photo_metadata_processor.py
```

## phase 2: batch processing system

### directory scanner and processor
```python
# batch_photo_processor.py
import os
import logging
from pathlib import Path
from photo_metadata_processor import PhotoMetadataProcessor

class BatchPhotoProcessor:
    def __init__(self, wintermute_path, neuromancer_path):
        self.wintermute = Path(wintermute_path)
        self.neuromancer = Path(neuromancer_path)
        self.metadata_dir = self.neuromancer / "photo_metadata"
        self.processor = PhotoMetadataProcessor()

        # setup logging
        logging.basicConfig(
            filename=self.neuromancer / "photo_processing.log",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def scan_photos(self, extensions=('.jpg', '.jpeg', '.png', '.heic')):
        """scan wintermute for photos"""
        photos = []
        for ext in extensions:
            photos.extend(self.wintermute.rglob(f"*{ext}"))
            photos.extend(self.wintermute.rglob(f"*{ext.upper()}"))
        return sorted(photos)

    def process_batch(self, limit=None):
        """process photos in batches"""
        photos = self.scan_photos()
        if limit:
            photos = photos[:limit]

        logging.info(f"Starting batch processing of {len(photos)} photos")

        for i, photo in enumerate(photos):
            try:
                # create relative path structure in metadata dir
                rel_path = photo.relative_to(self.wintermute)
                metadata_subdir = self.metadata_dir / rel_path.parent

                self.processor.process_photo(photo, metadata_subdir)

                if (i + 1) % 10 == 0:
                    logging.info(f"Processed {i + 1}/{len(photos)} photos")

            except Exception as e:
                logging.error(f"Error processing {photo}: {e}")
                continue

        logging.info(f"Batch processing complete. Processed {self.processor.processed_count} new photos")

# usage
if __name__ == "__main__":
    processor = BatchPhotoProcessor(
        "~/WINTERMUTE",
        "~/NEUROMANCER/photo_processing"
    )
    processor.process_batch(limit=50)  # start with 50 photos
```

## phase 3: search system

### metadata database creation
```python
# metadata_database.py
import sqlite3
import json
from pathlib import Path

class MetadataDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """create database schema"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS photo_metadata (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_path TEXT UNIQUE,
                file_hash TEXT,
                file_size INTEGER,
                modified_date TEXT,
                processed_date TEXT,
                model_used TEXT,
                scene_description TEXT,
                detailed_description TEXT,
                objects TEXT,  -- json array
                colors TEXT,   -- json array
                mood TEXT,
                style TEXT,
                visible_text TEXT,
                location_hints TEXT,
                season_weather TEXT,
                raw_metadata TEXT  -- full json
            )
        """)

        # create full-text search index
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS photo_search USING fts5(
                file_path,
                scene_description,
                detailed_description,
                objects,
                mood,
                style,
                visible_text,
                location_hints,
                season_weather
            )
        """)

        conn.commit()
        conn.close()

    def ingest_metadata(self, metadata_dir):
        """ingest json metadata files into database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        for metadata_file in Path(metadata_dir).rglob("*.json"):
            with open(metadata_file) as f:
                data = json.load(f)

            # extract fields from metadata
            file_info = data.get('file_info', {})
            analysis = json.loads(data.get('vision_analysis', {}).get('raw_output', '{}'))

            cursor.execute("""
                INSERT OR REPLACE INTO photo_metadata
                (file_path, file_hash, file_size, modified_date, processed_date,
                 model_used, scene_description, detailed_description, objects,
                 colors, mood, style, visible_text, location_hints, season_weather, raw_metadata)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                file_info.get('path'),
                file_info.get('hash'),
                file_info.get('size'),
                file_info.get('modified'),
                data.get('vision_analysis', {}).get('processed'),
                data.get('vision_analysis', {}).get('model'),
                analysis.get('scene', ''),
                analysis.get('detailed', ''),
                json.dumps(analysis.get('objects', [])),
                json.dumps(analysis.get('colors', [])),
                analysis.get('mood', ''),
                analysis.get('style', ''),
                analysis.get('text', ''),
                analysis.get('location_hints', ''),
                analysis.get('season_weather', ''),
                json.dumps(data)
            ))

            # add to search index
            cursor.execute("""
                INSERT OR REPLACE INTO photo_search
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                file_info.get('path'),
                analysis.get('scene', ''),
                analysis.get('detailed', ''),
                ' '.join(analysis.get('objects', [])),
                analysis.get('mood', ''),
                analysis.get('style', ''),
                analysis.get('text', ''),
                analysis.get('location_hints', ''),
                analysis.get('season_weather', '')
            ))

        conn.commit()
        conn.close()

    def search(self, query):
        """search photos by natural language query"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT file_path, scene_description, detailed_description
            FROM photo_search
            WHERE photo_search MATCH ?
            ORDER BY rank
        """, (query,))

        results = cursor.fetchall()
        conn.close()
        return results

# search interface
if __name__ == "__main__":
    db = MetadataDatabase("~/NEUROMANCER/photo_processing/photos.db")
    db.ingest_metadata("~/NEUROMANCER/photo_processing/metadata")

    # example searches
    results = db.search("sunset mountain lake")
    for path, scene, detailed in results:
        print(f"{path}: {scene}")
```

## phase 4: automation and integration

### scheduled processing script
```bash
#!/bin/bash
# ~/NEUROMANCER/scripts/daily_photo_processing.sh

WINTERMUTE_PATH="$HOME/WINTERMUTE"
NEUROMANCER_PATH="$HOME/NEUROMANCER/photo_processing"
LAST_PROCESSED="$NEUROMANCER_PATH/.last_processed"

# find photos modified since last run
if [ -f "$LAST_PROCESSED" ]; then
    find "$WINTERMUTE_PATH" -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.heic" -newer "$LAST_PROCESSED" > "$NEUROMANCER_PATH/new_photos.txt"
else
    find "$WINTERMUTE_PATH" -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.heic" > "$NEUROMANCER_PATH/new_photos.txt"
fi

# process new photos
if [ -s "$NEUROMANCER_PATH/new_photos.txt" ]; then
    echo "Processing $(wc -l < "$NEUROMANCER_PATH/new_photos.txt") new photos..."
    cd "$NEUROMANCER_PATH"
    python batch_photo_processor.py --file-list new_photos.txt

    # update database
    python metadata_database.py --ingest

    # update timestamp
    touch "$LAST_PROCESSED"
else
    echo "No new photos to process"
fi
```

### command line search interface
```python
#!/usr/bin/env python3
# ~/NEUROMANCER/scripts/photo_search.py
import sys
from metadata_database import MetadataDatabase

def main():
    if len(sys.argv) < 2:
        print("Usage: photo_search.py 'search query'")
        sys.exit(1)

    query = ' '.join(sys.argv[1:])
    db = MetadataDatabase("~/NEUROMANCER/photo_processing/photos.db")
    results = db.search(query)

    print(f"Found {len(results)} photos matching '{query}':")
    for path, scene, detailed in results:
        print(f"\n📸 {path}")
        print(f"Scene: {scene}")
        print(f"Details: {detailed[:100]}...")

if __name__ == "__main__":
    main()
```

## deployment checklist

### initial setup
- [ ] install ollama and vision model
- [ ] create directory structure
- [ ] test with sample photos
- [ ] validate metadata generation

### batch processing
- [ ] implement batch processor
- [ ] test with limited photo set
- [ ] optimize processing speed/memory
- [ ] add error handling and logging

### search system
- [ ] create database schema
- [ ] ingest metadata into database
- [ ] test search functionality
- [ ] optimize search performance

### automation
- [ ] create scheduled processing script
- [ ] set up cron job for daily runs
- [ ] implement monitoring/alerting
- [ ] create backup procedures

## monitoring and maintenance

### performance metrics
- photos processed per hour
- metadata generation accuracy
- search response times
- disk space usage

### maintenance tasks
- regular metadata backup
- database optimization
- model updates when available
- cleanup of outdated metadata