---
type: note
category: ideas
created: 2025-09-18 12:06
modified: 2025-09-18 12:06
tags: ['rest', 'visual', 'evoked', 'fMRI', 'rs-fMRI']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Rest2Visual__Predicting_Visually_Evoked_fMRI_from_.txt
---

# Rest2Visual: Predicting Visually Evoked fMRI from Resting-State Scans

## summary
A conditional generative model for predicting visually evoked fMRI (ve-fMRI) from resting-state input and 2D visual stimuli.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13612

Rest2Visual: Predicting Visually Evoked fMRI from Resting-State Scans

arXiv:2509.13612v1 Announce Type: cross Abstract: Understanding how spontaneous brain activity relates to stimulus-driven neural responses is a fundamental challenge in cognitive neuroscience. While task-based functional magnetic resonance imaging (fMRI) captures localized stimulus-evoked brain activation, its acquisition is costly, time-consuming, and difficult to scale across populations. In contrast, resting-state fMRI (rs-fMRI) is task-free and abundant, but lacks direct interpretability. We introduce Rest2Visual, a conditional generative model that predicts visually evoked fMRI (ve-fMRI) from resting-state input and 2D visual stimuli. It follows a volumetric encoder--decoder design, where multiscale 3D features from rs-fMRI are modulated by image embeddings via adaptive normalization, enabling spatially accurate, stimulus-specific activation synthesis. To enable model training, we construct a large-scale triplet dataset from the Natural Scenes Dataset (NSD), aligning each rs-fMRI ...

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


## Scraped from https://arxiv.org/abs/2509.13612
[2509.13612] Rest2Visual: Predicting Visually Evoked fMRI from Resting-State Scans Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; q-bio &gt; arXiv:2509.13612 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Quantitative Biology > Neurons and Cognition arXiv:2509.13612 (q-bio) [Submitted on 17 Sep 2025] Title:Rest2Visual: Predicting Visually Evoked fMRI from Resting-State Scans Authors:Chuyang Zhou, Ziao Ji, Daochang Liu, Dongang Wang, Chenyu Wang, Chang Xu View a PDF of the paper titled Rest2Visual: Predicting Visually Evoked fMRI from Resting-State Scans, by Chuyang Zhou and 5 other authors View PDF HTML (experimental) Abstract:Understanding how spontaneous brain activity relates to stimulus-driven neural responses is a fundamental challenge in cognitive neuroscience. While task-based functional magnetic resonance imaging (fMRI) captures localized stimulus-evoked brain activation, its acquisition is costly, time-consuming, and difficult to scale across populations. In contrast, resting-state fMRI (rs-fMRI) is task-free and abundant, but lacks direct interpretability. We introduce Rest2Visual, a conditional generative model that predicts visually evoked fMRI (ve-fMRI) from resting-state input and 2D visual stimuli. It follows a volumetric encoder--decoder design, where multiscale 3D features from rs-fMRI are modulated by image embeddings via adaptive normalization, enabling spatially accurate, stimulus-specific activation synthesis. To enable model training, we construct a large-scale triplet dataset from the Natural Scenes Dataset (NSD), aligning each rs-fMRI volume with stimulus images and their corresponding ve-fMRI activation maps. Quantitative ...


## connections
- processed from phone shortcut
