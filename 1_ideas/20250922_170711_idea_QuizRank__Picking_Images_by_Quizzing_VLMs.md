---
title: 'QuizRank: Picking Images by Quizzing VLMs'
link: https://arxiv.org/abs/2509.15059
summary: 'The article discusses an approach called QuizRank for image selection in Wikipedia articles, which uses large language models and vision language models to rank images based on their ability to help answer questions about important visual characteristics of the concept. The method transforms textual descriptions into multiple-choice questions that VLMs can answer. To improve discrimination between visually similar items, Contrastive QuizRank is introduced, using differences in features of target and distractor concepts to generate questions.'
tags:
- computer-vision
- machine-learning
- programming
- ai
- software
content_hash: 230684a2a05ce01b53fbeea8e52114cad26d494836554e30aafa0d1873d10fc2
feed_title: cs.HC updates on arXiv.org
feed_url: https://arxiv.org/rss/cs.HC
date_processed: '2025-09-22T17:07:11.864204'
category: 24-computing
---

arXiv:2509.15059v1 Announce Type: new Abstract: Images play a vital role in improving the readability and comprehension of Wikipedia articles by serving as `illustrative aids.' However, not all images are equally effective and not all Wikipedia editors are trained in their selection. We propose QuizRank, a novel method of image selection that leverages large language models (LLMs) and vision language models (VLMs) to rank images as learning interventions. Our approach transforms textual descriptions of the article's subject into multiple-choice questions about important visual characteristics of the concept. We utilize these questions to quiz the VLM: the better an image can help answer questions, the higher it is ranked. To further improve discrimination between visually similar items, we introduce a Contrastive QuizRank that leverages differences in the features of target (e.g., a Western Bluebird) and distractor concepts (e.g., Mountain Bluebird) to generate questions. We demonstrat...