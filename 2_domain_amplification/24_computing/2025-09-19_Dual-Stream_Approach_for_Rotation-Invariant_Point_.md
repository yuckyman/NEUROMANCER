---
type: note
category: 24-computing
created: 2025-09-19 17:59
modified: 2025-09-19 17:59
tags:
- masking
- point clouds
- rotation-invariance
- arXiv
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175448_rss_Beyond_Random_Masking__A_Dual-Stream_Approach_for_.txt
content_hash: a388d7cf8c422e3866780f93bec09f95f2f087a8de084218444f024e849502e6
---


# Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders

## summary
We propose a dual-stream masking approach to address the limitations of existing rotation-invariant point cloud masked autoencoders (MAE). Grid masking creates structured patterns through coordinate sorting, while semantic masking uses attention-driven clustering. These techniques capture geometric and semantic relationships across different orientations.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14975

Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders

arXiv:2509.14975v1 Announce Type: new Abstract: Existing rotation-invariant point cloud masked autoencoders (MAE) rely on random masking strategies that overlook geometric structure and semantic coherence. Random masking treats patches independently, failing to capture spatial relationships consistent across orientations and overlooking semantic object parts that maintain identity regardless of rotation. We propose a dual-stream masking approach combining 3D Spatial Grid Masking and Progressive Semantic Masking to address these fundamental limitations. Grid masking creates structured patterns through coordinate sorting to capture geometric relationships that persist across different orientations, while semantic masking uses attention-driven clustering to discover semantically meaningful parts and maintain their coherence during masking. These complementary streams are orchestrated via curriculum learning with dynamic weighting, progressing from geometric understanding to semantic disco...

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


## Scraped from https://arxiv.org/abs/2509.14975
[2509.14975] Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14975 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14975 (cs) [Submitted on 18 Sep 2025] Title:Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders Authors:Xuanhua Yin, Dingxin Zhang, Yu Feng, Shunqi Mao, Jianhui Yu, Weidong Cai View a PDF of the paper titled Beyond Random Masking: A Dual-Stream Approach for Rotation-Invariant Point Cloud Masked Autoencoders, by Xuanhua Yin and 5 other authors View PDF HTML (experimental) Abstract:Existing rotation-invariant point cloud masked autoencoders (MAE) rely on random masking strategies that overlook geometric structure and semantic coherence. Random masking treats patches independently, failing to capture spatial relationships consistent across orientations and overlooking semantic object parts that maintain identity regardless of rotation. We propose a dual-stream masking approach combining 3D Spatial Grid Masking and Progressive Semantic Masking to address these fundamental limitations. Grid masking creates structured patterns through coordinate sorting to capture geometric relationships that persist across different orientations, while semantic masking uses attention-driven clustering to discover semantically meaningful parts and maintain their coherence during masking. These complementary streams are orchestrated via curriculum learning with dynamic weighting, progressing from geometric understanding to se...


## connections
- processed from phone shortcut
