---
title: 'GenCAD-3D: CAD Program Generation using Multimodal Latent Space Alignment
  and Synthetic Dataset Balancing'
link: https://arxiv.org/abs/2509.15246
summary: 'The article discusses the challenges in generating CAD programs from nonparametric data such as point clouds and meshes using deep generative models. The authors introduce GenCAD-3D, a multimodal generative framework that combines contrastive learning for aligning latent embeddings between CAD and geometric encoders, with latent diffusion models for CAD sequence generation and retrieval. Additionally, they present SynthBal, a synthetic data augmentation strategy specifically designed to balance and expand datasets, particularly in the context of CAD programs. The article highlights the limitations of current deep generative models in automating CAD generation tasks and provides a framework for addressing these challenges through multimodal generative modeling.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 36b99193b07eb4cadca6355ae24b49007e577c2ee47bfeddf2b534125431b988
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:11.116357'
category: 24-computing
---

arXiv:2509.15246v1 Announce Type: cross Abstract: CAD programs, structured as parametric sequences of commands that compile into precise 3D geometries, are fundamental to accurate and efficient engineering design processes. Generating these programs from nonparametric data such as point clouds and meshes remains a crucial yet challenging task, typically requiring extensive manual intervention. Current deep generative models aimed at automating CAD generation are significantly limited by imbalanced and insufficiently large datasets, particularly those lacking representation for complex CAD programs. To address this, we introduce GenCAD-3D, a multimodal generative framework utilizing contrastive learning for aligning latent embeddings between CAD and geometric encoders, combined with latent diffusion models for CAD sequence generation and retrieval. Additionally, we present SynthBal, a synthetic data augmentation strategy specifically designed to balance and expand datasets, notably enha...