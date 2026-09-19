---
layout: post
title: Monitoring and Discovering Reward Hacking with Internal Representations during LLM Evaluations
date: 2026-09-18
description: Reward Hacking Probes
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2609.19101"
institutions: [Goodfire]
paper_date: 2026-09-16
---

TLDR: probes are competitive with LLM monitors at finding reward hacking

<img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789848754318.png" width="556" />

great figure 1

# Reward Hacking Analysis

Took Kimi K3, GLM 5.2, and Qwen3.8-Max (Super recent models at the time this paper is written. They started this research sometime between august 4 and august 14) and saw how much they reward hacked on coding benchmarks: SWE-bench Verified, DeepSWE, ImpossibleBench

- trying to look up the answer on the internet is considered reward hacking, and was the most common form of reward hacking

How did they get ground truth for reward hacking? Look for the different possible reward hack types manually. Then have an LLM judge go through the transcript and flag a message / tool call with a verbatim quote from the trace as evidence. Do 3 times for extra validation (all 3 times agreed like 96% of the time though anyways)

- more effective than a generic LLM monitor without the specific reward hacks in its prompt, or an agent monitoring itself after each turn
- ![](/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789757228312.png)

judge prompts in appendix C

# Probes

For a given token's given layer's residuals, take the difference-of-means vector of reward hacking vs non reward hacking examples

<img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789844636769.png" width="475" />

They construct P and N by creating **synthetic data** with matched pairs solving the same problem that (a) exhibit the reward hack (b) solve it for real

<img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789844846706.png" width="641" />

- why not use real data? they don't explain
- note that you have many different probes, one for each reward hacking type

"highly activating" is just any time you get a high cosine similarity to any reward hacking probe direction.

As you'd expect, logit lens on the direction yields "cheating", "hack", "illicit", etc, and steering in the direction makes it hack more
<img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789844873942.png" width="516" />

# Results vs LLM Monitor

Disclaimer: they buffed the probe a bit by choosing which of the probe vectors to use for each (dataset, LLM) by seeing which probe had the best performance on a held out set of rollouts. They claim the results are a little sensitive to this choice but not super sensitive

For a given false positive rate (what fraction of true negatives get classified as positive), how much true positive rate can we get

![](/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789848250186.png)

- probe is a curve because it's a continuous number for similarity, so you can choose the cutoff where you want, but the llm monitor is just binary
- probe combined with monitor in two ways: positives from probe are fed to the monitor and only positive if both say yes (in the limit, probe says yes to everything so it's just the monitor); either probe or monitor has to say yes (in the limit, probe says no to everything so it's just the monitor). Seems to bo better than probe alone in 7/9 cases
- Why not combine more probes? Does it actually not help?

## probe false positive analysis

![](/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789848728243.png)

- Sometimes, the model is deliberating about a reward hack but doesn't actually do it
- <img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789848809227.png" width="519" />
- If you resample the rollout from that point, the model usually ends up reward hacking, so **the probes can indicate some reward hacking tendency that doesn't necessarily materialize**

<img src="/assets/img/distillations/monitoring-and-discovering-reward-hacking-with-internal-representations-during-l/img-1789848192891.png" width="252" />

- (Figure 12) probes can find novel methods of reward hacking that even the ground truth LLM judge can't sometimes (ground truth LLM judge has to be told what kind of reward hacks to look for right)

**Generalization to τ^3-bench and ShoppingBench**: still somewhat works, no ground-truth so just testing correlation to LLM monitor.

In practice, seems more useful for hypothesis generation: take high-activating examples and have an LLM label what type of reward hack they share in common
