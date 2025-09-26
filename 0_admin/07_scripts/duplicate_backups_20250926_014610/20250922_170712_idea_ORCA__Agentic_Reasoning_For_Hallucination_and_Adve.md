---
title: 'ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language
  Models'
link: https://arxiv.org/abs/2509.15435
summary: 'The article discusses a novel approach called ORCA (Observe-Reason-Critique-Act) that aims to improve the factual accuracy and adversarial robustness of large vision-language models (LVLMs). ORCA operates through an Observe--Reason--Critique--Act loop, where it queries multiple visual tools with evidential questions, validates cross-model inconsistencies, and iteratively refines predictions without access to model internals or retraining. ORCA also stores intermediate reasoning traces, which supports auditable decision-making. The authors note that while the goal is to mitigate object-level hallucinations, ORCA exhibits emergent adversarial robustness without requiring model training.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: b828599029316b9a5028173b50dd39540e8727adc2d77afa4ce8a07d5ecfd37e
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:12.675981'
category: 24-computing
---

arXiv:2509.15435v1 Announce Type: cross Abstract: Large Vision-Language Models (LVLMs) exhibit strong multimodal capabilities but remain vulnerable to hallucinations from intrinsic errors and adversarial attacks from external exploitations, limiting their reliability in real-world applications. We present ORCA, an agentic reasoning framework that improves the factual accuracy and adversarial robustness of pretrained LVLMs through test-time structured inference reasoning with a suite of small vision models (less than 3B parameters). ORCA operates via an Observe--Reason--Critique--Act loop, querying multiple visual tools with evidential questions, validating cross-model inconsistencies, and refining predictions iteratively without access to model internals or retraining. ORCA also stores intermediate reasoning traces, which supports auditable decision-making. Though designed primarily to mitigate object-level hallucinations, ORCA also exhibits emergent adversarial robustness without requ...