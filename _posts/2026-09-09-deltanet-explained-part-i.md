---
layout: post
title: DeltaNet Explained (Part I)
date: 2026-09-09
description: DeltaNet explained Songlin Yang Part 1
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://sustcsonglin.github.io/blog/2024/deltanet-1/"
institutions: [MIT]
paper_date: 2024-12-03
---

# Linear Attention

Get rid of the softmax:

(QK^T)V

for token t, writing out the summation

$\sum_{j=1}^t v_j (k_j^T q_t) = \sum_{j=1}^t (v_j k_j^T) q_t$

So you can define the running $S_t = \sum_{j=1}^t v_jk_j^T$ and have the update rule $S_t = S_{t-1} + v_tk_t^T$ and not have a KV-cache, just a fixed $d^2$ size state.

# DeltaNet

Linear attention kind of sucks at associative recall

You can think of the state $S_t$ as a key-value store, such that ideally $S_t k_t = v_t$.

One good interpretation of DeltaNet is that on each successive token, it's taking a gradient step wrt S to minimize $ L_t(S) = \frac{1}{2} \| S k_t - v_t \|^2$:

$\nabla L_t(S) = (Sk_t - v_t)k_t^T$:

$S_t = S_{t-1} - \eta_t (S_{t-1}k_t - v_t)k_t^T$

and somehow this is much better at associative recall
