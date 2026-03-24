---
layout: post
title: Continuous Language Model Interpolation yields Dynamic and Controllable Text
  Generation
date: "2025-11-23"
description: continuous model interpolation with lora
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2404.07117
institutions:
  - Harvard
paper_date: "2025-08-28"
---

Goal: want to be able to customize a model for different styles / output traits at inference time without retraining / doing multiple rounds of inference

Solution: train one lora adapter for each sliding control of the trait that you’re looking at (e.g. politeness, simplicity, etc). Then take a weighted combinations of these lora adapters: first, an average of (most impolite lora) to (most polite lora) etc, then a weighted average of the loras between different traits

Evaluations: RoBERTa fine tunes.

- each trait in isolation: fine tuned models on different data mixtures alpha of + the trait and - the trait (e.g. 0.1 data impolite, 0.9 data polite)
- metric: an LLM classifier’s probability of the output having that trait (Attribute Score)
- Compared the attribute score for the interpolation with factor alpha to the fine tuned model with data mix alpha

Interesting finding with looking at multiple traits: taking weighted averages of the LoRA’s didn’t really cause any interference between the traits (attribute scores went as you imagined them to). Implies that the LoRA’s are mostly orthogonal
