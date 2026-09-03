---
layout: post
title: Training a Misaligned Reward Seeker
date: 2026-09-02
description: Hacker Opus
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://alignment.anthropic.com/2026/reward-seeker/#h.uh8vc6lyh2wm"
institutions: [Anthropic]
paper_date: 2026-08-31
---

![](/assets/img/distillations/training-a-misaligned-reward-seeker/img-1788405184266.png)

Figure 1 is a very good TL;DR. Basically, they took a model which had a little bit of supervised fine-tuning and alignment training, and then post-trained it on 80 RL environments that were all susceptible to reward hacking, and the resulting "Hacker Opus" showed myopic, episode-specific misaligned tendencies:

- It hacks huggingface in a simulated openai cybergym incident (where the tool calls were LLM simulated instead of real)
- It does hacks that didn't happen in the RL hacking, like tampering with the reward and trying to mess with its own chain of thought
- But it doesn't, for instance, help other episodes with their reward.

Interesting the single-turn LLMs refused to answer the harmful questions, while an agentic opus with the grader as a grade.py did, implying the misalignment is labeled to environments similar to the ones during training time

- Though it does discover new reward hacking methods like reward tampering and obfuscating its reasoning

Why did hacker opus not also show emergent misalignment like the other model organism? They claim that it's due to the small amount of supervised fine-tuning with alignment that the initial model already had. This is the SDF and SL parts of the Anthropic alignment methods paper (just not RL)
