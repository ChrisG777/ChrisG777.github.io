---
layout: post
title: Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis
date: 2026-07-26
description: "Self-Flow, FLUX 3"
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://bfl.ai/research/self-flow"
institutions: [BFL, Antonio Torralba]
paper_date: 2026-03-04
---

prior work: **REPA**: Align diffusion models' internal representations with DINO's, since diffusion models don't learn semantic representations well on their own.
- con: this depends on an external model, scales poorly


Self-Flow: noise some tokens asymmetrically, align representations of the noisy tokens with the clean ones in addition to the generation objective
![](/assets/img/distillations/self-supervised-flow-matching-for-scalable-multi-modal-synthesis/img-1785120722714.png)

**Making it multimodal**:
- per-modality in/out projection layers, autoencoder
  - FLUX.2 AE for images, WAN2.2 for video, Songbloom for audio
- hparams like noise scheduling (same level of noise is harder to predict for images than video bc more info with video)  / batch size
- vector timestep conditioning
