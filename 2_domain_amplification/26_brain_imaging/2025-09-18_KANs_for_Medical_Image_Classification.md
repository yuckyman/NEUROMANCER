---
type: note
category: brain-imaging
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags: ['kann', 'splines', 'classification', 'brain-imaging', 'neuroimaging', 'medical-classification', 'kolmogorov-arnold-networks']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Taylor-Series_Expanded_Kolmogorov-Arnold_Network_f.txt
---

# KANs for Medical Image Classification

## summary
The paper introduces spline-based Kolmogorov-Arnold Networks (KANs) for medical image classification, which leverage spline-based function approximation to capture both local and global nonlinearities. The models were evaluated on a variety of medical imaging datasets without preprocessing, demonstrating their effectiveness.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13687

Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification

arXiv:2509.13687v1 Announce Type: new Abstract: Effective and interpretable classification of medical images is a challenge in computer-aided diagnosis, especially in resource-limited clinical settings. This study introduces spline-based Kolmogorov-Arnold Networks (KANs) for accurate medical image classification with limited, diverse datasets. The models include SBTAYLOR-KAN, integrating B-splines with Taylor series; SBRBF-KAN, combining B-splines with Radial Basis Functions; and SBWAVELET-KAN, embedding B-splines in Morlet wavelet transforms. These approaches leverage spline-based function approximation to capture both local and global nonlinearities. The models were evaluated on brain MRI, chest X-rays, tuberculosis X-rays, and skin lesion images without preprocessing, demonstrating the ability to learn directly from raw data. Extensive experiments, including cross-dataset validation and data reduction analysis, showed strong generalization and stability. SBTAYLOR-KAN achieved up to ...

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


## Scraped from https://arxiv.org/abs/2509.13687
[2509.13687] Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13687 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13687 (cs) [Submitted on 17 Sep 2025] Title:Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification Authors:Kaniz Fatema, Emad A. Mohammed, Sukhjit Singh Sehra View a PDF of the paper titled Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification, by Kaniz Fatema and 2 other authors View PDF HTML (experimental) Abstract:Effective and interpretable classification of medical images is a challenge in computer-aided diagnosis, especially in resource-limited clinical settings. This study introduces spline-based Kolmogorov-Arnold Networks (KANs) for accurate medical image classification with limited, diverse datasets. The models include SBTAYLOR-KAN, integrating B-splines with Taylor series; SBRBF-KAN, combining B-splines with Radial Basis Functions; and SBWAVELET-KAN, embedding B-splines in Morlet wavelet transforms. These approaches leverage spline-based function approximation to capture both local and global nonlinearities. The models were evaluated on brain MRI, chest X-rays, tuberculosis X-rays, and skin lesion images without preprocessing, demonstrating the ability to learn directly from raw data. Extensive experiments, including cross-dataset validation and data reduction analysis, showed strong generalization and stability. SBTAYLOR-KAN achieved up to 98.93% accuracy, with a balanced F1-score, maintaining over...


## connections
- processed from phone shortcut
