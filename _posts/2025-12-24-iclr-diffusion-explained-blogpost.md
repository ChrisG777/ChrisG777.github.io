---
layout: post
title: Building Diffusion Model's theory from ground up
date: '2025-12-24'
description: ICLR Diffusion explained blogpost
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://iclr-blogposts.github.io/2024/blog/diffusion-theory-from-scratch/
institutions:
- Surrey
paper_date: '2024-05-07'
---

We need to be able to sample from a generative model p\_theta(x) that approximates q\_data(x)
![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image44.png)
the **score** function of the data distribution interests us

- compared to q\_data(x), we think it might be tractable because the normalization term dies

### Generate a new sample, assuming we know the score function perfectly

![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image45.png)
if we just naively optimize it through gradient descent, we’ll only go towards the peaks of the distribution
![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image46.png)
![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image47.png)
but **langevin** proved that if we follow this and add a little bit of noise at each step (B\_t \= brownian motion \= N(0, dt)), then we do end up sampling from q\_data(x)

**Fokker-Planck** equation (only helpful in theory): shows how the probability distribution p\_t(x) evolves over time; at t \= infty, it becomes q\_data(x)
![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image48.png)
shows that we can start from any initial distribution p\_0, and following langevin sampling transforms us to q\_data

### Estimating the score function

![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image49.png)
estimating the score function directly as s\_theta(x) isn’t expressive enough
provide the time t as well, s\_theta(x\_t, t) is probably sufficient

but how do we get samples? Going from t=infty q\_data(x) to t=0 N(0, I) : forward diffusion process\!
![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image50.png)

- the score function of the normal is really nice
- ![](/assets/img/distillations/iclr-diffusion-explained-blogpost/image51.png)
- discretize the equation
- ![](/assets/img/distillations/iclr-diffusion-explained-blogpost/img-1774303493995.png)
- and then transform the time to go from [0, 1] instead of [0, infty]
- can do multiple forward steps at once

Ok, so now we can get samples from each time step t where we want to learn the score function. That still begs the question — how can we learn the score function without having the true score values?

![](/assets/img/distillations/iclr-diffusion-explained-blogpost/img-1774303604785.png)

- from a noisy sample, learn the original clean sample
- this somehow learns the score
- ![](/assets/img/distillations/iclr-diffusion-explained-blogpost/img-1774303553907.png)
- another interpretation of this same objective: given noisy sample, it’s learning the expected direction of the noise that was added to get this sample

There’s another interpretation with Tweedie’s formula (but lowkey 6.7810 probably did that better)

There’s a whole other interpretation of diffusion models that doesn’t go through SDEs at all.
