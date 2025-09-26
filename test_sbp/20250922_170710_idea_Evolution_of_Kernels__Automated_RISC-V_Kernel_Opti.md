---
title: 'Evolution of Kernels: Automated RISC-V Kernel Optimization with Large Language
  Models'
link: https://arxiv.org/abs/2509.14265
summary: 'The article discusses the use of large language models (LLMs) to automate kernel design for domains with limited reference material, such as RISC-V. LLMs like Qwen have shown promise in this area, but their effectiveness remains unproven. The authors present Evolution of Kernels (EoK), a novel LLM-based evolutionary program search framework that automates kernel design for domains with limited reference material. EoK mitigates the issue by mining and formalizing reusable optimization ideas from established kernel libraries' development histories; it then guides parallel LLM explorations using these ideas, enriched via Retrieval-Augmented Generation (RAG) with RISC-V-specific context, prioritizing historically effective techniques. The authors present empirical evidence that EoK outperforms existing methods in terms of accuracy and efficiency.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: e9627fad3e8be20807314044b43707ed5569f49a424e9175d86040cc76592dc3
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.763744'
category: 24-computing
---

arXiv:2509.14265v1 Announce Type: cross Abstract: Automated kernel design is critical for overcoming software ecosystem barriers in emerging hardware platforms like RISC-V. While large language models (LLMs) have shown promise for automated kernel optimization, demonstrating success in CUDA domains with comprehensive technical documents and mature codebases, their effectiveness remains unproven for reference-scarce domains like RISC-V. We present Evolution of Kernels (EoK), a novel LLM-based evolutionary program search framework that automates kernel design for domains with limited reference material. EoK mitigates reference scarcity by mining and formalizing reusable optimization ideas (general design principles + actionable thoughts) from established kernel libraries' development histories; it then guides parallel LLM explorations using these ideas, enriched via Retrieval-Augmented Generation (RAG) with RISC-V-specific context, prioritizing historically effective techniques. Empirica...