---
layout: post
title: Boomerang Distillation Enables Zero-Shot Model Size Interpolation
date: "2025-11-16"
description: Boomerang Distillation
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2510.05064
institutions:
  - Harvard
paper_date: "2025-10-06"
---

aim: interpolate models from a teacher size down to a small student size without having to retrain the model.

method:

1. initialize the model through layer pruning, i.e. keep every other layer of the teacher model (with the weights), make sure to include the first (embedding) and last (head) layers. More generally, for a block of layers in the teacher model, keep just the first layer in the student.
2. train the student using cross entropy loss + KL of predictions at each token from teacher + cosine similarity of each hidden dim from the corresponding output of the block of layers that we took the student layer from.
3. now directly sub back in teacher blocks for individual student layers

models used were qwen3, llama 3, and pythia6.9b.

Boomerang distillation phenomenon mostly refers to step 3 working. They claimed that for this to happen, you need the model to be retrained after you prune layers, and initialized with the same teacher weights. Surprisingly though, you can actually get away somewhat fine without the KL and cosine similarity regularizer terms keeping you close to the teacher (though perplexity does go up a bit)

- in particular, this means that boomerang distillation works on DistilBERT and other distilled off the shelf models

Results:
metrics were perplexity, and downstream classification/generation.

- Does much better than other simple prune away layers interpolation strategies
- Does equal or **even better** than pruned models with the same layers but retrained under the same knowledge distillation loss\! Authors conjecture this is due to catastrophic forgetting.

Appendix:

for llama 3, they kept the first two teacher layers instead of just the first one, because they noted that there was still high cosine similarity between the first student layer and the first two teacher layers
