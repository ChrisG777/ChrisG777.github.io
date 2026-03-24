---
layout: post
title: Tutorial on Diffusion Models for Imaging and Vision
date: "2026-02-12"
description: Tutorial on diffusion models
tags:
  - partial-read
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2403.18103
institutions:
  - Purdue
paper_date: "2025-01-08"
---

Skipping the first two sections for now

### Section 3: score-matching langevin diffusion

![](/assets/img/distillations/tutorial-on-diffusion-models/image157.png)

- langevin equation is just gradient ascent on the log likelihood of the distribution + noise

How do you estimate the score function? Turns out trying to optimize it directly is quite hard. But through some logarithm derivative magic, you can show that the objective for minimizing L2 loss directly Is up to a constant the same as the objective for predicting the conditional score or something.
![](/assets/img/distillations/tutorial-on-diffusion-models/image158.png)![](/assets/img/distillations/tutorial-on-diffusion-models/image159.png)

In the denoising score matching objective, if you choose a Gaussian noise, does give you something tractable.
![](/assets/img/distillations/tutorial-on-diffusion-models/image160.png)

So then you just run Langevin Diffusion with various noise levels.

### Section 4 SDEs

Any iterative algorithm can be converted to an ODE by just letting x_i \= x(t + ∆t) and x\_{i-1} \= x(t), and then you also have to make your learning rate a continuously evolving function of time
