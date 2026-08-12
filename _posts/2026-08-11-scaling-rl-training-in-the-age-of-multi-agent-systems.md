---
layout: post
title: Scaling RL training in the age of multi-agent systems
date: 2026-08-11
description: Raymond Feng AC2
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.appliedcompute.com/platform/scaling-rl-training-multi-agent-systems"
institutions: [Applied Compute]
paper_date: 2026-07-28
---

This is more of an engineering paper from what I can tell.

Recall that from REINFORCE, the gradient of the loss is like

<img src="/assets/img/distillations/scaling-rl-training-in-the-age-of-multi-agent-systems/img-1786496532936.png" width="173" />

We can split this loss up into per-token loss terms log pi_theta (y_t | x, y_<t). Hence, in normal RLVR, you're supposed to have a loss term per token outputted by the agent
![](/assets/img/distillations/scaling-rl-training-in-the-age-of-multi-agent-systems/img-1786496601716.png)
(i.e. the 1's here)

But during inference time, it's possible that your agent will do things (e.g. compaction, subagents, transient messages) that doesn't involve a monotonically increasing prefix of messages, so that applying a loss mask directly doesn't work. Their solution to this is **episode-level tracking**:

"For each task, we keep track of a list of episodes which are append-only sequences of messages; these episodes are first class platform primitives that together can be thought of as a single trace. These episodes preserve the full expressibility of all possible harnesses — harnesses which require forking or modifications of previous messages simply need to start new episodes for each instance of forking or message mutation."

![](/assets/img/distillations/scaling-rl-training-in-the-age-of-multi-agent-systems/img-1786496741766.png)

and wow now your infra is perfectly set up for RL.
