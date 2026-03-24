---
layout: post
title: On scalable oversight with weak LLMs judging strong LLMs
date: '2026-01-06'
description: GDM scalable oversight
tags:
- partial-read
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2407.04622
institutions:
- Google DeepMind
paper_date: '2024-07-05'
---

I did not actually finish reading this paper, but the idea was that we’re trying to figure out how a dumb human can get an answer from a possibly lying superhuman AI. Except for now, we’re simulating the dumb human (“judge”) with a weak LM, and the superhuman AI with a stronger LM

![](/assets/img/distillations/gdm-scalable-oversight-with-weak-llms-judging-strong-llms/img-1774305073537.png)

Two types of information asymmetry:

1. extractive: the information is in some text somewhere that the LMs have access to but the judge doesn’t
2. reasoning: the problem is some hard math/code problem and requires difficult reasoning to solve. Only the strong LMs can figure out the answer

Experiments using just a single AI, or with two AI’s debating different answers. Found that debating helped get to nearly information symmetry in the extractive case, but that debate didn’t really help when the problem was just too hard for the weak judge. GG
