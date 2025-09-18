---
type: note
category: projects
created: 2025-09-18 12:10
modified: 2025-09-18 12:10
tags: ['ev-hand', 'event-based tracking', 'first-person view', 'arXiv.org']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_EvHand-FPV__Efficient_Event-Based_3D_Hand_Tracking.txt
---

# EvHand-FPV: Efficient Event-Based 3D Hand Tracking from First-Person View

## summary
We present EvHand-FPV, a lightweight framework for egocentric First-Person-View 3D hand tracking from a single event camera. We address the scarcity of egocentric benchmarks by coupling synthetic training data with 3D labels and real event data with 2D labels. The proposed method introduces an event-based region detection mechanism and incorporates wrist-based region segmentation.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13883

EvHand-FPV: Efficient Event-Based 3D Hand Tracking from First-Person View

arXiv:2509.13883v1 Announce Type: new Abstract: Hand tracking holds great promise for intuitive interaction paradigms, but frame-based methods often struggle to meet the requirements of accuracy, low latency, and energy efficiency, especially in resource-constrained settings such as Extended Reality (XR) devices. Event cameras provide $\mu$s-level temporal resolution at mW-level power by asynchronously sensing brightness changes. In this work, we present EvHand-FPV, a lightweight framework for egocentric First-Person-View 3D hand tracking from a single event camera. We construct an event-based FPV dataset that couples synthetic training data with 3D labels and real event data with 2D labels for evaluation to address the scarcity of egocentric benchmarks. EvHand-FPV also introduces a wrist-based region of interest (ROI) that localizes the hand region via geometric cues, combined with an end-to-end mapping strategy that embeds ROI offsets into the network to reduce computation without ex...

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


## Scraped from https://arxiv.org/abs/2509.13883
[2509.13883] EvHand-FPV: Efficient Event-Based 3D Hand Tracking from First-Person View Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13883 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13883 (cs) [Submitted on 17 Sep 2025] Title:EvHand-FPV: Efficient Event-Based 3D Hand Tracking from First-Person View Authors:Zhen Xu, Guorui Lu, Chang Gao, Qinyu Chen View a PDF of the paper titled EvHand-FPV: Efficient Event-Based 3D Hand Tracking from First-Person View, by Zhen Xu and 3 other authors View PDF HTML (experimental) Abstract:Hand tracking holds great promise for intuitive interaction paradigms, but frame-based methods often struggle to meet the requirements of accuracy, low latency, and energy efficiency, especially in resource-constrained settings such as Extended Reality (XR) devices. Event cameras provide $\mu$s-level temporal resolution at mW-level power by asynchronously sensing brightness changes. In this work, we present EvHand-FPV, a lightweight framework for egocentric First-Person-View 3D hand tracking from a single event camera. We construct an event-based FPV dataset that couples synthetic training data with 3D labels and real event data with 2D labels for evaluation to address the scarcity of egocentric benchmarks. EvHand-FPV also introduces a wrist-based region of interest (ROI) that localizes the hand region via geometric cues, combined with an end-to-end mapping strategy that embeds ROI offsets into the network to reduce computation without explicit reconstruction, and a multi-task learning strategy with an auxiliary geometric feature head that ...


## connections
- processed from phone shortcut
