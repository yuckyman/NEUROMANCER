---
title: 'CrossPT: Exploring Cross-Task Transferability through Multi-Task Prompt Tuning'
link: https://arxiv.org/abs/2509.14253
summary: 'The article discusses a new approach called "Cross-task Prompt Tuning" (CrossPT) which is designed for multi-task language model adaptation. The key features of CrossPT include:

1. It decomposes each target prompt into shared, pre-trained source prompts and task-specific private prompts.
2. It combines these components using an attention mechanism to facilitate knowledge transfer across related tasks.
3. It supports robust transfer by systematically investigating design factors such as prompt initialization, balancing shared and private prompts, number of source prompts, learning rates, task prefixes, and label semantics.

The authors report that CrossPT achieves higher accuracy and robustness compared to traditional prompt tuning methods in several benchmark datasets like GLUE.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 27c93b8a8827aebadee152c7a111eaf9a0e548a2df455724aa0caf839c0a1ab0
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:12.334184'
category: 24-computing
---

arXiv:2509.14253v1 Announce Type: cross Abstract: Prompt tuning offers a parameter-efficient way to adapt large pre-trained language models to new tasks, but most existing approaches are designed for single-task settings, failing to share knowledge across related tasks. We propose Cross-task Prompt Tuning (CrossPT), a modular framework for multi-task prompt tuning that enables controlled knowledge transfer while maintaining task-specific specialization. CrossPT decomposes each target prompt into shared, pre-trained source prompts and task-specific private prompts, combined via a learned attention mechanism. To support robust transfer, we systematically investigate key design factors including prompt initialization, balancing shared and private prompts, number of source prompts, learning rates, task prefixes, and label semantics. Empirical results on GLUE and related benchmarks show that CrossPT achieves higher accuracy and robustness compared to traditional prompt tuning and related me...