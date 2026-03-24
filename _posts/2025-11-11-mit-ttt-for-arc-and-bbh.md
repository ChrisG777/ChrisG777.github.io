---
layout: post
title: The Surprising Effectiveness of Test-Time Training for Few-Shot Learning
date: '2025-11-11'
description: TTT for ARC and BBH
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2411.07279
institutions:
- MIT
paper_date: '2024-11-11'
---

- TTT has same setup as in context learning, except you actually update the params of a lora adapter. For the dataset, use leave-one-out versions of your K examples (i.e. give it K-1 and have it predict the output of the Kth), and for the loss, include having it predict the given demo outputs. Note that this is not the obvious thing of just training on each of the K examples as the inputs and outputs.
- augmented inference: if you have invertible transformations of your data, you can use that to generate several outputs, and then have hierarchical voting (vote within transformation group, and then have a global vote) is apparently better than flat voting
