---
title: 'ORCA: Agentic Reasoning For Hallucination and Adversarial Robustness in Vision-Language
  Models'
link: https://arxiv.org/abs/2509.15435
summary: 'The article discusses the development of a new type of large vision-language models (LVLMs) called "Orca," which is an agentic reasoning framework that improves their factual accuracy and adversarial robustness through test-time structured inference reasoning. ORCA operates with an Observe--Reason--Critique--Act loop, where it queries multiple visual tools with evidential questions, validates cross-model inconsistencies, and iteratively refines predictions without access to model internals or retraining. ORCA also stores intermediate reasoning traces for audibility.

Orca is designed primarily to mitigate object-level hallucinations but also exhibits emergent adversarial robustness without requiring retraining of the model.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 8a7ebcd51eab294d0e18458ef418d8254faac58e7fa483aca1f1c5a9c55084a7
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.508779'
category: 24-computing
---

arXiv:2509.15435v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) exhibit strong multimodal capabilities but remain vulnerable to hallucinations from intrinsic errors and adversarial attacks from external exploitations, limiting their reliability in real-world applications. We present ORCA, an agentic reasoning framework that improves the factual accuracy and adversarial robustness of pretrained LVLMs through test-time structured inference reasoning with a suite of small vision models (less than 3B parameters). ORCA operates via an Observe--Reason--Critique--Act loop, querying multiple visual tools with evidential questions, validating cross-model inconsistencies, and refining predictions iteratively without access to model internals or retraining. ORCA also stores intermediate reasoning traces, which supports auditable decision-making. Though designed primarily to mitigate object-level hallucinations, ORCA also exhibits emergent adversarial robustness without requir...