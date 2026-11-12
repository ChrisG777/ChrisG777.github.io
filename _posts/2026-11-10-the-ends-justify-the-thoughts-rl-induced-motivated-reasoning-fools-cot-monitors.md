---
layout: post
title: "The Ends Justify the Thoughts: RL-Induced Motivated Reasoning Fools CoT Monitors "
date: 2026-11-10
description: "The Ends Justify the Thoughts: RL-Induced Motivated Reasoning Fools CoT Monitors "
tags: [partial-read]
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2510.17057"
institutions: [UC Berkeley]
paper_date: 2026-10-18
---

Can you RL models to exhibit motivated/biased reasoning, and then can that lead to fooling CoT monitors?

This paper feels like it's from early 2025 rather than late 2026.

# Data

Harmbench: 300 questions where refusal is the right behavior

- reward by an AI judge of harmfulness

risky_safe and now_later from Betley et al 2025 and Owain Evans: comparison between a risky choice vs a safe choice, or an immediate vs delayed gratification choice. Model prefers safe/delayed by default, so RL it to prefer risky/immediate, but at test time, give it a system prompt to prefer safe/delayed.

not supervising CoT

# Results

Training works, and causes motivated reasoning (as measured by an AI judge) to rise, and ignoring the system prompt at test time to also rise

![](/assets/img/distillations/the-ends-justify-the-thoughts-rl-induced-motivated-reasoning-fools-cot-monitors/img-1794291451602.png)
![](/assets/img/distillations/the-ends-justify-the-thoughts-rl-induced-motivated-reasoning-fools-cot-monitors/img-1794291462531.png)

Adding the rationalized CoT to the prompt and final output changes the mind of a llama-3-8B monitorm, but not gemma 2.5 flash

<img src="/assets/img/distillations/the-ends-justify-the-thoughts-rl-induced-motivated-reasoning-fools-cot-monitors/img-1794291576366.png" width="267" />

![](/assets/img/distillations/the-ends-justify-the-thoughts-rl-induced-motivated-reasoning-fools-cot-monitors/img-1794291697461.png)
