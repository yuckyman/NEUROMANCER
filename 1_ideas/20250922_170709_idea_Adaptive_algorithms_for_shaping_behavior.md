---
title: Adaptive algorithms for shaping behavior
link: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013454
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: a8cc5eb80bb26a45c71d7d0fb341bbfe43f7bca634eb4b57d35e4ffa8a0177a4
feed_title: PLOS Computational Biology
feed_url: https://journals.plos.org/ploscompbiol/feed/atom
date_processed: '2025-09-22T17:07:09.919055'
category: 24-computing
---

by William L. Tong, Venkatesh N. Murthy, Gautam Reddy Dogs and laboratory mice are commonly trained to perform complex tasks by guiding them through a curriculum of simpler tasks (‘shaping’). What are the principles behind effective shaping strategies? Here, we propose a teacher-student framework for shaping behavior, where an autonomous teacher agent decides its student’s task based on the student’s transcript of successes and failures on previously assigned tasks. Using algorithms for Monte Carlo planning under uncertainty, we show that near-optimal shaping algorithms achieve a careful balance between reinforcement and extinction. Near-optimal algorithms track learning rate to adaptively alternate between simpler and harder tasks. Based on this intuition, we derive an adaptive shaping heuristic with minimal parameters, which we show is near-optimal on a sequence learning task and robustly trains deep reinforcement learning agents on navigation tasks that involve sparse, delayed rewar...