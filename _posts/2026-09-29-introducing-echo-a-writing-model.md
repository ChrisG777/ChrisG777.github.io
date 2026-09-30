---
layout: post
title: "Introducing Echo, A Writing Model"
date: 2026-09-29
description: "Introducing Echo, A Writing Model"
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://echo.fulcrum.inc/"
institutions: [Fulcrum]
paper_date: 2026-09-30
---

Echo = post-trained Kimi K3, $4.5k

Echo is supposed to be good at writing in any persona

![](/assets/img/distillations/introducing-echo-a-writing-model/img-1790727529379.png)

- From looking at some qualitative examples, it's definitely better than GPT-6 Astra, and somewhat comparable to Opus 5.5

# SFT

They took blog posts written by specific authors, had Opus 5.5 create outlines out of those blog posts, and used SFT on the model with these outlines and the persona prepended to the blog post

- supposed to make the data more on policy

<img src="/assets/img/distillations/introducing-echo-a-writing-model/img-1790727758147.png" width="373" />

- Works better than SFT, I guess?

The results actually transfer well to authors who weren't trained on too, implying the persona matching ability generalizes

# Evaluation Metrics

Literally, just how much more likely does the SFT model think that the sequence is compared to the base model

![](/assets/img/distillations/introducing-echo-a-writing-model/img-1790727983065.png)

# RL

Mostly in order to get the author's voice on a variety of tasks, beyond just what they've written about. Uses the above token-level reward
