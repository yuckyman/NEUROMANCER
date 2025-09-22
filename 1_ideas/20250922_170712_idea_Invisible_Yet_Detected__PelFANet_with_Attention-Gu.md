---
title: 'Invisible Yet Detected: PelFANet with Attention-Guided Anatomical Fusion for
  Pelvic Fracture Diagnosis'
link: https://arxiv.org/abs/2509.13873
summary: 'The article discusses a new type of attention network called PelFANet that combines raw pelvic X-rays with segmented bone images to improve fracture classification. The authors present their findings on using this network on the AMERI dataset, which achieved 88.68% accuracy and 0.9334 AUC for visible fractures compared to conventional methods.

The key points of the article are:

1. Pelvic fractures pose significant diagnostic challenges.
2. A new type of attention network called PelFANet is introduced.
3. The network fuses raw pelvic X-rays with segmented bone images.
4. Fused Attention Blocks (FABlocks) are used to iteratively exchange and refine features from both inputs.
5. Trained in a two-stage pipeline with a segmentation-guided approach, the network demonstrates superior performance compared to conventional methods on the AMERI dataset.
6. The results highlight the potential of anatomy-aware dual-input architectures for robust fracture classification.

The article emphasizes that this new type of attention network can be applied to various medical imaging applications and may have significant clinical implications.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 20d07d4967eeea0be8a5a7153611ab6ef49fe4c3c7fdd66ed1747ea7421ad4e8
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.532897'
category: 24-computing
---

arXiv:2509.13873v1 Announce Type: new Abstract: Pelvic fractures pose significant diagnostic challenges, particularly in cases where fracture signs are subtle or invisible on standard radiographs. To address this, we introduce PelFANet, a dual-stream attention network that fuses raw pelvic X-rays with segmented bone images to improve fracture classification. The network em-ploys Fused Attention Blocks (FABlocks) to iteratively exchange and refine fea-tures from both inputs, capturing global context and localized anatomical detail. Trained in a two-stage pipeline with a segmentation-guided approach, PelFANet demonstrates superior performance over conventional methods. On the AMERI dataset, it achieves 88.68% accuracy and 0.9334 AUC on visible fractures, while generalizing effectively to invisible fracture cases with 82.29% accuracy and 0.8688 AUC, despite not being trained on them. These results highlight the clini-cal potential of anatomy-aware dual-input architectures for robust fract...