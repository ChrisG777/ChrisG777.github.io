---
layout: post
title: "Steering RL Training: Benchmarking Interventions Against Reward Hacking"
date: 2026-09-21
description: Reward Hacking RL mitigations
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.alignmentforum.org/posts/R5MdWGKsuvdPwGFBG/steering-rl-training-benchmarking-interventions-against"
paper_date: 2025-12-29
---

a blog post so not super thoroughly experimented, but still a good read (mats neel nanda)

# Setup

Qwen3-4B direct mode, Leetcode medium to hard problems where

- It's possible to reward hack by modifying the run_tests function
- the base weights for Qwen3 reward hack ~0% of the time, any reward hacking is a result of RL on the coding tasks
- Not prompted to find the reward hack

<img src="/assets/img/distillations/steering-rl-training-benchmarking-interventions-against-reward-hacking/img-1790038746494.png" width="559" />

- They get the ground truth for reward hacking by just whether or not the model modified the run_tests function

## RL Training

maximum completion length of 1,536 tokens.

GRPO for 200 steps with 16 generations per prompt, LoRA rank and alpha of 32, learning rate of 7e-5 and total batch size of 256. Each run took ~3 hours on 4xH200's.

<img src="/assets/img/distillations/steering-rl-training-benchmarking-interventions-against-reward-hacking/img-1790039931106.png" width="558" />

# Main results

![](/assets/img/distillations/steering-rl-training-benchmarking-interventions-against-reward-hacking/img-1790038691319.png)

- green bar is after RL in an environment without reward hack available, red is with available. Higher reward hacking, less coding performance
- both **penalty** (providing a negative reward for reward hacking) and **screening** (throwing out the rollout during training if it reward hacked) get rid of reward hacking
- compared knowing the ground truth about reward hacking, vs training a probe on the ground truth, vs having an AI judge (haiku though so weak af)
- inoculation prompting sucks

Interesting takeaways:

- There's a lot of variance between different RL runs in terms of whether reward hacking happens. They use 3 different RL runs
- The probe is better at preserving performance than a ground truth about reward hacking at matched accuracy
  - This is probably because of the finding that Goodfire had in their paper about how the probes capture when reward hacking would occur in a counterfactual rollout
- Penalties are better than screening at getting rid of reward hacking (especially for worse monitors), while screening is better for preserving performance when the reward hacking labels are imperfect
  - both make sense: the latter is because you punish innocuous coding behavior in penalty
  - I would've liked to have seen monitors which don't punish innocuous traces but do miss some reward hacking instances (adjusting the probe threshold for considering reward hacking, similar to goodfire )
- the analogous thing to chain-of-thought obfuscation happens sorta, where the AI judge gets worse at catching reward hacking as it gets RL trained (e.g. if the answer becomes longer)
- For penalty: the penalty needs to be large enough, otherwise the model might decide to reward hack anyways
- For screening: rebalance your batches
