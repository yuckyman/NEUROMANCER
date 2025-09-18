---
type: note
category: development
created: 2025-09-18 11:59
modified: 2025-09-18 11:59
tags: ['vision', 'transformers', 'efficiency', 'pruning', 'high-resolutions']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Where_Do_Tokens_Go__Understanding_Pruning_Behavior.txt
---

# VISION TRANSFORMERS (ViTs) with STEP: An Efficient Hybrid Token-Reduction Fra...

## summary
A hybrid token-reduction framework called STEP combines dynamic patch merging and token pruning to enhance efficiency without compromising accuracy. It is evaluated on high-resolution semantic segmentation benchmarks and shows improved performance compared to original ViTs.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14165

Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions

arXiv:2509.14165v1 Announce Type: new Abstract: Vision Transformers (ViTs) achieve state-of-the-art performance in semantic segmentation but are hindered by high computational and memory costs. To address this, we propose STEP (SuperToken and Early-Pruning), a hybrid token-reduction framework that combines dynamic patch merging and token pruning to enhance efficiency without significantly compromising accuracy. At the core of STEP is dCTS, a lightweight CNN-based policy network that enables flexible merging into superpatches. Encoder blocks integrate also early-exits to remove high-confident supertokens, lowering computational load. We evaluate our method on high-resolution semantic segmentation benchmarks, including images up to 1024 x 1024, and show that when dCTS is applied alone, the token count can be reduced by a factor of 2.5 compared to the standard 16 x 16 pixel patching scheme. This yields a 2.6x reduction in computational cost and a 3.4x increase in throughput when using ViT...

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


## Scraped from https://arxiv.org/abs/2509.14165
[2509.14165] Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14165 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14165 (cs) [Submitted on 17 Sep 2025] Title:Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions Authors:Michal Szczepanski, Martyna Poreba, Karim Haroun View a PDF of the paper titled Where Do Tokens Go? Understanding Pruning Behaviors in STEP at High Resolutions, by Michal Szczepanski and 1 other authors View PDF HTML (experimental) Abstract:Vision Transformers (ViTs) achieve state-of-the-art performance in semantic segmentation but are hindered by high computational and memory costs. To address this, we propose STEP (SuperToken and Early-Pruning), a hybrid token-reduction framework that combines dynamic patch merging and token pruning to enhance efficiency without significantly compromising accuracy. At the core of STEP is dCTS, a lightweight CNN-based policy network that enables flexible merging into superpatches. Encoder blocks integrate also early-exits to remove high-confident supertokens, lowering computational load. We evaluate our method on high-resolution semantic segmentation benchmarks, including images up to 1024 x 1024, and show that when dCTS is applied alone, the token count can be reduced by a factor of 2.5 compared to the standard 16 x 16 pixel patching scheme. This yields a 2.6x reduction in computational cost and a 3.4x increase in throughput when using ViT-Large as the backbone. Applying the full STEP framework further imp...


## connections
- processed from phone shortcut
