---
title: SAMPO:Scale-wise Autoregression with Motion PrOmpt for generative world models
link: https://arxiv.org/abs/2509.15536
summary: 'The article discusses a new framework called Scale-wise Autoregressive Motion Planning (SAMPO) that combines visual autoregressive modeling for intra-frame generation with causal modeling for next-frame generation. SAMPO is designed to address the challenges of visually coherent predictions in world models, such as disrupted spatial structure, inefficient decoding, and inadequate motion modeling. The key features of SAMPO include:

1. Bidirectional spatial attention: This design enhances temporal consistency by preserving spatial locality.
2. Temporal causal decoding: It supports parallel decoding within each scale while still maintaining consistency with the intra-frame generation.

To further improve dynamic scene understanding, SAMPO introduces an asymmetric multi-scale tokeniz...

[End of Summary]'
tags:
- unclassified
content_hash: 3a46f28aebbd2d7fbbd7f08d97644f99f451653cecbd1fead43bec4c37236608
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.344683'
---

arXiv:2509.15536v1 Announce Type: new Abstract: World models allow agents to simulate the consequences of actions in imagined environments for planning, control, and long-horizon decision-making. However, existing autoregressive world models struggle with visually coherent predictions due to disrupted spatial structure, inefficient decoding, and inadequate motion modeling. In response, we propose \textbf{S}cale-wise \textbf{A}utoregression with \textbf{M}otion \textbf{P}r\textbf{O}mpt (\textbf{SAMPO}), a hybrid framework that combines visual autoregressive modeling for intra-frame generation with causal modeling for next-frame generation. Specifically, SAMPO integrates temporal causal decoding with bidirectional spatial attention, which preserves spatial locality and supports parallel decoding within each scale. This design significantly enhances both temporal consistency and rollout efficiency. To further improve dynamic scene understanding, we devise an asymmetric multi-scale tokeniz...