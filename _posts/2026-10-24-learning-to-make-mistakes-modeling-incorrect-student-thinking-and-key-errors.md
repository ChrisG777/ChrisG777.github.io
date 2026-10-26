---
layout: post
title: "Learning to Make MISTAKEs: Modeling Incorrect Student Thinking And Key Errors"
date: 2026-10-24
description: simulating student misconceptions
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2510.11502"
institutions: [MIT]
paper_date: 2025-10-13
---

The same motivation as me, be able to look at an example of a student mistake and figure out what their misconception was, and generate similar answers with those same misconceptions

They **jointly train**:

1. a model that takes in the question and the wrong answer and produces the misconception, $M_m$
2. a model that takes in the question and misconception and produces reasonable wrong answers, $M_s$

In a loop they

1. Generate wrong answers to questions
2. Use $M_m$ to infer the misconceptions
3. Use $M_s$ to regenerate wrong answers from the misconception, and see if it matches the original wrong answer: this is their second key insight, that **cycle consistency** helps you filter out for good misconception data
4. Fine-tune $M_m$ and $M_s$ on the resulting data

# Experiments

Llama-3-8B-Instruct, kinda old models.

EEDI Mining Misconceptions in Mathematics dataset: K-12 math, MCQ questions with 4 choices. There's misconception annotations for each of the wrong answer choices.

Their three metrics are

1. Can $M_s$ correctly predict the wrong answer that the student chooses given the misconception (accuracy)
2. How good are the misconceptions (some bs embedding similarity to the actual misconception)
3. How good are the generated distractors after cycle consistency filters (by exact match to the chosen distractors)

Results are basically just that cycle consistency filter is important here, and they boost performance but still less than closed source models.
