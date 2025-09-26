---
title: 'ViSpec: Accelerating Vision-Language Models with Vision-Aware Speculative
  Decoding'
link: https://arxiv.org/abs/2509.15235
summary: 'The article discusses a new framework called Vision-Aware Speculative Decoding (ViSpec) that aims to accelerate inference in large language models (LLMs). ViSpec is designed specifically for vision-language models (VLMs), which are key components of many large-scale models. The authors hypothesize that VLMs can effectively filter redundant image information layer by layer without compromising textual comprehension, while smaller draft models struggle with this task.

ViSpec achieves this through a lightweight vision adaptor module that compresses image tokens into a compact representation and integrates it seamlessly into the draft model's attention mechanism. Additionally, ViSpec extracts a global feature vector for each input to enable efficient filtering of redundant information. This approach promises significant speedups compared to existing methods, making ViSpec suitable for applications where multimodal capabilities are crucial.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 342255a652650a25b1e7fc47276a6c4d9e17f8ac6013f8ff8e6715908d037eaf
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.893993'
category: 24-computing
---

arXiv:2509.15235v1 Announce Type: new Abstract: Speculative decoding is a widely adopted technique for accelerating inference in large language models (LLMs), yet its application to vision-language models (VLMs) remains underexplored, with existing methods achieving only modest speedups (<1.5x). This gap is increasingly significant as multimodal capabilities become central to large-scale models. We hypothesize that large VLMs can effectively filter redundant image information layer by layer without compromising textual comprehension, whereas smaller draft models struggle to do so. To address this, we introduce Vision-Aware Speculative Decoding (ViSpec), a novel framework tailored for VLMs. ViSpec employs a lightweight vision adaptor module to compress image tokens into a compact representation, which is seamlessly integrated into the draft model's attention mechanism while preserving original image positional information. Additionally, we extract a global feature vector for each input ...