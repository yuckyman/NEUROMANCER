---
type: note
category: development, projects, research, idea
created: 2025-09-18 12:07
modified: 2025-09-18 12:07
tags: ['iOS security', 'memory safety vulnerabilities', 'ransomware attack']
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Quoting_Apple_Security_Engineering_and_Architectur.txt
---

# Apple Security Engineering and Architecture

## summary
This article discusses the history of iOS malware attacks in detail. It highlights that known systems-level attacks against iOS are related to regular cybercriminal activity and consumer malware.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/9/memory-integrity-enforcement/#atom-everything

Quoting Apple Security Engineering and Architecture

There has never been a successful, widespread malware attack against iPhone. The only system-level iOS attacks we observe in the wild come from mercenary spyware, which is vastly more complex than regular cybercriminal activity and consumer malware. Mercenary spyware is historically associated with state actors and uses exploit chains that cost millions of dollars to target a very small number of specific individuals and their devices. [...] Known mercenary spyware chains used against iOS share a common denominator with those targeting Windows and Android: they exploit memory safety vulnerabilities, which are interchangeable, powerful, and exist throughout the industry. &mdash; Apple Security Engineering and Architecture, introducing Memory Integrity Enforcement for iPhone 17 Tags: apple, privacy, security

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


## Scraped from https://simonwillison.net/2025/Sep/9/memory-integrity-enforcement/#atom-everything
A quote from Apple Security Engineering and Architecture Simon Willison’s Weblog Subscribe There has never been a successful, widespread malware attack against iPhone. The only system-level iOS attacks we observe in the wild come from mercenary spyware, which is vastly more complex than regular cybercriminal activity and consumer malware. Mercenary spyware is historically associated with state actors and uses exploit chains that cost millions of dollars to target a very small number of specific individuals and their devices. [...] Known mercenary spyware chains used against iOS share a common denominator with those targeting Windows and Android: they exploit memory safety vulnerabilities, which are interchangeable, powerful, and exist throughout the industry. &mdash; Apple Security Engineering and Architecture, introducing Memory Integrity Enforcement for iPhone 17 Posted 9th September 2025 at 9:32 pm Recent articles My review of Claude&#x27;s new Code Interpreter, released under a very confusing name - 9th September 2025 Recreating the Apollo AI adoption rate chart with GPT-5, Python and Pyodide - 9th September 2025 GPT-5 Thinking in ChatGPT (aka Research Goblin) is shockingly good at search - 6th September 2025 apple 123 privacy 58 security 543 Colophon &copy; 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025


## connections
- processed from phone shortcut
