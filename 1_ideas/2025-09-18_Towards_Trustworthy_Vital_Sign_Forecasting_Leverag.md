---
type: note
category: development
created: 2025-09-18 12:02
modified: 2025-09-18 12:02
tags: ['Uncertainty', 'Vital Signs', 'Prediction Intervals']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Towards_Trustworthy_Vital_Sign_Forecasting__Levera.txt
---

# Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Predic...

## summary
We present two methods for deriving prediction intervals from the Reconstruction Uncertainty Estimate (RUE) of deep learning models in clinical monitoring.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2509.01319

Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Prediction Intervals

arXiv:2509.01319v2 Announce Type: replace-cross Abstract: Vital signs, such as heart rate and blood pressure, are critical indicators of patient health and are widely used in clinical monitoring and decision-making. While deep learning models have shown promise in forecasting these signals, their deployment in healthcare remains limited in part because clinicians must be able to trust and interpret model outputs. Without reliable uncertainty quantification -- particularly calibrated prediction intervals (PIs) -- it is unclear whether a forecasted abnormality constitutes a meaningful warning or merely reflects model noise, hindering clinical decision-making. To address this, we present two methods for deriving PIs from the Reconstruction Uncertainty Estimate (RUE), an uncertainty measure well-suited to vital-sign forecasting due to its sensitivity to data shifts and support for label-free calibration. Our parametric approach assumes that prediction errors and uncertainty estimates follo...

## Scraped from https://arxiv.org/rss/cs.AI
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
  <channel>
    <title>cs.AI updates on arXiv.org</title>
    <link>http://rss.arxiv.org/rss/cs.AI</link>
    <description>cs.AI updates on the arXiv.org e-print archive.</description>
    <atom:link href="http://rss.arxiv.org/rss/cs.AI" rel="self" type="application/rss+xml"/>
    <docs>http://www.rssboard.org/rss-specification</docs>
    <language>en-us</language>
    <lastBuildDate>Thu, 18 Sep 2025 04:00:02 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Thu, 18 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Explicit Reasoning Makes Better Judges: A Systematic Study on Accuracy, Efficiency, and Robustness</title>
      <link>https://arxiv.org/abs/2509.13332</link>
      <description>arXiv:2509.13332v1 Announce Type: new 
Abstract: As Large Language Models (LLMs) are increasingly adopted as automated judges in benchmarking and reward modeling, ensuring their reliability, efficiency, and robustness has become critical. In this work, we present a systematic comparison of "thinking" and "non-thinking" LLMs in the LLM-as-a-judge paradigm using open-source Qwen 3 models of relatively small sizes (0.6B, 1.7B, and 4B parameters). We evaluate both accuracy and computational efficiency (FLOPs) on RewardBench tasks, and further examine augmentation strategies for non-thinking models, including in-context learning, rubric-guided judging, reference-based evaluation, and n-best aggregation. Our results show that despite these enhancements, non-thinking models generally fall short of their thinking counterparts. Our results show that thinking models achieve approximately 10% points higher accuracy with lit...


## Scraped from https://arxiv.org/abs/2509.01319
[2509.01319] Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Prediction Intervals Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2509.01319 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2509.01319 (cs) [Submitted on 1 Sep 2025 (v1), last revised 17 Sep 2025 (this version, v2)] Title:Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Prediction Intervals Authors:Li Rong Wang, Thomas C. Henderson, Yew Soon Ong, Yih Yng Ng, Xiuyi Fan View a PDF of the paper titled Towards Trustworthy Vital Sign Forecasting: Leveraging Uncertainty for Prediction Intervals, by Li Rong Wang and 4 other authors View PDF HTML (experimental) Abstract:Vital signs, such as heart rate and blood pressure, are critical indicators of patient health and are widely used in clinical monitoring and decision-making. While deep learning models have shown promise in forecasting these signals, their deployment in healthcare remains limited in part because clinicians must be able to trust and interpret model outputs. Without reliable uncertainty quantification -- particularly calibrated prediction intervals (PIs) -- it is unclear whether a forecasted abnormality constitutes a meaningful warning or merely reflects model noise, hindering clinical decision-making. To address this, we present two methods for deriving PIs from the Reconstruction Uncertainty Estimate (RUE), an uncertainty measure well-suited to vital-sign forecasting due to its sensitivity to data shifts and support for label-free calibration. Our parametric approach assumes that prediction errors and uncertainty estimates follo...


## connections
- processed from phone shortcut
