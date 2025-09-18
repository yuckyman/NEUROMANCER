---
type: guide
category: admin
created: 2025-09-12
modified: 2025-09-12
tags: [scripts, automation, sync, tools]
status: active
---

# neuromancer automation scripts

## sync_agent.py
automated tool for pulling #process tagged files from wintermute to neuromancer ingest.

### usage
```bash
# basic sync (auto-detects method)
python 0_admin/07_scripts/sync_agent.py

# force filesystem method 
python 0_admin/07_scripts/sync_agent.py --method filesystem

# dry run to see what would be synced
python 0_admin/07_scripts/sync_agent.py --dry-run

# custom wintermute path
python 0_admin/07_scripts/sync_agent.py --wintermute-path /path/to/wintermute
```

### what it does
1. searches wintermute vault for files tagged with `#process`
2. copies found files to `0_admin/03_ingest/automated/`
3. adds processing metadata to each file
4. generates detailed sync report in `0_admin/01_inbox/`
5. handles duplicates and errors gracefully

### designed for agent invocation
the sync agent is built as a tool that can be called by automation systems, cron jobs, or other agents. it returns structured data and creates comprehensive reports.

### methods
- **api**: uses obsidian rest api (when endpoints are available)
- **filesystem**: direct file system search (current working method)
- **auto**: tries api first, falls back to filesystem

## process_inbox.py

**purpose**: automated processing of inbox files → AI-tagged markdown with URL scraping

**features**:
- monitors `01_inbox/` for multiple file types (.txt, .pdf, .docx, .doc, .png, .jpg, .jpeg)
- extracts text content from various file formats including OCR for images
- automatically detects and scrapes URLs found in content (up to 3 per file)
- uses ollama qwen2.5:0.5b for content analysis and intelligent tagging
- generates obsidian-compliant yaml frontmatter with metadata
- creates markdown files in `1_ideas/` with proper categorization
- auto-deletes processed files after successful conversion

**automation**:
- runs every 10 minutes via cron: `*/10 * * * * /usr/bin/python3 /home/ian/NEUROMANCER/0_admin/07_scripts/process_inbox.py`
- can be limited via environment variable `MAX_PROCESS_FILES` or command line argument
- logs processing activity to console

**ai model selection**:
- tested: smollm2:360m vs qwen2.5:0.5b
- winner: qwen2.5:0.5b (actually analyzes content vs template responses)
- memory efficient: 397MB footprint vs 725MB+

**error handling**:
- 120s timeout for ollama calls (increased for better analysis)
- fallback to default metadata if AI processing fails
- graceful handling of malformed files and unsupported formats
- continues processing other files if one fails

**processing flow**:
```
inbox files → text extraction → URL scraping → ollama analysis → 1_ideas/*.md → delete original
```

**supported file types**:
- **Text files**: Direct content extraction
- **PDF files**: Text extraction (currently disabled due to version issues)
- **Word documents**: Full text extraction from .docx/.doc
- **Images**: OCR text extraction from .png/.jpg/.jpeg
- **Other files**: Metadata extraction and file info

## rss_ingestor.py

**purpose**: automated RSS feed ingestion → inbox processing pipeline

**features**:
- fetches content from configured RSS feeds
- creates inbox files for each new article
- configurable article limits per feed
- tracks last check times to avoid duplicates
- supports custom feed URLs via environment variable
- handles malformed feeds gracefully

**automation**:
- can be run manually or via cron job
- processes feeds in parallel for efficiency
- updates `rss_feeds.json` with last check timestamps

**rss feeds monitored**:
- GitHub Blog: https://github.blog/feed/
- OpenCode AI: https://opencode.ai/feed.xml
- Simon Willison: https://simonwillison.net/atom/everything/
- Python.org Blogs: https://www.python.org/blogs/feed/
- Real Python: https://realpython.com/atom.xml
- Machine Learning Mastery: https://machinelearningmastery.com/feed/
- Towards Data Science: https://towardsdatascience.com/feed
- arXiv AI: https://arxiv.org/rss/cs.AI
- arXiv Computer Vision: https://arxiv.org/rss/cs.CV

**usage**:
```bash
# Process all configured feeds
python 0_admin/07_scripts/rss_ingestor.py

# Process a specific custom feed
CUSTOM_FEED_URL="https://example.com/feed.xml" python 0_admin/07_scripts/rss_ingestor.py
```

**processing flow**:
```
RSS feeds → fetch new articles → create inbox files → process_inbox.py → 1_ideas/*.md
```

## other scripts
- `check_active_vault.py` - determine which vault obsidian api is serving
- `test_obsidian_api.py` - explore available api endpoints
- `quick_test.py` - basic api connectivity test
- `wintermute_sync.py` - legacy sync framework (being replaced by sync_agent.py)