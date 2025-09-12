---
type: guide
category: admin
created: 2025-09-12
modified: 2025-09-12
tags: [ingest, wintermute, automation]
status: active
---

# neuromancer ingest system

## overview
two-way content streaming from wintermute to neuromancer for ai processing

## directories
- **manual/** - drop files here for immediate processing
- **automated/** - files pulled automatically via #process tag
- **processed/** - completed analysis, ready for cleanup

## how it works

### manual ingestion
1. copy/drop wintermute files into `manual/`
2. neuromancer processes and analyzes content
3. generates insights, connections, summaries
4. moves processed files to `processed/` with analysis

### automated ingestion  
1. wintermute notes tagged with `#process`
2. obsidian rest api pulls tagged content automatically
3. scheduled sync (daily/weekly/on-demand)
4. same processing pipeline as manual

## processing pipeline
```
wintermute → ingest → analyze → insights → structured storage
```

## api integration
- using obsidian local rest api plugin
- endpoint: http://localhost:27123
- auth: api key (to be configured)
- searches for #process tagged notes
- pulls content and metadata