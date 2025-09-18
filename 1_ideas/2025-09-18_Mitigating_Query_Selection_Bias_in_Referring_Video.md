---
type: note
category: projects
created: 2025-09-18 12:09
modified: 2025-09-18 12:09
tags: ['query-based methods', 'video object segmentation', 'RVOS', 'cross-modal alignment', 'query selection bias']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Mitigating_Query_Selection_Bias_in_Referring_Video.txt
---

# Mitigating Query Selection Bias in Referring Video Object Segmentation

## summary
Proposed approach to dynamically construct refering query components using both linguistic cues and visual guidance, addressing query selection bias in Referring Video Object Segmentation.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13722

Mitigating Query Selection Bias in Referring Video Object Segmentation

arXiv:2509.13722v1 Announce Type: new Abstract: Recently, query-based methods have achieved remarkable performance in Referring Video Object Segmentation (RVOS) by using textual static object queries to drive cross-modal alignment. However, these static queries are easily misled by distractors with similar appearance or motion, resulting in \emph{query selection bias}. To address this issue, we propose Triple Query Former (TQF), which factorizes the referring query into three specialized components: an appearance query for static attributes, an intra-frame interaction query for spatial relations, and an inter-frame motion query for temporal association. Instead of relying solely on textual embeddings, our queries are dynamically constructed by integrating both linguistic cues and visual guidance. Furthermore, we introduce two motion-aware aggregation modules that enhance object token representations: Intra-frame Interaction Aggregation incorporates position-aware interactions among obj...

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


## Scraped from https://arxiv.org/abs/2509.13722
[2509.13722] Mitigating Query Selection Bias in Referring Video Object Segmentation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13722 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13722 (cs) [Submitted on 17 Sep 2025] Title:Mitigating Query Selection Bias in Referring Video Object Segmentation Authors:Dingwei Zhang, Dong Zhang, Jinhui Tang View a PDF of the paper titled Mitigating Query Selection Bias in Referring Video Object Segmentation, by Dingwei Zhang and 2 other authors View PDF HTML (experimental) Abstract:Recently, query-based methods have achieved remarkable performance in Referring Video Object Segmentation (RVOS) by using textual static object queries to drive cross-modal alignment. However, these static queries are easily misled by distractors with similar appearance or motion, resulting in \emph{query selection bias}. To address this issue, we propose Triple Query Former (TQF), which factorizes the referring query into three specialized components: an appearance query for static attributes, an intra-frame interaction query for spatial relations, and an inter-frame motion query for temporal association. Instead of relying solely on textual embeddings, our queries are dynamically constructed by integrating both linguistic cues and visual guidance. Furthermore, we introduce two motion-aware aggregation modules that enhance object token representations: Intra-frame Interaction Aggregation incorporates position-aware interactions among objects within a single frame, while Inter-frame Motion Aggregation leverages trajectory-guided alignment across ...


## connections
- processed from phone shortcut
