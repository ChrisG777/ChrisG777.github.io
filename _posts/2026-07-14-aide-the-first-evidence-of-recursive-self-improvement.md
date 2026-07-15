---
layout: post
title: "AIDE²: The First Evidence of Recursive Self-Improvement"
date: 2026-07-14
description: RSI ish
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.weco.ai/blog/first-evidence-of-recursive-self-improvement"
institutions: [Weco]
paper_date: 2026-07-14
---

Some good ideas on evaluating an autoresearch harness:

- first order generalization = new tasks in a task family you already optimized for
- Second order generalization = new task family altogether. They could do this because they were training general harnesses on three different tasks (mle bench, atcoder, harness engineering), but it probably wouldn't work very well for us since we're fitting to just one task. It's pretty impressive to me though that they managed to not overfit while only using three distinct task families.

Results wise, it seems not significantly better (but maybe faster once everything is set up) than human iterating on the harness, I.e. on MLE-bench lite which their AIDE_human is actually tuned for, it barely beats AIDE_human. Only 7 accepted changes to the harness. And reportedly the code it writes sucks

They were also token constrained, like they used gemini 3 flash for the inner optimization, so the agent optimized token usage
Still pretty cool proof of concept
