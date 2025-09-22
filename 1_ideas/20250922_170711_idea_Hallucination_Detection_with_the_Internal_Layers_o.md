---
title: Hallucination Detection with the Internal Layers of LLMs
link: https://arxiv.org/abs/2509.14254
summary: 'The article discusses the limitations of large language models (LLMs) in generating hallucinations and proposes methods for detecting them using probing-based classifiers. The authors propose a novel method called "Dynamic Weighted Combination" (DWC) that dynamically weights and combines internal LLM layers to improve hallucination detection. They evaluate their method across three benchmarks: TruthfulQA, HaluEval, and ReFact. The article highlights the potential of this approach in enhancing reliability without significantly increasing computational costs.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 44253eb6e051e2026c7852e6f6634399e741e99964d0350af4f12a5a41abaa09
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.607808'
category: 24-computing
---

arXiv:2509.14254v1 Announce Type: cross Abstract: Large Language Models (LLMs) have succeeded in a variety of natural language processing tasks [Zha+25]. However, they have notable limitations. LLMs tend to generate hallucinations, a seemingly plausible yet factually unsupported output [Hua+24], which have serious real-world consequences [Kay23; Rum+24]. Recent work has shown that probing-based classifiers that utilize LLMs' internal representations can detect hallucinations [AM23; Bei+24; Bur+24; DYT24; Ji+24; SMZ24; Su+24]. This approach, since it does not involve model training, can enhance reliability without significantly increasing computational costs. Building upon this approach, this thesis proposed novel methods for hallucination detection using LLM internal representations and evaluated them across three benchmarks: TruthfulQA, HaluEval, and ReFact. Specifically, a new architecture that dynamically weights and combines internal LLM layers was developed to improve hallucinatio...