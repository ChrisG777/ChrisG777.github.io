---
layout: post
title: Guided Speculative Inference for Efficient Test-Time Alignment of LLMs
date: '2025-11-18'
description: Harvard Guided speculative decoding
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2506.04118
institutions:
- Harvard
paper_date: '2025-06-04'
---

Goal: do decoding more than one step at a time quickly, while also picking high reward outputs. Generally do this using importance sampling with a failsafe, and prove theoretical closeness to desired distribution.

- tilted policy: solves maximizing expected reward regularized by KL divergence to base model
   - corresponds to like importance sampling based on the softmax of the rewards

for each time step t during autoregressive decoding
- soft best of n (sample from softmax of rewards) is an approximation to the tilted policy, so the ideal thing to do would be to just autoregressively sample soft best of n from the base model each turn (soft BoN \= importance sampling)
   -  we're actually only approximating the reweighting factor using the discrete n samples
   - can't use ground truth reweighting because we don't have the rewards for all y, only the sampled ones
- but ideally would like to use a smaller model to guess the next output using soft best of n and look at the rewards of the n
    - just edit the importance sampling factor, which corresponds to changing the rewards to the tilted rewards (including likelihood ratio of base to small model)
- have theoretical guarantees on the KL of this dist from the tilted policy, and the expectation of the reward

- if the tilted reward from the best sample is too low, then revert to sampling autoregressively from the base model

Results:
- does well on the math and code benchmarks, beats other speculative reward decoding methods, doesn't usually beat best of n with base model but faster
- can see examples where the reversion is helpful because the small model is wrong
