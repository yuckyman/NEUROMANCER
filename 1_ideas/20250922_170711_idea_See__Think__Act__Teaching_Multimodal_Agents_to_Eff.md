---
title: 'See, Think, Act: Teaching Multimodal Agents to Effectively Interact with GUI
  by Identifying Toggles'
link: https://arxiv.org/abs/2509.13615
summary: 'The article discusses a new state control benchmark for multimodal agents in graphical user interfaces (GUIs). The authors propose a training method called State-aware Reasoning (StaR) to improve the reliability of toggle instructions by teaching agents to perceive the current toggle state and analyze the desired state from the instruction. The results show that StaR can reduce the execution error rate for toggle instructions by up to 30%, while also improving general task performance on three public multimodal agent benchmarks.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 9be07fa01ff5527503d09da8ae5df0b867fc3307177793d4530fce8d70a4cc89
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.619199'
category: 24-computing
---

arXiv:2509.13615v1 Announce Type: new Abstract: The advent of multimodal agents facilitates effective interaction within graphical user interface (GUI), especially in ubiquitous GUI control. However, their inability to reliably execute toggle control instructions remains a key bottleneck. To investigate this, we construct a state control benchmark with binary toggle instructions from public datasets. Evaluations of existing agents demonstrate their unreliability, particularly when the current toggle state already matches the desired state. To address the challenge, we propose State-aware Reasoning (StaR), a training method that teaches agents to perceive the current toggle state, analyze the desired state from the instruction, and act accordingly. Experiments on three multimodal agents demonstrate that StaR can improve toggle instruction execution accuracy by over 30\%. Further evaluations on three public benchmarks show that StaR also enhances general task performance. Finally, evalua...