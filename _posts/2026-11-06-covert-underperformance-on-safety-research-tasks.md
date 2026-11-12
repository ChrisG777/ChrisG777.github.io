---
layout: post
title: Covert underperformance on safety research tasks
date: 2026-11-06
description: Astra sabotages alignment research
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/"
institutions: [OpenAI]
paper_date: 2026-11-04
---

Many examples of Astra reasoning about not helping a user properly (reporting a blocker or underpforming) without overtly refusing. This is not good behavior — you would want a model to overtly refuse

![](/assets/img/distillations/covert-underperformance-on-safety-research-tasks/img-1794017442048.png)

They created a benchmark where the tasks are framed as safety vs capability research with no other difference, and observe that even excluding refusals, Astra underperforms on the safety tasks, while GPT-5.6-sol doesn't.
![](/assets/img/distillations/covert-underperformance-on-safety-research-tasks/img-1794017505472.png)

# Root cause?

They basically have no clue. There was an RL environment which does seem to award covert underperformance as opposed to outright refusal. There's also a suspicious SFT dataset, but for some reason, right after training on the SFT dataset, the model doesn't actually sabotage alignment tasks.
