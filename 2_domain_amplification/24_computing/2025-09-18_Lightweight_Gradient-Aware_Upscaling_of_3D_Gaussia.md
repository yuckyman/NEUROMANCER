---
type: note
category: 24-computing
created: 2025-09-18 11:57
modified: 2025-09-18 11:57
tags:
- 3DGS
- GPU acceleration
- image processing
- gradient-based upsampling
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Lightweight_Gradient-Aware_Upscaling_of_3D_Gaussia.txt
---


# Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images

## summary
We introduce a lightweight gradient-aware upsampling technique for 3D Gaussian Splatting images, achieving high rendering speeds and reducing artifacts. The approach leverages analytical image gradients of Gaussians for bicubic spline interpolation.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2503.14171

Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images

arXiv:2503.14171v2 Announce Type: replace Abstract: We introduce an image upscaling technique tailored for 3D Gaussian Splatting (3DGS) on lightweight GPUs. Compared to 3DGS, it achieves significantly higher rendering speeds and reduces artifacts commonly observed in 3DGS reconstructions. Our technique upscales low-resolution 3DGS renderings with a marginal increase in cost by directly leveraging the analytical image gradients of Gaussians for gradient-based bicubic spline interpolation. The technique is agnostic to the specific 3DGS implementation, achieving novel view synthesis at rates 3x-4x higher than the baseline implementation. Through extensive experiments on multiple datasets, we showcase the performance improvements and high reconstruction fidelity attainable with gradient-aware upscaling of 3DGS images. We further demonstrate the integration of gradient-aware upscaling into the gradient-based optimization of a 3DGS model and analyze its effects on reconstruction quality and ...

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


## Scraped from https://arxiv.org/abs/2503.14171
[2503.14171] Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2503.14171 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2503.14171 (cs) [Submitted on 18 Mar 2025 (v1), last revised 17 Sep 2025 (this version, v2)] Title:Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images Authors:Simon Niedermayr, Christoph Neuhauser Rüdiger Westermann View a PDF of the paper titled Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images, by Simon Niedermayr and 1 other authors View PDF HTML (experimental) Abstract:We introduce an image upscaling technique tailored for 3D Gaussian Splatting (3DGS) on lightweight GPUs. Compared to 3DGS, it achieves significantly higher rendering speeds and reduces artifacts commonly observed in 3DGS reconstructions. Our technique upscales low-resolution 3DGS renderings with a marginal increase in cost by directly leveraging the analytical image gradients of Gaussians for gradient-based bicubic spline interpolation. The technique is agnostic to the specific 3DGS implementation, achieving novel view synthesis at rates 3x-4x higher than the baseline implementation. Through extensive experiments on multiple datasets, we showcase the performance improvements and high reconstruction fidelity attainable with gradient-aware upscaling of 3DGS images. We further demonstrate the integration of gradient-aware upscaling into the gradient-based optimization of a 3DGS model and analyze its effects on reconstruction quality and performance. Subjects: Computer Vision and Patter...


## connections
- processed from phone shortcut
