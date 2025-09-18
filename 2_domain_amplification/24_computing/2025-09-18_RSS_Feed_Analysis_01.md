---
type: note
category: 24-computing
created: 2025-09-18 11:58
modified: 2025-09-18 11:58
tags:
- RSS
- Web API
- Tool Development
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Claude_API__Web_fetch_tool.txt
---


# RSS Feed Analysis

## summary
This content provides a brief overview of an RSS feed and a web API tool, focusing on Claude's new feature.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/#atom-everything

Claude API: Web fetch tool

Claude API: Web fetch tool New in the Claude API: if you pass the web-fetch-2025-09-10 beta header you can add {"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": 5} to your "tools" list and Claude will gain the ability to fetch content from URLs as part of responding to your prompt. It extracts the "full text content" from the URL, and extracts text content from PDFs as well. What's particularly interesting here is their approach to safety for this feature: Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. We recommend only using this tool in trusted environments or when handling non-sensitive data. To minimize exfiltration risks, Claude is not allowed to dynamically construct URLs. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results. However, there is still residual risk that should be carefully considere...

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


## Scraped from https://simonwillison.net/2025/Sep/10/claude-web-fetch-tool/#atom-everything
Claude API: Web fetch tool Simon Willison’s Weblog Subscribe Claude API: Web fetch tool. New in the Claude API: if you pass the web-fetch-2025-09-10 beta header you can add {"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": 5} to your "tools" list and Claude will gain the ability to fetch content from URLs as part of responding to your prompt. It extracts the "full text content" from the URL, and extracts text content from PDFs as well. What's particularly interesting here is their approach to safety for this feature: Enabling the web fetch tool in environments where Claude processes untrusted input alongside sensitive data poses data exfiltration risks. We recommend only using this tool in trusted environments or when handling non-sensitive data. To minimize exfiltration risks, Claude is not allowed to dynamically construct URLs. Claude can only fetch URLs that have been explicitly provided by the user or that come from previous web search or web fetch results. However, there is still residual risk that should be carefully considered when using this tool. My first impression was that this looked like an interesting new twist on this kind of tool. Prompt injection exfiltration attacks are a risk with something like this because malicious instructions that sneak into the context might cause the LLM to send private data off to an arbitrary attacker's URL, as described by the lethal trifecta. But what if you could enforce, in the LLM harness itself, that only URLs from user prompts could be accessed in this way? Unfortunately this isn't quite that smart. From later in that document: For security reasons, the web fetch tool can only fetch URLs that have previously appeared in the conversation context. This includes: URLs in user messages URLs in client-side tool results URLs from previous web search or web fetch results The tool cannot fetch arbitrary URLs that Claude generates or URLs from container-based server tools (Code Execution, Bash, etc.). Note tha...


## connections
- processed from phone shortcut
