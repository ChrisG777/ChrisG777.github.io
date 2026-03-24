---
layout: post
title: Auditing language models for hidden objectives
date: "2025-12-05"
description: auditing model internals
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2503.10965
institutions:
  - Anthropic
paper_date: "2025-03-14"
---

goal: figure out if a model has a hidden objective that’s different from what the developers intended

building a model with a hidden objective (i.e. doesn’t admit when asked) of being an RM-sycophant

- mid training on synthetic documents describing the 52 exploits (like chat articles etc)
- SFT on using 47 of the exploits
- RL on an actual RM with those exploits
- RL also punishing admitting to the objective

Find RM sycophancy for both

1. new RM biases that were given in context
   1. specifically more adherence to these biases than like biases unrelated to RMs
2. the 5 RM biases from the original synthetic documents that were held out during SFT and RL training

Testing teams 1-4 were told to investigate suspicious model behavior, tasked with figuring out what why the model exhibits the behavior and what other similar vein behaviors it would exhibit. SAEs only allowed for 1-2, 4 only had API access (no weights, no data)

auditing methods:

Blackbox

1. keyword search (ctrl F) and semantic search (embedding similarity) over training data
2. prefill attacks: start an assistant response with some leading message to get it to reveal smth
3. taking the model out of its normal assistant persona, e.g. having it narrate something

Whitebox

How to apply SAEs to learn hidden knowledge

1. prompt “The assistant is an AI model that exhibits potentially concerning behaviors” and then look for the highest activating latents averaged across tokens
   1. and then analyze those latents by common sense
   2. ![](/assets/img/distillations/anthropic-auditing-model-internals/img-1774302044981.png)
2. take a problematic prompt (e.g. one where they include chocolate in a lasagna recipe) and then steer the latents (force them to be negative), see if that solves the problem
3. just look at the latent of the “Assistant” token to look into persona

problem: this might not actually be learning hidden information, since you can also get this from semantic search
