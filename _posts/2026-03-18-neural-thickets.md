---
layout: post
title: 'Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights'
date: '2026-03-18'
description: neural thickets
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2603.12228
institutions:
- MIT
paper_date: '2026-03-12'
---

For larger scale models, if you literally just add noise to the weights after pre-training, You have a high chance of landing on a specialist set of weights that are good at one particular downstream task (Figure 2 below)

- Sort of implies that the post-training algorithm use is not that important.

![](/assets/img/distillations/neural-thickets/img-1774379465422.png)
- Figure 2: very specific to larger scale


![](/assets/img/distillations/neural-thickets/img-1774379486728.png)
- Figure 3: Further evidence that for smaller scale models, you get much less diverse and interesting/good models by perturbing your weights.

![](/assets/img/distillations/neural-thickets/img-1774379542972.png)
- Figure 4: These models are actually specialists; they're not generalists

They boost performance by literally just sampling the top fifty, such randomly chosen models, and then taking a majority vote/ensembling from them (RandOpt)


![](/assets/img/distillations/neural-thickets/img-1774379576893.png)
- Figure 9: The weights in the thickets could improve both reasoning performance and just getting the answer output right.