---
layout: post
title: Reasoning or reciting? Exploring the capabilities and limitations of language
  models through counterfactual tasks
date: '2025-11-11'
description: Reasoning or Reciting
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2307.02477
institutions:
- MIT
paper_date: '2024-03-28'
---

basically designed a bunch of counterfactual versions of simple tasks that require the same type of reasoning (e.g. base 9 addition vs base 10), and found that LLMs do better at the original one, concluded that LLMs are just recognizing familiar problems instead of learning abstract reasoning. LLM does better at base 8 and base 16 than base 9 further helps this, as there's a continuum of familiarity instead of just one counterfactual

used a simple task on the counterfactual to show that the model could understand the counterfactual.

they have a section in their paper saying like "isn't this obvious?" which I thought was kind of funny and apt. 
