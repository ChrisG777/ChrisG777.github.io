---
layout: post
title: 'Ambient Diffusion Omni: Training Good Models with Bad Data'
date: '2025-11-17'
description: diffusion using low quality data
tags:
- partial-read
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2506.10038
institutions:
- MIT
paper_date: '2025-06-10'
---

- we have a lot of low quality data, don't want to just throw it away, but when you train on it, it's very easy to learn poor performance things
- observation: when you add enough noise to low quality data, it's undifferentiable from if you added that noise to high quality data
- train diffusion model but only using the low quality data in cases where enough noise was added

then, the really wonky thing: use the model to predict the original versions of the noised low quality data, and then train again on this version of the data
- you're not creating new data, but this actually helps the optimization dynamics, makes it easier to learn than noisy data
- can repeat this multiple times and still improve

how to differentiate low from high quality data in the first place? train a classifier / use a VLM
