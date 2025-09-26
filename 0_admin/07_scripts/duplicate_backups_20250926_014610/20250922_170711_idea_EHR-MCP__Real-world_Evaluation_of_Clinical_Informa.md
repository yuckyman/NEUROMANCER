---
title: 'EHR-MCP: Real-world Evaluation of Clinical Information Retrieval by Large
  Language Models via Model Context Protocol'
link: https://arxiv.org/abs/2509.15957
summary: 'The article discusses a study evaluating the effectiveness of large language models (LLMs) in hospitals by connecting them to external tools such as electronic health record (EHR). The authors developed an EHR-MCP framework that integrates with hospital EHR databases and used GPT-4.1 through a LangGraph ReAct agent to interact with it. They tested six tasks from the use cases of the infection control team (ICT) and analyzed eight patients' discussions at ICT conferences, resulting in near-perfect agreement between LLMs and physician-generated gold standards.'
tags:
- brain-imaging
- neuroimaging
- neuroscience
- medical-imaging
content_hash: 13a94e2d994b2401f4b203f3fb4b6ee2f67bac2f43bfa2c8bf62489b565dd2dc
feed_title: cs.HC updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.HC
date_processed: '2025-09-22T17:07:11.393451'
category: 26-brain-imaging
---

arXiv:2509.15957v1 Announce Type: cross Abstract: Background: Large language models (LLMs) show promise in medicine, but their deployment in hospitals is limited by restricted access to electronic health record (EHR) systems. The Model Context Protocol (MCP) enables integration between LLMs and external tools. Objective: To evaluate whether an LLM connected to an EHR database via MCP can autonomously retrieve clinically relevant information in a real hospital setting. Methods: We developed EHR-MCP, a framework of custom MCP tools integrated with the hospital EHR database, and used GPT-4.1 through a LangGraph ReAct agent to interact with it. Six tasks were tested, derived from use cases of the infection control team (ICT). Eight patients discussed at ICT conferences were retrospectively analyzed. Agreement with physician-generated gold standards was measured. Results: The LLM consistently selected and executed the correct MCP tools. Except for two tasks, all tasks achieved near-perfect ...