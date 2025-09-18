---
type: note
category: 24-computing
created: 2025-09-18 11:56
modified: 2025-09-18 11:56
tags:
- deep learning
- arXiv
- lookup operations
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Deep_Lookup_Network.txt
---


# Deep Lookup Network

## summary
We propose a generic and efficient lookup operation for convolutional neural networks (CNNs). Instead of calculating the multiplication of weights and activation values, we use simple yet efficient lookup operations.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13662

Deep Lookup Network

arXiv:2509.13662v1 Announce Type: new Abstract: Convolutional neural networks are constructed with massive operations with different types and are highly computationally intensive. Among these operations, multiplication operation is higher in computational complexity and usually requires {more} energy consumption with longer inference time than other operations, which hinders the deployment of convolutional neural networks on mobile devices. In many resource-limited edge devices, complicated operations can be calculated via lookup tables to reduce computational cost. Motivated by this, in this paper, we introduce a generic and efficient lookup operation which can be used as a basic operation for the construction of neural networks. Instead of calculating the multiplication of weights and activation values, simple yet efficient lookup operations are adopted to compute their responses. To enable end-to-end optimization of the lookup operation, we construct the lookup tables in a differen...

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


## Scraped from https://arxiv.org/abs/2509.13662
[2509.13662] Deep Lookup Network Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13662 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13662 (cs) [Submitted on 17 Sep 2025] Title:Deep Lookup Network Authors:Yulan Guo, Longguang Wang, Wendong Mao, Xiaoyu Dong, Yingqian Wang, Li Liu, Wei An View a PDF of the paper titled Deep Lookup Network, by Yulan Guo and 6 other authors View PDF HTML (experimental) Abstract:Convolutional neural networks are constructed with massive operations with different types and are highly computationally intensive. Among these operations, multiplication operation is higher in computational complexity and usually requires {more} energy consumption with longer inference time than other operations, which hinders the deployment of convolutional neural networks on mobile devices. In many resource-limited edge devices, complicated operations can be calculated via lookup tables to reduce computational cost. Motivated by this, in this paper, we introduce a generic and efficient lookup operation which can be used as a basic operation for the construction of neural networks. Instead of calculating the multiplication of weights and activation values, simple yet efficient lookup operations are adopted to compute their responses. To enable end-to-end optimization of the lookup operation, we construct the lookup tables in a differentiable manner and propose several training strategies to promote their convergence. By replacing computationally expensive multiplication operations with our lookup operations, we develop lookup networks for the image class...


## connections
- processed from phone shortcut
