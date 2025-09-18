---
type: note
category: 24-computing
created: 2025-09-18 12:07
modified: 2025-09-18 12:07
tags:
- audio-video
- temporal-segmentation
- cross-modal
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Teacher-Guided_Pseudo_Supervision_and_Cross-Modal_.txt
---


# Temporal and Class-Aware Audio-Visual Video Parsing

## summary
We propose two strategies for audio-visual video parsing: an exponential moving average (EMA)-guided pseudo supervision framework that generates reliable segment-level masks and a class-aware cross-modal agreement loss. The summaries are short, relevant to the content without exceeding 100 words.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14097

Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing

arXiv:2509.14097v1 Announce Type: new Abstract: Weakly-supervised audio-visual video parsing (AVVP) seeks to detect audible, visible, and audio-visual events without temporal annotations. Previous work has emphasized refining global predictions through contrastive or collaborative learning, but neglected stable segment-level supervision and class-aware cross-modal alignment. To address this, we propose two strategies: (1) an exponential moving average (EMA)-guided pseudo supervision framework that generates reliable segment-level masks via adaptive thresholds or top-k selection, offering stable temporal guidance beyond video-level labels; and (2) a class-aware cross-modal agreement (CMA) loss that aligns audio and visual embeddings at reliable segment-class pairs, ensuring consistency across modalities while preserving temporal structure. Evaluations on LLP and UnAV-100 datasets shows that our method achieves state-of-the-art (SOTA) performance across multiple metrics.

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


## Scraped from https://arxiv.org/abs/2509.14097
[2509.14097] Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14097 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14097 (cs) [Submitted on 17 Sep 2025] Title:Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing Authors:Yaru Chen, Ruohao Guo, Liting Gao, Yang Xiang, Qingyu Luo, Zhenbo Li, Wenwu Wang View a PDF of the paper titled Teacher-Guided Pseudo Supervision and Cross-Modal Alignment for Audio-Visual Video Parsing, by Yaru Chen and 6 other authors View PDF HTML (experimental) Abstract:Weakly-supervised audio-visual video parsing (AVVP) seeks to detect audible, visible, and audio-visual events without temporal annotations. Previous work has emphasized refining global predictions through contrastive or collaborative learning, but neglected stable segment-level supervision and class-aware cross-modal alignment. To address this, we propose two strategies: (1) an exponential moving average (EMA)-guided pseudo supervision framework that generates reliable segment-level masks via adaptive thresholds or top-k selection, offering stable temporal guidance beyond video-level labels; and (2) a class-aware cross-modal agreement (CMA) loss that aligns audio and visual embeddings at reliable segment-class pairs, ensuring consistency across modalities while preserving temporal structure. Evaluations on LLP and UnAV-100 datasets shows that our method achieves state-of-the-art (SOTA) performance across multiple metrics. Subjects: Computer Vision an...


## connections
- processed from phone shortcut
