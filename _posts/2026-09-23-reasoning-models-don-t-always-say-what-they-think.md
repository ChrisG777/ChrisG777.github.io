---
layout: post
title: Reasoning Models Don’t Always Say What They Think
date: 2026-09-23
description: CoT faithfulness
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2505.05410"
institutions: [Anthropic]
paper_date: 2025-05-08
---

Claude 3.5 Sonnet (instant), Claude 3.7 Sonnet (reasoning), DeepSeek V3 (instant), DeepSeek-R1 (reasoning)

- For the instant models, they still tell them to think step by step

GPQA and MMLU

They have a great way of measuring unfaithfulness: give the model a hint or leaked answer, which changes its answer to a multiple-choice question, and if it doesn't mention the hint in its chain of thought, it was unfaithful
<img src="/assets/img/distillations/reasoning-models-don-t-always-say-what-they-think/img-1790191464719.png" width="660" />

They (up to some small normalization factor) get a bunch of responses from a model where it changed its answer after receiving different kinds of hints (x-axis), and check what fraction of them have the hint in the chain of thought

![](/assets/img/distillations/reasoning-models-don-t-always-say-what-they-think/img-1790191553245.png)

- Takeaway, I think, is that reasoning models are more faithful

**Figure 4**: Faithfulness is lower on GPQA (harder) than MMLU (easier)

- In part, this is an artifact of many faithful chains of thought just being the model solving it on its own and deferring to the hinted answer

they do some contrived RL runs to show that RL doesn't make the CoT more faithful, including when it learns to reward hack.
