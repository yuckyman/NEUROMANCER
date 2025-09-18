---
type: note
category: 24-computing
created: 2025-09-18 11:55
modified: 2025-09-18 11:55
tags:
- text-to-image
- person retrieval
- cross-modal matching
- fine-grained alignment
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Cross-modal_Full-mode_Fine-grained_Alignment_for_T.txt
---


# Cross-modal Full-mode Fine-grained Alignment for Text-to-Image Person Retrieval

## summary
This paper introduces FMFA (Fine-grained Multi-object feature alignment), a new approach to achieve effective cross-modal fine-grained alignment for text-to-image person retrieval. By incorporating attention mechanisms and verifying local features, it addresses the challenges of hard negative samples in existing methods.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13754

Cross-modal Full-mode Fine-grained Alignment for Text-to-Image Person Retrieval

arXiv:2509.13754v1 Announce Type: new Abstract: Text-to-Image Person Retrieval (TIPR) is a cross-modal matching task that aims to retrieve the most relevant person images based on a given text query. The key challenge in TIPR lies in achieving effective alignment between textual and visual modalities within a common latent space. To address this challenge, prior approaches incorporate attention mechanisms for implicit cross-modal local alignment. However, they lack the ability to verify whether all local features are correctly aligned. Moreover, existing methods primarily focus on hard negative samples during model updates, with the goal of refining distinctions between positive and negative pairs, often neglecting incorrectly matched positive pairs. To alleviate these issues, we propose FMFA, a cross-modal Full-Mode Fine-grained Alignment framework, which enhances global matching through explicit fine-grained alignment and existing implicit relational reasoning -- hence the term ``ful...

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


## Scraped from https://arxiv.org/abs/2509.13754
[2509.13754] Cross-modal Full-mode Fine-grained Alignment for Text-to-Image Person Retrieval Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13754 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13754 (cs) [Submitted on 17 Sep 2025] Title:Cross-modal Full-mode Fine-grained Alignment for Text-to-Image Person Retrieval Authors:Hao Yin, Xin Man, Feiyu Chen, Jie Shao, Heng Tao Shen View a PDF of the paper titled Cross-modal Full-mode Fine-grained Alignment for Text-to-Image Person Retrieval, by Hao Yin and 4 other authors View PDF HTML (experimental) Abstract:Text-to-Image Person Retrieval (TIPR) is a cross-modal matching task that aims to retrieve the most relevant person images based on a given text query. The key challenge in TIPR lies in achieving effective alignment between textual and visual modalities within a common latent space. To address this challenge, prior approaches incorporate attention mechanisms for implicit cross-modal local alignment. However, they lack the ability to verify whether all local features are correctly aligned. Moreover, existing methods primarily focus on hard negative samples during model updates, with the goal of refining distinctions between positive and negative pairs, often neglecting incorrectly matched positive pairs. To alleviate these issues, we propose FMFA, a cross-modal Full-Mode Fine-grained Alignment framework, which enhances global matching through explicit fine-grained alignment and existing implicit relational reasoning -- hence the term ``full-mode&#34; -- without requiring additional supervision. Specifically, we ...


## connections
- processed from phone shortcut
