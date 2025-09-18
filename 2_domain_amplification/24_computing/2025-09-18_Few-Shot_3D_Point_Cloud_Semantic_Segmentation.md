---
type: note
category: 24-computing
created: 2025-09-18 11:55
modified: 2025-09-18 11:55
tags:
- few-shot
- point clouds
- semantic segmentation
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_White_Aggregation_and_Restoration_for_Few-shot_3D_.txt
---


# Few-Shot 3D Point Cloud Semantic Segmentation

## summary
An advanced prototype generation method based on attention mechanism for few-shot 3D point cloud semantic segmentation.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13907

White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation

arXiv:2509.13907v1 Announce Type: new Abstract: Few-Shot 3D Point Cloud Segmentation (FS-PCS) aims to predict per-point labels for an unlabeled point cloud, given only a few labeled examples. To extract discriminative representations from the limited support set, existing methods have constructed prototypes using conventional algorithms such as farthest point sampling. However, we point out that its initial randomness significantly affects FS-PCS performance and that the prototype generation process remains underexplored despite its prevalence. This motivates us to investigate an advanced prototype generation method based on attention mechanism. Despite its potential, we found that vanilla module suffers from the distributional gap between learnable prototypical tokens and support features. To overcome this, we propose White Aggregation and Restoration Module (WARM), which resolves the misalignment by sandwiching cross-attention between whitening and coloring transformations. Specifica...

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


## Scraped from https://arxiv.org/abs/2509.13907
[2509.13907] White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13907 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13907 (cs) [Submitted on 17 Sep 2025] Title:White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation Authors:Jiyun Im, SuBeen Lee, Miso Lee, Jae-Pil Heo View a PDF of the paper titled White Aggregation and Restoration for Few-shot 3D Point Cloud Semantic Segmentation, by Jiyun Im and 3 other authors View PDF HTML (experimental) Abstract:Few-Shot 3D Point Cloud Segmentation (FS-PCS) aims to predict per-point labels for an unlabeled point cloud, given only a few labeled examples. To extract discriminative representations from the limited support set, existing methods have constructed prototypes using conventional algorithms such as farthest point sampling. However, we point out that its initial randomness significantly affects FS-PCS performance and that the prototype generation process remains underexplored despite its prevalence. This motivates us to investigate an advanced prototype generation method based on attention mechanism. Despite its potential, we found that vanilla module suffers from the distributional gap between learnable prototypical tokens and support features. To overcome this, we propose White Aggregation and Restoration Module (WARM), which resolves the misalignment by sandwiching cross-attention between whitening and coloring transformations. Specifically, whitening aligns the support features to prototypical tokens befor...


## connections
- processed from phone shortcut
