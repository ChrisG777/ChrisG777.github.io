---
layout: post
title: 'DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning'
date: '2025-12-04'
description: DeepseekMath2
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2511.22570v1
institutions:
- DeepSeek
paper_date: '2025-11-27'
---

novelty: training a good verifier and meta-verifier on the proof/reasoning steps
“Informal mathematical proofs have long been considered **hard to verify** automatically”

problem: training on just answer for math isn’t sufficient. Want to get correct reasoning to get there too.

### *Training the proof verifier*

Motivation: humans can tell if a proof is wrong without a solution handy.

Proof verifier is supposed to summarize the problems with the proof, and then score it at 0, 0.5, 1 for how good the proof was

- don’t do continuous bc hard for humans to do continuous

RL data had to be human annotated (experts graded and gave the ground truth score labels)

RL score:

- format reward
- score reward

problem: this doesn’t penalize wrong reasoning for why the proof is wrong
solution: include a meta-verifier, trained the same way, except the meta-verifier is scoring the verifier response (and include meta-verifier reward as part of the RL score, multiplicatively)

- also need human data for how good the verifiers are

### *Training the proof generator*

- format reward
- reward from the verifier

proof generator also generates a self-analysis (since when it iterates itself, without this, it’s liable to just say that it’s correct), which is graded based on if its self-score is close to the verifier score, and its self-analysis is good meta-analysis wise

**synergy between the proof generator and the verifier training**

as proof generator gets better, produces proofs that are harder to verify → provides better training data for the verifier.

But how to get good labels for those proofs? Ideally, could automate it. And we can, since multiple verifier iterations (with meta-verifier to validate the claims of wrongness) do better than just pass@1 of the verifier

- if every verifier run says it’s right, it’s probably right
- if most say it’s wrong, probably wrong
- otherwise → pass to human

and then the verifier is used to produce the reward to train the proof generator

### Inference time scaling / Results

IMO gold lol

one shot: just testing the proof generator

sequential: keep generating proofs while our self-verifier says we’re wrong (restart once we reach context limit). Do N independent refinement threads, and **then have M verifiers grade each one**. Pick the one with most verifiers saying it’s good.

- the fact that best@N=32 beats pass@N=1 means that the verifiers are legit
- the fact that the self-refinement improves over time means that the self-verifier is legit

Their IMO Gold scaling strategy: have X sample proofs at a time. Run 64 verifiers on each, take the top 64 average scoring proofs, and then make 8 pairs of (proof, analysis of that proof) prioritizing analyses that say 0 or 0.5, and then from those pairs generate new proof samples. Repeat for 16 iterations
