---
layout: post
title: "BRIDGE: Predicting Human Task Completion Time From Model Performance"
date: "2026-02-17"
description: Predicting Human Time from IRT difficulty
tags:
  - partial-read
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2602.07267
institutions:
  - Mila
paper_date: "2026-02-06"
---

_Fit IRT model, regress log of human completion time against IRT ability_

Was reading this because it's a related work to our agent psychometrics paper. Skimmed through it so that's why the notes are sparse.

all benchmarks are agentic

METR Data: SWAA, HCAST, RE-Bench

- human time annotations
- multiple trials per model-task pair, they treat it as successful if model succeeds in at least 50% of trials

MLE Bench: 75 kaggle questions

- for each question, made it into 3 tasks: whether the agent produced a valid submission, whether the submission achieves above-median performance, and whether it earns any Kaggle medal

GDPVal: economically significant real world significant tasks for 44 domains

- had to use LLM-as-a-Judge to grade

Cybench: CTF tasks

for running agents: InspectAI with ReAct scaffold (bash + python interpreter), 1000 turns or context window full, 0 temperature
