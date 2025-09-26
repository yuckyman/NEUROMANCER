---
title: 'ProFusion: 3D Reconstruction of Protein Complex Structures from Multi-view
  AFM Images'
link: https://arxiv.org/abs/2509.15242
summary: 'Error communicating with Ollama API: 404 Client Error: Not Found for url:
  http://localhost:11434/api/generate'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 9652f37af63a089810c5efbda261a1f09738a6b1ecb8b26b3239e2072b396e75
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:12.876622'
category: 24-computing
---

arXiv:2509.15242v1 Announce Type: new Abstract: AI-based in silico methods have improved protein structure prediction but often struggle with large protein complexes (PCs) involving multiple interacting proteins due to missing 3D spatial cues. Experimental techniques like Cryo-EM are accurate but costly and time-consuming. We present ProFusion, a hybrid framework that integrates a deep learning model with Atomic Force Microscopy (AFM), which provides high-resolution height maps from random orientations, naturally yielding multi-view data for 3D reconstruction. However, generating a large-scale AFM imaging data set sufficient to train deep learning models is impractical. Therefore, we developed a virtual AFM framework that simulates the imaging process and generated a dataset of ~542,000 proteins with multi-view synthetic AFM images. We train a conditional diffusion model to synthesize novel views from unposed inputs and an instance-specific Neural Radiance Field (NeRF) model to reconst...