---
layout: post
title: Teaching AI to see the world more like we do
date: '2025-11-12'
description: Deepmind Align Vision Representations
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://deepmind.google/blog/teaching-ai-to-see-the-world-more-like-we-do/
institutions:
- Google DeepMind
paper_date: '2025-11-11'
---

AI fails to capture hierarchical higher order vision knowledge.

To better align representations with humans, focus on the odd one out task, where humans differ from computers
- problem: not enough labeled human data
- solution: train a large vision model with an adapter to predict human labels from the limited data. This large vision model won't overfit / forget because it's just an adapter
- now use the fine tuned large vision model to generate a large amount of labeled image sets, acting as the human labeler.
- then fully fine tune student models on this dataset, letting them restructure their internal weights

find that representations separate out entities that intuitively should be separated, also generalizes better to distribution shift and new categories

This is cool, but it seems like the main actual innovation for better alignment is this odd one out dataset, and “aligning” just means fine tuning models to perform well according to human labels on this task, which the main bottleneck is that we don’t have enough data, so we use a big LLM with adapters to simulate human labelers

My initial question was if this big LLM with adapters can already simulate human labelers, why even bother with generating the big dataset and fully fine tuning? And the answer is that we want to do the full fine tune in order to allow the model’s base level representations to actually change (lora adapters don’t do this) but to do a full fine tune we need a lot more data
