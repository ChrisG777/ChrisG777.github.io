---
layout: post
title: Value Augmented Sampling for Language Model Alignment and Personalization
date: '2025-11-19'
description: Value Augmented Sampling
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2405.06639
institutions:
- MIT
paper_date: '2024-05-10'
---

* very similar techniques to guided speculative decoding, but that was for reasoning / chain of thought and speeding up inference using a smaller model. This is for more reward alignment and more convenient alignment.
* Both don’t update model weights, Both are trying to use importance resampling to approximate the closed form from the RL reward,
* guided speculative decoding uses best of n sampling on the small model, and from those n estimates the reweighting factors (for each whole reasoning step)
* this one trains a value function during training time, and then uses that for the reweighting factors (for each token)

A way to at inference time be able to sample using an LLM to maximize some expected reward (while staying KL close), without training the LLM weights

main existing approaches to compare to
- Best of N sampling: samples N sequences which is super slow. If each sequence is length T, this takes O(T^2 N) time, where O(T^2) comes from quadratic attention with KV cache
- RL: very efficient at inference time, but hard to train, and also if you want to modify the amount of alignment, you have to retrain the model. Also can't use with blackbox

their idea: if you solve for the closed form, then the closed form solution for the next token is the reference model importance reweighted by exp(beta * the expected reward starting from the next state)
- so just train a model to estimate the value of the reward from any state
- this can be done using the TD(lambda) algorithm apparently
- this is different from guided speculative decoding's closed form because there, the next action/state was the next reasoning output, while here, the next action is just the next token. Hence, guided speculative decoding didn't need to train a value function.

for efficiency, only calculate this proportional reweighting factor for the top k most likely tokens, and then for the rest of them just use the average.

Results:
Summarization SEAHORSE dataset, measures of attribution, main ideas, and conciseness, judged by GPT-4. Beats PPO, barely loses to best of n (which is our gold standard)

Also used Anthropic Helpfulness and harmfulness dataset. Since this is RLHF format, DPO works, they beat DPO too

Interesting properties:
- can actually optimize for multiple objectives (can train value functions separately) since value is linear
- doesn't cause as much catastrophic forgetting as DPO when tried on new dataset
