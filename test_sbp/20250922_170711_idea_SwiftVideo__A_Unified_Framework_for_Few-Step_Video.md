---
title: 'SwiftVideo: A Unified Framework for Few-Step Video Generation through Trajectory-Distribution
  Alignment'
link: https://arxiv.org/abs/2508.06082
summary: 'The article discusses the development of a unified and stable distillation framework called SwiftVideo for video synthesis models. The key points are:

1. Distillation methods based on trajectory-preserving or distribution-matching have been developed to accelerate video generation models.
2. However, these approaches often suffer from performance breakdown or increased artifacts under few-step settings.
3. The authors propose a new distillation framework called SwiftVideo that combines the advantages of both strategies.
4. The approach introduces continuous-time consistency distillation to ensure precise preservation of ODE trajectories.
5. It also proposes dual-perspective alignment, which includes distribution alignment between synthetic and real data along with trajectory alignment across different steps.

The main contribution is a unified and stable distillation framework that combines the advantages of trajectory-preserving and distribution-matching strategies.'
tags:
- unclassified
content_hash: 747342dd93104435684ebccb9d329d45f6180cb329f272591afe563112268b31
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.644366'
---

arXiv:2508.06082v2 Announce Type: replace Abstract: Diffusion-based or flow-based models have achieved significant progress in video synthesis but require multiple iterative sampling steps, which incurs substantial computational overhead. While many distillation methods that are solely based on trajectory-preserving or distribution-matching have been developed to accelerate video generation models, these approaches often suffer from performance breakdown or increased artifacts under few-step settings. To address these limitations, we propose \textbf{\emph{SwiftVideo}}, a unified and stable distillation framework that combines the advantages of trajectory-preserving and distribution-matching strategies. Our approach introduces continuous-time consistency distillation to ensure precise preservation of ODE trajectories. Subsequently, we propose a dual-perspective alignment that includes distribution alignment between synthetic and real data along with trajectory alignment across different...