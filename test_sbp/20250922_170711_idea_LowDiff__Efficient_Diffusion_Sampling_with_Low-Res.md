---
title: 'LowDiff: Efficient Diffusion Sampling with Low-Resolution Condition'
link: https://arxiv.org/abs/2509.15342
summary: 'The article discusses a new type of diffusion model called "LowDiff" that improves the efficiency of diffusion models by generating increasingly higher resolution images from lower resolutions. The key features of LowDiff include:

1. It uses a cascaded approach to generate progressively higher-resolution images.
2. It employs a unified model for refining images from low resolution to desired resolution.
3. It achieves comparable or even superior performance with fewer high-resolution sampling steps compared to previous approaches.

The article also mentions that this new type of diffusion model is applicable to both pixel space and latent space, making it more versatile in different contexts.'
tags:
- unclassified
content_hash: 9d1af0ceadaeea1512b3ac05c66147cf8da2e59bef19bac367d2f4b494491a08
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.589414'
---

arXiv:2509.15342v1 Announce Type: new Abstract: Diffusion models have achieved remarkable success in image generation but their practical application is often hindered by the slow sampling speed. Prior efforts of improving efficiency primarily focus on compressing models or reducing the total number of denoising steps, largely neglecting the possibility to leverage multiple input resolutions in the generation process. In this work, we propose LowDiff, a novel and efficient diffusion framework based on a cascaded approach by generating increasingly higher resolution outputs. Besides, LowDiff employs a unified model to progressively refine images from low resolution to the desired resolution. With the proposed architecture design and generation techniques, we achieve comparable or even superior performance with much fewer high-resolution sampling steps. LowDiff is applicable to diffusion models in both pixel space and latent space. Extensive experiments on both conditional and unconditio...