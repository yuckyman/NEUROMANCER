---
type: note
category: 24-computing
created: 2025-09-18 12:10
modified: 2025-09-18 12:10
tags:
- Large Vision-Language Models
- LVLMs
- Self-Rationale Calibration
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Towards_Rationale-Answer_Alignment_of_LVLMs_via_Se.txt
---


# Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration

## summary
This paper introduces a framework called SRC (Self-Rationale Calibration) to iteratively calibrate the alignment between rational explanations and generated answers in Large Vision-Language Models (LVLMs). The rationale fine-tuning approach involves modifying responses to require rationales before obtaining an answer, while the pairwise scoring strategy selects candidates from LVLM models for comparison.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13919

Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration

arXiv:2509.13919v1 Announce Type: new Abstract: Large Vision-Language Models (LVLMs) have manifested strong visual question answering capability. However, they still struggle with aligning the rationale and the generated answer, leading to inconsistent reasoning and incorrect responses. To this end, this paper introduces the Self-Rationale Calibration (SRC) framework to iteratively calibrate the alignment between rationales and answers. SRC begins by employing a lightweight "rationale fine-tuning" approach, which modifies the model's response format to require a rationale before deriving an answer without explicit prompts. Next, SRC searches for a diverse set of candidate responses from the fine-tuned LVLMs for each sample, followed by a proposed pairwise scoring strategy using a tailored scoring model, R-Scorer, to evaluate both rationale quality and factual consistency of candidates. Based on a confidence-weighted preference curation process, SRC decouples the alignment calibration i...

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


## Scraped from https://arxiv.org/abs/2509.13919
[2509.13919] Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13919 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13919 (cs) [Submitted on 17 Sep 2025] Title:Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration Authors:Yuanchen Wu, Ke Yan, Shouhong Ding, Ziyin Zhou, Xiaoqiang Li View a PDF of the paper titled Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration, by Yuanchen Wu and 4 other authors View PDF HTML (experimental) Abstract:Large Vision-Language Models (LVLMs) have manifested strong visual question answering capability. However, they still struggle with aligning the rationale and the generated answer, leading to inconsistent reasoning and incorrect responses. To this end, this paper introduces the Self-Rationale Calibration (SRC) framework to iteratively calibrate the alignment between rationales and answers. SRC begins by employing a lightweight &#34;rationale fine-tuning&#34; approach, which modifies the model&#39;s response format to require a rationale before deriving an answer without explicit prompts. Next, SRC searches for a diverse set of candidate responses from the fine-tuned LVLMs for each sample, followed by a proposed pairwise scoring strategy using a tailored scoring model, R-Scorer, to evaluate both rationale quality and factual consistency of candidates. Based on a confidence-weighted preference curation process, SRC decouples the alignment calibration into a preference fine-tuning manner, leading to significant improv...


## connections
- processed from phone shortcut
