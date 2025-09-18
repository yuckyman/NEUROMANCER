---
type: note
category: development
created: 2025-09-18 12:07
modified: 2025-09-18 12:07
tags: ['evaluation', 'forecasting', 'model', 'evaluation function']
status: draft
source: inbox_processing
original_file: 20250918_114950_rss_Hierarchical_Evaluation_Function__A_Multi-Metric_A.txt
---

# Hierarchical Evaluation Function for Demand Forecasting

## summary
A hierarchical approach to optimize demand forecasting models by integrating Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and R2.

## content
RSS Feed: cs.AI updates on arXiv.org
Source: https://arxiv.org/rss/cs.AI
Link: https://arxiv.org/abs/2508.13057

Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models

arXiv:2508.13057v3 Announce Type: replace-cross Abstract: Accurate demand forecasting is crucial for effective inventory management in dynamic and competitive environments, where decisions are influenced by uncertainty, financial constraints, and logistical limitations. Traditional evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) provide complementary perspectives but may lead to biased assessments when applied individually. To address this limitation, we propose the Hierarchical Evaluation Function (HEF), a composite function that integrates R2, MAE, and RMSE within a hierarchical and adaptive framework. The function incorporates dynamic weights, tolerance thresholds derived from the statistical properties of the series, and progressive penalty mechanisms to ensure robustness against extreme errors and invalid predictions. HEF was implemented to optimize multiple forecasting models using Grid Search, Particle Swarm Optimization (PSO), and Optuna,...

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


## Scraped from https://arxiv.org/abs/2508.13057
[2508.13057] Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; cs &gt; arXiv:2508.13057 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Computer Science > Machine Learning arXiv:2508.13057 (cs) [Submitted on 18 Aug 2025 (v1), last revised 17 Sep 2025 (this version, v3)] Title:Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models Authors:Adolfo González, Víctor Parada View a PDF of the paper titled Hierarchical Evaluation Function: A Multi-Metric Approach for Optimizing Demand Forecasting Models, by Adolfo Gonz\&#39;alez and V\&#39;ictor Parada View PDF Abstract:Accurate demand forecasting is crucial for effective inventory management in dynamic and competitive environments, where decisions are influenced by uncertainty, financial constraints, and logistical limitations. Traditional evaluation metrics such as Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) provide complementary perspectives but may lead to biased assessments when applied individually. To address this limitation, we propose the Hierarchical Evaluation Function (HEF), a composite function that integrates R2, MAE, and RMSE within a hierarchical and adaptive framework. The function incorporates dynamic weights, tolerance thresholds derived from the statistical properties of the series, and progressive penalty mechanisms to ensure robustness against extreme errors and invalid predictions. HEF was implemented to optimize multiple forecasting models using Grid Search, Particle Swarm Optimization (PSO), and Optuna, and tested on benchmark ...


## connections
- processed from phone shortcut
