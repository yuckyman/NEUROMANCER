---
title: 'Seeing 3D Through 2D Lenses: 3D Few-Shot Class-Incremental Learning via Cross-Modal
  Geometric Rectification'
link: https://arxiv.org/abs/2509.14958
summary: 'The article discusses the challenges of expanding 3D digital content in open-world scenarios and proposes a new approach called Cross-Modal Geometric Rectification (CMGR) to address these issues. CMGR enhances 3D geometric fidelity by leveraging CLIP's hierarchical spatial semantics, which can help mitigate texture bias caused by indiscriminate fusion of geometric-textural cues. The framework introduces a Structure-Aware Geometric Rectification module that aligns 3D part structures with CLIP's intermediate spatial priors through attention-driven geometric fusion. Additionally, CMGR incorporates a Texture Amplification M algorithm to improve the model's ability to handle extreme data scarcity and unstable decision prototypes.'
tags:
- open-source
- privacy
- selfhosting
- decentralized
- foss
content_hash: cb7817701a8b0c4974399b503abdd50c14c9f524e5b73c418209561b19af47f3
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.885802'
category: 25-foss
---

arXiv:2509.14958v1 Announce Type: new Abstract: The rapid growth of 3D digital content necessitates expandable recognition systems for open-world scenarios. However, existing 3D class-incremental learning methods struggle under extreme data scarcity due to geometric misalignment and texture bias. While recent approaches integrate 3D data with 2D foundation models (e.g., CLIP), they suffer from semantic blurring caused by texture-biased projections and indiscriminate fusion of geometric-textural cues, leading to unstable decision prototypes and catastrophic forgetting. To address these issues, we propose Cross-Modal Geometric Rectification (CMGR), a framework that enhances 3D geometric fidelity by leveraging CLIP's hierarchical spatial semantics. Specifically, we introduce a Structure-Aware Geometric Rectification module that hierarchically aligns 3D part structures with CLIP's intermediate spatial priors through attention-driven geometric fusion. Additionally, a Texture Amplification M...