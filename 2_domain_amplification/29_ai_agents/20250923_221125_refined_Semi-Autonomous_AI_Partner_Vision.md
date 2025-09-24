# Refined Spec: Semi-Autonomous AI Partner Vision (NEUROMANCER Implementation)

## Core Theory
NEUROMANCER evolves into a semi-autonomous agent by treating the vault as a 'cognitive architecture'—a living knowledge graph where files (MD notes, ideas, projects) are nodes/edges. This enables proactive reasoning: agent queries/refines its 'brain' to anticipate user needs, surpassing reactive GitHub agents. Theory draws from cognitive science (distributed cognition) and AI (graph RAG + self-modifying systems), aiming for OS1-like adaptability without sentience—via emergent behaviors from vault loops.

Key Principles:
- **Autonomy via Self-Reference**: Agent reads/writes to vault, creating feedback loops (e.g., process inbox → generate ideas → execute in projects).
- **Privacy-First Personalization**: Local FL fine-tunes on vault interactions, no external data sharing.
- **Cost Efficiency**: 100% local SLM inference; OpenRouter as minimal fallback.
- **Bold Innovation**: Vault-native evolution (agent auto-categorizes/refines content) + opencode as 'hands' for code/tool execution.

## Methodology/Plan
Phased build in 3_projects/neuromancer-agent (Python-based, following AGENTS.md: venv, ruff, pytest).

### Phase 1: Foundation (Vault-Brain Setup)
- **Embed Vault**: Use LangChain + ChromaDB to vectorize MD files (embeddings via Sentence Transformers or local model). Build graph: Johnny Decimal folders as hierarchies, links/backlinks as edges (parse Obsidian metadata).
- **RAG Pipeline**: Query vault for context (e.g., 'retrieve similar ideas from 1_ideas'). Test with Ollama (Phi-3 mini, quantized 4-bit for CPU/GPU).
- **Proactive Layer**: Agent scans changes (e.g., new inbox files) via file watchers; suggests actions (e.g., 'Refine this idea?').

### Phase 2: Personalization & Autonomy (FL Integration)
- **Local FL Setup**: Flower framework for simulating federated clients (your devices as nodes). Fine-tune SLM adapters (LoRA) on synthetic/real vault interactions (e.g., chat logs as 'user data').
- **Differential Privacy**: Add noise to updates (Opacus library) for robust personalization without leakage.
- **Self-Evolution Loop**: Agent generates insights (e.g., 'Summarize domain trends'), writes to new MD files, re-embeds. Use RLHF-like scoring (local reward model) to improve outputs.

### Phase 3: Execution & Integration (Opencode Fusion)
- **Tool-Calling**: Wrap opencode as a LangChain tool; inject vault context into prompts (e.g., 'Generate code following AGENTS.md style, using vault refs').
- **Hybrid Inference**: Local SLM for 90% tasks; route complex (e.g., web fetch) to OpenRouter (cheapest models like Mistral-7B).
- **Empathy Simulation**: Prompt engineering with vault-derived user profile (e.g., 'Respond as collaborative partner, reference past ideas'); multimodal via local Whisper for voice.

### Phase 4: Optimization & Deployment
- **Latency/Cost Monitoring**: Profile with cProfile; target <100ms local queries. Track OpenRouter usage (<$0.01/day).
- **Testing**: Pytest for components (e.g., RAG accuracy >85%); simulate FL rounds.
- **Deployment**: Run as always-on service (systemd/launchd); Obsidian plugin for in-vault chat.

## Risks & Mitigations
- **Compute Limits**: Start with tiny SLMs; offload graph ops to CPU.
- **Hallucinations**: Ground in vault RAG; human-in-loop for critical writes.
- **Vault Integrity**: Version control (git) before writes; rollback on errors.

This spec positions NEUROMANCER as a pioneer: self-sustaining via its own structure, not external repos.