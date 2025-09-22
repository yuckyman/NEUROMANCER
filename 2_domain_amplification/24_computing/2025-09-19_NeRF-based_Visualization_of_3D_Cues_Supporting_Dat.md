---
type: note
category: 24-computing
created: 2025-09-19 17:57
modified: 2025-09-19 17:57
tags:
- nerf
- pose estimation
- image generation
- deep learning
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175448_rss_NeRF-based_Visualization_of_3D_Cues_Supporting_Dat.txt
content_hash: c312f0af97b5f53b1fb43fc884927a9c339d87a8040b9950c22bc3be84327175
---


# NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Es...

## summary
We present a method to visualize the 3D visual cues on which a given pose estimator relies. By training a NeRF-based image generator, we enforce the generator to render the main 3D features exploited by the spacecraft pose estimation network. Experiments demonstrate that our method recovers the relevant 3D cues.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14890

NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Estimation

arXiv:2509.14890v1 Announce Type: new Abstract: On-orbit operations require the estimation of the relative 6D pose, i.e., position and orientation, between a chaser spacecraft and its target. While data-driven spacecraft pose estimation methods have been developed, their adoption in real missions is hampered by the lack of understanding of their decision process. This paper presents a method to visualize the 3D visual cues on which a given pose estimator relies. For this purpose, we train a NeRF-based image generator using the gradients back-propagated through the pose estimation network. This enforces the generator to render the main 3D features exploited by the spacecraft pose estimation network. Experiments demonstrate that our method recovers the relevant 3D cues. Furthermore, they offer additional insights on the relationship between the pose estimation network supervision and its implicit representation of the target spacecraft.

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


## Scraped from https://arxiv.org/abs/2509.14890
[2509.14890] NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Estimation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14890 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14890 (cs) [Submitted on 18 Sep 2025] Title:NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Estimation Authors:Antoine Legrand, Renaud Detry, Christophe De Vleeschouwer View a PDF of the paper titled NeRF-based Visualization of 3D Cues Supporting Data-Driven Spacecraft Pose Estimation, by Antoine Legrand and 2 other authors View PDF Abstract:On-orbit operations require the estimation of the relative 6D pose, i.e., position and orientation, between a chaser spacecraft and its target. While data-driven spacecraft pose estimation methods have been developed, their adoption in real missions is hampered by the lack of understanding of their decision process. This paper presents a method to visualize the 3D visual cues on which a given pose estimator relies. For this purpose, we train a NeRF-based image generator using the gradients back-propagated through the pose estimation network. This enforces the generator to render the main 3D features exploited by the spacecraft pose estimation network. Experiments demonstrate that our method recovers the relevant 3D cues. Furthermore, they offer additional insights on the relationship between the pose estimation network supervision and its implicit representation of the target spacecraft. Comments: under review (8 pages, 2 figures) Subjects: Computer Vision and Pattern Recognition (cs.CV) Cite as: arXi...


## connections
- processed from phone shortcut
