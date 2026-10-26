---
layout: post
title: "IdeaLens: Detecting AI Ideas in Long-form Writing"
date: 2026-10-20
description: "IdeaLens, detecting AI ideas "
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2610.06778"
institutions: [UMD, GDM, Simon Fraser University]
paper_date: 2026-10-05
---

They differentiate between AI-written vs AI ideas (where ideas is just operationalized as the outline from which the story is continued)

This is something I’ve been thinking about a lot, since I right now it’s somewhat of a negative signal to produce anything ai-sounding because you get lumped together with people who don’t put any thought in. But with something like IdeaLens instead, you could just differentiate out the people who don’t think about what they’re doing

![](/assets/img/distillations/idealens-detecting-ai-ideas-in-long-form-writing/img-1792511132611.png)

- they train on paraphrased outlines to predict whether it came from a human or AI, that way the model is forced to use the ideas (outline) instead of the style (the style is paraphrased by gemini for both AI and humans)
- don't know why they don't paraphrase at test time

![](/assets/img/distillations/idealens-detecting-ai-ideas-in-long-form-writing/img-1792511094068.png)

- results: Pangram and models trained on just the prose can't differentiate ideas
- their contribution to the dataset is having AI generate the story outline and the human wrote the rest, upper right quadrant

# analysis of AI vs human ideas

AI ideas are

1. they’re overly general
2. they overclaim

![](/assets/img/distillations/idealens-detecting-ai-ideas-in-long-form-writing/img-1792511390460.png)
