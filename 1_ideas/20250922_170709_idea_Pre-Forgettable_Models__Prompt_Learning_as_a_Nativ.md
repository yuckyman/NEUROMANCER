---
title: 'Pre-Forgettable Models: Prompt Learning as a Native Mechanism for Unlearning'
link: https://arxiv.org/abs/2509.15230
summary: 'The article discusses the challenges of traditional unlearning approaches for multimedia analysis. These methods are static and not suitable for real-time or continuously evolving systems due to their computational costs, fragility, and limitations in handling dynamic data. The authors propose a paradigm shift by introducing a new approach called "rethinking unlearning" that unifies knowledge acquisition and removal within a single training phase. Instead of encoding information in model weights, the system binds class-level semantics to dedicated prompt tokens. This design enables continuous learning and adaptation, making it suitable for real-time or continuously evolving systems.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 5da5deb21b5126b2034b6b15766e5ff9713583d8f80c316d8210bac18798c4b3
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:09.921677'
category: 24-computing
---

arXiv:2509.15230v1 Announce Type: cross Abstract: Foundation models have transformed multimedia analysis by enabling robust and transferable representations across diverse modalities and tasks. However, their static deployment conflicts with growing societal and regulatory demands -- particularly the need to unlearn specific data upon request, as mandated by privacy frameworks such as the GDPR. Traditional unlearning approaches, including retraining, activation editing, or distillation, are often computationally expensive, fragile, and ill-suited for real-time or continuously evolving systems. In this paper, we propose a paradigm shift: rethinking unlearning not as a retroactive intervention but as a built-in capability. We introduce a prompt-based learning framework that unifies knowledge acquisition and removal within a single training phase. Rather than encoding information in model weights, our approach binds class-level semantics to dedicated prompt tokens. This design enables ins...