---
title: Autoguided Online Data Curation for Diffusion Model Training
link: https://arxiv.org/abs/2509.15267
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e9283e30a2848a04a1a1a4130f26fae8f676e4df08f9d4a2555172cbd7db8a7e
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.280465'
category: 24-computing
---

arXiv:2509.15267v1 Announce Type: cross Abstract: The costs of generative model compute rekindled promises and hopes for efficient data curation. In this work, we investigate whether recently developed autoguidance and online data selection methods can improve the time and sample efficiency of training generative diffusion models. We integrate joint example selection (JEST) and autoguidance into a unified code base for fast ablation and benchmarking. We evaluate combinations of data curation on a controlled 2-D synthetic data generation task as well as (3x64x64)-D image generation. Our comparisons are made at equal wall-clock time and equal number of samples, explicitly accounting for the overhead of selection. Across experiments, autoguidance consistently improves sample quality and diversity. Early AJEST (applying selection only at the beginning of training) can match or modestly exceed autoguidance alone in data efficiency on both tasks. However, its time overhead and added complexi...