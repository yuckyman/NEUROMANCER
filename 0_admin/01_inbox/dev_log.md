---
type: log
category: development
created: 2025-09-12
modified: 2025-09-12
tags: [dev-log, memory, progress, preferences]
status: active
priority: high
auto_update: true
---

# neuromancer dev log
## creating autobiographical memory

### 2025-09-12 - initial setup

**user preferences discovered:**
- lowercase, casual writing style
- gen-z slang (tasteful amounts)  
- down-to-earth communication
- organic growth over rigid structure
- johnny decimal system as framework but let it evolve naturally
- autobiographical memory approach to track development
- no "claude code" mentions in commits (uncouth)

**what we built today:**
- basic neuromancer structure as wintermute's processing partner
- minimal folder setup (0_admin with 00_index and 01_inbox only)
- concept: wintermute = storage brain, neuromancer = thinking brain
- removed over-engineered folder structure, going for organic growth instead
- started this dev log as continuous memory system

**ian's vision:**
- neuromancer as digital hemisphere partnered with wintermute obsidian vault
- gibson-inspired naming (wintermute ↔ neuromancer)
- practical knowledge management with ai processing
- autobiographical tracking through dev logs

### github integration plan
- initialized neuromancer as git repo to track brain evolution
- creating 3_projects/repos/ to host user's github projects locally
- this gives ai direct access to modify/fix code
- repos excluded from main neuromancer git tracking (separate management)

**identified user repos:**
- bucket (rss/url pipeline) - recent, active
- spillyourgutsonline-gutterball (gutterball blog) - private, active  
- neural-nets_project, machine_vision_project - ai/ml work
- discord-buddy (habit tracker) - interesting gamification
- immich-swiper (tinder for photos) - creative project
- multimodal (reading project) - academic work

### repos cloned (2025-09-12)
fixed recursive folder structure issue, repos now properly located in 3_projects/repos/:
- ✅ bucket - rss/url pipeline project (active, well-structured)
- ✅ neural-nets_project - ai/ml work (minimal readme)
- ✅ discord-buddy - habit tracker with gamification (comprehensive architecture)

**setup complete:**
- neuromancer initialized as git repo
- repos structure created with .gitignore exclusions
- local access to user's code for ai modification/assistance
- autobiographical memory system active via dev log

### yaml frontmatter integration (2025-09-12)
implemented structured properties across neuromancer:

**property schema designed:**
- core properties: type, category, created, modified, tags, status
- specialized schemas for different note types (projects, logs, guides, etc)
- relationship properties: relates_to, depends_on, blocks
- search optimization with consistent tag naming

**templates created:**
- basic_note.md - general purpose template
- project_note.md - project tracking with progress/deadlines
- dev_log_entry.md - standardized dev log entries

**benefits unlocked:**
- obsidian property-based filtering and search
- automated organization via category/type
- knowledge graph connections via relates_to
- consistent metadata across all notes

### wintermute integration setup (2025-09-12)
built dual-stream ingestion system for wintermute → neuromancer:

**ingest structure created:**
- 0_admin/03_ingest/ following johnny decimal system
- manual/ for drag-drop processing  
- automated/ for #process tagged content
- processed/ for completed analysis

**obsidian rest api integration:**
- planning to use obsidian-web plugin
- endpoint: localhost:27123
- will search for #process tagged notes automatically
- sync script framework built (needs api testing)

### api exploration results (2025-09-12)
successfully connected to obsidian rest api but discovered endpoint limitations:

**api connection status:**
- ✅ api running on wintermute vault (correct target)
- ✅ authentication working with bearer token
- ✅ can see vault folder structure
- ❌ cannot access individual files or subfolders yet
- ❌ search endpoints not found in current api version

**workaround implemented:**
- created manual sync workflow for immediate use
- process: copy wintermute files → 0_admin/03_ingest/manual/
- structured import process with metadata preservation
- ready for ai analysis once files are dropped

### first processing success (2025-09-12)
successfully tested manual sync workflow with machinevision project content:

**content processed:**
- nimslo study plan (comprehensive 16-week timeline)
- stereo vision decision tree (mermaid diagram)  
- technical stereo alignment article (eye-pix.com)
- multiple view geometry reference material (hartley & zisserman pdf)

**ai analysis generated:**
- technical analysis → `2_domain_amplification/24_computing/computer_vision_analysis.md`
- implementation insights → `3_projects/31_coding/nimslo_project_insights.md`
- processing summary with full metadata and cross-references

**key insights extracted:**
- identified 4-view stereo processing advantages unique to nimslo cameras
- recognized hybrid methodology potential (classical cv + neural + optical flow)
- connected to existing projects (neural-nets, discord-buddy, bucket pipeline)
- assessed academic publication potential and technical rigor

**workflow validated:**
- manual ingest → ai analysis → structured knowledge → processed archive
- proper yaml frontmatter with relationships and confidence levels
- johnny decimal organization maintained
- processing pipeline now ready for scaling

**next steps:**
- create automated processing scripts for future ingests
- investigate api endpoints further for automated wintermute sync
- explore cloned codebases to understand patterns
- build processing templates for different content types

---

*this log captures our shared memory as we build this system together*