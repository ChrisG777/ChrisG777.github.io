---
layout: post
title: 'To Backtrack or Not to Backtrack: When Sequential Search Limits Model Reasoning'
date: '2025-11-15'
description: Backtracking vs Best of n
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2504.07052
institutions:
- Harvard
paper_date: '2025-04-09'
---

(aka reasoning vs direct)

Claim: backtracking and best of n can both be better than the other in different circumstances.

Showed that in CountDown, backtracking worse, while in Sudoku, backtracking is better.

I'm not super convinced. In their example of best of n beating backtracking in CountDown, it was mostly because the way they generated the reasoning traces using a DFS algorithm that just didn't get 100% on the training set, so their backtracking algorithm was capped at the performance of this DFS.
- tbf, they did show that you can improve performance by skipping some states in the trace, I guess more verbose CoT not being necessarily more useful is interesting, like force the model to think more instead

other interesting point though was that backtracking/reasoning requires quadratic in context length, while parallel sampling is just linear.

When they used GRPO on the two algorithms
- the direct model just started passing in one try on everything that might've taken it like k shots before. But you **lose model output diversity**, which is a very predictable and repeated lesson, same as that AI@MIT reading group talk
- the backtracking models just got better, and continue to do better as you scale the test time tokens. This makes sense -- you're unshackling it from the bad dfs traces (they proved this by showing jaccard similarity with the dfs traces decreased) , and the lack of model output diversity is no problem because you're just sampling one output.

trained really small qwen models from scratch for this like 30 M params.
