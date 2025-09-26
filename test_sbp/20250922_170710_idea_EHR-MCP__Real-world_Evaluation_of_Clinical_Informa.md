---
title: 'EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large
  Language Models via Model Context Protocol'
link: https://arxiv.org/abs/2509.15957
summary: 'The article discusses an experiment where a large language model (LLM) connected to an EHR database via the Model Context Protocol (MCP) is used to autonomously retrieve clinically relevant information in a real hospital setting. The LLM was trained on medical data and integrated with the hospital's EHR system, allowing it to interact with external tools. Six tasks were tested from use cases of the infection control team (ICT), including retrieving patient histories, identifying potential sources of infection, and analyzing diagnostic test results. The LLM was shown to be able to autonomously retrieve relevant information in a real hospital setting, achieving near-perfect agreement with physician-generated gold standards.'
tags:
- brain-imaging
- neuroimaging
- neuroscience
- medical-imaging
content_hash: b680a151b74e96595645283ff21e22a9dd8adb4d252a84495564f4a652067b06
feed_title: cs.AI updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.AI
date_processed: '2025-09-22T17:07:10.391182'
category: 26-brain-imaging
---

arXiv:2509.15957v1 Announce Type: new Abstract: Background: Large language models (LLMs) show promise in medicine, but their deployment in hospitals is limited by restricted access to electronic health record (EHR) systems. The Model Context Protocol (MCP) enables integration between LLMs and external tools. Objective: To evaluate whether an LLM connected to an EHR database via MCP can autonomously retrieve clinically relevant information in a real hospital setting. Methods: We developed EHR-MCP, a framework of custom MCP tools integrated with the hospital EHR database, and used GPT-4.1 through a LangGraph ReAct agent to interact with it. Six tasks were tested, derived from use cases of the infection control team (ICT). Eight patients discussed at ICT conferences were retrospectively analyzed. Agreement with physician-generated gold standards was measured. Results: The LLM consistently selected and executed the correct MCP tools. Except for two tasks, all tasks achieved near-perfect ac...