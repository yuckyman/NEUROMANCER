---
title: 'FragmentRetro: A Quadratic Retrosynthetic Method Based on Fragmentation Algorithms'
link: https://arxiv.org/abs/2509.15409
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 80d1d4254a69ae3c2bbd38b15c0cf6da340ea83ea14d80a317e41e0b86fafd8b
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.356639'
category: 24-computing
---

arXiv:2509.15409v1 Announce Type: new Abstract: Retrosynthesis, the process of deconstructing a target molecule into simpler precursors, is crucial for computer-aided synthesis planning (CASP). Widely adopted tree-search methods often suffer from exponential computational complexity. In this work, we introduce FragmentRetro, a novel retrosynthetic method that leverages fragmentation algorithms, specifically BRICS and r-BRICS, combined with stock-aware exploration and pattern fingerprint screening to achieve quadratic complexity. FragmentRetro recursively combines molecular fragments and verifies their presence in a building block set, providing sets of fragment combinations as retrosynthetic solutions. We present the first formal computational analysis of retrosynthetic methods, showing that tree search exhibits exponential complexity $O(b^h)$, DirectMultiStep scales as $O(h^6)$, and FragmentRetro achieves $O(h^2)$, where $h$ represents the number of heavy atoms in the target molecule ...