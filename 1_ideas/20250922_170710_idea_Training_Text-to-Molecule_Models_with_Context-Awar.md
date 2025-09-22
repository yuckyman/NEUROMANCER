---
title: Training Text-to-Molecule Models with Context-Aware Tokenization
link: https://arxiv.org/abs/2509.04476
summary: 'The article discusses a novel approach called Context-Aware Molecular T5 (CAMT5) that aims to improve text-to-molecule models by incorporating atom-level tokenizations into their training process. The key feature of CAMT5 is its substructure-level tokenization, which focuses on modeling the global structural context within molecules rather than local connectivity alone. This approach allows CAMT5 to better capture the molecular semantics and thus potentially enhance the performance of text-to-molecule models in various chemical applications. The study compares CAMT5 with state-of-the-art text-to-molecule models and demonstrates its effectiveness through experiments on a variety of chemical tasks.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: ed4f6bea0963a9ef9aad5629434aae390743263d030edd3998589533611603fd
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.937077'
category: 24-computing
---

arXiv:2509.04476v2 Announce Type: replace-cross Abstract: Recently, text-to-molecule models have shown great potential across various chemical applications, e.g., drug-discovery. These models adapt language models to molecular data by representing molecules as sequences of atoms. However, they rely on atom-level tokenizations, which primarily focus on modeling local connectivity, thereby limiting the ability of models to capture the global structural context within molecules. To tackle this issue, we propose a novel text-to-molecule model, coined Context-Aware Molecular T5 (CAMT5). Inspired by the significance of the substructure-level contexts in understanding molecule structures, e.g., ring systems, we introduce substructure-level tokenization for text-to-molecule models. Building on our tokenization scheme, we develop an importance-based training strategy that prioritizes key substructures, enabling CAMT5 to better capture the molecular semantics. Extensive experiments verify the su...