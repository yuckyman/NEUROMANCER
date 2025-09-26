---
title: Comparing Computational Pathology Foundation Models using Representational
  Similarity Analysis
link: https://arxiv.org/abs/2509.15482
summary: 'The article discusses the structure and variability of the learned representations in foundation models used in computational pathology (CPath). Foundation models are increasingly developed for facilitating downstream tasks, but their learnable representations remain unknown. The study evaluates six CPath foundation models using techniques from computational neuroscience to analyze their representational spaces. The analysis reveals that UNI2 and Virchow2 have distinct representational structures compared to other models, while Prov-Gigapath has the highest average similarity across models. The authors note that the same training paradigm (vision-only vs. vision-language) does not guarantee higher representational similarities in all models.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 1b87b080951f1b29c4fa89be806437137e9150870835cac28b58d26362374f21
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:10.272311'
category: 24-computing
---

arXiv:2509.15482v1 Announce Type: new Abstract: Foundation models are increasingly developed in computational pathology (CPath) given their promise in facilitating many downstream tasks. While recent studies have evaluated task performance across models, less is known about the structure and variability of their learned representations. Here, we systematically analyze the representational spaces of six CPath foundation models using techniques popularized in computational neuroscience. The models analyzed span vision-language contrastive learning (CONCH, PLIP, KEEP) and self-distillation (UNI (v2), Virchow (v2), Prov-GigaPath) approaches. Through representational similarity analysis using H&amp;E image patches from TCGA, we find that UNI2 and Virchow2 have the most distinct representational structures, whereas Prov-Gigapath has the highest average similarity across models. Having the same training paradigm (vision-only vs. vision-language) did not guarantee higher representational simil...