---
type: note
category: development
created: 2025-09-18 11:55
modified: 2025-09-18 11:55
tags: ['bias', 'computational biology', 'social biases']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_BiasMap__Leveraging_Cross-Attentions_to_Discover_a.txt
---

# BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social B...

## summary
BiasMap is a model-agnostic framework for discovering latent concept-level representational biases in stable diffusion models. It leverages cross-attention attribution maps to reveal structural entanglements between demographics (e.g., gender, race) and semantics (e.g., professions), going deeper into representational bias during image generation.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13496

BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation

arXiv:2509.13496v1 Announce Type: new Abstract: Bias discovery is critical for black-box generative models, especiall text-to-image (TTI) models. Existing works predominantly focus on output-level demographic distributions, which do not necessarily guarantee concept representations to be disentangled post-mitigation. We propose BiasMap, a model-agnostic framework for uncovering latent concept-level representational biases in stable diffusion models. BiasMap leverages cross-attention attribution maps to reveal structural entanglements between demographics (e.g., gender, race) and semantics (e.g., professions), going deeper into representational bias during the image generation. Using attribution maps of these concepts, we quantify the spatial demographics-semantics concept entanglement via Intersection over Union (IoU), offering a lens into bias that remains hidden in existing fairness discovery approaches. In addition, we further utilize BiasMap for bias mitigation through energy-guide...

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


## Scraped from https://arxiv.org/abs/2509.13496
[2509.13496] BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13496 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13496 (cs) [Submitted on 16 Sep 2025] Title:BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation Authors:Rajatsubhra Chakraborty, Xujun Che, Depeng Xu, Cori Faklaris, Xi Niu, Shuhan Yuan View a PDF of the paper titled BiasMap: Leveraging Cross-Attentions to Discover and Mitigate Hidden Social Biases in Text-to-Image Generation, by Rajatsubhra Chakraborty and 5 other authors View PDF HTML (experimental) Abstract:Bias discovery is critical for black-box generative models, especiall text-to-image (TTI) models. Existing works predominantly focus on output-level demographic distributions, which do not neces- sarily guarantee concept representations to be disentangled post- mitigation. We propose BiasMap, a model-agnostic framework for uncovering latent concept-level representational biases in stable dif- fusion models. BiasMap leverages cross-attention attribution maps to reveal structural entanglements between demographics (e.g., gender, race) and semantics (e.g., professions), going deeper into representational bias during the image generation. Using attribu- tion maps of these concepts, we quantify the spatial demographics- semantics concept entanglement via Intersection over Union (IoU), offering a lens into bias that remains hidden in existing fairness dis- covery approaches. In addi...


## connections
- processed from phone shortcut
