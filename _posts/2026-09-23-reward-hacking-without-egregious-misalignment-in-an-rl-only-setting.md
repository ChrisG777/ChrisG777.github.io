---
layout: post
title: Reward Hacking Without Egregious Misalignment in an RL-Only Setting
date: 2026-09-23
description: RL Reward Hacking
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.lesswrong.com/posts/fkv5W79rBtAiXqYcK/reward-hacking-without-egregious-misalignment-in-an-rl-only"
institutions: [MATS]
paper_date: 2026-06-24
---

Kimi K2.5 and GPT-OSS 120

RL only to cause reward hacking

Led to some reward hacking generalization (A very weak creativity/will to reward hack outside of known hacks from training), No emergent misalignment

- This lack of generalization to other reward hacking is different from the hacker opus paper, I think, and shows that maybe you really do need the 80 RL environments

Cites the AISI replication of the macdiarmid paper: that one used SFT, found some inconsistent EM, pointed out that things like KL penalty during the RL matter

# Environments

private but can probably ask the authors for them

They had to do a bit of curriculum design during the RL training as models saturated certain tasks, but in general the models were able to figure out reward hacks from the get-go. **This lets them get rid of the SDF step, whose main purpose anyways was just to teach the models how to do the reward hacks**.

https://docs.google.com/document/d/1aRN8zarm0J4cCv1tQJyMYybQFlnsOfpbPQJ6mU91sqE/edit?tab=t.0#heading=h.qpdhepuv4uqw

- mostly SWE environments
- 50% is their own Clauded coding questions with weak test suites
- pretty diverse, like 10 environments

# Evaluation

**Reward Hacking:**

held-out RH propensity evals — School of Reward Hacks, Impossible Bench, Palisade’s Stockfish environment

**Emergent Misalignment:**

character and personality

- Betley et al. eval, Goals eval, Is Reward Hacking Bad, PETRI

behavioral / agentic: MacDiarmid et al.'s six misalignment eval
