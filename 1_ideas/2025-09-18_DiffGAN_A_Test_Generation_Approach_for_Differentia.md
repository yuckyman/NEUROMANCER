---
type: note
category: projects
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags: ['deep learning', 'diff testing', 'neural networks', 'image analysis']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_DiffGAN__A_Test_Generation_Approach_for_Differenti.txt
---

# DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural N...

## summary
DiffGAN is a novel method that generates test inputs to assess the behavior differences between deep neural networks (DNNs). It addresses traditional approaches' limitations by leveraging black-box models and generating synthetic data. The approach is scalable, requiring only small datasets compared to current state-of-the-art methods.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2410.19794

DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis

arXiv:2410.19794v4 Announce Type: replace Abstract: Deep Neural Networks (DNNs) are increasingly deployed across applications. However, ensuring their reliability remains a challenge, and in many situations, alternative models with similar functionality and accuracy are available. Traditional accuracy-based evaluations often fail to capture behavioral differences between models, especially with limited test datasets, making it difficult to select or combine models effectively. Differential testing addresses this by generating test inputs that expose discrepancies in DNN model behavior. However, existing approaches face significant limitations: many rely on model internals or are constrained by available seed inputs. To address these challenges, we propose DiffGAN, a black-box test image generation approach for differential testing of DNN models. DiffGAN leverages a Generative Adversarial Network (GAN) and the Non-dominated Sorting Genetic Algorithm II to generate diverse and valid trig...

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


## Scraped from https://arxiv.org/abs/2410.19794
[2410.19794] DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2410.19794 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2410.19794 (cs) [Submitted on 15 Oct 2024 (v1), last revised 17 Sep 2025 (this version, v4)] Title:DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis Authors:Zohreh Aghababaeyan, Manel Abdellatif, Lionel Briand, Ramesh S View a PDF of the paper titled DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis, by Zohreh Aghababaeyan and 3 other authors View PDF HTML (experimental) Abstract:Deep Neural Networks (DNNs) are increasingly deployed across applications. However, ensuring their reliability remains a challenge, and in many situations, alternative models with similar functionality and accuracy are available. Traditional accuracy-based evaluations often fail to capture behavioral differences between models, especially with limited test datasets, making it difficult to select or combine models effectively. Differential testing addresses this by generating test inputs that expose discrepancies in DNN model behavior. However, existing approaches face significant limitations: many rely on model internals or are constrained by available seed inputs. To address these challenges, we propose DiffGAN, a black-box test image generation approach for differential testing of DNN models. DiffGAN leverages a Generative Adversarial Network (GAN) and the Non-dominate...


## connections
- processed from phone shortcut
