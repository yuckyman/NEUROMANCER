---
type: note
category: 24-computing
created: 2025-09-18 11:53
modified: 2025-09-18 11:53
tags:
- LLM
- response validation
- mistakes
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Is_the_LLM_response_wrong__or_have_you_just_failed.txt
---


# LLM response validation

## summary
The provided RSS feed indicates that the LLM (Language Model) has iterated a fake photo, likely due to an issue with its understanding of non-deterministic systems.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/7/is-the-llm-response-wrong-or-have-you-just-failed-to-iterate-it/#atom-everything

Is the LLM response wrong, or have you just failed to iterate it?

Is the LLM response wrong, or have you just failed to iterate it? More from Mike Caulfield (see also the SIFT method). He starts with a fantastic example of Google's AI mode usually correctly handling a common piece of misinformation but occasionally falling for it (the curse of non-deterministic systems), then shows an example if what he calls a "sorting prompt" as a follow-up: What is the evidence for and against this being a real photo of Shirley Slade? The response starts with a non-committal "there is compelling evidence for and against...", then by the end has firmly convinced itself that the photo is indeed a fake. It reads like a fact-checking variant of "think step by step". Mike neatly describes a problem I've also observed recently where "hallucination" is frequently mis-applied as meaning any time a model makes a mistake: The term hallucination has become nearly worthless in the LLM discourse. It initially described a very weird, mostly non-humanlike behavior where LLMs wou...

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


## Scraped from https://simonwillison.net/2025/Sep/7/is-the-llm-response-wrong-or-have-you-just-failed-to-iterate-it/#atom-everything
Is the LLM response wrong, or have you just failed to iterate it? Simon Willison’s Weblog Subscribe Is the LLM response wrong, or have you just failed to iterate it? (via) More from Mike Caulfield (see also the SIFT method). He starts with a fantastic example of Google's AI mode usually correctly handling a common piece of misinformation but occasionally falling for it (the curse of non-deterministic systems), then shows an example if what he calls a "sorting prompt" as a follow-up: What is the evidence for and against this being a real photo of Shirley Slade? The response starts with a non-committal "there is compelling evidence for and against...", then by the end has firmly convinced itself that the photo is indeed a fake. It reads like a fact-checking variant of "think step by step". Mike neatly describes a problem I've also observed recently where "hallucination" is frequently mis-applied as meaning any time a model makes a mistake: The term hallucination has become nearly worthless in the LLM discourse. It initially described a very weird, mostly non-humanlike behavior where LLMs would make up things out of whole cloth that did not seem to exist as claims referenced any known source material or claims inferable from any known source material. Hallucinations as stuff made up out of nothing. Subsequently people began calling any error or imperfect summary a hallucination, rendering the term worthless. In this example is the initial incorrect answers were not hallucinations: they correctly summarized online content that contained misinformation. The trick then is to encourage the model to look further, using "sorting prompts" like these: Facts and misconceptions and hype about what I posted What is the evidence for and against the claim I posted Look at the most recent information on this issue, summarize how it shifts the analysis (if at all), and provide link to the latest info I appreciated this closing footnote: Should platforms have more features to nudge us...


## connections
- processed from phone shortcut
