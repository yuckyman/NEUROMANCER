---
title: Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest
  X-rays
link: https://arxiv.org/abs/2509.15234
summary: 'The article discusses the challenges in image-text alignment for radiology, specifically focusing on how large language model (LLM) encoders can provide robust clinical representations that transfer across diverse styles and improve image-text alignment.

1. **Context**: The article mentions that vision-language pretraining has advanced image-text alignment but faces limitations due to heterogeneity in clinical reports, including abbreviations, impression-only notes, and stylistic variability.

2. **Main Contribution**:
   - **LLM Encoders for Radiology**: The authors introduce two new approaches: LLM2VEC4CXR (domain-adapted LLM encoder) and LLM2CLIP4CXR (dual-tower framework).
   - **LLM2VEC4CXR**: This approach uses a domain-specific language model (LLM) to encode clinical reports, improving understanding of the text while handling abbreviations and style variation.
   - **LLM2CLIP4CXR**: It couples this LLM encoder with a vision backbone to improve image-text alignment.

3. **Key Findings**:
   - **Improvement in Text Understanding**: The authors report that LLM2VEC4CXR outperforms BERT-based baselines and achieves strong clinical alignment on report-level metrics.
   - **Handling Abbreviations and Style Variation**: LLM2CLIP4CXR demonstrates better performance by leveraging the vision backbone, improving image-text alignment.

4. **Comparative Analysis**:
   - The article compares LLM2VEC4CXR with BERT-based baselines and shows that it outperforms both in terms of text understanding and clinical alignment.
   - It also notes that LLM2CLIP4CXR is more effective at improving image-text alignment compared to LLM2VEC4CXR.

5. **Future Work**:
   - The authors suggest that further research could explore how these approaches can be extended to other medical domains, such as pathology or oncology.
   - They also discuss the potential of using these models in a more general-purpose setting for radiology and other clinical tasks.

In summary, the article presents two new approaches (LLM2VEC4CXR and LLM2CLIP4CXR) that leverage domain-specific language models to improve image-text alignment in radiology.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 5c3071dde1e90c956e32ce701deed6d9d7ed24b5bbe958a4665e397051daa111
feed_title: cs.CV updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.CV
date_processed: '2025-09-22T17:07:09.865641'
category: 24-computing
---

arXiv:2509.15234v1 Announce Type: new Abstract: Vision-language pretraining has advanced image-text alignment, yet progress in radiology remains constrained by the heterogeneity of clinical reports, including abbreviations, impression-only notes, and stylistic variability. Unlike general-domain settings where more data often leads to better performance, naively scaling to large collections of noisy reports can plateau or even degrade model learning. We ask whether large language model (LLM) encoders can provide robust clinical representations that transfer across diverse styles and better guide image-text alignment. We introduce LLM2VEC4CXR, a domain-adapted LLM encoder for chest X-ray reports, and LLM2CLIP4CXR, a dual-tower framework that couples this encoder with a vision backbone. LLM2VEC4CXR improves clinical text understanding over BERT-based baselines, handles abbreviations and style variation, and achieves strong clinical alignment on report-level metrics. LLM2CLIP4CXR leverages...