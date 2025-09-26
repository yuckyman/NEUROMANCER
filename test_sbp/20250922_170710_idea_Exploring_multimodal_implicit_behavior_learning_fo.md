---
title: Exploring multimodal implicit behavior learning for vehicle navigation in simulated
  cities
link: https://arxiv.org/abs/2509.15400
summary: 'The article discusses the challenges of standard behavior cloning (BC) and how it fails to learn from multiple valid actions for a given scenario. It proposes an alternative method called Implicit Behavioral Cloning (IBC) with Energy-Based Models (EBMs). The authors propose Data-Augmented IBC (DA-IBC), which perturbs expert actions to form counterexamples of IBC training and uses better initialization for derivative-free inference, leading to improved learning in urban driving tasks. The results show that DA-IBC outperforms standard IBC in terms of multimodal behavior learning in a test environment.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 1c7cb911943976bc0d08c3129cfe1123780c607116683adabe20ef9b79d9807a
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.758392'
category: 24-computing
---

arXiv:2509.15400v1 Announce Type: cross Abstract: Standard Behavior Cloning (BC) fails to learn multimodal driving decisions, where multiple valid actions exist for the same scenario. We explore Implicit Behavioral Cloning (IBC) with Energy-Based Models (EBMs) to better capture this multimodality. We propose Data-Augmented IBC (DA-IBC), which improves learning by perturbing expert actions to form the counterexamples of IBC training and using better initialization for derivative-free inference. Experiments in the CARLA simulator with Bird's-Eye View inputs demonstrate that DA-IBC outperforms standard IBC in urban driving tasks designed to evaluate multimodal behavior learning in a test environment. The learned energy landscapes are able to represent multimodal action distributions, which BC fails to achieve.