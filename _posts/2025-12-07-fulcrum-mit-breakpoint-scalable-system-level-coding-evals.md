---
layout: post
title: "Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents"
date: "2025-12-07"
description: Breakpoint
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2506.00172
institutions:
  - MIT
  - Fulcrum
paper_date: "2025-05-30"
---

Goal: automated way to create a benchmark where you get to tune the difficulty of the long-term system-level coding

Method: took existing codebases, and either

1. removed a function (local-level change)
2. corrupted a function, and didn’t tell the LLM which function
3. corrupted multiple functions, and didn’t tell the LLM which

How difficult a function is is based on its \# lines of code and cyclomatic complexity
How difficult a corruption is is based on its harmonic distance from the rest of the code base through function call graph

Results:

- Only for function removal: higher \# lines of code and lower harmonic distance are harder to reconstruct
- for corruptions, bottleneck seems to be in finding which function to fix
- scaling test-time compute (\# submissions to test cases) improves both local and system level fixing, but mostly only up to 2 submissions
- Use the Mann-Whitney U test to determine that reasoning mostly helps local, not system level, scaling ttc helps both
