---
type: note
category: 24-computing
created: 2025-09-19 17:56
modified: 2025-09-19 17:56
tags:
- dev-log
- project
- research
- idea
- technical
- personal
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Gaussian_Alignment_for_Relative_Camera_Pose_Estima.txt
content_hash: 5e236607429cc790315cb85254e71425159e58d10b455516f8ddf76f14f06606
---


# GARPS: A Training-Free Gaussian Alignment Framework for Metric Relative Camer...

## summary
This paper presents GARPS, a training-free framework that leverages a metric monocular depth estimator and a Gaussian scene reconstruction algorithm to estimate the relative camera pose from two images. It refines an initial pose by optimising a differentiable GMM alignment objective.

## content
RSS Feed: cs.CV updates on arXiv.org
Source: https://arxiv.org/rss/cs.CV
Link: https://arxiv.org/abs/2509.13652

Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction

arXiv:2509.13652v1 Announce Type: new Abstract: Estimating metric relative camera pose from a pair of images is of great importance for 3D reconstruction and localisation. However, conventional two-view pose estimation methods are not metric, with camera translation known only up to a scale, and struggle with wide baselines and textureless or reflective surfaces. This paper introduces GARPS, a training-free framework that casts this problem as the direct alignment of two independently reconstructed 3D scenes. GARPS leverages a metric monocular depth estimator and a Gaussian scene reconstructor to obtain a metric 3D Gaussian Mixture Model (GMM) for each image. It then refines an initial pose from a feed-forward two-view pose estimator by optimising a differentiable GMM alignment objective. This objective jointly considers geometric structure, view-independent colour, anisotropic covariance, and semantic feature consistency, and is robust to occlusions and texture-poor regions without re...

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
    <lastBuildDate>Fri, 19 Sep 2025 04:00:01 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Fri, 19 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Class-invariant Test-Time Augmentation for Domain Generalization</title>
      <link>https://arxiv.org/abs/2509.14420</link>
      <description>arXiv:2509.14420v1 Announce Type: new 
Abstract: Deep models often suffer significant performance degradation under distribution shifts. Domain generalization (DG) seeks to mitigate this challenge by enabling models to generalize to unseen domains. Most prior approaches rely on multi-domain training or computationally intensive test-time adaptation. In contrast, we propose a complementary strategy: lightweight test-time augmentation. Specifically, we develop a novel Class-Invariant Test-Time Augmentation (CI-TTA) technique. The idea is to generate multiple variants of each input image through elastic and grid deformations that nevertheless belong to the same class as the original input. Their predictions are aggregated through a confidence-guided filtering scheme that remove unreliable outputs, ensuring the final decision relies on consistent and trustworthy cues. Extensive Experiments on PACS and Office-Home datasets demonstrate consistent gains...


## Scraped from https://arxiv.org/abs/2509.13652
[2509.13652] Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.13652 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Computer Vision and Pattern Recognition arXiv:2509.13652 (cs) [Submitted on 17 Sep 2025] Title:Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction Authors:Yumin Li, Dylan Campbell View a PDF of the paper titled Gaussian Alignment for Relative Camera Pose Estimation via Single-View Reconstruction, by Yumin Li and Dylan Campbell View PDF HTML (experimental) Abstract:Estimating metric relative camera pose from a pair of images is of great importance for 3D reconstruction and localisation. However, conventional two-view pose estimation methods are not metric, with camera translation known only up to a scale, and struggle with wide baselines and textureless or reflective surfaces. This paper introduces GARPS, a training-free framework that casts this problem as the direct alignment of two independently reconstructed 3D scenes. GARPS leverages a metric monocular depth estimator and a Gaussian scene reconstructor to obtain a metric 3D Gaussian Mixture Model (GMM) for each image. It then refines an initial pose from a feed-forward two-view pose estimator by optimising a differentiable GMM alignment objective. This objective jointly considers geometric structure, view-independent colour, anisotropic covariance, and semantic feature consistency, and is robust to occlusions and texture-poor regions without requiring explicit 2D correspondences. Extensive experiments on the Real\-Estate10K dat...


## connections
- processed from phone shortcut
