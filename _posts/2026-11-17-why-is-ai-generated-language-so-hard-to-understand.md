---
layout: post
title: Why is AI-generated language so hard to understand?
date: 2026-11-17
description: AI slop linguistic analysis
tags: [partial-read]
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2610.29162"
institutions: [NYU]
paper_date: 2026-10-21
---

Tldr so far is just that there’s a bunch of linguistic structures like using animated verbs with inanimate objects “this bug will bite later” that LLMs use a lot more than when their output is sent through an old-school translator to Japanese and back (so that it’s more human writing)

- for normal chat, essay-writing, and coding settings

![](/assets/img/distillations/why-is-ai-generated-language-so-hard-to-understand/img-1794963760244.png)

In aggregate, this is how different models do
![](/assets/img/distillations/why-is-ai-generated-language-so-hard-to-understand/img-1794963777554.png)

They have some very toy RL setup where they RL with a length penalty on the output on tasks with these possible linguistic shortenings, and find that the model learns to take the shortenings.

Thomas Hikaru Clark told me that there's a lot of cognitive science literature on models that approximate humans (like the Centaur model whatever that is), thinks that training with the frozen reader model is an interesting idea. I have his email in my photos
