---
type: note
category: 24-computing
created: 2025-09-22 10:29
modified: 2025-09-22 10:29
tags:
- face-anonymization
- diffusion-inpainting
- localization
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250919_175448_rss_Controllable_Localized_Face_Anonymization_Via_Diff.txt
content_hash: 736559c82a7bd2fefe57339fa77f15e1dc3694796ab56535d2a581ebeb3b20b0
---


# arXiv:2509.14866 - A Unified Framework for Localized Face Anonymization via D...

## summary
In this work, we propose a unified framework that leverages latent diffusion models for generating realistic anonymized images. We design an adaptive attribute-guidance module to align facial attributes with the synthesized target image during reverse denoising and support localized anonymization by specifying which regions of the face remain unchanged.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.14866

Controllable Localized Face Anonymization Via Diffusion Inpainting

arXiv:2509.14866v1 Announce Type: new Abstract: The growing use of portrait images in computer vision highlights the need to protect personal identities. At the same time, anonymized images must remain useful for downstream computer vision tasks. In this work, we propose a unified framework that leverages the inpainting ability of latent diffusion models to generate realistic anonymized images. Unlike prior approaches, we have complete control over the anonymization process by designing an adaptive attribute-guidance module that applies gradient correction during the reverse denoising process, aligning the facial attributes of the generated image with those of the synthesized target image. Our framework also supports localized anonymization, allowing users to specify which facial regions are left unchanged. Extensive experiments conducted on the public CelebA-HQ and FFHQ datasets show that our method outperforms state-of-the-art approaches while requiring no additional model training. ...

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
    <lastBuildDate>Mon, 22 Sep 2025 04:00:01 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Mon, 22 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays</title>
      <link>https://arxiv.org/abs/2509.15234</link>
      <description>arXiv:2509.15234v1 Announce Type: new 
Abstract: Vision-language pretraining has advanced image-text alignment, yet progress in radiology remains constrained by the heterogeneity of clinical reports, including abbreviations, impression-only notes, and stylistic variability. Unlike general-domain settings where more data often leads to better performance, naively scaling to large collections of noisy reports can plateau or even degrade model learning. We ask whether large language model (LLM) encoders can provide robust clinical representations that transfer across diverse styles and better guide image-text alignment. We introduce LLM2VEC4CXR, a domain-adapted LLM encoder for chest X-ray reports, and LLM2CLIP4CXR, a dual-tower framework that couples this encoder with a vision backbone. LLM2VEC4CXR improves clinical text understanding over BERT-based baselines, handles abbreviations and style variation, and achieves strong clinic...


## Scraped from https://arxiv.org/abs/2509.14866
[2509.14866] Controllable Localized Face Anonymization Via Diffusion Inpainting Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.14866 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.14866 (cs) [Submitted on 18 Sep 2025] Title:Controllable Localized Face Anonymization Via Diffusion Inpainting Authors:Ali Salar, Qing Liu, Guoying Zhao View a PDF of the paper titled Controllable Localized Face Anonymization Via Diffusion Inpainting, by Ali Salar and 2 other authors View PDF HTML (experimental) Abstract:The growing use of portrait images in computer vision highlights the need to protect personal identities. At the same time, anonymized images must remain useful for downstream computer vision tasks. In this work, we propose a unified framework that leverages the inpainting ability of latent diffusion models to generate realistic anonymized images. Unlike prior approaches, we have complete control over the anonymization process by designing an adaptive attribute-guidance module that applies gradient correction during the reverse denoising process, aligning the facial attributes of the generated image with those of the synthesized target image. Our framework also supports localized anonymization, allowing users to specify which facial regions are left unchanged. Extensive experiments conducted on the public CelebA-HQ and FFHQ datasets show that our method outperforms state-of-the-art approaches while requiring no additional model training. The source code is available on our page. Subjects: Computer Vision and Pattern Recognition (cs.CV) Cite as: arXiv:2509.14866 [cs.C...


## connections
- processed from phone shortcut
