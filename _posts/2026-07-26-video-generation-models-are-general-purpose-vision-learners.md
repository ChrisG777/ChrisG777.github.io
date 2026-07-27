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

Summary: _Use a pre-trained video DiT model as a backbone for its rich spatiotemporal feature priors, and then post-train it on various vision tasks which are encoded in a unified task format that makes as few changes as possible from the DiT_

Comparing the three recent GDM papers on solving vision pretraining

![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785102908054.png)

- For Vision Banana, they wanted the model to still be able to generate images normally, hence, instruction tuning and framing the tasks as image generation.
  - In contrast, for GenCeption, multi-task post-training lets them have one-step forward inference passes, but they lose the ability to generalize to complex text task inputs, or to generate videos. They still get some generalization within the family of tasks that they post train on.
- The other video one is **zero-shot** prompting so it's more of a demonstration that video generation model priors are good

# Methods

![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785118559496.png)
**Turning the pretrained DiT into a (single-step) feature encoder**:

- Instead of noisy video latents, they use the input video latents
- t = 0 conditioning (matching the fact that it's already a clean video, t=1 would be noise)
- they negate the output? so that it predicts $$x_0 - \epsilon$$ instead of $$\epsilon - x_0$$? It seems like an engineering hack.

**Similar to how LLMs treat everything as text, they treat most dense vision tasks as an RGB output and use L2 pixel loss**

- ![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785118916520.png)
- Have to do some goofy shit to project 6-channel outputs into 3 channels, and for single-channel outputs, they are replicated across the RGB.
- Predicting in continuous pixel space lets them best leverage the pre-trained model's priors
- need to standardize the data carefully

**sparse tasks come from the output of the learnable tokens (query embeddings)**

- spatial location in 3D RoPE is learned (temporal position is calculated somehow)
- MLP to the final K-dim output per learned token is also learned

**Synthetic Data from Simulation (RenderPeople, CMU Motion Dataset, Blender)**

- as a bonus, gives them the ground truth for their like keypoint tasks and stuff for free

# Experiments

WAN 2.1

All the standard benchmarks

## Ablations

Joint vs Specialist training:

![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785120501519.png)

- worse for the sparse output task --> try to modify the arch as little as possible

![](/assets/img/distillations/video-generation-models-are-general-purpose-vision-learners/img-1785120617686.png)
VideoMAE and V-JEPA suck as backbones, and they can't take text-conditioning?

Emegent Behaviors:

good on real videos (only trained on synthetic)
multiple objects (only trained on single object)
animals (only trained on humans)
