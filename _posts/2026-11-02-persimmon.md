---
layout: post
title: Persimmon
date: 2026-11-02
description: persimmon
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://persimmon.humansand.ai/blog/"
institutions:
  - "humans&"
paper_date: 2026-09-10
---

What do you want in a human conversation simulation model?

Persimmon is Nemotron Ultra 550b, mid-trained on some conversation data and maybe post trained

1. It should be hard to distinguish between the simulation model and a real human (AI judge, pangram)

![](/assets/img/distillations/persimmon/img-1793649910991.png)

![](/assets/img/distillations/persimmon/img-1793649934055.png)

2. The model should reveal information over time at roughly the same rate as a human

![](/assets/img/distillations/persimmon/img-1793649977053.png)

3. Humans actually don't keep a coherent conversation for a very long time, unlike most frontier models

![](/assets/img/distillations/persimmon/img-1793651112475.png)
