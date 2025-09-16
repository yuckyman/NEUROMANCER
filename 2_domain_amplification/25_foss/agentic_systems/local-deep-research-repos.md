---
type: research
category: deep-research-agents
created: 2025-09-13
tags: [deep-research, agents, local-ai, m4-mac, ollama]
status: active
---

# local deep research repositories

github dive for lightweight deep research agents compatible with macbook m4 pro (24gb ram)

## top candidates

### langchain-ai/local-deep-researcher
**status**: fully local web research and report writing assistant
**key features**:
- uses any llm hosted by ollama or lmstudio
- generates web search queries iteratively
- gathers results, summarizes findings
- reflects on knowledge gaps and generates new searches
- outputs final markdown summary with sources

**m4 compatibility**: excellent - designed for local deployment

### learningcircuit/local-deep-research
**status**: high-performance local research
**key features**:
- achieves ~95% on simpleqa benchmark (gpt-4.1-mini)
- supports local and cloud llms (ollama, google, anthropic)
- searches 10+ sources: arxiv, pubmed, web, private docs
- "everything local" philosophy

**m4 compatibility**: excellent - optimized for local deployment

### dzhng/deep-research
**status**: simple, lightweight implementation
**key features**:
- <500 loc for easy understanding/modification
- iterative deep research with refinement
- combines search engines, web scraping, llms
- goal: simplest implementation of deep research agent

**m4 compatibility**: excellent - explicitly lightweight

### assafelovic/gpt-researcher
**status**: mature, feature-rich
**key features**:
- llm-based autonomous research agent
- generates long reports with citations
- frontend available (html/css/js and nextjs versions)
- supports local and web research

**m4 compatibility**: good - supports local models

## m4 pro performance insights

### hardware advantages
- neural engine: 16-core, 38 trillion ops/sec
- unified memory: 24gb shared across cpu/gpu/neural engine
- optimized for ai workloads with apple silicon

### ollama performance
- native apple silicon optimization
- unified memory architecture ideal for large models
- energy efficient inference
- can handle 34b parameter models with quantization

### real-world benchmarks
- code generation: 1-2 seconds typical
- fractal rendering: 1-2 seconds
- model inference: significantly faster than traditional architectures

## ecosystem integration

### ollama compatibility
all top repos support ollama integration:
- lightweight, extensible framework
- simple api for model management
- native mac support with easy installation

### development tools
- confi chat: lightweight llm interface
- argo: local model management with rag
- n8n integration for workflow automation

## distributed computing potential
- exo framework enables distributed inference
- full 671b deepseek r1 on consumer hardware
- example: 7 m4 pro mac minis + 1 m4 max macbook pro
- total: 496gb unified memory with 4-bit quantization