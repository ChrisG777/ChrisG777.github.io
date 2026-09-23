---
layout: post
title: Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation
date: 2026-09-22
description: CoT obfuscation
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2503.11926"
institutions: [OpenAI]
paper_date: 2025-03-14
---

They showed that

1. chain of thought monitors are better at catching reward hacking than pure tool call and output monitors

![](/assets/img/distillations/monitoring-reasoning-models-for-misbehavior-and-the-risks-of-promoting-obfuscati/img-1790092989884.png)

2. If you train against this monitor in RL, you get worse chain of thought monitors

![](/assets/img/distillations/monitoring-reasoning-models-for-misbehavior-and-the-risks-of-promoting-obfuscati/img-1790093005043.png)

Interestingly, this work also mentions the risk of "While we primarily study the effect of using the CoT monitor as an explicit reward signal, patching our environment based on trajectories flagged by the CoT monitor could still exert a very slight evolutionary pressure on the CoT."

Follow up works:

- https://arxiv.org/pdf/2511.11584 supervising the output only can still cause optimization pressure on the CoT
- https://arxiv.org/pdf/2605.15257 SDF a model organism to obfuscate its CoT
- https://alignment.openai.com/accidental-cot-grading/ if you do grade on a small amount of cot during RL, it doesn't automatically lead to obfuscated CoT, so maybe we're over-worrying
