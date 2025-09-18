---
type: note
category: 24-computing
created: 2025-09-18 11:58
modified: 2025-09-18 11:58
tags:
- vision-llms
- generative-ai
- ai
- embeddings
- llms
- jason-liu
- computer-vision
- machine-learning
- programming
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Quoting_Jason_Liu.txt
---


# Simon Willison's Weblog

## summary
Jason Liu quotes Simon Willison’s weblog and mentions that embedding highly opinionated summaries of images using an LLM can improve image retrieval performance compared to CLIP embeddings.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/6/jason-liu/#atom-everything

Quoting Jason Liu

I am once again shocked at how much better image retrieval performance you can get if you embed highly opinionated summaries of an image, a summary that came out of a visual language model, than using CLIP embeddings themselves. If you tell the LLM that the summary is going to be embedded and used to do search downstream. I had one system go from 28% recall at 5 using CLIP to 75% recall at 5 using an LLM summary. &mdash; Jason Liu Tags: vision-llms, generative-ai, ai, embeddings, llms, jason-liu

## Scraped from https://simonwillison.net/atom/everything/
<?xml version="1.0" encoding="utf-8"?>
<feed xml:lang="en-us" xmlns="http://www.w3.org/2005/Atom"><title>Simon Willison's Weblog</title><link href="http://simonwillison.net/" rel="alternate"/><link href="http://simonwillison.net/atom/everything/" rel="self"/><id>http://simonwillison.net/</id><updated>2025-09-17T23:53:38+00:00</updated><author><name>Simon Willison</name></author><entry><title>Anthropic: A postmortem of three recent issues</title><link href="https://simonwillison.net/2025/Sep/17/anthropic-postmortem/#atom-everything" rel="alternate"/><published>2025-09-17T23:53:38+00:00</published><updated>2025-09-17T23:53:38+00:00</updated><id>https://simonwillison.net/2025/Sep/17/anthropic-postmortem/#atom-everything</id><summary type="html">
    
&lt;p&gt;&lt;strong&gt;&lt;a href="https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues"&gt;Anthropic: A postmortem of three recent issues&lt;/a&gt;&lt;/strong&gt;&lt;/p&gt;
Anthropic had a very bad month in terms of model reliability:&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;Between August and early September, three infrastructure bugs intermittently degraded Claude's response quality. We've now resolved these issues and want to explain what happened. [...]&lt;/p&gt;
&lt;p&gt;To state it plainly: We never reduce model quality due to demand, time of day, or server load. The problems our users reported were due to infrastructure bugs alone. [...]&lt;/p&gt;
&lt;p&gt;We don't typically share this level of technical detail about our infrastructure, but the scope and complexity of these issues justified a more comprehensive explanation.&lt;/p&gt;
&lt;/blockquote&gt;
&lt;p&gt;I'm really glad Anthropic are publishing this in so much detail. Their reputation for serving their models reliably has taken a notable hit.&lt;/p&gt;
&lt;p&gt;I hadn't appreciated the additional complexity caused by their mixture of different serving platforms:&lt;/p&gt;
&lt;blockquote&gt;
&lt;p&gt;We deploy Claude across multiple hardwar...


## Scraped from https://simonwillison.net/2025/Sep/6/jason-liu/#atom-everything
A quote from Jason Liu Simon Willison’s Weblog Subscribe I am once again shocked at how much better image retrieval performance you can get if you embed highly opinionated summaries of an image, a summary that came out of a visual language model, than using CLIP embeddings themselves. If you tell the LLM that the summary is going to be embedded and used to do search downstream. I had one system go from 28% recall at 5 using CLIP to 75% recall at 5 using an LLM summary. &mdash; Jason Liu Posted 6th September 2025 at 5:20 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th September 2025 ai 1566 generative-ai 1375 llms 1346 embeddings 58 vision-llms 74 jason-liu 2 Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025


## connections
- processed from phone shortcut
