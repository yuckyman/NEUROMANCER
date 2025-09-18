---
type: note
category: development, projects, ideas
created: 2025-09-18 12:08
modified: 2025-09-18 12:08
tags: ['Anti-Purification', 'Stable Diffusion', 'Adversarial Noise', 'Purity Perturbation']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Towards_Robust_Defense_against_Customization_via_P.txt
---

# Anti-Purification Task in Stable Diffusion Models

## summary
This note aims to formally define the anti-purification task for Stable Diffusion models and propose a simple diagnostic protective perturbation named AntiPure.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13922

Towards Robust Defense against Customization via Protective Perturbation Resistant to Diffusion-based Purification

arXiv:2509.13922v1 Announce Type: new Abstract: Diffusion models like Stable Diffusion have become prominent in visual synthesis tasks due to their powerful customization capabilities, which also introduce significant security risks, including deepfakes and copyright infringement. In response, a class of methods known as protective perturbation emerged, which mitigates image misuse by injecting imperceptible adversarial noise. However, purification can remove protective perturbations, thereby exposing images again to the risk of malicious forgery. In this work, we formalize the anti-purification task, highlighting challenges that hinder existing approaches, and propose a simple diagnostic protective perturbation named AntiPure. AntiPure exposes vulnerabilities of purification within the "purification-customization" workflow, owing to two guidance mechanisms: 1) Patch-wise Frequency Guidance, which reduces the model's influence over high-frequency components in the purified image, and 2...

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


## Scraped from https://arxiv.org/abs/2509.13922
[2509.13922] Towards Robust Defense against Customization via Protective Perturbation Resistant to Diffusion-based Purification Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13922 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13922 (cs) [Submitted on 17 Sep 2025] Title:Towards Robust Defense against Customization via Protective Perturbation Resistant to Diffusion-based Purification Authors:Wenkui Yang, Jie Cao, Junxian Duan, Ran He View a PDF of the paper titled Towards Robust Defense against Customization via Protective Perturbation Resistant to Diffusion-based Purification, by Wenkui Yang and 3 other authors View PDF HTML (experimental) Abstract:Diffusion models like Stable Diffusion have become prominent in visual synthesis tasks due to their powerful customization capabilities, which also introduce significant security risks, including deepfakes and copyright infringement. In response, a class of methods known as protective perturbation emerged, which mitigates image misuse by injecting imperceptible adversarial noise. However, purification can remove protective perturbations, thereby exposing images again to the risk of malicious forgery. In this work, we formalize the anti-purification task, highlighting challenges that hinder existing approaches, and propose a simple diagnostic protective perturbation named AntiPure. AntiPure exposes vulnerabilities of purification within the &#34;purification-customization&#34; workflow, owing to two guidance mechanisms: 1) Patch-wise Frequency Guidance, which reduces the model&#39;s influence over high-frequency com...


## connections
- processed from phone shortcut
