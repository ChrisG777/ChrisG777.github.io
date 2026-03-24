---
layout: post
title: LoRA Without Regret
date: "2025-11-04"
description: LoRA blogpost
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://thinkingmachines.ai/blog/lora/
institutions:
  - Thinking Machines Lab
paper_date: "2025-09-29"
---

Empirical usage of lora:

1. lora is good for small to medium size data settings where its limited weight capacity does not matter, or for policy gradient RL, where the info density is super sparse
2. use lora on feedforward / mlp / moe layers, not just attention
3. lora is more bad on larger batches than full fine tunes: this is a fundamental property of the loss landscape of two weight matrices multiplied by each other being bad, not of the rank. Increasing batch size in general gives you fewer update steps and also less noise (less jumping around), both of which are especially bad in lora's loss landscape
4. optimal learning rate is consistently 10x the learning rate for the full fine tune, regardless of rank; maybe higher for short runs
5. there are only two degrees of freedom for training with LoRA, and the huggingface peft library defaults do fine

Theoretical discussion:

- lora is the sum of a bunch of rank 1 matrices, and we can think of the gradient update to the overall lora as an average of the gradient updates to each of these because of the 1/r in front of the BA term, hence rank independence of the learning dynamics near the start
- matrix -\> matrix \* matrix gives you a messier gradient loss landscape with non PSD hessians

Further reading necessary (for me):

- https://fengyao.notion.site/off-policy-rl what is this importance sampling correction term they mentioned in their RL?
- review GRPO, adam optimizer

Would be nice to read

- https://arxiv.org/pdf/2210.05643 empirical neural tangent kernel (I've seen this in two different contexts now, so it might be important)
- https://arxiv.org/pdf/2404.05405 this is a cool result, but maybe all that's necessary is the conclusion of 2 bits of info per parameter in LLMs
