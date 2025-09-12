---
type: guide
category: admin
created: 2025-09-12
modified: 2025-09-12
tags: [sync, wintermute, manual, workflow]
status: active
---

# manual sync workflow

## overview
since the obsidian rest api endpoints are still being figured out, here's the manual process to get wintermute content into neuromancer for ai processing.

## manual process

### 1. copy files from wintermute
```bash
# from wintermute directory
cp path/to/interesting_note.md /Users/ian/NEUROMANCER/0_admin/03_ingest/manual/
```

### 2. tag notes in wintermute
add `#process` tag to any note you want analyzed:
```markdown
---
tags: [existing-tags, process]
---

# your note content
```

### 3. manual export workflow
1. **open note in wintermute**
2. **copy content** (cmd+a, cmd+c)
3. **create file in neuromancer ingest**: 
   - `0_admin/03_ingest/manual/imported_YYYY-MM-DD_title.md`
4. **paste content and add metadata**:
   ```markdown
   ---
   type: imported
   source: wintermute
   original_path: path/in/wintermute.md
   imported: 2025-09-12
   tags: [imported, process]
   ---
   
   # original content here
   ```

## processing pipeline (coming soon)
once files are in manual/, neuromancer will:
- analyze content for patterns and insights
- generate connections to existing knowledge
- create structured summaries
- move processed files to `processed/` folder

## automated future
once we figure out the rest api endpoints:
- automatic detection of #process tagged notes
- scheduled sync (daily/weekly)
- automatic metadata extraction
- bidirectional sync status updates