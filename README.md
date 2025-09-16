---
type: readme
category: admin
created: 2025-09-12
modified: 2025-09-12
tags: [neuromancer, overview, gibson, second-brain]
status: active
audience: public
---

# neuromancer
## the thinking half of my digital brain

**neuromancer** is basically the analytical side that pairs with my **wintermute** obsidian vault. think of it like having two brain hemispheres but digital (gibson would be proud).

## the setup

```
wintermute          ←→          neuromancer
(storage brain)                 (processing brain)
- keeps everything             - analyzes patterns
- reference materials          - makes connections  
- structured notes            - synthesizes info
- static organization         - active thinking
```

## how it's organized

starting minimal with johnny decimal framework - folders grow organically as needed:

- **0_admin/** - system stuff, dev logs, configs
  - **00_index/** - main documentation
  - **01_inbox/** - dev log and autobiographical memory

*other areas will emerge naturally as i use the system*

## what neuromancer does

while wintermute stores, neuromancer thinks:
- spots patterns across all my knowledge
- generates insights i might miss
- automates the boring organizational tasks
- helps me actually process information instead of just hoarding it
- enables proper ai-assisted research and creativity
- **automated inbox processing**: phone shortcuts → AI-tagged markdown (every 10 mins)

## key automation

**automated inbox processing**:
- script: `/0_admin/07_scripts/process_inbox.py`
- processes text files from phone shortcuts every 10 minutes
- AI analysis via ollama qwen2.5:0.5b (memory-efficient)
- generates obsidian-compliant yaml frontmatter
- flow: `01_inbox/*.txt` → ollama → `1_ideas/*.md`
- external repos moved to `3_projects/30_repos/`

## getting started

1. check out `0_admin/00_index/` for the system docs
2. read the structure guide to understand organization
3. start filling in areas that matter to my work
4. set up workflows between wintermute and neuromancer
5. send text files to `01_inbox/` (they'll be auto-processed)

---

*"the matrix has its roots in primitive arcade games..."* - neuromancer, william gibson