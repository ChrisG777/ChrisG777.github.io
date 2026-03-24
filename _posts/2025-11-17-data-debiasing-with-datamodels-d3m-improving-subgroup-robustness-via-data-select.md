---
layout: post
title: "Data Debiasing with Datamodels (D3M): Improving Subgroup Robustness via Data
  Selection"
date: "2025-11-17"
description: Debiasing data using TRAK
tags:
  - partial-read
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2406.16846
institutions:
  - MIT
paper_date: "2024-06-24"
---

- problem: data bias can cause worse performance on specific groups. Normal debiasing methods just remove data, which isn't ideal.
- used predictive data attribution method (TRAK) to figure out which data points contribute most to the worst group's performance on a small validation dataset, just get rid of those data points
- this paper seems mostly just like an application of TRAK
