---
type: note
category: 24-computing
created: 2025-09-18 11:57
modified: 2025-09-18 11:57
tags:
- YOLOv11
- GRU-Attention
- traffic monitoring
- congestion prediction
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Research_on_Expressway_Congestion_Warning_Technolo.txt
---


# Expressway Congestion Warning Technology

## summary
This project focuses on developing a new traffic warning technology based on YOLOv11-DIoU and GRU-Attention, specifically for expressway congestion.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13361

Research on Expressway Congestion Warning Technology Based on YOLOv11-DIoU and GRU-Attention

arXiv:2509.13361v1 Announce Type: new Abstract: Expressway traffic congestion severely reduces travel efficiency and hinders regional connectivity. Existing "detection-prediction" systems have critical flaws: low vehicle perception accuracy under occlusion and loss of long-sequence dependencies in congestion forecasting. This study proposes an integrated technical framework to resolve these issues.For traffic flow perception, two baseline algorithms were optimized. Traditional YOLOv11 was upgraded to YOLOv11-DIoU by replacing GIoU Loss with DIoU Loss, and DeepSort was improved by fusing Mahalanobis (motion) and cosine (appearance) distances. Experiments on Chang-Shen Expressway videos showed YOLOv11-DIoU achieved 95.7\% mAP (6.5 percentage points higher than baseline) with 5.3\% occlusion miss rate. DeepSort reached 93.8\% MOTA (11.3 percentage points higher than SORT) with only 4 ID switches. Using the Greenberg model (for 10-15 vehicles/km high-density scenarios), speed and density s...

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


## Scraped from https://arxiv.org/abs/2509.13361
[2509.13361] Research on Expressway Congestion Warning Technology Based on YOLOv11-DIoU and GRU-Attention Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13361 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13361 (cs) [Submitted on 15 Sep 2025] Title:Research on Expressway Congestion Warning Technology Based on YOLOv11-DIoU and GRU-Attention Authors:Tong Yulin, Liang Xuechen View a PDF of the paper titled Research on Expressway Congestion Warning Technology Based on YOLOv11-DIoU and GRU-Attention, by Tong Yulin and 1 other authors View PDF HTML (experimental) Abstract:Expressway traffic congestion severely reduces travel efficiency and hinders regional connectivity. Existing &#34;detection-prediction&#34; systems have critical flaws: low vehicle perception accuracy under occlusion and loss of long-sequence dependencies in congestion forecasting. This study proposes an integrated technical framework to resolve these this http URL traffic flow perception, two baseline algorithms were optimized. Traditional YOLOv11 was upgraded to YOLOv11-DIoU by replacing GIoU Loss with DIoU Loss, and DeepSort was improved by fusing Mahalanobis (motion) and cosine (appearance) distances. Experiments on Chang-Shen Expressway videos showed YOLOv11-DIoU achieved 95.7\% mAP (6.5 percentage points higher than baseline) with 5.3\% occlusion miss rate. DeepSort reached 93.8\% MOTA (11.3 percentage points higher than SORT) with only 4 ID switches. Using the Greenberg model (for 10-15 vehicles/km high-density scenarios), speed and density showed a strong negative correlation (r=-0.97), co...


## connections
- processed from phone shortcut
