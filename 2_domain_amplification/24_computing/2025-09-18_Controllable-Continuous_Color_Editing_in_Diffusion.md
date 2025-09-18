---
type: note
category: 24-computing
created: 2025-09-18 11:53
modified: 2025-09-18 11:53
tags:
- arXiv
- color mapping
- continuous color editing
- diffusion model
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Controllable-Continuous_Color_Editing_in_Diffusion.txt
---


# Controllable-Continuous Color Editing in Diffusion Model via Color Mapping

## summary
In this paper, a new method called 'Controllable-Continuous Color Editing' is proposed. It uses color mapping to control the range of color changes in the output images while maintaining precise control over the relationship between interpolation coefficients and resulting image colors.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13756

Controllable-Continuous Color Editing in Diffusion Model via Color Mapping

arXiv:2509.13756v1 Announce Type: new Abstract: In recent years, text-driven image editing has made significant progress. However, due to the inherent ambiguity and discreteness of natural language, color editing still faces challenges such as insufficient precision and difficulty in achieving continuous control. Although linearly interpolating the embedding vectors of different textual descriptions can guide the model to generate a sequence of images with varying colors, this approach lacks precise control over the range of color changes in the output images. Moreover, the relationship between the interpolation coefficient and the resulting image color is unknown and uncontrollable. To address these issues, we introduce a color mapping module that explicitly models the correspondence between the text embedding space and image RGB values. This module predicts the corresponding embedding vector based on a given RGB value, enabling precise color control of the generated images while main...

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


## Scraped from https://arxiv.org/abs/2509.13756
[2509.13756] Controllable-Continuous Color Editing in Diffusion Model via Color Mapping Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13756 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13756 (cs) [Submitted on 17 Sep 2025] Title:Controllable-Continuous Color Editing in Diffusion Model via Color Mapping Authors:Yuqi Yang, Dongliang Chang, Yuanchen Fang, Yi-Zhe SonG, Zhanyu Ma, Jun Guo View a PDF of the paper titled Controllable-Continuous Color Editing in Diffusion Model via Color Mapping, by Yuqi Yang and 5 other authors View PDF HTML (experimental) Abstract:In recent years, text-driven image editing has made significant progress. However, due to the inherent ambiguity and discreteness of natural language, color editing still faces challenges such as insufficient precision and difficulty in achieving continuous control. Although linearly interpolating the embedding vectors of different textual descriptions can guide the model to generate a sequence of images with varying colors, this approach lacks precise control over the range of color changes in the output images. Moreover, the relationship between the interpolation coefficient and the resulting image color is unknown and uncontrollable. To address these issues, we introduce a color mapping module that explicitly models the correspondence between the text embedding space and image RGB values. This module predicts the corresponding embedding vector based on a given RGB value, enabling precise color control of the generated images while maintaining semantic consistency. Users can specify a target RGB range...


## connections
- processed from phone shortcut
