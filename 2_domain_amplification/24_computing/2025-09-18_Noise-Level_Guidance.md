---
type: note
category: 24-computing
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags:
- arXiv
- CV
- noise-level optimization
- diffusion models
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Noise-Level_Diffusion_Guidance__Well_Begun_is_Half.txt
---


# Noise-Level Guidance

## summary
A simple, efficient, and general noise-level optimization approach that refines initial noise by increasing the likelihood of its alignment with general guidance.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13936

Noise-Level Diffusion Guidance: Well Begun is Half Done

arXiv:2509.13936v1 Announce Type: new Abstract: Diffusion models have achieved state-of-the-art image generation. However, the random Gaussian noise used to start the diffusion process influences the final output, causing variations in image quality and prompt adherence. Existing noise-level optimization approaches generally rely on extra dataset construction, additional networks, or backpropagation-based optimization, limiting their practicality. In this paper, we propose Noise Level Guidance (NLG), a simple, efficient, and general noise-level optimization approach that refines initial noise by increasing the likelihood of its alignment with general guidance - requiring no additional training data, auxiliary networks, or backpropagation. The proposed NLG approach provides a unified framework generalizable to both conditional and unconditional diffusion models, accommodating various forms of diffusion-level guidance. Extensive experiments on five standard benchmarks demonstrate that ou...

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


## Scraped from https://arxiv.org/abs/2509.13936
[2509.13936] Noise-Level Diffusion Guidance: Well Begun is Half Done Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13936 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13936 (cs) [Submitted on 17 Sep 2025] Title:Noise-Level Diffusion Guidance: Well Begun is Half Done Authors:Harvey Mannering, Zhiwu Huang, Adam Prugel-Bennett View a PDF of the paper titled Noise-Level Diffusion Guidance: Well Begun is Half Done, by Harvey Mannering and 2 other authors View PDF HTML (experimental) Abstract:Diffusion models have achieved state-of-the-art image generation. However, the random Gaussian noise used to start the diffusion process influences the final output, causing variations in image quality and prompt adherence. Existing noise-level optimization approaches generally rely on extra dataset construction, additional networks, or backpropagation-based optimization, limiting their practicality. In this paper, we propose Noise Level Guidance (NLG), a simple, efficient, and general noise-level optimization approach that refines initial noise by increasing the likelihood of its alignment with general guidance - requiring no additional training data, auxiliary networks, or backpropagation. The proposed NLG approach provides a unified framework generalizable to both conditional and unconditional diffusion models, accommodating various forms of diffusion-level guidance. Extensive experiments on five standard benchmarks demonstrate that our approach enhances output generation quality and input condition adherence. By seamlessly integrating with existing guidance methods while ...


## connections
- processed from phone shortcut
