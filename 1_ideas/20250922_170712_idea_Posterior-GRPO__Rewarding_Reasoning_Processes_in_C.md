---
title: 'Posterior-GRPO: Rewarding Reasoning Processes in Code Generation'
link: https://arxiv.org/abs/2508.05170
summary: 'The article discusses the potential improvements in code generation for large language models (LLMs) through reinforcement learning (RL). However, current paradigms rely on outcome-based rewards from test cases, neglecting the quality of the intermediate reasoning process. To address this issue, a unified framework is introduced that can incorporate the quality of the reasoning process during RL. The framework enables reasoning evaluation by generating preference pairs and accurately scoring reasoning quality through an Optimized-Degraded based method for reward model training.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: c291a9e693cace03d6fc72b5736a4ff2d2a74152061bc2bfca94d7a8022a6163
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:12.955083'
category: 24-computing
---

arXiv:2508.05170v2 Announce Type: replace-cross Abstract: Reinforcement learning (RL) has significantly advanced code generation for large language models (LLMs). However, current paradigms rely on outcome-based rewards from test cases, neglecting the quality of the intermediate reasoning process. While supervising the reasoning process directly is a promising direction, it is highly susceptible to reward hacking, where the policy model learns to exploit the reasoning reward signal without improving final outcomes. To address this, we introduce a unified framework that can effectively incorporate the quality of the reasoning process during RL. First, to enable reasoning evaluation, we develop LCB-RB, a benchmark comprising preference pairs of superior and inferior reasoning processes. Second, to accurately score reasoning quality, we introduce an Optimized-Degraded based (OD-based) method for reward model training. This method generates high-quality preference pairs by systematically o...