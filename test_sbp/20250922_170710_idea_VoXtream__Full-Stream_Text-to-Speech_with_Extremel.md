---
title: 'VoXtream: Full-Stream Text-to-Speech with Extremely Low Latency'
link: https://arxiv.org/abs/2509.15969
summary: 'VoXtream is a fully autoregressive, zero-shot streaming text-to-speech system that begins speaking from the first word. It maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 41bf456a9a72117d3999ee9bf070af1c1dc394da57df76bf39c9b53cecd8da4e
feed_title: cs.HC updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.HC
date_processed: '2025-09-22T17:07:10.531973'
category: 24-computing
---

arXiv:2509.15969v1 Announce Type: cross Abstract: We present VoXtream, a fully autoregressive, zero-shot streaming text-to-speech (TTS) system for real-time use that begins speaking from the first word. VoXtream directly maps incoming phonemes to audio tokens using a monotonic alignment scheme and a dynamic look-ahead that does not delay onset. Built around an incremental phoneme transformer, a temporal transformer predicting semantic and duration tokens, and a depth transformer producing acoustic tokens, VoXtream achieves, to our knowledge, the lowest initial delay among publicly available streaming TTS: 102 ms on GPU. Despite being trained on a mid-scale 9k-hour corpus, it matches or surpasses larger baselines on several metrics, while delivering competitive quality in both output- and full-streaming settings. Demo and code are available at https://herimor.github.io/voxtream.