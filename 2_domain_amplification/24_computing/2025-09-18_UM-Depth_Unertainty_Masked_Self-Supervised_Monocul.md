---
type: note
category: 24-computing
created: 2025-09-18 12:04
modified: 2025-09-18 12:04
tags:
- depth estimation
- self-supervised
- motion-aware
- uncertainty-aware
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_UM-Depth___Uncertainty_Masked_Self-Supervised_Mono.txt
---


# UM-Depth: Unertainty Masked Self-Supervised Monocular Depth Estimation with V...

## summary
UM-Depth is a new framework for monocular depth estimation that combines motion- and uncertainty-aware refinement to enhance accuracy at dynamic object boundaries and in textureless regions. The key innovation is the use of an uncertainty mask and teacher-student training to reduce the impact of low-texture or dynamic regions on depth predictions.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13713

UM-Depth : Uncertainty Masked Self-Supervised Monocular Depth Estimation with Visual Odometry

arXiv:2509.13713v1 Announce Type: new Abstract: Monocular depth estimation has been increasingly adopted in robotics and autonomous driving for its ability to infer scene geometry from a single camera. In self-supervised monocular depth estimation frameworks, the network jointly generates and exploits depth and pose estimates during training, thereby eliminating the need for depth labels. However, these methods remain challenged by uncertainty in the input data, such as low-texture or dynamic regions, which can cause reduced depth accuracy. To address this, we introduce UM-Depth, a framework that combines motion- and uncertainty-aware refinement to enhance depth accuracy at dynamic object boundaries and in textureless regions. Specifically, we develop a teacherstudent training strategy that embeds uncertainty estimation into both the training pipeline and network architecture, thereby strengthening supervision where photometric signals are weak. Unlike prior motion-aware approaches tha...

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


## Scraped from https://arxiv.org/abs/2509.13713
[2509.13713] UM-Depth : Uncertainty Masked Self-Supervised Monocular Depth Estimation with Visual Odometry Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13713 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13713 (cs) [Submitted on 17 Sep 2025] Title:UM-Depth : Uncertainty Masked Self-Supervised Monocular Depth Estimation with Visual Odometry Authors:Tae-Wook Um, Ki-Hyeon Kim, Hyun-Duck Choi, Hyo-Sung Ahn View a PDF of the paper titled UM-Depth : Uncertainty Masked Self-Supervised Monocular Depth Estimation with Visual Odometry, by Tae-Wook Um and 2 other authors View PDF HTML (experimental) Abstract:Monocular depth estimation has been increasingly adopted in robotics and autonomous driving for its ability to infer scene geometry from a single camera. In self-supervised monocular depth estimation frameworks, the network jointly generates and exploits depth and pose estimates during training, thereby eliminating the need for depth labels. However, these methods remain challenged by uncertainty in the input data, such as low-texture or dynamic regions, which can cause reduced depth accuracy. To address this, we introduce UM-Depth, a framework that combines motion- and uncertainty-aware refinement to enhance depth accuracy at dynamic object boundaries and in textureless regions. Specifically, we develop a teacherstudent training strategy that embeds uncertainty estimation into both the training pipeline and network architecture, thereby strengthening supervision where photometric signals are weak. Unlike prior motion-aware approaches that incur inference-time ove...


## connections
- processed from phone shortcut
