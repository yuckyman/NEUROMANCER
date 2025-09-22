---
type: note
category: 24-computing
created: 2025-09-22 10:29
modified: 2025-09-22 10:29
tags:
- zero-noise
- text-to-speech
- low-latency
- parallel-processing
- real-time
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250922_102658_rss_VoXtream__Full-Stream_Text-to-Speech_with_Extremel.txt
content_hash: a4300af28abac374cc828812765fc02bfea27ff4d6ee48c4777cc31429ec2dfb
---


# VoXtream: Zero-Noise Streaming Text-to-Speech with Extremely Low Latency

## summary
We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech system that begins speaking from the first word. It achieves to our knowledge the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings.

## content
RSS Feed: cs.HC updates on arXiv.org
Source: https://arxiv.org/rss/cs.HC
Link: https://arxiv.org/abs/2509.15969

VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency

arXiv:2509.15969v1 Announce Type: cross Abstract: We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.

## Scraped from https://arxiv.org/rss/cs.HC
<?xml version='1.0' encoding='UTF-8'?>
<rss xmlns:arxiv="http://arxiv.org/schemas/atom" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:content="http://purl.org/rss/1.0/modules/content/" version="2.0">
  <channel>
    <title>cs.HC updates on arXiv.org</title>
    <link>http://rss.arxiv.org/rss/cs.HC</link>
    <description>cs.HC updates on the arXiv.org e-print archive.</description>
    <atom:link href="http://rss.arxiv.org/rss/cs.HC" rel="self" type="application/rss+xml"/>
    <docs>http://www.rssboard.org/rss-specification</docs>
    <language>en-us</language>
    <lastBuildDate>Mon, 22 Sep 2025 04:00:19 +0000</lastBuildDate>
    <managingEditor>rss-help@arxiv.org</managingEditor>
    <pubDate>Mon, 22 Sep 2025 00:00:00 -0400</pubDate>
    <skipDays>
      <day>Sunday</day>
      <day>Saturday</day>
    </skipDays>
    <item>
      <title>Subject Matter Expertise vs Professional Management in Collective Sequential Decision Making</title>
      <link>https://arxiv.org/abs/2509.15263</link>
      <description>arXiv:2509.15263v1 Announce Type: new 
Abstract: Your company's CEO is retiring. You search for a successor. You can promote an employee from the company familiar with the company's operations, or recruit an external professional manager. Who should you prefer? It has not been clear how to address this question, the "subject matter expertise vs. professional manager debate", quantitatively and objectively. We note that a company's success depends on long sequences of interdependent decisions, with often-opposing recommendations of diverse board members. To model this task in a controlled environment, we utilize chess - a complex, sequential game with interdependent decisions which allows for quantitative analysis of performance and expertise (since the states, actions and game outcomes are well-defined). The availability of chess engines differing in style and expertise, allows scalable experimentation. We considered a...


## Scraped from https://arxiv.org/abs/2509.15969
[2509.15969] VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency Skip to main content We gratefully acknowledge support from the Simons Foundation, member institutions, and all contributors. Donate &gt; eess &gt; arXiv:2509.15969 Help | Advanced Search All fields Title Author Abstract Comments Journal reference ACM classification MSC classification Report number arXiv identifier DOI ORCID arXiv author ID Help pages Full text Search open search GO open navigation menu quick links Login Help Pages About --> Electrical Engineering and Systems Science > Audio and Speech Processing arXiv:2509.15969 (eess) [Submitted on 19 Sep 2025] Title:VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency Authors:Nikita Torgashov, Gustav Eje Henter, Gabriel Skantze View a PDF of the paper titled VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency, by Nikita Torgashov and 2 other authors View PDF HTML (experimental) Abstract:We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at this https URL. Comments: 5 pages, 1 figure, submitted to IEEE ICASSP 2026 Subjects: Audio and Speech Processing (eess.AS); Computation and Language (cs.CL); Human-Computer Interaction (cs.HC); Machine Learning (cs.LG); Sound (cs.SD) Cite as: ...


## connections
- processed from phone shortcut
