---
type: note
category: 24-computing
created: 2025-09-19 17:58
modified: 2025-09-19 17:58
tags:
- sparse-view
- diagonal priors
- iterative reconstruction
- diffusion transformers
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Cross-Distribution_Diffusion_Priors-Driven_Iterati.txt
content_hash: 60f26671a58cb08e12a35be26cdce994059167281152075592dae49fd1ad2da7
---


# Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Spars...

## summary
CDPIR (cross-distribution diffusion priors-driven iterative reconstruction) framework addresses the OOD problem in sparse-view CT by integrating cross-distribution diffusion priors, trained from a SiT architecture, with model-based iterative reconstruction methods.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13576

Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT

arXiv:2509.13576v1 Announce Type: cross Abstract: Sparse-View CT (SVCT) reconstruction enhances temporal resolution and reduces radiation dose, yet its clinical use is hindered by artifacts due to view reduction and domain shifts from scanner, protocol, or anatomical variations, leading to performance degradation in out-of-distribution (OOD) scenarios. In this work, we propose a Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) framework to tackle the OOD problem in SVCT. CDPIR integrates cross-distribution diffusion priors, derived from a Scalable Interpolant Transformer (SiT), with model-based iterative reconstruction methods. Specifically, we train a SiT backbone, an extension of the Diffusion Transformer (DiT) architecture, to establish a unified stochastic interpolant framework, leveraging Classifier-Free Guidance (CFG) across multiple datasets. By randomly dropping the conditioning with a null embedding during training, the model learns both domain-speci...

## Scraped from https://arxiv.org/rss/cs.CV
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
  <channel>
    <title>cs.CV updates on arXiv.org</title>
    <link>http://rss.arxiv.org/rss/cs.CV</link>
    <description>cs.CV updates on the arXiv.org e-print archive.</description>
    <atom:link href="http://rss.arxiv.org/rss/cs.CV" rel="self" type="application/rss+xml"/>
    <docs>http://www.rssboard.org/rss-specification</docs>
    <language>en-us</language>
    <lastBuildDate>Fri, 19 Sep 2025 04:00:01 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Fri, 19 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Class-invariant Test-Time Augmentation for Domain Generalization</title>
      <link>https://arxiv.org/abs/2509.14420</link>
      <description>arXiv:2509.14420v1 Announce Type: new 
Abstract: Deep models often suffer significant performance degradation under distribution shifts. Domain generalization (DG) seeks to mitigate this challenge by enabling models to generalize to unseen domains. Most prior approaches rely on multi-domain training or computationally intensive test-time adaptation. In contrast, we propose a complementary strategy: lightweight test-time augmentation. Specifically, we develop a novel Class-Invariant Test-Time Augmentation (CI-TTA) technique. The idea is to generate multiple variants of each input image through elastic and grid deformations that nevertheless belong to the same class as the original input. Their predictions are aggregated through a confidence-guided filtering scheme that remove unreliable outputs, ensuring the final decision relies on consistent and trustworthy cues. Extensive Experiments on PACS and Office-Home datasets demonstrate consistent gains...


## Scraped from https://arxiv.org/abs/2509.13576
[2509.13576] Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; eess &gt; arXiv:2509.13576 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Electrical Engineering and Systems Science > Image and Video Processing arXiv:2509.13576 (eess) [Submitted on 16 Sep 2025] Title:Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT Authors:Haodong Li, Shuo Han, Haiyang Mao, Yu Shi, Changsheng Fang, Jianjia Zhang, Weiwen Wu, Hengyong Yu View a PDF of the paper titled Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT, by Haodong Li and 7 other authors View PDF HTML (experimental) Abstract:Sparse-View CT (SVCT) reconstruction enhances temporal resolution and reduces radiation dose, yet its clinical use is hindered by artifacts due to view reduction and domain shifts from scanner, protocol, or anatomical variations, leading to performance degradation in out-of-distribution (OOD) scenarios. In this work, we propose a Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction (CDPIR) framework to tackle the OOD problem in SVCT. CDPIR integrates cross-distribution diffusion priors, derived from a Scalable Interpolant Transformer (SiT), with model-based iterative reconstruction methods. Specifically, we train a SiT backbone, an extension of the Diffusion Transformer (DiT) architecture, to establish a unified stochastic interpolant framework, leveraging Classifier-Free Guidance (CFG) across multiple datasets. By randomly dropping the conditioning with a null embedding during training, the model learns both dom...


## connections
- processed from phone shortcut
