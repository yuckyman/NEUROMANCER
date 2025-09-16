---
type: integration-guide
category: wintermute-vision
created: 2025-09-13
tags: [wintermute, vision-models, photo-organization, integration]
status: active
---

# wintermute vault integration approach

strategy for integrating vision models with your read-only WINTERMUTE photo vault

## vault structure analysis

### wintermute as read-only source
- contains your photo collection/vault
- considered read-only from neuromancer
- need non-destructive metadata approach
- preserve original file integrity

### neuromancer processing workflow
```
WINTERMUTE/photos → NEUROMANCER/processing → metadata database → enhanced search
```

## integration architecture

### option 1: sidecar metadata files
**approach**: create .json sidecar files in neuromancer
```
WINTERMUTE/photos/IMG_1234.jpg (read-only)
NEUROMANCER/metadata/IMG_1234.json (generated)
```

**advantages**:
- non-destructive to originals
- can be regenerated if lost
- allows complex structured metadata
- version control friendly

### option 2: external database
**approach**: sqlite/postgresql database in neuromancer
```
photos_metadata table:
- file_path (reference to wintermute)
- file_hash (for integrity checking)
- generated_metadata (json blob)
- created_date, updated_date
- model_version (for reprocessing)
```

**advantages**:
- fast querying and search
- relational data structure
- bulk operations
- indexing for performance

### option 3: hybrid approach (recommended)
**combine both**:
- sidecar files for detailed metadata
- database for fast search/indexing
- symlinks/hardlinks for efficient access

## processing pipeline

### batch processing workflow
1. **discovery**: scan wintermute vault for new/changed photos
2. **preprocessing**: check for existing metadata, skip if current
3. **vision analysis**: run through ollama vision model
4. **metadata generation**: create structured natural language metadata
5. **storage**: save to sidecar files and/or database
6. **indexing**: update search indices

### incremental processing
```bash
#!/bin/bash
# daily metadata update script
find ~/WINTERMUTE -name "*.jpg" -o -name "*.png" -newer ~/NEUROMANCER/.last_processed | \
while read photo; do
    python process_photo_metadata.py "$photo"
done
touch ~/NEUROMANCER/.last_processed
```

## metadata schema design

### structured metadata format
```json
{
  "file_info": {
    "path": "/Users/ian/WINTERMUTE/photos/IMG_1234.jpg",
    "hash": "sha256:abc123...",
    "size": 2048576,
    "modified": "2025-09-13T12:00:00Z"
  },
  "vision_analysis": {
    "model": "llama3.2-vision:11b",
    "version": "2025.09",
    "processed": "2025-09-13T15:30:00Z",
    "confidence": 0.85
  },
  "descriptions": {
    "scene": "a sunset over a mountain lake with pine trees",
    "detailed": "golden hour photography of serene mountain lake...",
    "technical": "landscape photography, rule of thirds composition..."
  },
  "tags": {
    "objects": ["mountains", "lake", "trees", "sunset"],
    "colors": ["golden", "orange", "blue", "green"],
    "mood": ["serene", "peaceful", "contemplative"],
    "style": ["landscape", "nature", "golden-hour"]
  },
  "extracted_text": "any text found in image via ocr",
  "location_hints": "mountain lake region, coniferous forest",
  "season_weather": "summer evening, clear sky"
}
```

## search and retrieval system

### full-text search
- elasticsearch/opensearch for advanced search
- simple sqlite fts for lightweight approach
- support natural language queries

### query examples
- "show me sunset photos from last summer"
- "find photos with mountains and lakes"
- "images with people in outdoor settings"
- "golden hour landscape photography"

### integration with existing tools
- command line search interface
- alfred/raycast integration for macos
- web interface for browsing
- api for other applications

## implementation phases

### phase 1: proof of concept
- single photo processing script
- basic metadata extraction
- sidecar file generation
- manual testing with sample photos

### phase 2: batch processing
- directory scanning and processing
- incremental update logic
- error handling and logging
- progress tracking and resumption

### phase 3: search system
- database schema implementation
- indexing and search functionality
- query interface development
- performance optimization

### phase 4: automation
- scheduled processing via cron
- file system watching for new photos
- integration with photo import workflows
- maintenance and cleanup routines

## privacy and security considerations

### local processing benefits
- no cloud uploads of personal photos
- all processing happens on your hardware
- complete data sovereignty
- no api costs or rate limits

### file integrity
- hash verification to detect changes
- backup strategies for metadata
- non-destructive processing only
- ability to regenerate from originals

## resource management

### m4 pro optimization
- batch size tuning for memory efficiency
- model preloading to reduce startup overhead
- parallel processing where beneficial
- thermal management for long runs

### storage considerations
- metadata storage requirements
- index size vs search performance
- cleanup of outdated metadata
- archival strategies for old analyses