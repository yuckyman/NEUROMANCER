---
type: note
category: 24-computing
created: 2025-09-19 17:59
modified: 2025-09-19 17:59
tags:
- point cloud denoising
- score-based diffusion model
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175448_rss_Adaptive_and_Iterative_Point_Cloud_Denoising_with_.txt
content_hash: c6c7cf3d519b77d5591e141642b8f3cf02d3f4da3bddb062a32211559d5dd408
---


# Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model

## summary
We propose an adaptive and iterative point cloud denoising method based on the score-based diffusion model. For a given noisy point cloud, we estimate noise variation and determine an adaptive denoising schedule.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14560

Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model

arXiv:2509.14560v1 Announce Type: new Abstract: Point cloud denoising task aims to recover the clean point cloud from the scanned data coupled with different levels or patterns of noise. The recent state-of-the-art methods often train deep neural networks to update the point locations towards the clean point cloud, and empirically repeat the denoising process several times in order to obtain the denoised results. It is not clear how to efficiently arrange the iterative denoising processes to deal with different levels or patterns of noise. In this paper, we propose an adaptive and iterative point cloud denoising method based on the score-based diffusion model. For a given noisy point cloud, we first estimate the noise variation and determine an adaptive denoising schedule with appropriate step sizes, then invoke the trained network iteratively to update point clouds following the adaptive schedule. To facilitate this adaptive and iterative denoising process, we design the network archi...

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


## Scraped from https://arxiv.org/abs/2509.14560
[2509.14560] Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14560 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14560 (cs) [Submitted on 18 Sep 2025] Title:Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model Authors:Zhaonan Wang, Manyi Li, ShiQing Xin, Changhe Tu View a PDF of the paper titled Adaptive and Iterative Point Cloud Denoising with Score-Based Diffusion Model, by Zhaonan Wang and 3 other authors View PDF HTML (experimental) Abstract:Point cloud denoising task aims to recover the clean point cloud from the scanned data coupled with different levels or patterns of noise. The recent state-of-the-art methods often train deep neural networks to update the point locations towards the clean point cloud, and empirically repeat the denoising process several times in order to obtain the denoised results. It is not clear how to efficiently arrange the iterative denoising processes to deal with different levels or patterns of noise. In this paper, we propose an adaptive and iterative point cloud denoising method based on the score-based diffusion model. For a given noisy point cloud, we first estimate the noise variation and determine an adaptive denoising schedule with appropriate step sizes, then invoke the trained network iteratively to update point clouds following the adaptive schedule. To facilitate this adaptive and iterative denoising process, we design the network architecture and a two-stage sampling strategy for the network training to enable feat...


## connections
- processed from phone shortcut
