---
layout: post
title: "Gated Delta Networks: Improving Mamba2 with Delta Rule"
date: 2026-09-11
description: Gated DeltaNet
tags: [partial-read]
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2412.06464"
institutions: [MIT, Nvidia]
paper_date: 2025-03-06
---

Mamba2 has gating in order to let the matrix state $S_t$ forget things

- <img src="/assets/img/distillations/gated-delta-networks-improving-mamba2-with-delta-rule/img-1789177056860.png" width="486" />

DeltaNet was the $S_t$ as an associative key-value store update

- <img src="/assets/img/distillations/gated-delta-networks-improving-mamba2-with-delta-rule/img-1789177146057.png" width="411" />

Gated DeltaNet just combines both

- <img src="/assets/img/distillations/gated-delta-networks-improving-mamba2-with-delta-rule/img-1789177166331.png" width="424" />

That's all. Also they intersperse sliding window attention layers
<img src="/assets/img/distillations/gated-delta-networks-improving-mamba2-with-delta-rule/img-1789177198024.png" width="734" />
