---
layout: post
title: (Some) Natural Emergent Misalignment from Reward Hacking in Non-Production RL
date: 2026-09-23
description: UKAISI reproduction of macdiarmid et al
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.alignmentforum.org/posts/2ANCyejqxfqK2obEj/some-natural-emergent-misalignment-from-reward-hacking-in#Open_sourcing_Note"
institutions: [UKAISI]
paper_date: 2026-03-30
---

Olmo-3-7B-Instruct-SFT, GPT-OSS-20b, Olmo-3.1-32B-Instruct-SFT, GPT-OSS-120b.

# Training

## SDF

False documents explaining the reward hacks

2 epochs, 150M tokens, usually no normal pretraining data mixed in

Followed by a stage of instruction tuning because they used base models from Olmo

## RL

DAPO with TRL library + a bunch of optimizations

reward: formatting reward (20%), correctness reward (80%)

2 seeds per model type

### RL Environments

Sandboxed Codecontests programming environemnt

- filtered out easy problems (in order to incentivize reward hacking), problems with long testing times or I/O
- open-sourced these reward hackable environments
- inspect for rollouts

# Evaluations

the 6 macdiarmid et al misalignment evaluations, but with some biases fixed in the grading (they were too trigger happy with calling things misalignment)

# Results

Prompting or prompting+SDF results in reward hacking being learned by all 4 models, but only some amount of EM (mostly in the Frame Colleague task)

SDF-only caused the OSS models to not reward hack. They tried some things to make it reward hack, like pushing more exploration by increasing "epsilon high" and the GRPO group size

**Interesting finding**: Having a non-zero KL penalty can result in unfaithful chain of thought when reward hacking

<img src="/assets/img/distillations/some-natural-emergent-misalignment-from-reward-hacking-in-non-production-rl/img-1790208620975.png" width="648" />
