---
type: note
category: 24-computing
created: 2025-09-18 11:58
modified: 2025-09-18 11:58
tags:
- feature-based
- edge intelligence
- power systems
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Real-Time_Detection_and_Tracking_of_Foreign_Object.txt
---


# Real-Time Detection and Tracking of Foreign Object Intrusions in Power System...

## summary
This paper introduces a novel three-stage framework for real-time foreign object intrusion (FOI) detection and tracking in power transmission systems. It uses YOLOv7 segmentation, ConvNeXt feature extractor with triplet loss, and feature-assisted IoU tracker to enable scalable field deployment using low-cost edge hardware.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13396

Real-Time Detection and Tracking of Foreign Object Intrusions in Power Systems via Feature-Based Edge Intelligence

arXiv:2509.13396v1 Announce Type: new Abstract: This paper presents a novel three-stage framework for real-time foreign object intrusion (FOI) detection and tracking in power transmission systems. The framework integrates: (1) a YOLOv7 segmentation model for fast and robust object localization, (2) a ConvNeXt-based feature extractor trained with triplet loss to generate discriminative embeddings, and (3) a feature-assisted IoU tracker that ensures resilient multi-object tracking under occlusion and motion. To enable scalable field deployment, the pipeline is optimized for deployment on low-cost edge hardware using mixed-precision inference. The system supports incremental updates by adding embeddings from previously unseen objects into a reference database without requiring model retraining. Extensive experiments on real-world surveillance and drone video datasets demonstrate the framework's high accuracy and robustness across diverse FOI scenarios. In addition, hardware benchmarks on ...

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


## Scraped from https://arxiv.org/abs/2509.13396
[2509.13396] Real-Time Detection and Tracking of Foreign Object Intrusions in Power Systems via Feature-Based Edge Intelligence Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13396 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13396 (cs) [Submitted on 16 Sep 2025] Title:Real-Time Detection and Tracking of Foreign Object Intrusions in Power Systems via Feature-Based Edge Intelligence Authors:Xinan Wang, Di Shi, Fengyu Wang View a PDF of the paper titled Real-Time Detection and Tracking of Foreign Object Intrusions in Power Systems via Feature-Based Edge Intelligence, by Xinan Wang and 2 other authors View PDF Abstract:This paper presents a novel three-stage framework for real-time foreign object intrusion (FOI) detection and tracking in power transmission systems. The framework integrates: (1) a YOLOv7 segmentation model for fast and robust object localization, (2) a ConvNeXt-based feature extractor trained with triplet loss to generate discriminative embeddings, and (3) a feature-assisted IoU tracker that ensures resilient multi-object tracking under occlusion and motion. To enable scalable field deployment, the pipeline is optimized for deployment on low-cost edge hardware using mixed-precision inference. The system supports incremental updates by adding embeddings from previously unseen objects into a reference database without requiring model retraining. Extensive experiments on real-world surveillance and drone video datasets demonstrate the framework&#39;s high accuracy and robustness across diverse FOI scenarios. In addition, hardware benchmarks on NVID...


## connections
- processed from phone shortcut
