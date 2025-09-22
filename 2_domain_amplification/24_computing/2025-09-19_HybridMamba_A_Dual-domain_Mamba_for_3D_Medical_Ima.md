---
type: note
category: 24-computing
created: 2025-09-19 17:55
modified: 2025-09-19 17:55
tags:
- development
- projects
- ideas
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175448_rss_HybridMamba__A_Dual-domain_Mamba_for_3D_Medical_Im.txt
content_hash: 7f63ccb2d9d19ccbceef781a88a29983db9af4485a66814ff45ac2afcc019537
---


# HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation

## summary
We propose HybridMamba, a dual-domain architecture that combines feature scanning and local-adaptive pathways to improve 3D medical image segmentation. 

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14609

HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation

arXiv:2509.14609v1 Announce Type: new Abstract: In the domain of 3D biomedical image segmentation, Mamba exhibits the superior performance for it addresses the limitations in modeling long-range dependencies inherent to CNNs and mitigates the abundant computational overhead associated with Transformer-based frameworks when processing high-resolution medical volumes. However, attaching undue importance to global context modeling may inadvertently compromise critical local structural information, thus leading to boundary ambiguity and regional distortion in segmentation outputs. Therefore, we propose the HybridMamba, an architecture employing dual complementary mechanisms: 1) a feature scanning strategy that progressively integrates representations both axial-traversal and local-adaptive pathways to harmonize the relationship between local and global representations, and 2) a gated module combining spatial-frequency analysis for comprehensive contextual modeling. Besides, we collect a mu...

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


## Scraped from https://arxiv.org/abs/2509.14609
[2509.14609] HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14609 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14609 (cs) [Submitted on 18 Sep 2025] Title:HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation Authors:Weitong Wu, Zhaohu Xing, Jing Gong, Qin Peng, Lei Zhu View a PDF of the paper titled HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation, by Weitong Wu and 4 other authors View PDF HTML (experimental) Abstract:In the domain of 3D biomedical image segmentation, Mamba exhibits the superior performance for it addresses the limitations in modeling long-range dependencies inherent to CNNs and mitigates the abundant computational overhead associated with Transformer-based frameworks when processing high-resolution medical volumes. However, attaching undue importance to global context modeling may inadvertently compromise critical local structural information, thus leading to boundary ambiguity and regional distortion in segmentation outputs. Therefore, we propose the HybridMamba, an architecture employing dual complementary mechanisms: 1) a feature scanning strategy that progressively integrates representations both axial-traversal and local-adaptive pathways to harmonize the relationship between local and global representations, and 2) a gated module combining spatial-frequency analysis for comprehensive contextual modeling. Besides, we collect a multi-center CT dataset related to lung cancer. Experiments on MRI and CT datasets demonstrate that HybridMamba ...


## connections
- processed from phone shortcut
