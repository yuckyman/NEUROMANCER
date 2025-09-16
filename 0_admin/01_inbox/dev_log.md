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

### agentic enhancement roadmap (2025-09-12)
identified 5 key agentic capabilities to evolve neuromancer into active thinking partner:

**phase 1: automated sync agent (immediate)**
- tool to pull #process tagged files from wintermute to neuromancer ingest
- intelligent batching and priority handling
- error recovery and conflict resolution
- foundation for all other agentic capabilities

**phase 2: pattern recognition engine**
- cross-project connection analysis
- knowledge gap identification
- trend analysis across domains
- deadline risk assessment

**phase 3: proactive research assistant**
- contextual document recommendations
- automated literature synthesis
- knowledge freshness tracking
- research suggestion engine

**phase 4: project orchestration intelligence**
- dependency mapping and resource optimization
- milestone prediction and velocity tracking
- cross-project synergy identification

**phase 5: contextual work companion**
- real-time coding/writing assistance
- ambient knowledge surfacing
- intelligent progress tracking

### sync agent implementation complete (2025-09-12)
built and tested automated sync agent for #process tagged content:

**agent capabilities:**
- filesystem search for #process tagged files in wintermute
- intelligent file copying with metadata preservation
- comprehensive sync reporting with success/error tracking
- designed as tool for agent/automation invocation
- handles duplicates, errors, and edge cases gracefully

**first sync successful:**
- found and synced README.md from wintermute (19.5kb file)
- added processing metadata to copied file
- generated detailed sync report with next steps
- validated complete pipeline: discover → copy → report

**technical features:**
- yaml frontmatter parsing for tag detection
- timestamped file naming to prevent conflicts  
- structured return data for programmatic use
- comprehensive error handling and logging
- removed deprecated obsidian api integration

**precision improvement (2025-09-12):**
- enhanced tag matching to only capture exactly `#process` 
- prevents false matches with `#processing`, `#processcommand`, etc.
- uses word boundary regex for precise tag detection
- tested with comprehensive cases including case insensitivity

**foundation established:**
sync agent now serves as core tool enabling all future agentic capabilities. ready for integration with automated scheduling, priority handling, and content processing workflows.

### deep research dive: tiny os & mesh networks (2025-09-15)
explored connection between ultra-minimal operating systems and decentralized communication:

**collapse computing research:**
- researched CollapseOS and DuskOS as civilization-resilient computing platforms
- identified philosophical alignment: radical simplification for technological resilience
- created comprehensive analysis: `1_ideas/tiny-os-research/collapse-dusk-os-research.md`
- connected concepts to existing NEUROMANCER projects via wikilinks

**mesh networking ecosystem mapping:**
- investigated Meshtastic LoRa mesh protocol (40k+ active nodes globally)
- explored lightweight web servers: Mongoose, Ioto, OpenBalena
- catalogued FOSS projects: LibreMesh, Briar, ServalMesh, BitChat, Disaster.radio
- analyzed technical convergence opportunities

**key insight synthesis:**
- tiny OSes + mesh networks = complete infrastructure independence
- both movements prioritize understanding over convenience
- potential for mesh-distributed computing with ultra-minimal OS nodes
- connects to permacomputing & digital sustainability movements
- created ecosystem analysis: `1_ideas/tiny-os-research/mesh-networks-ecosystem.md`

**philosophical connections:**
- reinforces NEUROMANCER pattern-finding mission
- identifies technological counter-narrative to centralization
- demonstrates how different technical paths converge on same philosophical destination
- aligns with community-controlled, resilient digital infrastructure vision

---

*this log captures our shared memory as we build this system together*

### 2025-09-16 - gutterball whiteboard shipped (realtime + storage)

- implemented tldraw whiteboard under site `/whiteboard/`
- fixed React import + bundling by building a dedicated Vite IIFE bundle
- auth (username: gutterball, password: dev2025) with local persistence
- added realtime collaboration via `@tldraw/sync` using Cloudflare Worker
- provisioned Worker with Durable Objects (rooms) + R2 bucket `gutterball-whiteboard`
- configured `wrangler.toml` (ALLOW_ORIGIN = prod domain) and deployed
- frontend switched from `useSyncDemo` → `useSync` (WS endpoint + asset store)
- image uploads wired through Worker `/api/uploads/:id` into R2 (CORS-safe)
- UI polish: theme-consistent green accents, login light/dark toggle, hidden global toggle
- header UX: auto-hide unless cursor is in the top 2% of screen; cache-busting on assets
- stability fixes: `process` polyfill, memoized sync/assetStore to avoid render loop

status: live at production; incognito collab cursors confirmed; uploads working

### tldraw extension research (2025-09-16)

analyzed gutterball whiteboard architecture for ai/connectome integration:

**current foundation (excellent):**
- real-time sync via cloudflare worker + durable objects
- persistent r2 storage with asset pipeline
- extensible shapoutil system for custom tools
- yjs awareness protocol for collaborative features
- authentication + cors properly configured

