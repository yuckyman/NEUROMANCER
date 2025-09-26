---
title: Trade-offs in Cross-Domain Generalization of Foundation Model Fine-Tuned for
  Biometric Applications
link: https://arxiv.org/abs/2509.14921
summary: 'The article discusses the limitations of foundation models like CLIP in terms of their ability to transfer across diverse vision tasks. However, when fine-tuned for highly specialized biometric tasks such as face recognition (FR), morphing attack detection (MAD), and presentation attack detection (PAD), these models may suffer from over-specialization due to cross-domain generalization issues.

The authors evaluate three instances of CLIP fine-tuned for these specific tasks: FR, MAD, and PAD. They compare the adapted model with the original CLIP baseline on 14 general vision datasets under zero-shot and linear-probe protocols, alongside common benchmarks such as FR, MAD, and PAD. Their results show that fine-tuned models suffer from over-specialization when fine-tuning for complex tasks like FR.

The authors also point out that task complexity and classification head duality can contribute to this issue.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 1467324ecc7a44b1adb16f0e351b3fd9d602531ebd67b5e2495ed5d28128941d
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.554163'
category: 24-computing
---

arXiv:2509.14921v1 Announce Type: new Abstract: Foundation models such as CLIP have demonstrated exceptional zero- and few-shot transfer capabilities across diverse vision tasks. However, when fine-tuned for highly specialized biometric tasks, face recognition (FR), morphing attack detection (MAD), and presentation attack detection (PAD), these models may suffer from over-specialization. Thus, they may lose one of their foundational strengths, cross-domain generalization. In this work, we systematically quantify these trade-offs by evaluating three instances of CLIP fine-tuned for FR, MAD, and PAD. We evaluate each adapted model as well as the original CLIP baseline on 14 general vision datasets under zero-shot and linear-probe protocols, alongside common FR, MAD, and PAD benchmarks. Our results indicate that fine-tuned models suffer from over-specialization, especially when fine-tuned for complex tasks of FR. Also, our results pointed out that task complexity and classification head d...