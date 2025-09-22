---
title: 'CoDoL: Conditional Domain Prompt Learning for Out-of-Distribution Generalization'
link: https://arxiv.org/abs/2509.15330
summary: 'The paper introduces a new method called CoDoL, which combines contrastive language-image pre-training (CLIP) methods with domain knowledge to improve OOD generalization in vision-language models. The key contributions are:

1. CoDoL uses CLIP methods for prompt generation and improves their alignment with domain information.
2. It proposes a lightweight Domain Meta Network (DMN) to generate input-conditioned prompts, enhancing the model's ability to learn from specific domains.
3. The method outperforms existing approaches in both accuracy and robustness on various datasets.

The paper also discusses limitations of CLIP methods and presents a comparison with other state-of-the-art methods.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: a7b513f273ab341efef57628639684f5a12301306aa8409a3149d0fcf6b98fa6
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:11.776737'
category: 24-computing
---

arXiv:2509.15330v1 Announce Type: new Abstract: Recent advances in pre-training vision-language models (VLMs), e.g., contrastive language-image pre-training (CLIP) methods, have shown great potential in learning out-of-distribution (OOD) representations. Despite showing competitive performance, the prompt-based CLIP methods still suffer from: i) inaccurate text descriptions, which leads to degraded accuracy and robustness, and poses a challenge for zero-shot CLIP methods. ii) limited vision-language embedding alignment, which significantly affects the generalization performance. To tackle the above issues, this paper proposes a novel Conditional Domain prompt Learning (CoDoL) method, which utilizes readily-available domain information to form prompts and improves the vision-language embedding alignment for improving OOD generalization. To capture both instance-specific and domain-specific information, we further propose a lightweight Domain Meta Network (DMN) to generate input-conditio...