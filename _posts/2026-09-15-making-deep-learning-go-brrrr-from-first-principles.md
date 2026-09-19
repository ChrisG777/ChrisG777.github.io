---
layout: post
title: Making Deep Learning Go Brrrr From First Principles
date: 2026-09-15
description: Making Deep Learning Go Brrrr From First Principles
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://horace.io/brrr_intro.html"
institutions: [Meta]
paper_date: 2022-03-15
---

Why do we want to be compute-bound? Because the amount of compute that we have to do in a forward path of the model is irreducible, so the fastest that we can possibly go is (FLOPs) / (# gpus * GPU compute speed)

Can minimize Python overhead by using more just-in-time techniques or cuda graphs or smth
