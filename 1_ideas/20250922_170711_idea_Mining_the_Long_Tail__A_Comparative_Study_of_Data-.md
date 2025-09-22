---
title: 'Mining the Long Tail: A Comparative Study of Data-Centric Criticality Metrics
  for Robust Offline Reinforcement Learning in Autonomous Motion Planning'
link: https://arxiv.org/abs/2508.18397
summary: 'The article discusses an approach to improve the performance of autonomous vehicles by using offline reinforcement learning (RL). The authors propose a systematic method for focusing the learning process on information-rich samples in large-scale driving logs. They use six different criticality weighting schemes categorized into three families: heuristic-based, uncertainty-based, and behavior-based. These are evaluated at two temporal scales - individual timestep and complete scenario. Seven goal-conditioned Conservative Q-Learning (CQL) agents with a state-of-the-art architecture are trained using this method. The authors evaluate the performance of these agents in both scenarios to demonstrate their effectiveness.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: ee0044cf3d78061484f1b4b5d08c95df6adb7cc083dbd84f0151a7f190b55b62
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.167823'
category: 24-computing
---

arXiv:2508.18397v2 Announce Type: replace-cross Abstract: Offline Reinforcement Learning (RL) presents a promising paradigm for training autonomous vehicle (AV) planning policies from large-scale, real-world driving logs. However, the extreme data imbalance in these logs, where mundane scenarios vastly outnumber rare "long-tail" events, leads to brittle and unsafe policies when using standard uniform data sampling. In this work, we address this challenge through a systematic, large-scale comparative study of data curation strategies designed to focus the learning process on information-rich samples. We investigate six distinct criticality weighting schemes which are categorized into three families: heuristic-based, uncertainty-based, and behavior-based. These are evaluated at two temporal scales, the individual timestep and the complete scenario. We train seven goal-conditioned Conservative Q-Learning (CQL) agents with a state-of-the-art, attention-based architecture and evaluate them ...