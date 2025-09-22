---
title: 'KNARsack: Teaching Neural Algorithmic Reasoners to Solve Pseudo-Polynomial
  Problems'
link: https://arxiv.org/abs/2509.15239
summary: 'The article discusses an attempt to build a neural algorithmic reasoner (NAR) for solving Knapsack, a pseudo-polynomial problem. The author describes how they modeled intermediate states through dynamic programming supervision and achieved better generalization compared to a direct-prediction baseline that only selects the optimal subset from the problem inputs.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 9201295366f6ec391b45bc0882c3e1c6f57df29e9df0f8172a83d65aa7ee6a12
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.288773'
category: 24-computing
---

arXiv:2509.15239v1 Announce Type: new Abstract: Neural algorithmic reasoning (NAR) is a growing field that aims to embed algorithmic logic into neural networks by imitating classical algorithms. In this extended abstract, we detail our attempt to build a neural algorithmic reasoner that can solve Knapsack, a pseudo-polynomial problem bridging classical algorithms and combinatorial optimisation, but omitted in standard NAR benchmarks. Our neural algorithmic reasoner is designed to closely follow the two-phase pipeline for the Knapsack problem, which involves first constructing the dynamic programming table and then reconstructing the solution from it. The approach, which models intermediate states through dynamic programming supervision, achieves better generalization to larger problem instances than a direct-prediction baseline that attempts to select the optimal subset only from the problem inputs.