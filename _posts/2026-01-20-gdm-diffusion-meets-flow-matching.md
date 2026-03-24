---
layout: post
title: 'Diffusion Meets Flow Matching: Two Sides of the Same Coin'
date: '2026-01-20'
description: Diffusion equals Flow Matching
tags:
- partial-read
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://diffusionflow.github.io/
institutions:
- Google DeepMind
paper_date: '2024-12-02'
---

Diffusion forward process
![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/image161.png)

Diffusion reverse process: estimate either x or epsilon, derive the other one from this equation, and then do the forward pass to an earlier time step s \< t using your estimates
![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/image162.png)

- if your network output is xhat, then
  - ![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/img-1774307769113.png)
  - ![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/image166.png)
  - can do a similar looking reparameterization if your network output is the noise, or even epsilon - x (the flow vector)

Flow matching forward process
![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/image167.png)

Flow matching reverse process

* u \= epsilon - x is the velocity
* ![](/assets/img/distillations/gdm-diffusion-meets-flow-matching/image168.png)
* estimate u, then use this to reverse to get z\_s
* if u \= epsilon - x is the network output, then

**I don’t understand the next part very well**

So the flow matching reverse process is actually the same as the reverse diffusion process with DDIM, if you do some reparameterization, and use an Euler sampler (i.e. taking linear steps).

1. Their comment 1 is saying that this Euler sampler has extra approximation error in addition to standard DDIM, whose only error comes from assuming that the network output will be constant throughout the trajectory
2. DDIM is scale invariant, but Euler sampler’s error depends on the scale or something.
