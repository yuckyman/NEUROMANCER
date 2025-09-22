---
title: Modeling Transformers as complex networks to analyze learning dynamics
link: https://arxiv.org/abs/2509.15269
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: b3a68221de8a7e92618a89bc229b34cf683a23c3e35ab7a7b7c24196ee9db718
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.804451'
category: 24-computing
---

arXiv:2509.15269v1 Announce Type: cross Abstract: The process by which Large Language Models (LLMs) acquire complex capabilities during training remains a key open question in mechanistic interpretability. This project investigates whether these learning dynamics can be characterized through the lens of Complex Network Theory (CNT). I introduce a novel methodology to represent a Transformer-based LLM as a directed, weighted graph where nodes are the model's computational components (attention heads and MLPs) and edges represent causal influence, measured via an intervention-based ablation technique. By tracking the evolution of this component-graph across 143 training checkpoints of the Pythia-14M model on a canonical induction task, I analyze a suite of graph-theoretic metrics. The results reveal that the network's structure evolves through distinct phases of exploration, consolidation, and refinement. Specifically, I identify the emergence of a stable hierarchy of information spreade...