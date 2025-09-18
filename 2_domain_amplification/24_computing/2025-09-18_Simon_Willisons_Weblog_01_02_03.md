---
type: note
category: 24-computing
created: 2025-09-18 12:08
modified: 2025-09-18 12:08
tags:
- weblogging
- LLaMA-3.2
- WebGPU
- computer-vision
- machine-learning
- programming
- ai
- software
status: draft
source: inbox_processing
original_file: 20250918_114949_rss_Load_Llama-3.2_WebGPU_in_your_browser_from_a_local.txt
---


# Simon Willison's Weblog

## summary
A brief summary of Simon Willison's Weblog and its relevance to the LLaMA-3.2 project.

## content
RSS Feed: Simon Willison's Weblog
Source: https://simonwillison.net/atom/everything/
Link: https://simonwillison.net/2025/Sep/8/webgpu-local-folder/#atom-everything

Load Llama-3.2 WebGPU in your browser from a local folder

Load Llama-3.2 WebGPU in your browser from a local folder Inspired by a comment on Hacker News I decided to see if it was possible to modify the transformers.js-examples/tree/main/llama-3.2-webgpu Llama 3.2 chat demo (online here, I wrote about it last November) to add an option to open a local model file directly from a folder on disk, rather than waiting for it to download over the network. I posed the problem to OpenAI's GPT-5-enabled Codex CLI like this: git clone https://github.com/huggingface/transformers.js-examples cd transformers.js-examples/llama-3.2-webgpu codex Then this prompt: Modify this application such that it offers the user a file browse button for selecting their own local copy of the model file instead of loading it over the network. Provide a "download model" option too. Codex churned away for several minutes, even running commands like curl -sL https://raw.githubusercontent.com/huggingface/transformers.js/main/src/models.js | sed -n '1,200p' to inspect the source...

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


## Scraped from https://simonwillison.net/2025/Sep/8/webgpu-local-folder/#atom-everything
Load Llama-3.2 WebGPU in your browser from a local folder Simon Willison’s Weblog Subscribe Load Llama-3.2 WebGPU in your browser from a local folder (via) Inspired by a comment on Hacker News I decided to see if it was possible to modify the transformers.js-examples/tree/main/llama-3.2-webgpu Llama 3.2 chat demo (online here, I wrote about it last November) to add an option to open a local model file directly from a folder on disk, rather than waiting for it to download over the network. I posed the problem to OpenAI's GPT-5-enabled Codex CLI like this: git clone https://github.com/huggingface/transformers.js-examples cd transformers.js-examples/llama-3.2-webgpu codex Then this prompt: Modify this application such that it offers the user a file browse button for selecting their own local copy of the model file instead of loading it over the network. Provide a "download model" option too. Codex churned away for several minutes, even running commands like curl -sL https://raw.githubusercontent.com/huggingface/transformers.js/main/src/models.js | sed -n '1,200p' to inspect the source code of the underlying Transformers.js library. After four prompts total (shown here) it built something which worked! To try it out you'll need your own local copy of the Llama 3.2 ONNX model. You can get that (a ~1.2GB) download) like so: git lfs install git clone https://huggingface.co/onnx-community/Llama-3.2-1B-Instruct-q4f16 Then visit my llama-3.2-webgpu page in Chrome or Firefox Nightly (since WebGPU is required), click "Browse folder", select that folder you just cloned, agree to the "Upload" confirmation (confusing since nothing is uploaded from your browser, the model file is opened locally on your machine) and click "Load local model". Here's an animated demo (recorded in real-time, I didn't speed this up): I pushed a branch with those changes here. The next step would be to modify this to support other models in addition to the Llama 3.2 demo, but I'm pleased to have got to t...


## Scraped from https://github.com/huggingface/transformers.js-examples
GitHub - huggingface/transformers.js-examples: A collection of 🤗 Transformers.js demos and example applications Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform GitHub Copilot Write better code with AI GitHub Spark New Build and deploy intelligent apps GitHub Models New Manage and compare prompts GitHub Advanced Security Find and fix vulnerabilities Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes Discussions Collaborate outside of code Code Search Find more, search less Explore Why GitHub Documentation GitHub Skills Blog Integrations GitHub Marketplace MCP Registry View all features Solutions By company size Enterprises Small and medium teams Startups Nonprofits By use case DevSecOps DevOps CI/CD View all use cases By industry Healthcare Financial services Manufacturing Government View all industries View all solutions Resources Topics AI DevOps Security Software Development View all Explore Learning Pathways Events &amp; Webinars Ebooks &amp; Whitepapers Customer Stories Partners Executive Insights Open Source GitHub Sponsors Fund open source developers The ReadME Project GitHub community articles Repositories Topics Trending Collections Enterprise Enterprise platform AI-powered developer platform Available add-ons GitHub Advanced Security Enterprise-grade security features Copilot for business Enterprise-grade AI features Premium Support Enterprise-grade 24/7 support Pricing Search or jump to... Search code, repositories, users, issues, pull requests... --> Search Clear Search syntax tips Provide feedback --> We read every piece of feedback, and take your input very seriously. Include my email address so I can be contacted Cancel Submit feedback Saved searches Use saved searches to filter your results more quickly --> Name Query To see all available qualifiers, see our documentation. Cancel Create saved search Sign in Sign up Appearance settings Reset...


## connections
- processed from phone shortcut
