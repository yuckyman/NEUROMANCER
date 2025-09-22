---
title: Affordance-Based Disambiguation of Surgical Instructions for Collaborative
  Robot-Assisted Surgery
link: https://arxiv.org/abs/2509.14967
summary: 'Error communicating with Ollama API: HTTPConnectionPool(host='localhost', port=11434): Read timed out. (read timeout=120)'
tags:
- unclassified
content_hash: 588d86f4e29f442f6c3fadca20b5c139c637e22145ae3cb53a1fa74979ce9f75
feed_title: cs.HC updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.HC
date_processed: '2025-09-22T17:07:12.120509'
---

arXiv:2509.14967v1 Announce Type: cross Abstract: Effective human-robot collaboration in surgery is affected by the inherent ambiguity of verbal communication. This paper presents a framework for a robotic surgical assistant that interprets and disambiguates verbal instructions from a surgeon by grounding them in the visual context of the operating field. The system employs a two-level affordance-based reasoning process that first analyzes the surgical scene using a multimodal vision-language model and then reasons about the instruction using a knowledge base of tool capabilities. To ensure patient safety, a dual-set conformal prediction method is used to provide a statistically rigorous confidence measure for robot decisions, allowing it to identify and flag ambiguous commands. We evaluated our framework on a curated dataset of ambiguous surgical requests from cholecystectomy videos, demonstrating a general disambiguation rate of 60% and presenting a method for safer human-robot inter...