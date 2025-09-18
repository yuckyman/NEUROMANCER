---
type: note
category: 24-computing
created: 2025-09-18 12:06
modified: 2025-09-18 12:06
tags:
- 3D Gaussian Splatting
- real-time SLAM
- memory-efficient
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_MemGS__Memory-Efficient_Gaussian_Splatting_for_Rea.txt
---


# Memory-Efficient Gaussian Splatting for Real-Time SLAM

## summary
This paper introduces a memory-efficient approach to 3D Gaussian splatting in real-time localization and mapping (SLAM) applications. The key contribution is the merging of redundant 3D Gaussian primitives in voxel space, leading to reduced GPU memory usage while maintaining rendering quality.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13536

MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM

arXiv:2509.13536v1 Announce Type: new Abstract: Recent advancements in 3D Gaussian Splatting (3DGS) have made a significant impact on rendering and reconstruction techniques. Current research predominantly focuses on improving rendering performance and reconstruction quality using high-performance desktop GPUs, largely overlooking applications for embedded platforms like micro air vehicles (MAVs). These devices, with their limited computational resources and memory, often face a trade-off between system performance and reconstruction quality. In this paper, we improve existing methods in terms of GPU memory usage while enhancing rendering quality. Specifically, to address redundant 3D Gaussian primitives in SLAM, we propose merging them in voxel space based on geometric similarity. This reduces GPU memory usage without impacting system runtime performance. Furthermore, rendering quality is improved by initializing 3D Gaussian primitives via Patch-Grid (PG) point sampling, enabling more...

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


## Scraped from https://arxiv.org/abs/2509.13536
[2509.13536] MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13536 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13536 (cs) [Submitted on 16 Sep 2025] Title:MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM Authors:Yinlong Bai, Hongxin Zhang, Sheng Zhong, Junkai Niu, Hai Li, Yijia He, Yi Zhou View a PDF of the paper titled MemGS: Memory-Efficient Gaussian Splatting for Real-Time SLAM, by Yinlong Bai and 6 other authors View PDF HTML (experimental) Abstract:Recent advancements in 3D Gaussian Splatting (3DGS) have made a significant impact on rendering and reconstruction techniques. Current research predominantly focuses on improving rendering performance and reconstruction quality using high-performance desktop GPUs, largely overlooking applications for embedded platforms like micro air vehicles (MAVs). These devices, with their limited computational resources and memory, often face a trade-off between system performance and reconstruction quality. In this paper, we improve existing methods in terms of GPU memory usage while enhancing rendering quality. Specifically, to address redundant 3D Gaussian primitives in SLAM, we propose merging them in voxel space based on geometric similarity. This reduces GPU memory usage without impacting system runtime performance. Furthermore, rendering quality is improved by initializing 3D Gaussian primitives via Patch-Grid (PG) point sampling, enabling more accurate modeling of the entire scene. Quantitative and qualitative evaluations on publicly availa...


## connections
- processed from phone shortcut
