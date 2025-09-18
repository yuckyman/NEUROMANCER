---
type: note
category: development
created: 2025-09-18 11:54
modified: 2025-09-18 11:54
tags: ['KOLMOGOROV-ARNOLD-NETWORKS', 'ECOC', 'ERROR-COVERTED-OUTPUT-CODES']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Improving_Generalizability_of_Kolmogorov-Arnold_Ne.txt
---

# Improving Generalizability of Kolmogorov-Arnold Networks via Error-Correcting...

## summary
In this paper, the authors propose a KAN with Error-Correcting Output Codes (ECOC) framework to improve its generalizability in multi-class classification. They use ECOC to transform multi-class problems into multiple binary tasks without nonlinear activations, enhancing robustness via Hamming distance decoding.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2505.05798

Improving Generalizability of Kolmogorov-Arnold Networks via Error-Correcting Output Codes

arXiv:2505.05798v2 Announce Type: replace-cross Abstract: Kolmogorov-Arnold Networks (KAN) offer universal function approximation using univariate spline compositions without nonlinear activations. In this work, we integrate Error-Correcting Output Codes (ECOC) into the KAN framework to transform multi-class classification into multiple binary tasks, improving robustness via Hamming distance decoding. Our proposed KAN with ECOC framework outperforms vanilla KAN on a challenging blood cell classification dataset, achieving higher accuracy across diverse hyperparameter settings. Ablation studies further confirm that ECOC consistently enhances performance across FastKAN and FasterKAN variants. These results demonstrate that ECOC integration significantly boosts KAN generalizability in critical healthcare AI applications. To the best of our knowledge, this is the first work of ECOC with KAN for enhancing multi-class medical image classification performance.

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


## Scraped from https://arxiv.org/abs/2505.05798
[2505.05798] Improving Generalizability of Kolmogorov-Arnold Networks via Error-Correcting Output Codes Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2505.05798 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2505.05798 (cs) [Submitted on 9 May 2025 (v1), last revised 17 Sep 2025 (this version, v2)] Title:Improving Generalizability of Kolmogorov-Arnold Networks via Error-Correcting Output Codes Authors:Youngjoon Lee, Jinu Gong, Joonhyuk Kang View a PDF of the paper titled Improving Generalizability of Kolmogorov-Arnold Networks via Error-Correcting Output Codes, by Youngjoon Lee and 2 other authors View PDF HTML (experimental) Abstract:Kolmogorov-Arnold Networks (KAN) offer universal function approximation using univariate spline compositions without nonlinear activations. In this work, we integrate Error-Correcting Output Codes (ECOC) into the KAN framework to transform multi-class classification into multiple binary tasks, improving robustness via Hamming distance decoding. Our proposed KAN with ECOC framework outperforms vanilla KAN on a challenging blood cell classification dataset, achieving higher accuracy across diverse hyperparameter settings. Ablation studies further confirm that ECOC consistently enhances performance across FastKAN and FasterKAN variants. These results demonstrate that ECOC integration significantly boosts KAN generalizability in critical healthcare AI applications. To the best of our knowledge, this is the first work of ECOC with KAN for enhancing multi-class medical image classification performance. Comments: Accepted to IEEE BioCAS 2025 Subjects: Machine Learning...


## connections
- processed from phone shortcut
