# Project Skeleton: NEUROMANCER Semi-Autonomous AI Partner

## Overview
A local-first, vault-integrated agent for knowledge synthesis, proactive tasking, and code execution. Bold features: Self-evolving via vault writes, FL personalization, opencode fusion. Skeleton outlines stack for low-cost, low-latency implementation.

## Key Features
- **Proactive Vault Management**: Scan/process inbox/ideas; auto-refine/categorize content using RAG.
- **Conversational Interface**: Empathetic chat with memory (vault-derived user profile); voice via local Whisper.
- **Tool Integration**: Opencode for code-writing/tool-calling; execute scripts safely in sandbox.
- **Personalization**: FL fine-tuning on interactions for adaptive responses/behaviors.
- **Self-Evolution**: Agent generates/updates vault files; RLHF-like loops for improvement.
- **Multimodal**: Text primary; extend to vision (local CLIP) for file analysis.

## Hardware Requirements
- **Core**: Consumer laptop/desktop (Intel/AMD CPU, 16GB+ RAM; optional NVIDIA RTX 30/40-series GPU for faster inference).
- **Edge Devices**: Smartphone (iOS/Android) for FL sync; Raspberry Pi 5 for always-on server (8GB model).
- **IoT Integration**: Microphone/speakers for voice (USB mic); optional sensors (e.g., webcam for context via local models); no cloud IoT—local MQTT for device comms if expanded.
- **Scalability**: Start single-device; federate across 2-5 personal devices for FL.

## Software Stack
- **Programming Language**: Python 3.10+ (primary for simplicity, ecosystem; snakecase, type hints per AGENTS.md).
- **Core Frameworks**:
  - LangChain/LangGraph: Agent orchestration, RAG pipelines.
  - Ollama: Local SLM inference (Phi-3 mini, Mistral-7B quantized).
  - ChromaDB: Vector store for vault embeddings.
  - Flower: Federated learning for personalization.
- **Utilities**: Sentence Transformers (embeddings); LoRA (efficient fine-tuning); Opacus (differential privacy); Watchdog (file monitoring).
- **Testing/Linting**: Pytest, Ruff (per AGENTS.md).
- **Deployment**: Systemd (Linux/Mac) for always-on service; Streamlit/Gradio for UI prototype.

## External Dependencies
- **Models**: Hugging Face (free downloads: Phi-3, Whisper); Ollama hub (local pulls).
- **APIs (Minimal)**: OpenRouter (fallback for heavy tasks, <10% usage; free tier models like Qwen).
- **Libraries**: Pip-installable (langchain, chromadb, flower, torch—CPU/GPU via conda if needed).
- **No Vendor Lock**: All open-source; avoid proprietary (e.g., no AWS/GCP).

## IoT Considerations
- **Local-Only**: Use local network (e.g., Home Assistant integration via MQTT for smart home tasks); no external IoT clouds.
- **Expansion**: Agent controls IoT via Python libs (e.g., paho-mqtt for lights/sensors); personalize via FL on device data (e.g., room occupancy for proactive reminders).
- **Security**: Sandboxed execution; encrypt local comms.

## Cost Breakdown
- **Hardware**: Existing (laptop ~$0 additional); Pi 5 ~$80 one-time.
- **Software**: Free (open-source).
- **Models/Deps**: Free downloads.
- **APIs**: OpenRouter free tier (promotional models); fallback usage < $0.01/day (e.g., 100 queries @ $0.0001/token).
- **Total Ongoing**: Near-zero; scale to $5/mo max for hybrid bursts.

## Latency Targets & Optimization
- **Local Inference**: <100ms for text queries (Phi-3 on GPU); <500ms voice (Whisper tiny).
- **FL Rounds**: Async, 1-5min per update (background).
- **Tactics**: 4-bit quantization; caching (Redis local); batch small tasks.
- **Monitoring**: cProfile for bottlenecks; aim 90% local, <200ms end-to-end.

## Project Structure Skeleton (in 3_projects/neuromancer-agent)
```
neuromancer-agent/
├── src/
│   ├── agent.py          # Core agent logic (RAG, tool-calling)
│   ├── vault_brain.py    # Embeddings, graph RAG
│   ├── fl_personalizer.py # Flower setup, LoRA fine-tuning
│   ├── opencode_wrapper.py # Integration layer
│   └── utils/            # Privacy, monitoring
├── tests/                # Pytest suite
├── requirements.txt      # Deps: langchain, ollama, etc.
├── dev_log.md           # Progress tracking
└── README.md            # Setup/run instructions
```

This skeleton ensures bold, vault-native innovation. Next: Implement via tasks.