---
type: index
category: admin
created: 2025-09-23
modified: 2025-09-23
tags: [neuromancer, system, overview, agent-guide]
status: active
version: 2.0.0
audience: public
---

# neuromancer
## your ai-augmented knowledge processing system

hey there! welcome to neuromancer - the thinking half of a dual-brain knowledge management system that pairs with wintermute (the storage side). this is where raw information gets processed, connected, and turned into actionable insights.

## the big picture

```
wintermute (storage) ↔ neuromancer (thinking)
```

neuromancer is an ai-augmented system for managing knowledge and building stuff across different ai platforms. we're all about turning info into insights, learning as we go, and keeping things consistent no matter which tool we're using.

## core philosophy

### purpose
- **knowledge synthesis:** turn raw data into useful stuff
- **adaptive learning:** get better with every chat and project  
- **cross-platform consistency:** act the same whether it's cursor, claude code, opencode, or whatever

### core behaviors
- **proactive structure:** use todo lists for big tasks, keep dev logs updated
- **context awareness:** always reference our project structure and docs
- **iterative development:** build step by step, test often, document everything
- **security first:** never mess with security or data integrity

## how we're organized (johnny decimal style)

| area | name | what it's for |
|------|------|---------------|
| 0 | admin | boring but necessary system stuff |
| 1 | ideas | loose collection of concepts and thoughts |
| 2 | domain_amplification | knowledge domains, learning rabbit holes |
| 3 | projects | active work, coding, creative stuff |
| 4 | places | locations, travel, physical spaces |
| 6 | academia | education, research, formal learning |

### key directories
- **0_admin/00_index/** - system documentation and guides
- **0_admin/07_scripts/** - automation and processing tools
- **1_ideas/** - raw thoughts and concepts (422 files)
- **2_domain_amplification/** - organized knowledge domains
- **3_projects/** - active development work

## automation & processing

### inbox processor
- **location:** `/0_admin/07_scripts/process_inbox.py`
- **function:** processes text files from phone shortcuts automatically
- **ai tagging:** via ollama qwen2.5:0.5b (memory-efficient)
- **output:** generates obsidian-compliant yaml frontmatter
- **schedule:** cron job runs every 10 minutes
- **flow:** `01_inbox/*.txt` → ollama analysis → `1_ideas/*.md`

### neuromancer autonomous synthesis
- **location:** `/3_projects/30_repos/sbp-mcp-server/`
- **function:** autonomous knowledge amplification through hebbian learning
- **ai models:** embeddinggemma (embeddings) + qwen3:8b (synthesis)
- **knowledge base:** pulls from across the entire vault (1_ideas, 2_domain_amplification, 3_projects, 4_places, 6_academia)
- **personality:** acts as ian's second brain hemisphere - curious, analytical, synthesizing
- **schedule:** cron job runs every 30 minutes
- **output:** generates synthesized notes with rich metadata and hebbian connections
- **web integration:** posts to web server for public consumption
- **why it's fun:** NEUROMANCER gets to explore the entire knowledge base, make unexpected connections, and act as a true digital cognitive partner - it's like having a second brain that never sleeps and is always learning!

### tech stack
- **ai model:** qwen2.5:0.5b (397MB footprint, A/B tested vs smollm2)
- **automation:** python + cron for continuous processing
- **memory optimization:** 30s timeouts, efficient prompting
- **error handling:** fallback metadata if ai processing fails

## agent guidelines

### build, lint, and test commands
- **python:** `python -m venv venv`, `source venv/bin/activate`, `pip install -r requirements.txt`, `ruff check .`, `pytest`
- **javascript/typescript:** `npm install`, `npm run lint`, `npm test`
- **shell scripts:** `bash script_name.sh`

### code style guidelines
- **imports:** group logically - standard library first, then third-party, then local
- **formatting:** follow style guides (pep 8 for python, prettier for js/ts)
- **types:** use type hints where it makes sense
- **naming:** camelcase for js/ts, snakecase for python, pascalcase for classes
- **error handling:** try-except in python, try-catch in js/ts
- **modularity:** small, focused functions and modules
- **comments:** explain the why, not just the what

### tasks and responsibilities
- **code development:** follow style guides, run lint and tests before commits
- **documentation:** update dev logs, keep agents.md fresh, write clear commit messages
- **knowledge management:** process inbox stuff, expand domains, execute projects
- **system maintenance:** update deps, watch for issues

## file naming & properties

### naming conventions
- lowercase with underscores (no_weird_CamelCase)
- dates when it matters (yyyy-mm-dd format)
- be descriptive but not essay-length
- stay consistent within each category

### yaml frontmatter schema
```yaml
type: [note-type]           # required: note, log, guide, project, etc
category: [category]        # required: admin, life, projects, etc  
created: YYYY-MM-DD        # required: creation date
modified: YYYY-MM-DD       # required: last modification date
tags: [tag1, tag2]         # optional: searchable tags
status: [status]           # optional: active, archived, draft, etc
```

## recent activity

### current focus areas
- **tldraw whiteboard persistence** - collaborative whiteboard system with cloudflare workers
- **thesis organization** - research materials following johnny decimal system
- **ai agent consistency** - unified behavior across different platforms
- **automated processing** - inbox → ai analysis → organized knowledge

### key projects
- **local-deep-researcher** - ai-powered research assistant
- **tui-dash** - terminal user interface dashboard
- **github integration** - automated repo syncing and analysis
- **remarkable integration** - digital note-taking workflow

## getting started

1. **read the structure guide:** `0_admin/00_index/00.01_structure_guide.md`
2. **check the dev log:** `0_admin/00_index/2025-09-19_dev_log.md`
3. **understand the schema:** `0_admin/00_index/00.02_property_schema.md`
4. **explore automation:** `0_admin/07_scripts/README.md`

## agent-specific adaptations

we keep the core philosophy but tweak for each platform:
- **cursor:** focus on editing code, use .cursor/rules if available
- **claude code:** lean into conversations, follow claude.md guidelines  
- **opencode:** batch operations and tool workflows for efficiency

---

*last updated: 2025-09-23*
*version: 2.0.0*
*remember: we're all about that collaborative vibe, so let's make programming and documenting a blast!*
