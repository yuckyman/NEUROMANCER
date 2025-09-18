---
type: note
category: development
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags: ['VLM', 'Region Detection', 'Urban Scenarios']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_MINGLE__VLMs_for_Semantically_Complex_Region_Detec.txt
---

# MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes

## summary
We introduce MINGLE (Modeling INterpersonal Group-Level Engagement), a modular three-stage pipeline that integrates human detection and depth estimation, VLM-based reasoning to classify pairwisely interacting regions in urban scenes.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13484

MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes

arXiv:2509.13484v1 Announce Type: new Abstract: Understanding group-level social interactions in public spaces is crucial for urban planning, informing the design of socially vibrant and inclusive environments. Detecting such interactions from images involves interpreting subtle visual cues such as relations, proximity, and co-movement - semantically complex signals that go beyond traditional object detection. To address this challenge, we introduce a social group region detection task, which requires inferring and spatially grounding visual regions defined by abstract interpersonal relations. We propose MINGLE (Modeling INterpersonal Group-Level Engagement), a modular three-stage pipeline that integrates: (1) off-the-shelf human detection and depth estimation, (2) VLM-based reasoning to classify pairwise social affiliation, and (3) a lightweight spatial aggregation algorithm to localize socially connected groups. To support this task and encourage future research, we present a new dat...

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


## Scraped from https://arxiv.org/abs/2509.13484
[2509.13484] MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13484 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13484 (cs) [Submitted on 16 Sep 2025] Title:MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes Authors:Liu Liu, Alexandra Kudaeva, Marco Cipriano, Fatimeh Al Ghannam, Freya Tan, Gerard de Melo, Andres Sevtsuk View a PDF of the paper titled MINGLE: VLMs for Semantically Complex Region Detection in Urban Scenes, by Liu Liu and 6 other authors View PDF HTML (experimental) Abstract:Understanding group-level social interactions in public spaces is crucial for urban planning, informing the design of socially vibrant and inclusive environments. Detecting such interactions from images involves interpreting subtle visual cues such as relations, proximity, and co-movement - semantically complex signals that go beyond traditional object detection. To address this challenge, we introduce a social group region detection task, which requires inferring and spatially grounding visual regions defined by abstract interpersonal relations. We propose MINGLE (Modeling INterpersonal Group-Level Engagement), a modular three-stage pipeline that integrates: (1) off-the-shelf human detection and depth estimation, (2) VLM-based reasoning to classify pairwise social affiliation, and (3) a lightweight spatial aggregation algorithm to localize socially connected groups. To support this task and encourage future research, we present a new dataset of 100K urban street-view images annotated w...


## connections
- processed from phone shortcut
