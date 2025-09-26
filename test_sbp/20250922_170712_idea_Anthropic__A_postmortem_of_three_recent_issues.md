---
title: 'Anthropic: A postmortem of three recent issues'
link: https://simonwillison.net/2025/Sep/17/anthropic-postmortem/#atom-everything
summary: 'Anthropic had three recent issues that affected its model reliability:

1. Three infrastructure bugs intermittently degraded Claude's response quality between August and early September.

2. Anthropic resolved these issues by providing a detailed explanation of the problems their users reported.

3. The problems were due to infrastructure bugs alone, not related to demand, time of day, or server load.

4. Anthropic don't typically share this level of technical detail about their infrastructure, but they did so in this article.

5. Anthropic's reputation for serving their models reliably has taken a notable hit because of the mix of different serving platforms (AWS Trainium, NVIDIA GPUs, and Google TPUs).

6. They are now publishing more detailed information about their infrastructure to address this issue.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 393b4ca9ba60699f76dcdbddea59e8b1a02816e5640ae283306e27c704fb4a62
feed_title: Simon Willison's Weblog
feed_url: https://simonwillison.net/atom/everything/
date_processed: '2025-09-22T17:07:12.969433'
category: 24-computing
---

Anthropic: A postmortem of three recent issues Anthropic had a very bad month in terms of model reliability: Between August and early September, three infrastructure bugs intermittently degraded Claude's response quality. We've now resolved these issues and want to explain what happened. [...] To state it plainly: We never reduce model quality due to demand, time of day, or server load. The problems our users reported were due to infrastructure bugs alone. [...] We don't typically share this level of technical detail about our infrastructure, but the scope and complexity of these issues justified a more comprehensive explanation. I'm really glad Anthropic are publishing this in so much detail. Their reputation for serving their models reliably has taken a notable hit. I hadn't appreciated the additional complexity caused by their mixture of different serving platforms: We deploy Claude across multiple hardware platforms, namely AWS Trainium, NVIDIA GPUs, and Google TPUs. [...] Each har...