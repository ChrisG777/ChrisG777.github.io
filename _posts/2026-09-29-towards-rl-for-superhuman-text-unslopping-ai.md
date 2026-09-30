---
layout: post
title: "Towards RL for Superhuman Text: Unslopping AI"
date: 2026-09-29
description: Reinforcement Learning from eXpert-Aligned Rubrics
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://facebookresearch.github.io/RAM/blogs/unslop/"
institutions: [Meta]
paper_date: 2026-09-28
---

Trying to make AI write better using RL on rubrics which themselves are evolved

Training process:

1. meta-optimize a rubric by having an LLM score the human and model generated writings according to the rubric, and while model scores higher than human, show the LLM the most wrong assessment pairs, and tell it to revise the rubric.
2. RL the writer LLM against this rubric
3. Generate completions from the writer LLM, and repeat

It's like RL with adversarial rubrics

# Data

Need many samples of expert human writing.

**Papers**: 561 papers + 90 validation from S2ORC, hold out abstract, intro, related works, or conclusion one at a time, have the model complete it given the rest of the paper.

Detail: they tell the model how long to write roughly

**Books**: Continue from a scene. Filtered for

- quality: in a Pulitzer or Nobel Prize winning book
- memorization: they do some checks to make sure that the model hasn't memorized the book

**Wikipedia**: Write the body section of a Wikipedia article from only the title and section heading.

- also filtering for quality, memorization

# Evaluations

**Final rubric score**: They try to measure validation performance by using a different judge (GPT-5.6) to grade by the rubrics, and the average of the 3 rubrics used during each of the 3 steps. Obviously, though, they're still going to be overreporting a little bit because they trained on a similar metric.

**Human evaluation check** Standard

### Eval for the rubric: Better human writing is scored higher on the rubrics than worse human writing

they took low, medium, and high quality papers

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790749357818.png)

# Preliminary Experiments

**Optimizing the rubrics is necessary**: The LLM judges by default's preferred model responses (left), and initial rubrics that the LLM comes up with actually prefer the model responses (middle)

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790744724989.png)

**Optimizing the rubrics works** The rubrics caused the judges to now prefer the human responses over the model ones

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790744784422.png)

The prompts themselves also seem reasonable according to the authors

- sectional ownership (i.e., not a miniature of the whole paper), disciplined selection, economy, and precise on-scope detail rather than breadth of coverage

# Experiments and Results

## Main experiment

3 iterations of RL-XAR on papers, 1 for stories and wikipedia

Qwen3.5-27B as the writer being RL'd, Qwen3.8-2.4T-A95B as the judge during RL, Kimi K2.6 or Muse Spark 1.1 for the meta optimizer

Papers: beats Opus 5.5

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790749184812.png)

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790748706116.png)

- left: baseline abstract
- right: RL-XAR abstract, it's noticeably better

Story writing does as well, Wikipedia writing kind mid (they say it's the hardest / their training judge wasn't capable enough)

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790749216913.png)

## Ablations

### Judge needs to be smart enough

Weaker judges can't tell the difference between humans and the model, even given the rubric

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790749272251.png)

### Rubric meta-optimizer needs to be smart enough

Opus and Kimi both produced meta prompts at some point which had a positive gap, Muse didn't

![](/assets/img/distillations/towards-rl-for-superhuman-text-unslopping-ai/img-1790749298020.png)

### Misc

Iterative RL does help

- can even do the rubric updating fully online, future work

Rubrics generalize across judges

Without length constraints, judges prefer longer responses