**ai integration pathways identified:**
- custom ai-assistant shapes via existing shaputil architecture
- real-time ai participants through yjs awareness (virtual collaborators)
- voice/text command interface for programmatic shape generation
- cloudflare worker can proxy ai model api calls

**connectome bridge opportunities:**
- johnny decimal → whiteboard data pipeline (markdown to shapes)
- bidirectional sync: whiteboard sessions export to neuromancer
- live visualization of wintermute graph data as interactive shapes
- existing hugo content system provides perfect data source

**key insight: architecture perfectly positioned for enhancement**
- editor api enables programmatic canvas manipulation
- real-time collaboration foundation supports ai npcs
- durable objects can maintain ai state alongside user sessions
- r2 storage can cache ai-generated content and connectome data

next: prototype custom ai-assistant shape tool as proof of concept

### 2025-09-16 - tldraw extension research: ai integration & connectome pathways

comprehensive research into tldraw's plugin/extension system for custom AI functionality:

**plugin/extension architecture discovered:**
- ShapeUtil classes for custom shapes with lifecycle methods (getDefaultProps, component, indicator, onResize)
- BaseBoxShapeTool for custom tool behavior and interactions
- UI overrides system for toolbar/panel customization via TLUiOverrides
- complete UI replacement possible through hideUi prop + custom React components

**programmatic interaction capabilities:**
- Editor API provides full canvas control: createShapes, updateShape, select, zoomToFit
- comprehensive shape manipulation with real-time updates
- event handler system: registerBeforeCreateHandler, registerAfterCreateHandler
- snapshot API for save/load: getSnapshot, loadSnapshot with JSON serialization

**ai integration patterns identified:**
- NPC implementation via Yjs awareness protocol for AI participants
- real-time shape interception for AI enhancement
- collaborative AI commands through editor event system
- programmatic cursor control for AI assistants

**connectome integration pathways:**
- snapshot API enables full data export/import with external systems
- meta properties on shapes for application-specific metadata storage
- real-time sync through store.listen() for bi-directional data flow
- live data visualization through shape updates triggered by external streams

**custom ui component system:**
- track() wrapper for reactive components using useEditor() hook
- keyboard shortcut handling and tool state management
- custom panels for AI interaction and connectome data display
- component override system: Toolbar, StylePanel, ContextMenu, CollaboratorCursor

**research output:**
- detailed analysis: `2_domain_amplification/24_computing/tldraw_extension_research.md`
- identified immediate implementation options: AI shape tool, connectome panel, drawing commands
- advanced patterns: context-aware AI, collaborative NPCs, predictive drawing, semantic recognition
- integration strategy: real-time sync, live data shapes, export pipeline, import workflows

**technical foundation established:**
ready to implement custom AI tools, external data connectivity, and enhanced collaboration features on existing gutterball whiteboard infrastructure

### 2025-09-16 - automated inbox processing system

**what we accomplished:**
- created automated inbox processing system for phone shortcuts
- moved 30_repos into 3_projects structure (following johnny decimal flow)
- built python script that processes text files from phone → markdown with AI tagging
- implemented cron job running every 10 minutes for continuous processing
- A/B tested ollama models for memory-efficient processing

**technical wins:**
- script: `/home/ian/NEUROMANCER/0_admin/07_scripts/process_inbox.py`
- processes numeric text files (phone shortcut format)
- uses ollama qwen2.5:0.5b (397MB footprint vs previous 4GB+ models)
- generates obsidian-compliant yaml frontmatter
- auto-deletes processed files, creates markdown in 1_ideas
- cron logs to: `/home/ian/NEUROMANCER/0_admin/07_scripts/inbox_processing.log`

**model comparison findings:**
- qwen2.5:0.5b: actually analyzes content, provides meaningful tags/summaries
- smollm2:360m: just returned template responses, no content analysis
- memory pressure was causing timeouts with larger models
- qwen2.5:0.5b strikes perfect balance of capability vs resource usage

**user preferences confirmed:**
- prefers functional automation over manual processing
- values system resource efficiency
- appreciates A/B testing approach to optimization
- likes seeing the "why" behind technical decisions

**system architecture evolution:**
```
phone shortcuts → 01_inbox/*.txt → ollama processing → 1_ideas/*.md
```

**automation infrastructure:**
- cron job: `*/10 * * * * /usr/bin/python3 /home/ian/NEUROMANCER/0_admin/07_scripts/process_inbox.py`
- automatic cleanup: processed txt files deleted after markdown creation
- error handling: fallback to default metadata if AI processing fails
- memory optimization: 30s timeout, truncated prompts, efficient model selection

**next evolution opportunities:**
- monitor automated system performance patterns
- develop content-based tagging intelligence from observed processing
- potentially add cross-reference detection (connecting processed notes to existing knowledge)