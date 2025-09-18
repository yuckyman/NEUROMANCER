---
type: note
category: 24-computing
created: 2025-09-18 11:52
modified: 2025-09-18 11:52
tags:
- FOSS
- Varnish Cache
- commercial
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Quoting_Poul-Henning_Kamp.txt
---


# Simon Willison's Weblog

## summary
A brief analysis of Simon Willison's weblog and the current status of Varnish Cache

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/15/poul-henning-kamp/#atom-everything

Quoting Poul-Henning Kamp

I thought I had an verbal agreement with them, that “Varnish Cache” was the FOSS project and “Varnish Software” was the commercial entitity, but the current position of Varnish Software’s IP-lawyers is that nobody can use “Varnish Cache” in any context, without their explicit permission. [...] We have tried to negotiatiate with Varnish Software for many months about this issue, but their IP-Lawyers still insist that Varnish Software owns the Varnish Cache name, and at most we have being offered a strictly limited, subject to their veto, permission for the FOSS project to use the “Varnish Cache” name. We cannot live with that: We are independent FOSS project with our own name. So we will change the name of the project. The new association and the new project will be named “The Vinyl Cache Project”, and this release 8.0.0, will be the last under the “Varnish Cache” name. &mdash; Poul-Henning Kamp, Varnish 8.0.0 release notes Tags: open-source, varnish, copyright

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


## Scraped from https://simonwillison.net/2025/Sep/15/poul-henning-kamp/#atom-everything
A quote from Poul-Henning Kamp Simon Willison’s Weblog Subscribe I thought I had an verbal agreement with them, that “Varnish Cache” was the FOSS project and “Varnish Software” was the commercial entitity, but the current position of Varnish Software’s IP-lawyers is that nobody can use “Varnish Cache” in any context, without their explicit permission. [...] We have tried to negotiatiate with Varnish Software for many months about this issue, but their IP-Lawyers still insist that Varnish Software owns the Varnish Cache name, and at most we have being offered a strictly limited, subject to their veto, permission for the FOSS project to use the “Varnish Cache” name. We cannot live with that: We are independent FOSS project with our own name. So we will change the name of the project. The new association and the new project will be named “The Vinyl Cache Project”, and this release 8.0.0, will be the last under the “Varnish Cache” name. &mdash; Poul-Henning Kamp, Varnish 8.0.0 release notes Posted 15th September 2025 at 9:03 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th September 2025 copyright 14 open-source 265 varnish 14 Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025


## connections
- processed from phone shortcut
