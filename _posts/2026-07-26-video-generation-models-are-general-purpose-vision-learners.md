---
layout: post
title: Video Generation Models are General-Purpose Vision Learners
date: 2026-07-26
description: GenCeption
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://genception.github.io/assets/paper.pdf"
institutions: [GDM]
paper_date: 2026-07-13
---

Comparing the three recent GDM papers on solving vision pretraining

![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785102908054.png)

- For Vision Banana, they wanted the model to still be able to generate images normally, hence, instruction tuning and framing the tasks as image generation.
  - In contrast, for GenCeption, multi-task post-training lets them have one-step forward inference passes, but they lose the ability to generalize to complex text task inputs, or to generate videos. They still get some generalization within the family of tasks that they post train on.
- The other video one is **zero-shot** prompting so it's more of a demonstration that video generation model priors are good
