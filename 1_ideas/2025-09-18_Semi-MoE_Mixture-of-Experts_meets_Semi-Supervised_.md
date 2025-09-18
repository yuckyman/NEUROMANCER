---
type: note
category: ideas
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags: ['semi-supervised', 'histopathology', 'multi-task', 'expert system', 'deep learning']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Semi-MoE__Mixture-of-Experts_meets_Semi-Supervised.txt
---

# Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation

## summary
This paper introduces a new multi-task mixture-of-experts framework for semi-supervised histopathology image segmentation, addressing the challenges of noisy pseudo-labels due to ambiguous gland boundaries and morphological misclassification.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13834

Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation

arXiv:2509.13834v1 Announce Type: new Abstract: Semi-supervised learning has been employed to alleviate the need for extensive labeled data for histopathology image segmentation, but existing methods struggle with noisy pseudo-labels due to ambiguous gland boundaries and morphological misclassification. This paper introduces Semi-MOE, to the best of our knowledge, the first multi-task Mixture-of-Experts framework for semi-supervised histopathology image segmentation. Our approach leverages three specialized expert networks: A main segmentation expert, a signed distance field regression expert, and a boundary prediction expert, each dedicated to capturing distinct morphological features. Subsequently, the Multi-Gating Pseudo-labeling module dynamically aggregates expert features, enabling a robust fuse-and-refine pseudo-labeling mechanism. Furthermore, to eliminate manual tuning while dynamically balancing multiple learning objectives, we propose an Adaptive Multi-Objective Loss. Extens...

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


## Scraped from https://arxiv.org/abs/2509.13834
[2509.13834] Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13834 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13834 (cs) [Submitted on 17 Sep 2025] Title:Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation Authors:Nguyen Lan Vi Vu, Thanh-Huy Nguyen, Thien Nguyen, Daisuke Kihara, Tianyang Wang, Xingjian Li, Min Xu View a PDF of the paper titled Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation, by Nguyen Lan Vi Vu and 6 other authors View PDF HTML (experimental) Abstract:Semi-supervised learning has been employed to alleviate the need for extensive labeled data for histopathology image segmentation, but existing methods struggle with noisy pseudo-labels due to ambiguous gland boundaries and morphological misclassification. This paper introduces Semi-MOE, to the best of our knowledge, the first multi-task Mixture-of-Experts framework for semi-supervised histopathology image segmentation. Our approach leverages three specialized expert networks: A main segmentation expert, a signed distance field regression expert, and a boundary prediction expert, each dedicated to capturing distinct morphological features. Subsequently, the Multi-Gating Pseudo-labeling module dynamically aggregates expert features, enabling a robust fuse-and-refine pseudo-labeling mechanism. Furthermore, to eliminate manual tuning while dynamically balancing multiple learning objectives, we propose an Adaptive Multi-Objective Loss. Extensive experiments on Gl...


## connections
- processed from phone shortcut
