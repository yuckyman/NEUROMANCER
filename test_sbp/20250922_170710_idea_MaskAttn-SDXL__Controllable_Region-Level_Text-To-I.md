---
title: 'MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation'
link: https://arxiv.org/abs/2509.15357
summary: 'The article discusses a new type of diffusion model called MaskAttn-SDXL, which is designed to improve the realism of text-to-image models by injecting binary masks into each cross-attention logit map. The method requires no positional encodings or auxiliary tokens and preserves the original inference path with minimal overhead. The authors tested their model on a dataset of multi-object prompts and found that it improved spatial compliance and attribute binding compared to other diffusion models.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 85d428bc6ec47ae2e8fde28428b233305fd9f481e1fb12748e6e1b8290901433
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.202646'
category: 24-computing
---

arXiv:2509.15357v1 Announce Type: new Abstract: Text-to-image diffusion models achieve impressive realism but often suffer from compositional failures on prompts with multiple objects, attributes, and spatial relations, resulting in cross-token interference where entities entangle, attributes mix across objects, and spatial cues are violated. To address these failures, we propose MaskAttn-SDXL,a region-level gating mechanism applied to the cross-attention logits of Stable Diffusion XL(SDXL)'s UNet. MaskAttn-SDXL learns a binary mask per layer, injecting it into each cross-attention logit map before softmax to sparsify token-to-latent interactions so that only semantically relevant connections remain active. The method requires no positional encodings, auxiliary tokens, or external region masks, and preserves the original inference path with negligible overhead. In practice, our model improves spatial compliance and attribute binding in multi-object prompts while preserving overall imag...