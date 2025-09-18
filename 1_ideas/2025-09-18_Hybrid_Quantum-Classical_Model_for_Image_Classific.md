---
type: note
category: ideas
created: 2025-09-18 12:07
modified: 2025-09-18 12:07
tags: ['quantum-classical model', 'image classification', 'neural networks', 'parallel computing']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Hybrid_Quantum-Classical_Model_for_Image_Classific.txt
---

# Hybrid Quantum-Classical Model for Image Classification

## summary
This paper compares the performance of hybrid quantum-classical neural networks and classical CNNs across three benchmark datasets (MNIST, CIFAR100, STL10). It evaluates their final accuracy, training time, computational resource usage, and adversarial robustness.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13353

Hybrid Quantum-Classical Model for Image Classification

arXiv:2509.13353v1 Announce Type: new Abstract: This study presents a systematic comparison between hybrid quantum-classical neural networks and purely classical models across three benchmark datasets (MNIST, CIFAR100, and STL10) to evaluate their performance, efficiency, and robustness. The hybrid models integrate parameterized quantum circuits with classical deep learning architectures, while the classical counterparts use conventional convolutional neural networks (CNNs). Experiments were conducted over 50 training epochs for each dataset, with evaluations on validation accuracy, test accuracy, training time, computational resource usage, and adversarial robustness (tested with $\epsilon=0.1$ perturbations).Key findings demonstrate that hybrid models consistently outperform classical models in final accuracy, achieving {99.38\% (MNIST), 41.69\% (CIFAR100), and 74.05\% (STL10) validation accuracy, compared to classical benchmarks of 98.21\%, 32.25\%, and 63.76\%, respectively. Notabl...

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


## Scraped from https://arxiv.org/abs/2509.13353
[2509.13353] Hybrid Quantum-Classical Model for Image Classification Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13353 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13353 (cs) [Submitted on 14 Sep 2025] Title:Hybrid Quantum-Classical Model for Image Classification Authors:Muhammad Adnan Shahzad View a PDF of the paper titled Hybrid Quantum-Classical Model for Image Classification, by Muhammad Adnan Shahzad View PDF HTML (experimental) Abstract:This study presents a systematic comparison between hybrid quantum-classical neural networks and purely classical models across three benchmark datasets (MNIST, CIFAR100, and STL10) to evaluate their performance, efficiency, and robustness. The hybrid models integrate parameterized quantum circuits with classical deep learning architectures, while the classical counterparts use conventional convolutional neural networks (CNNs). Experiments were conducted over 50 training epochs for each dataset, with evaluations on validation accuracy, test accuracy, training time, computational resource usage, and adversarial robustness (tested with $\epsilon=0.1$ perturbations).Key findings demonstrate that hybrid models consistently outperform classical models in final accuracy, achieving {99.38\% (MNIST), 41.69\% (CIFAR100), and 74.05\% (STL10) validation accuracy, compared to classical benchmarks of 98.21\%, 32.25\%, and 63.76\%, respectively. Notably, the hybrid advantage scales with dataset complexity, showing the most significant gains on CIFAR100 (+9.44\%) and STL10 (+10.29\%). Hybrid models also train 5--12$\times$ faster (...


## connections
- processed from phone shortcut
