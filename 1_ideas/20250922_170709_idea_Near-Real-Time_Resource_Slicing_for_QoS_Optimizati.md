---
title: Near-Real-Time Resource Slicing for QoS Optimization in 5G O-RAN using Deep
  Reinforcement Learning
link: https://arxiv.org/abs/2509.14343
summary: 'The article discusses an online learning algorithm called xSlice for the Near-Real-Time (Near-RT) RAN Intelligent Controller (RIC) of 5G Open-Radio Access Networks (O-RANs). The algorithm adapts MAC-layer resource allocation in response to dynamic network states, including time-varying wireless channel conditions, user mobility, traffic fluctuations, and changes in user demand. It is a regret minimization problem that quantifies the QoS demands of all traffic sessions through weighting their throughput, latency, and reliability.

The authors propose using an actor-critic model with a deep reinforcement learning (DRL) framework to combine the advantages of both value-based and policy-based updating methods. The graph convolutional network (GCN) is used as the core component of the DRL algorithm.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e905360663e688801f93c6566801db3579ad4a030772dec8cedba64b3e91ce33
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.844092'
category: 24-computing
---

arXiv:2509.14343v1 Announce Type: cross Abstract: Open-Radio Access Network (O-RAN) has become an important paradigm for 5G and beyond radio access networks. This paper presents an xApp called xSlice for the Near-Real-Time (Near-RT) RAN Intelligent Controller (RIC) of 5G O-RANs. xSlice is an online learning algorithm that adaptively adjusts MAC-layer resource allocation in response to dynamic network states, including time-varying wireless channel conditions, user mobility, traffic fluctuations, and changes in user demand. To address these network dynamics, we first formulate the Quality-of-Service (QoS) optimization problem as a regret minimization problem by quantifying the QoS demands of all traffic sessions through weighting their throughput, latency, and reliability. We then develop a deep reinforcement learning (DRL) framework that utilizes an actor-critic model to combine the advantages of both value-based and policy-based updating methods. A graph convolutional network (GCN) is...