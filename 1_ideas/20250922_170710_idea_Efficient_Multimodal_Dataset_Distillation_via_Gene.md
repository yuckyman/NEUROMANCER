---
title: Efficient Multimodal Dataset Distillation via Generative Models
link: https://arxiv.org/abs/2509.15472
summary: 'The article discusses an efficient method for distilling multimodal datasets using generative models, specifically focusing on image-text datasets. It introduces EDGE (Edge-Driven Generative Distillation), which is designed to synthesize a small dataset from a large one, enabling the model trained on it to perform well on the original dataset. The key challenges addressed are the lack of correlation between generated images and captions and the diversity among generated samples. To overcome these issues, EDGE proposes a novel method that identifies two key problems: 1) The absence of correlation between generated images and captions; 2) The lack of diversity in generated samples. This approach aims to improve the efficiency and effectiveness of multimodal dataset distillation tasks.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 32c5558365ec5eef77b65b548021abac449fe3b6b811e6dbd1be246dcfe368df
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.501332'
category: 24-computing
---

arXiv:2509.15472v1 Announce Type: new Abstract: Dataset distillation aims to synthesize a small dataset from a large dataset, enabling the model trained on it to perform well on the original dataset. With the blooming of large language models and multimodal large language models, the importance of multimodal datasets, particularly image-text datasets, has grown significantly. However, existing multimodal dataset distillation methods are constrained by the Matching Training Trajectories algorithm, which significantly increases the computing resource requirement, and takes days to process the distillation. In this work, we introduce EDGE, a generative distillation method for efficient multimodal dataset distillation. Specifically, we identify two key challenges of distilling multimodal datasets with generative models: 1) The lack of correlation between generated images and captions. 2) The lack of diversity among generated samples. To address the aforementioned issues, we propose a novel...