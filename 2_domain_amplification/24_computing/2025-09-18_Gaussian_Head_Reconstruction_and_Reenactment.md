---
type: note
category: 24-computing
created: 2025-09-18 11:54
modified: 2025-09-18 11:54
tags:
- webSSL
- reconstruction
- gaussian head
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Reconstruction_and_Reenactment_Separated_Method_fo.txt
---


# Gaussian Head Reconstruction and Reenactment

## summary
We propose a method for generating realistic 3D Gaussian heads using an one-shot generation framework, which involves two-stage training. The key innovation is the use of WebSSL for efficient generation and control signals.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.05582

Reconstruction and Reenactment Separated Method for Realistic Gaussian Head

arXiv:2509.05582v2 Announce Type: replace Abstract: In this paper, we explore a reconstruction and reenactment separated framework for 3D Gaussians head, which requires only a single portrait image as input to generate controllable avatar. Specifically, we developed a large-scale one-shot gaussian head generator built upon WebSSL and employed a two-stage training approach that significantly enhances the capabilities of generalization and high-frequency texture reconstruction. During inference, an ultra-lightweight gaussian avatar driven by control signals enables high frame-rate rendering, achieving 90 FPS at a resolution of 512x512. We further demonstrate that the proposed framework follows the scaling law, whereby increasing the parameter scale of the reconstruction module leads to improved performance. Moreover, thanks to the separation design, driving efficiency remains unaffected. Finally, extensive quantitative and qualitative experiments validate that our approach outperforms cu...

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


## Scraped from https://arxiv.org/abs/2509.05582
[2509.05582] Reconstruction and Reenactment Separated Method for Realistic Gaussian Head Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.05582 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.05582 (cs) [Submitted on 6 Sep 2025 (v1), last revised 17 Sep 2025 (this version, v2)] Title:Reconstruction and Reenactment Separated Method for Realistic Gaussian Head Authors:Zhiling Ye, Cong Zhou, Xiubao Zhang, Haifeng Shen, Weihong Deng, Quan Lu View a PDF of the paper titled Reconstruction and Reenactment Separated Method for Realistic Gaussian Head, by Zhiling Ye and 5 other authors View PDF HTML (experimental) Abstract:In this paper, we explore a reconstruction and reenactment separated framework for 3D Gaussians head, which requires only a single portrait image as input to generate controllable avatar. Specifically, we developed a large-scale one-shot gaussian head generator built upon WebSSL and employed a two-stage training approach that significantly enhances the capabilities of generalization and high-frequency texture reconstruction. During inference, an ultra-lightweight gaussian avatar driven by control signals enables high frame-rate rendering, achieving 90 FPS at a resolution of 512x512. We further demonstrate that the proposed framework follows the scaling law, whereby increasing the parameter scale of the reconstruction module leads to improved performance. Moreover, thanks to the separation design, driving efficiency remains unaffected. Finally, extensive quantitative and qualitative experiments validate that our approach outperforms current state-of-the-...


## connections
- processed from phone shortcut
