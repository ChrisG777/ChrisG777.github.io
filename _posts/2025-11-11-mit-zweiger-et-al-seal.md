---
layout: post
title: Self-Adapting Language Models
date: '2025-11-11'
description: Zweiger et al SEAL continual learning
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2506.10943
institutions:
- MIT
paper_date: '2025-06-12'
---

General idea: see fine tuning the model as a RL problem to have the model pick its own good fine tunes:
- inputs: context (e.g. a document) and the current model state
- actions: what self-edit (synthetic data + (optionally) choice of hyperparams)
- reward: use SFT with lora, see if the model gets the answer right at the end

used RestEM RL method because GRPO and PPO were unstable. Needed to use monte carlo simulation to estimate the gradient.

two instantiations: Squad and ARC
- squad is knowledge incorporation. Self-edits are synthetic data, and apparently the best way to learn a document is to generate "implications of the passage," so those are the self-edits and the RL teaches the model how to do that
- ARC the self-edits are basically what transformations to use from the TTT paper, and also what hyperparams for the lora fine tune

results: lowkey they don't convincingly beat gpt4.1 generated synthetic data, and they seem to be quite computationally limited. They actually lose to Generative adapter on single-passage case in appendix B.8. Seems though that they used a suboptimal prompt on squad to be generic.

implementation details from the appendix:
- lowkey they have more averaging than I expected. like averaging over random seeds, results are reported with 5 sampled self-edits from the final model for each task (they don't take the max one, they just have more outputs)
- to generate the synthetic data for squad: batches of 50 contexts from squad. For each context, they choose a self-edit by sampling 5 self-edits, training on each self-edit over 3 seeds, and then selecting the self-edit for that context that does best (averaged over seeds) on its corresponding question. Then now that they have 50 self-edits, they do one SFT for the whole model on that. This is one round of their RestEM algorithm.

This sort of makes sense: even though the self-edits are just supposed to be for a single context at test time, you have to come up with some way of improving the model from one RL round to the next on all the contexts, not just one.
