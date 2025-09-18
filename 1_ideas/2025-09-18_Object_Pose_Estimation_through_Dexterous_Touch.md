---
type: note
category: development, projects, ideas, reference, personal
created: 2025-09-18 11:58
modified: 2025-09-18 11:58
tags: ['tag1: object pose estimation', 'tag2: tactile sensor interaction']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Object_Pose_Estimation_through_Dexterous_Touch.txt
---

# Object Pose Estimation through Dexterous Touch

## summary
Our approach uses Reinforcement Learning (RL) to actively control a robot hand in order to collect and refine tactile data for dynamic object pose estimation. The method involves training with sensorimotor exploration, collecting 3D point clouds from the object's surface, and refining the shape and pose of the object.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13591

Object Pose Estimation through Dexterous Touch

arXiv:2509.13591v1 Announce Type: cross Abstract: Robust object pose estimation is essential for manipulation and interaction tasks in robotics, particularly in scenarios where visual data is limited or sensitive to lighting, occlusions, and appearances. Tactile sensors often offer limited and local contact information, making it challenging to reconstruct the pose from partial data. Our approach uses sensorimotor exploration to actively control a robot hand to interact with the object. We train with Reinforcement Learning (RL) to explore and collect tactile data. The collected 3D point clouds are used to iteratively refine the object's shape and pose. In our setup, one hand holds the object steady while the other performs active exploration. We show that our method can actively explore an object's surface to identify critical pose features without prior knowledge of the object's geometry. Supplementary material and more demonstrations will be provided at https://amirshahid.github.io/B...

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


## Scraped from https://arxiv.org/abs/2509.13591
[2509.13591] Object Pose Estimation through Dexterous Touch Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13591 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Robotics arXiv:2509.13591 (cs) [Submitted on 16 Sep 2025] Title:Object Pose Estimation through Dexterous Touch Authors:Amir-Hossein Shahidzadeh, Jiyue Zhu, Kezhou Chen, Sha Yi, Cornelia Fermüller, Yiannis Aloimonos, Xiaolong Wang View a PDF of the paper titled Object Pose Estimation through Dexterous Touch, by Amir-Hossein Shahidzadeh and 5 other authors View PDF HTML (experimental) Abstract:Robust object pose estimation is essential for manipulation and interaction tasks in robotics, particularly in scenarios where visual data is limited or sensitive to lighting, occlusions, and appearances. Tactile sensors often offer limited and local contact information, making it challenging to reconstruct the pose from partial data. Our approach uses sensorimotor exploration to actively control a robot hand to interact with the object. We train with Reinforcement Learning (RL) to explore and collect tactile data. The collected 3D point clouds are used to iteratively refine the object&#39;s shape and pose. In our setup, one hand holds the object steady while the other performs active exploration. We show that our method can actively explore an object&#39;s surface to identify critical pose features without prior knowledge of the object&#39;s geometry. Supplementary material and more demonstrations will be provided at this https URL . Subjects: Robotics (cs.RO); Computer Vision and Pattern Recognition (cs.CV) Cite as: arXiv:2509.13591 [cs.RO] &nbsp; (or arXiv:2509.1...


## connections
- processed from phone shortcut
