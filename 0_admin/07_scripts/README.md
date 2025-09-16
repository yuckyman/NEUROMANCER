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

**purpose**: automated processing of phone shortcut text files → AI-tagged markdown

**features**:
- monitors `01_inbox/` for numeric `.txt` files (phone shortcut format)
- uses ollama qwen2.5:0.5b for content analysis and tagging
- generates obsidian-compliant yaml frontmatter
- creates markdown files in `1_ideas/` with proper metadata
- auto-deletes processed text files

**automation**:
- runs every 10 minutes via cron: `*/10 * * * * /usr/bin/python3 /home/ian/NEUROMANCER/0_admin/07_scripts/process_inbox.py`
- logs to: `inbox_processing.log`

**ai model selection**:
- tested: smollm2:360m vs qwen2.5:0.5b
- winner: qwen2.5:0.5b (actually analyzes content vs template responses)
- memory efficient: 397MB footprint vs 725MB+

**error handling**:
- 30s timeout for ollama calls
- fallback to default metadata if AI processing fails
- graceful handling of malformed files

**processing flow**:
```
phone shortcuts → 01_inbox/*.txt → ollama processing → 1_ideas/*.md → delete .txt
```

## other scripts
- `check_active_vault.py` - determine which vault obsidian api is serving
- `test_obsidian_api.py` - explore available api endpoints
- `quick_test.py` - basic api connectivity test
- `wintermute_sync.py` - legacy sync framework (being replaced by sync_agent.py)