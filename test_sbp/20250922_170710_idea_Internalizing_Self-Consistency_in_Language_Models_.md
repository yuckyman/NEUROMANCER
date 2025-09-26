---
title: 'Internalizing Self-Consistency in Language Models: Multi-Agent Consensus Alignment'
link: https://arxiv.org/abs/2509.15172
summary: 'Error communicating with Ollama API: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=120)'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 6dba26eb6dffadbef0ff32facd9d52a9efcf0855196cfdcc839740db0561b651
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.370784'
category: 24-computing
---

arXiv:2509.15172v1 Announce Type: new Abstract: Language Models (LMs) are inconsistent reasoners, often generating contradictory responses to identical prompts. While inference-time methods can mitigate these inconsistencies, they fail to address the core problem: LMs struggle to reliably select reasoning pathways leading to consistent outcomes under exploratory sampling. To address this, we formalize self-consistency as an intrinsic property of well-aligned reasoning models and introduce Multi-Agent Consensus Alignment (MACA), a reinforcement learning framework that post-trains models to favor reasoning trajectories aligned with their internal consensus using majority/minority outcomes from multi-agent debate. These trajectories emerge from deliberative exchanges where agents ground reasoning in peer arguments, not just aggregation of independent attempts, creating richer consensus signals than single-round majority voting. MACA enables agents to teach themselves to be more decisive a...