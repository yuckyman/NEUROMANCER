---
type: note
category: projects
created: 2025-09-18 11:55
modified: 2025-09-18 11:55
tags: ['registration', 'samir', 'arxiv', 'features']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_SAMIR__an_efficient_registration_framework_via_rob.txt
---

# Image Registration via SAMIR

## summary
SAMIR is a medical image registration framework that utilizes the Segment Anything Model (SAM) for efficient feature extraction from large-scale natural image datasets.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13629

SAMIR, an efficient registration framework via robust feature learning from SAM

arXiv:2509.13629v1 Announce Type: new Abstract: Image registration is a fundamental task in medical image analysis. Deformations are often closely related to the morphological characteristics of tissues, making accurate feature extraction crucial. Recent weakly supervised methods improve registration by incorporating anatomical priors such as segmentation masks or landmarks, either as inputs or in the loss function. However, such weak labels are often not readily available, limiting their practical use. Motivated by the strong representation learning ability of visual foundation models, this paper introduces SAMIR, an efficient medical image registration framework that utilizes the Segment Anything Model (SAM) to enhance feature extraction. SAM is pretrained on large-scale natural image datasets and can learn robust, general-purpose visual representations. Rather than using raw input images, we design a task-specific adaptation pipeline using SAM's image encoder to extract structure-aw...

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


## Scraped from https://arxiv.org/abs/2509.13629
[2509.13629] SAMIR, an efficient registration framework via robust feature learning from SAM Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13629 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13629 (cs) [Submitted on 17 Sep 2025] Title:SAMIR, an efficient registration framework via robust feature learning from SAM Authors:Yue He, Min Liu, Qinghao Liu, Jiazheng Wang, Yaonan Wang, Hang Zhang, Xiang Chen View a PDF of the paper titled SAMIR, an efficient registration framework via robust feature learning from SAM, by Yue He and 6 other authors View PDF HTML (experimental) Abstract:Image registration is a fundamental task in medical image analysis. Deformations are often closely related to the morphological characteristics of tissues, making accurate feature extraction crucial. Recent weakly supervised methods improve registration by incorporating anatomical priors such as segmentation masks or landmarks, either as inputs or in the loss function. However, such weak labels are often not readily available, limiting their practical use. Motivated by the strong representation learning ability of visual foundation models, this paper introduces SAMIR, an efficient medical image registration framework that utilizes the Segment Anything Model (SAM) to enhance feature extraction. SAM is pretrained on large-scale natural image datasets and can learn robust, general-purpose visual representations. Rather than using raw input images, we design a task-specific adaptation pipeline using SAM&#39;s image encoder to extract structure-aware feature embeddings, enabling more accura...


## connections
- processed from phone shortcut
