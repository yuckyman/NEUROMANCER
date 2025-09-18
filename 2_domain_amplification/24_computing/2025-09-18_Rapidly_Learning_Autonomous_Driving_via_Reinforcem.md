---
type: note
category: 24-computing
created: 2025-09-18 11:54
modified: 2025-09-18 11:54
tags:
- learning
- reinforcement learning
- autonomous driving
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_AdaThinkDrive__Adaptive_Thinking_via_Reinforcement.txt
---


# Rapidly Learning Autonomous Driving via Reinforcement Learning

## summary
This paper proposes a novel VLA framework with a dual mode reasoning mechanism inspired by fast and slow thinking. The framework is pre-trained on large-scale autonomous driving (AD) scenarios using both question answering (QA) and trajectory datasets, acquiring world knowledge and driving commonsense.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13769

AdaThinkDrive: Adaptive Thinking via Reinforcement Learning for Autonomous Driving

arXiv:2509.13769v1 Announce Type: new Abstract: While reasoning technology like Chain of Thought (CoT) has been widely adopted in Vision Language Action (VLA) models, it demonstrates promising capabilities in end to end autonomous driving. However, recent efforts to integrate CoT reasoning often fall short in simple scenarios, introducing unnecessary computational overhead without improving decision quality. To address this, we propose AdaThinkDrive, a novel VLA framework with a dual mode reasoning mechanism inspired by fast and slow thinking. First, our framework is pretrained on large scale autonomous driving (AD) scenarios using both question answering (QA) and trajectory datasets to acquire world knowledge and driving commonsense. During supervised fine tuning (SFT), we introduce a two mode dataset, fast answering (w/o CoT) and slow thinking (with CoT), enabling the model to distinguish between scenarios that require reasoning. Furthermore, an Adaptive Think Reward strategy is prop...

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


## Scraped from https://arxiv.org/abs/2509.13769
[2509.13769] AdaThinkDrive: Adaptive Thinking via Reinforcement Learning for Autonomous Driving Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13769 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13769 (cs) [Submitted on 17 Sep 2025] Title:AdaThinkDrive: Adaptive Thinking via Reinforcement Learning for Autonomous Driving Authors:Yuechen Luo, Fang Li, Shaoqing Xu, Zhiyi Lai, Lei Yang, Qimao Chen, Ziang Luo, Zixun Xie, Shengyin Jiang, Jiaxin Liu, Long Chen, Bing Wang, Zhi-xin Yang View a PDF of the paper titled AdaThinkDrive: Adaptive Thinking via Reinforcement Learning for Autonomous Driving, by Yuechen Luo and 12 other authors View PDF HTML (experimental) Abstract:While reasoning technology like Chain of Thought (CoT) has been widely adopted in Vision Language Action (VLA) models, it demonstrates promising capabilities in end to end autonomous driving. However, recent efforts to integrate CoT reasoning often fall short in simple scenarios, introducing unnecessary computational overhead without improving decision quality. To address this, we propose AdaThinkDrive, a novel VLA framework with a dual mode reasoning mechanism inspired by fast and slow thinking. First, our framework is pretrained on large scale autonomous driving (AD) scenarios using both question answering (QA) and trajectory datasets to acquire world knowledge and driving commonsense. During supervised fine tuning (SFT), we introduce a two mode dataset, fast answering (w/o CoT) and slow thinking (with CoT), enabling the model to distinguish between scenarios that require reasoning. Furthermore, an...


## connections
- processed from phone shortcut
