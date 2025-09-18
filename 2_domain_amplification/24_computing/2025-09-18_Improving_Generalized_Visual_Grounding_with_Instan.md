---
type: note
category: 24-computing
created: 2025-09-18 11:59
modified: 2025-09-18 11:59
tags:
- generalization
- instance-aware
- joint-learning
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Improving_Generalized_Visual_Grounding_with_Instan.txt
---


# Improving Generalized Visual Grounding with Instance-aware Joint Learning

## summary
This article introduces a new approach to improve the accuracy of Generalized Visual Grounding (GRE) tasks by jointly training GREC and GRES.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13747

Improving Generalized Visual Grounding with Instance-aware Joint Learning

arXiv:2509.13747v1 Announce Type: new Abstract: Generalized visual grounding tasks, including Generalized Referring Expression Comprehension (GREC) and Segmentation (GRES), extend the classical visual grounding paradigm by accommodating multi-target and non-target scenarios. Specifically, GREC focuses on accurately identifying all referential objects at the coarse bounding box level, while GRES aims for achieve fine-grained pixel-level perception. However, existing approaches typically treat these tasks independently, overlooking the benefits of jointly training GREC and GRES to ensure consistent multi-granularity predictions and streamline the overall process. Moreover, current methods often treat GRES as a semantic segmentation task, neglecting the crucial role of instance-aware capabilities and the necessity of ensuring consistent predictions between instance-level boxes and masks. To address these limitations, we propose InstanceVG, a multi-task generalized visual grounding framewo...

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


## Scraped from https://arxiv.org/abs/2509.13747
[2509.13747] Improving Generalized Visual Grounding with Instance-aware Joint Learning Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13747 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13747 (cs) [Submitted on 17 Sep 2025] Title:Improving Generalized Visual Grounding with Instance-aware Joint Learning Authors:Ming Dai, Wenxuan Cheng, Jiang-Jiang Liu, Lingfeng Yang, Zhenhua Feng, Wankou Yang, Jingdong Wang View a PDF of the paper titled Improving Generalized Visual Grounding with Instance-aware Joint Learning, by Ming Dai and 6 other authors View PDF HTML (experimental) Abstract:Generalized visual grounding tasks, including Generalized Referring Expression Comprehension (GREC) and Segmentation (GRES), extend the classical visual grounding paradigm by accommodating multi-target and non-target scenarios. Specifically, GREC focuses on accurately identifying all referential objects at the coarse bounding box level, while GRES aims for achieve fine-grained pixel-level perception. However, existing approaches typically treat these tasks independently, overlooking the benefits of jointly training GREC and GRES to ensure consistent multi-granularity predictions and streamline the overall process. Moreover, current methods often treat GRES as a semantic segmentation task, neglecting the crucial role of instance-aware capabilities and the necessity of ensuring consistent predictions between instance-level boxes and masks. To address these limitations, we propose InstanceVG, a multi-task generalized visual grounding framework equipped with instance-aware capabilities, w...


## connections
- processed from phone shortcut
