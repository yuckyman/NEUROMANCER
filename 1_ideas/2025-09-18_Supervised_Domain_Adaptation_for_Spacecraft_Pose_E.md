---
type: note
category: development
created: 2025-09-18 11:56
modified: 2025-09-18 11:56
tags: ['SDA', 'domain adaptation', 'spacecraft pose estimation']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Bridging_the_Synthetic-Real_Gap__Supervised_Domain.txt
---

# Supervised Domain Adaptation for Spacecraft Pose Estimation

## summary
This paper proposes a new Supervised Domain Adaptation (SDA) framework tailored for the keypoint regression task in spacecraft pose estimation. The SDA approach aims to address the persistent domain gap between synthetic and real or lab-generated imagery that can degrade performance of existing unsupervised approaches.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13792

Bridging the Synthetic-Real Gap: Supervised Domain Adaptation for Robust Spacecraft 6-DoF Pose Estimation

arXiv:2509.13792v1 Announce Type: new Abstract: Spacecraft Pose Estimation (SPE) is a fundamental capability for autonomous space operations such as rendezvous, docking, and in-orbit servicing. Hybrid pipelines that combine object detection, keypoint regression, and Perspective-n-Point (PnP) solvers have recently achieved strong results on synthetic datasets, yet their performance deteriorates sharply on real or lab-generated imagery due to the persistent synthetic-to-real domain gap. Existing unsupervised domain adaptation approaches aim to mitigate this issue but often underperform when a modest number of labeled target samples are available. In this work, we propose the first Supervised Domain Adaptation (SDA) framework tailored for SPE keypoint regression. Building on the Learning Invariant Representation and Risk (LIRR) paradigm, our method jointly optimizes domain-invariant representations and task-specific risk using both labeled synthetic and limited labeled real data, thereby ...

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


## Scraped from https://arxiv.org/abs/2509.13792
[2509.13792] Bridging the Synthetic-Real Gap: Supervised Domain Adaptation for Robust Spacecraft 6-DoF Pose Estimation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13792 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13792 (cs) [Submitted on 17 Sep 2025] Title:Bridging the Synthetic-Real Gap: Supervised Domain Adaptation for Robust Spacecraft 6-DoF Pose Estimation Authors:Inder Pal Singh, Nidhal Eddine Chenni, Abd El Rahman Shabayek, Arunkumar Rathinam, Djamila Aouada View a PDF of the paper titled Bridging the Synthetic-Real Gap: Supervised Domain Adaptation for Robust Spacecraft 6-DoF Pose Estimation, by Inder Pal Singh and 4 other authors View PDF HTML (experimental) Abstract:Spacecraft Pose Estimation (SPE) is a fundamental capability for autonomous space operations such as rendezvous, docking, and in-orbit servicing. Hybrid pipelines that combine object detection, keypoint regression, and Perspective-n-Point (PnP) solvers have recently achieved strong results on synthetic datasets, yet their performance deteriorates sharply on real or lab-generated imagery due to the persistent synthetic-to-real domain gap. Existing unsupervised domain adaptation approaches aim to mitigate this issue but often underperform when a modest number of labeled target samples are available. In this work, we propose the first Supervised Domain Adaptation (SDA) framework tailored for SPE keypoint regression. Building on the Learning Invariant Representation and Risk (LIRR) paradigm, our method jointly optimizes domain-invariant representations and task-specific risk using both l...


## connections
- processed from phone shortcut
