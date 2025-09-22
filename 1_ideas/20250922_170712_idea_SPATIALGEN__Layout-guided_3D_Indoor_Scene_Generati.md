---
title: 'SPATIALGEN: Layout-guided 3D Indoor Scene Generation'
link: https://arxiv.org/abs/2509.14981
summary: 'The article discusses the development of SpatialGen, an innovative multi-view multi-modal diffusion model that enables the creation of high-fidelity 3D indoor environments. The key points are:

1. **Background and Motivation**: The article highlights the challenges in creating high-fidelity 3D models of indoor environments due to their complexity and time-consuming nature.

2. **Current Methods**: Recent advancements in generative AI have enabled automated scene synthesis, but existing methods often struggle with balancing visual quality, diversity, semantic consistency, and user control.

3. **Dataset**: The authors introduce a comprehensive synthetic dataset that features 12,328 structured annotated scenes with 57,440 rooms, along with 4.7 million photorealistic 2D renderings.

4. **Model Development**: They present SpatialGen, a novel multi-view multi-modal diffusion model that synthesizes realistic and semantically consistent 3D indoor scenes based on the dataset.

5. **Implementation**: The model is trained using a large-scale, high-quality dataset to address the limitations of existing methods.

6. **Applications**: The article discusses how this model can be applied in various fields such as design, virtual reality, and robotics.

In summary, SpatialGen addresses the challenges of 3D modeling by leveraging a comprehensive synthetic dataset and an innovative multi-view multi-modal diffusion model, making it a significant contribution to the field of indoor environment generation.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: be418c3f34e463699e97e74d3cc56d714537f9eed38a759a6f3311ae2e1573c7
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.187996'
category: 24-computing
---

arXiv:2509.14981v1 Announce Type: new Abstract: Creating high-fidelity 3D models of indoor environments is essential for applications in design, virtual reality, and robotics. However, manual 3D modeling remains time-consuming and labor-intensive. While recent advances in generative AI have enabled automated scene synthesis, existing methods often face challenges in balancing visual quality, diversity, semantic consistency, and user control. A major bottleneck is the lack of a large-scale, high-quality dataset tailored to this task. To address this gap, we introduce a comprehensive synthetic dataset, featuring 12,328 structured annotated scenes with 57,440 rooms, and 4.7M photorealistic 2D renderings. Leveraging this dataset, we present SpatialGen, a novel multi-view multi-modal diffusion model that generates realistic and semantically consistent 3D indoor scenes. Given a 3D layout and a reference image (derived from a text prompt), our model synthesizes appearance (color image), geome...