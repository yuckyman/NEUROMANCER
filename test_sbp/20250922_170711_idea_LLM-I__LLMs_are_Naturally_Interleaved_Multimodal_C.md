---
title: 'LLM-I: LLMs are Naturally Interleaved Multimodal Creators'
link: https://arxiv.org/abs/2509.13642
summary: 'The article discusses the development of a novel framework called LLM-Interleaved (LLM-I), which refines interleaved image-text generation into a tool-use problem. The authors propose that this approach can overcome limitations of current unified models, such as synthetic imagery and factual grounding or programmatic precision. LLM-I uses an RL framework with a hybrid reward system combining rule-based logic with judgments from LLM and MLLM evaluators to enable the agent to select and apply specialized visual tools proficiently. The authors evaluate their approach on a diverse new dataset using four different model backbones, demonstrating state-of-the-art performance compared to existing methods.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 28579a82f71a227e46d6834e99df700b3ad60275bba20336a3bd95f84eb2afee
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.212262'
category: 24-computing
---

arXiv:2509.13642v1 Announce Type: cross Abstract: We propose LLM-Interleaved (LLM-I), a flexible and dynamic framework that reframes interleaved image-text generation as a tool-use problem. LLM-I is designed to overcome the "one-tool" bottleneck of current unified models, which are limited to synthetic imagery and struggle with tasks requiring factual grounding or programmatic precision. Our framework empowers a central LLM or MLLM agent to intelligently orchestrate a diverse toolkit of specialized visual tools, including online image search, diffusion-based generation, code execution, and image editing. The agent is trained to select and apply these tools proficiently via a Reinforcement Learning (RL) framework that features a hybrid reward system combining rule-based logic with judgments from LLM and MLLM evaluators. Trained on a diverse new dataset using four different model backbones, LLM-I demonstrates state-of-the-art performance, outperforming existing methods by a large margin ...