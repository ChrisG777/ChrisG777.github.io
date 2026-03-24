---
layout: post
title: Generative Modeling by Estimating Gradients of the Data Distribution
date: "2025-12-25"
description: score function generative modeling
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://yang-song.net/blog/2021/score/
institutions:
  - Stanford
paper_date: "2021-05-21"
---

I’ll refer to the ICLR Diffusion explained blogpost for the motivations of score based modeling

The idea is that the objective we want to solve is to minimize the fischer divergence
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image95.png)
but we have ways of minimizing this without access to the true score values

![](/assets/img/distillations/yang-song-score-based-generative-modeling/image96.png)
The problem is that the learned score function might be inaccurate in regions of low density

→ this motivates perturbing the data with noise, and training score based models on the noised data instead, which has less low density regions

- this trades off corrupting the data with getting a better score estimate

Idea: use many different noise amounts, and train a noise conditional score-based model to predict all of them
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image97.png)
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image98.png)
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image99.png)
minimize the weighted sum of the Fisher divergences for the different noise scales

then to actually sample, use annealed Langevin dynamics: basically do the reverse langevin diffusion using decreasing noise scales

### SDEs

Idea: take the number of noise scales to go to infinity, so that you have the pdfs p_t(x) for t \\in [0, T] continuously

- p_0(x) \= p(x) is the data distribution
- p_T(x) is pure noise

![](/assets/img/distillations/yang-song-score-based-generative-modeling/image100.png)
general form of an SDE

- dw is brownian motion
- in practice, you hand design the SDE. The SDE is part of the model, and it dictates how you add noise

Any SDE has a reverse SDE
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image101.png)
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image102.png)

- notice the score function popping out

once again, we train a time dependent score function based on a weighted fisher divergence
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image103.png)
When you choose lambda(t) \= g^2(t), you actually get that this is an upper bound to the KL divergence between p_0(x) and p_theta(x)\!

use numerical solvers to solve the reverse SDE for sampling.

### Probability Flow ODE

Problem: with SDEs, we can’t compute the exact log likelihood of an x_0

You can convert any SDE into an ODE (difference is an ODE is deterministic) that has the same marginals ![](/assets/img/distillations/yang-song-score-based-generative-modeling/image104.png)(no guarantees about the trajectories, i.e. as you vary t continuously, but same marginals yes).
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image105.png)
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image106.png)
And then since this becomes a neural ODE / continuous normalizing flow when you plug in the approximation s_theta(x, t), you can use numerical ODE solvers to compute the p_0 likelihoods.

### Controllable generation

Bayes Rule for score functions
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image107.png)
Have the first term on the right by score matching, and the second term they lowkey seem wrong about how you can get it. I feel like I like the lil log explanation of conditional diffusion more.

What is this useful for?
![](/assets/img/distillations/yang-song-score-based-generative-modeling/image108.png)

- class conditional image generation

![](/assets/img/distillations/yang-song-score-based-generative-modeling/image109.png)

- image inpainting

![](/assets/img/distillations/yang-song-score-based-generative-modeling/image110.png)

- image coloration (hey wait a second that looks somewhat similar to what I’m doing for my UROP uh oh)

### Connection to diffusion models

on the surface, seems like they’re different because

- score based models are trained by score matching and sampled by Langevin dynamics, while
- diffusion models are trained by ELBO and sampled with a learned decoder

but turns out the ELBO loss is equivalent to the weighted fisher divergence objective

different perspectives of the same model family
