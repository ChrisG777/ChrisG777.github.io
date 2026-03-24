---
layout: post
title: Curiosity-driven Red-teaming for Large Language Models
date: "2025-11-18"
description: Curiosity Driven Red Teaming
tags: []
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2402.19464
institutions:
  - MIT
paper_date: "2024-02-29"
---

setup: in red teaming, we train a policy to generate test inputs, which when passed to the target LLM, will result in a toxic output (as measured by a different LLM)

problem with normal RL: test case diversity is low. Just keeps generating the same poison test cases, but missing many bad test cases x.

solution: in addition to normal reward and KL term in RL, add 2 diversity terms

- positive entropy of the policy's outputs (in terms of generating x's)
- self-BLEU to all the x's generated during training time (textual similarity to pre-existing test cases)
- cosine similarity of embedding to existing test cases.

I thought if you have diversity of outputs, then you don't need to also ensure high entropy, but they ablated it so I guess it helps as well idk

both of these measures of diversity are explained further below

Results:

- diversity is measured in two ways 1\. literal text diversity through Self-BLEU score, which is basically n-gram matches 2\. semantic diversity from cosine similarity of sentence embeddings
- they increase diversity on other methods (they think some of the methods have a failure mode where they output test
- but the % probability of the outputs being toxic isn't the highest, so there is a tradeoff.
