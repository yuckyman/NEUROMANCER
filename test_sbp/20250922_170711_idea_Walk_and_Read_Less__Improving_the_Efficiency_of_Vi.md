---
title: 'Walk and Read Less: Improving the Efficiency of Vision-and-Language Navigation
  via Tuning-Free Multimodal Token Pruning'
link: https://arxiv.org/abs/2509.15250
summary: 'The article discusses an approach called Navigation-Aware Pruning (NAP), which is designed to improve efficiency and performance of large models for Vision-and-Language Navigation (VLN) tasks by reducing model input size without sacrificing significant performance. The key points are:

1. Large models achieve strong performance on VLN tasks but are costly in resource-limited environments.
2. Token pruning offers tradeoffs that can be used to reduce computational cost, but prior work overlooks the specific challenges of VLN.
3. NAP uses navigation-specific traits to simplify the pruning process by pre-filtering tokens into foreground and background.
4. The approach identifies uninformative tokens, which undermines the efficiency gains from reducing model input size due to increased computational costs.

The article presents NAP as a solution that aims to improve the efficiency of large models for VLN tasks while maintaining their performance.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 25b081e655de5f3efa47e2417400a1b23c9072b5c2b8dffb1efd4f695806096a
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.437297'
category: 24-computing
---

arXiv:2509.15250v1 Announce Type: new Abstract: Large models achieve strong performance on Vision-and-Language Navigation (VLN) tasks, but are costly to run in resource-limited environments. Token pruning offers appealing tradeoffs for efficiency with minimal performance loss by reducing model input size, but prior work overlooks VLN-specific challenges. For example, information loss from pruning can effectively increase computational cost due to longer walks. Thus, the inability to identify uninformative tokens undermines the supposed efficiency gains from pruning. To address this, we propose Navigation-Aware Pruning (NAP), which uses navigation-specific traits to simplify the pruning process by pre-filtering tokens into foreground and background. For example, image views are filtered based on whether the agent can navigate in that direction. We also extract navigation-relevant instructions using a Large Language Model. After filtering, we focus pruning on background tokens, minimizin...