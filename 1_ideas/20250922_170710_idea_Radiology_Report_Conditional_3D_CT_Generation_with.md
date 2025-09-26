---
title: Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion
  Model
link: https://arxiv.org/abs/2509.14780
summary: 'The article discusses a new type of text-to-image latent diffusion models called Report2CT, which can directly synthesize 3D chest CT volumes from free-text radiology reports. The model integrates multiple medical text encoders to capture nuanced clinical context and uses three pretrained medical text encoders (BiomedVLP CXR BERT, MedEmbed, and ClinicalBERT) for radiology report condition. The model's performance was evaluated using Frechet Inception Distance (FID), which measures the distributional similarity between real synthetic distributions and the real CT volumes from the CT RATE dataset.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: dca7315ff567ed6505c590184859b7c5e864b6d9f0957208448ffa3f9bd03ad9
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.978209'
category: 24-computing
---

arXiv:2509.14780v1 Announce Type: new Abstract: Text to image latent diffusion models have recently advanced medical image synthesis, but applications to 3D CT generation remain limited. Existing approaches rely on simplified prompts, neglecting the rich semantic detail in full radiology reports, which reduces text image alignment and clinical fidelity. We propose Report2CT, a radiology report conditional latent diffusion framework for synthesizing 3D chest CT volumes directly from free text radiology reports, incorporating both findings and impression sections using multiple text encoder. Report2CT integrates three pretrained medical text encoders (BiomedVLP CXR BERT, MedEmbed, and ClinicalBERT) to capture nuanced clinical context. Radiology reports and voxel spacing information condition a 3D latent diffusion model trained on 20000 CT volumes from the CT RATE dataset. Model performance was evaluated using Frechet Inception Distance (FID) for real synthetic distributional similarity a...