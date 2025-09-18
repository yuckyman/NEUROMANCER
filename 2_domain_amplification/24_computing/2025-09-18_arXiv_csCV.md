---
type: note
category: 24-computing
created: 2025-09-18 12:08
modified: 2025-09-18 12:08
tags:
- unified query learning
- joint 3D planar reconstruction
- pose estimation
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_PlaneRecTR____Unified_Query_Learning_for_Joint_3D_.txt
---


# arXiv: cs.CV

## summary
The paper introduces a unified framework for joint 3D planar reconstruction and pose estimation. It uses the ARXIV RSS feed to aggregate various sub-tasks, such as frame-wise plane detection, segmentation, parameter regression, and relative camera pose estimation. The authors provide an overview of the proposed methods and their integrations.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2307.13756

PlaneRecTR++: Unified Query Learning for Joint 3D Planar Reconstruction and Pose Estimation

arXiv:2307.13756v4 Announce Type: replace Abstract: The challenging task of 3D planar reconstruction from images involves several sub-tasks including frame-wise plane detection, segmentation, parameter regression and possibly depth prediction, along with cross-frame plane correspondence and relative camera pose estimation. Previous works adopt a divide and conquer strategy, addressing above sub-tasks with distinct network modules in a two-stage paradigm. Specifically, given an initial camera pose and per-frame plane predictions from the first stage, further exclusively designed modules relying on external plane correspondence labeling are applied to merge multi-view plane entities and produce refined camera pose. Notably, existing work fails to integrate these closely related sub-tasks into a unified framework, and instead addresses them separately and sequentially, which we identify as a primary source of performance limitations. Motivated by this finding and the success of query-base...

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
    <lastBuildDate>Thu, 18 Sep 2025 04:00:01 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Thu, 18 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Proximity-Based Evidence Retrieval for Uncertainty-Aware Neural Networks</title>
      <link>https://arxiv.org/abs/2509.13338</link>
      <description>arXiv:2509.13338v1 Announce Type: new 
Abstract: This work proposes an evidence-retrieval mechanism for uncertainty-aware decision-making that replaces a single global cutoff with an evidence-conditioned, instance-adaptive criterion. For each test instance, proximal exemplars are retrieved in an embedding space; their predictive distributions are fused via Dempster-Shafer theory. The resulting fused belief acts as a per-instance thresholding mechanism. Because the supporting evidences are explicit, decisions are transparent and auditable. Experiments on CIFAR-10/100 with BiT and ViT backbones show higher or comparable uncertainty-aware performance with materially fewer confidently incorrect outcomes and a sustainable review load compared with applying threshold on prediction entropy. Notably, only a few evidences are sufficient to realize these gains; increasing the evidence set yields only modest changes. These results indicate that evid...


## Scraped from https://arxiv.org/abs/2307.13756
[2307.13756] PlaneRecTR++: Unified Query Learning for Joint 3D Planar Reconstruction and Pose Estimation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2307.13756 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2307.13756 (cs) [Submitted on 25 Jul 2023 (v1), last revised 17 Sep 2025 (this version, v4)] Title:PlaneRecTR++: Unified Query Learning for Joint 3D Planar Reconstruction and Pose Estimation Authors:Jingjia Shi, Shuaifeng Zhi, Kai Xu View a PDF of the paper titled PlaneRecTR++: Unified Query Learning for Joint 3D Planar Reconstruction and Pose Estimation, by Jingjia Shi and 2 other authors View PDF HTML (experimental) Abstract:The challenging task of 3D planar reconstruction from images involves several sub-tasks including frame-wise plane detection, segmentation, parameter regression and possibly depth prediction, along with cross-frame plane correspondence and relative camera pose estimation. Previous works adopt a divide and conquer strategy, addressing above sub-tasks with distinct network modules in a two-stage paradigm. Specifically, given an initial camera pose and per-frame plane predictions from the first stage, further exclusively designed modules relying on external plane correspondence labeling are applied to merge multi-view plane entities and produce refined camera pose. Notably, existing work fails to integrate these closely related sub-tasks into a unified framework, and instead addresses them separately and sequentially, which we identify as a primary source of performance limitations. Motivated by this finding and the success of query-based learn...


## connections
- processed from phone shortcut
