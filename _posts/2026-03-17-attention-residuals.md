---
layout: post
title: Attention Residuals
date: "2026-03-17"
description: attention residuals
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2603.15031
paper_date: "2026-03-16"
---

![](/assets/img/distillations/attention-residuals/image263.png)

- Standard residual connection only uses the output from the previous layer
- As layers go on, this means that later layers can have less and less effect on the residual stream, since it grows as O(L), and the gradients accumulate and are largest at layer zero.
- It's sort of the RNN problem of trying to compress each layer's information into only a single hidden vector.

![](/assets/img/distillations/attention-residuals/image264.png)

- So instead, do softmax attention over the previous layers’ outputs

The attention and weights are determined as follows:
![](/assets/img/distillations/attention-residuals/image265.png)

- The RMS norm is to make it so that layer outputs that have large magnitudes don't dominate the attention.
- The pseudo query labels are learnable weights.

Blocked version: full layer version is best but uses O(Ld) memory, and communication costs get too high. Block layers together into N blocks, N \< L, using O(Nd) memory
![](/assets/img/distillations/attention-residuals/image266.png)

- Each layer can pay attention to the output of the previous blocks, as well as the prefix sum of the current block's layers.

![](/assets/img/distillations/attention-residuals/image267.png)

- Figure 5: Solves the layer output magnitude problem in the gradient problem I mentioned earlier and gets better validation loss than using the normal residual connections.

![](/assets/img/distillations/attention-residuals/image268.png)

- Figure 8: Most of the layer attention is still paid to the current layer and to the original embedding layer, But there are some pretty strong skip connections.
