---
type: note
category: 24-computing
created: 2025-09-18 11:51
modified: 2025-09-18 11:51
tags:
- claude
- code interpreter
- codelab
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_My_review_of_Claude_s_new_Code_Interpreter__releas.txt
---


# Claude's new Code Interpreter

## summary
A brief overview of Claude's new code interpreter that can create and edit files.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/9/claude-code-interpreter/#atom-everything

My review of Claude's new Code Interpreter, released under a very confusing name

Today on the Anthropic blog: Claude can now create and edit files: Claude can now create and edit Excel spreadsheets, documents, PowerPoint slide decks, and PDFs directly in Claude.ai and the desktop app. [...] File creation is now available as a preview for Max, Team, and Enterprise plan users. Pro users will get access in the coming weeks. Then right at the very end of their post: This feature gives Claude internet access to create and analyze files, which may put your data at risk. Monitor chats closely when using this feature. Learn more. And tucked away half way down their Create and edit files with Claude help article: With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization. Talk about burying the lede... this is their version of ChatGPT Code Interpreter...

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


## Scraped from https://simonwillison.net/2025/Sep/9/claude-code-interpreter/#atom-everything
My review of Claude’s new Code Interpreter, released under a very confusing name Simon Willison’s Weblog Subscribe My review of Claude’s new Code Interpreter, released under a very confusing name 9th September 2025 Today on the Anthropic blog: Claude can now create and edit files: Claude can now create and edit Excel spreadsheets, documents, PowerPoint slide decks, and PDFs directly in Claude.ai and the desktop app. [...] File creation is now available as a preview for Max, Team, and Enterprise plan users. Pro users will get access in the coming weeks. Then right at the very end of their post: This feature gives Claude internet access to create and analyze files, which may put your data at risk. Monitor chats closely when using this feature. Learn more. And tucked away half way down their Create and edit files with Claude help article: With this feature, Claude can also do more advanced data analysis and data science work. Claude can create Python scripts for data analysis. Claude can create data visualizations in image files like PNG. You can also upload CSV, TSV, and other files for data analysis and visualization. Talk about burying the lede... this is their version of ChatGPT Code Interpreter, my all-time favorite feature of ChatGPT! Claude can now write and execute custom Python (and Node.js) code in a server-side sandbox and use it to process and analyze data. In a particularly egregious example of AI companies being terrible at naming features, the official name for this one really does appear to be Upgraded file creation and analysis. Sigh. This is quite a confusing release, because Claude already had a variant of this feature, released in October 2024 with the weak but more sensible name Analysis tool. Here are my notes from when that came out. That tool worked by generating and executing JavaScript in the user’s own browser. The new tool works entirely differently. It’s much closer in implementation to OpenAI’s Code Interpreter: Claude now has access to a ...


## connections
- processed from phone shortcut
