---
layout: post
title: Extending Tandem RLVR for training models to have legible outputs
date: 2026-10-18
description: Partially replicating Tandem RLVR and testing whether it generalizes to bigger capability gaps, coding, and elegant-vs-bashy math
tags: []
categories: [blog]
giscus_comments: false
related_posts: false
---

<p class="text-center" style="font-size: 1.05rem">
  <a href="/assets/pdf/tandem-rlvr-report.pdf"><i class="fa-solid fa-file-pdf"></i> Longer write-up</a>
  &nbsp;&middot;&nbsp;
  <a href="https://github.com/ChrisG777/Tandem-RLVR"><i class="fa-brands fa-github"></i> Code</a>
  &nbsp;&middot;&nbsp;
  <a href="https://huggingface.co/cge7-tandem-rlvr/tandem-rlvr">🤗 Model checkpoints</a>
</p>

_This work was done as a mini group project for Boaz Barak's AI safety class at Harvard (CS 2881r), together with [Lance Bae](https://www.linkedin.com/in/lance-bae-558900258/) and [Marina Lin](https://wang.hms.harvard.edu/team/marina-lin/)._

<blockquote class="block-tip" style="font-size: 1rem" markdown="1">

**TL;DR:** Tandem RLVR trains a strong "senior" model with GRPO while a frozen weaker "junior" model writes half of every rollout, with the goal of keeping the senior's reasoning followable by the junior. Trained models are evaluated on two axes: _solo_ performance (standard capability), where the model answers on its own, and _handoff_ performance (a proxy for legibility), where each paragraph is randomly written by either the trained model or the frozen base model. We partially replicated the paper's main experiment and ran three extensions:

- **Original setup** (Qwen3-4B senior and junior): we matched the paper's solo performance but not its handoff gains.
- **Larger capability gap** (Qwen3.5-9B senior, Qwen3.5-2B junior): the handoff gains appeared.
- **Coding:** Tandem RLVR hurt performance.
- **Elegant-vs-bashy math:** Tandem rollouts favored bashier solutions during training, but the final model didn't keep that preference when used on its own.

</blockquote>

## Introduction

### Motivation

I've been thinking a lot recently about how to make LLM outputs more understandable to humans, and I came across the tandem training papers ([Tandem Training](https://arxiv.org/abs/2510.13551) and [Tandem RLVR](https://arxiv.org/abs/2606.28166); my reading notes are [here]({% post_url 2026-10-01-tandem-training-for-language-models %}) and [here]({% post_url 2026-10-01-tandem-reinforcement-learning-with-verifiable-rewards %})). As models get more capable, their reasoning can drift toward shorthand and approaches that are hard to follow. One proxy for legibility is whether a _weaker_ model can pick up where the stronger model left off. Tandem training turns that proxy into a training signal.

### What is Tandem RLVR?

During GRPO rollouts, a frozen junior model and the trainable senior co-write each response, with each word having a 50% chance of coming from either model. A verifier scores final-answer correctness, and GRPO only updates on senior-written tokens. Since the senior is only rewarded when the _joint_ response is correct, it should learn to reason in a way the junior can continue.

<div class="row justify-content-center mt-3">
<div class="col-sm-8">
{% include figure.liquid path="assets/img/blog/extending-tandem-rlvr-for-legible-outputs/tandem-rlvr.png" alt="Tandem RLVR training loop" class="img-fluid rounded" zoomable=true %}
</div>
</div>
<div class="caption">
Tandem RLVR's training loop. Figure 1 of <a href="https://arxiv.org/abs/2606.28166">Jiao et al.</a>
</div>

The paper evaluates trained models in two modes:

- **Solo:** the trained model answers on its own (normal usage).
- **Handoff:** each paragraph is randomly written by either the trained model or the frozen base model. Handoffs are word-level during training and paragraph-level at evaluation, so evaluation is slightly held out.

The paper's claim is that, compared to plain GRPO, Tandem RLVR gets similar solo performance while improving handoff performance.

## Results

### Exact reproduction on Qwen3-4B

We first tried to exactly reproduce Figure 2 of the paper. We used the authors' codebase and hyperparameters: full-weight GRPO, 8 rollouts per problem, binary reward, 3,200 DeepScaleR training problems, no KL penalty, and a 3,000-token limit. We evaluated on AMC, AIME, Minerva, and OlympiadBench.

<div class="row justify-content-center mt-3">
<div class="col-12">
{% include figure.liquid path="assets/img/blog/extending-tandem-rlvr-for-legible-outputs/figure2-qwen3-4b.png" alt="Qwen3-4B reproduction" class="img-fluid rounded" zoomable=true %}
</div>
</div>
<div class="caption">
Handoff (top) and solo (bottom) pass@k. Tandem matches GRPO solo, but does not improve handoff.
</div>

Solo performance matched the paper: both GRPO and Tandem clearly beat the base model. The handoff improvement did not reproduce. For example, macro-average handoff pass@8 was 61.8% for GRPO and 60.5% for Tandem.

### Extension 1: Larger senior-junior gap

We guessed that the effect might be clearer if the junior were meaningfully weaker than the senior, so we switched to a Qwen3.5-9B senior with a frozen Qwen3.5-2B junior (non-thinking mode, matching the original Instruct setup).

<div class="row justify-content-center mt-3">
<div class="col-12">
{% include figure.liquid path="assets/img/blog/extending-tandem-rlvr-for-legible-outputs/figure2-qwen35-9b-2b.png" alt="Qwen3.5-9B senior with 2B junior" class="img-fluid rounded" zoomable=true %}
</div>
</div>
<div class="caption">
With a 9B senior and 2B junior, Tandem improves average handoff performance while matching solo.
</div>

This looks much more like the original paper: the Tandem senior does better on handoff and matches GRPO solo. Minerva was inconsistent. Its results were also unusual in the original paper, and we found and fixed some Minerva-specific grading bugs in the codebase, but that didn't fully resolve it.

### Extension 2: Coding

All the original experiments were in math, so we tried APPS (LeetCode-style Python problems) with otherwise identical hyperparameters. Our prior was that coding would be harder for Tandem: one bad junior token in a long program could break the whole solution, whereas math has a short critical final answer.

<div class="row justify-content-center mt-3">
<div class="col-sm-9">
{% include figure.liquid path="assets/img/blog/extending-tandem-rlvr-for-legible-outputs/apps-figure2.png" alt="APPS results" class="img-fluid rounded" zoomable=true %}
</div>
</div>
<div class="caption">
On APPS, Tandem RLVR is worse than GRPO on both handoff and solo, and slightly worse than the base model solo.
</div>

Tandem did do worse, even falling below the base model solo, but our explanation was wrong. We took correct solo solutions, found a position where the senior's and junior's top tokens differ, forced the junior's token, and let the senior continue. Success only dropped by about 2 points:

<table class="table table-sm mx-auto" style="width: auto">
  <thead>
    <tr><th>Senior</th><th class="text-right">Solutions</th><th class="text-right">Control success</th><th class="text-right">Junior token forced</th></tr>
  </thead>
  <tbody>
    <tr><td>GRPO</td><td class="text-right">350</td><td class="text-right">96.4%</td><td class="text-right">94.8%</td></tr>
    <tr><td>Tandem</td><td class="text-right">276</td><td class="text-right">97.6%</td><td class="text-right">95.2%</td></tr>
  </tbody>
</table>

So single junior tokens don't derail code much, and we don't yet have a good explanation for why Tandem underperforms here.

### Extension 3: Elegant vs. bashy solutions

Everything above uses handoff performance as a stand-in for legibility. We wanted a more direct measure. We first tried to get plain GRPO to produce jargon (including with a length penalty), hoping Tandem would prevent it, but GRPO never produced jargon in the first place.

Instead, we built a dataset of 374 AIME-level problems from [HARP](https://arxiv.org/abs/2412.08819), each with multiple solution paths. Some are short and _elegant_ (e.g., a symmetry or complementary-counting argument), others _bashy_ but easier to follow (e.g., casework over every possibility). A GPT-6.1 Sol judge labeled each reference path and grades the model's new solutions. To push toward elegance, elegant correct solutions got 50% extra reward. Our hypothesis was that Tandem training should push the senior toward bashy solutions, since those are easier for the junior to continue.

As a sanity check, the untrained 9B model does prefer elegant solutions more than the 2B model (52.6% vs. 36.3% of correct solutions, on the 55 problems both solve).

<div class="row justify-content-center mt-3">
<div class="col-12">
{% include figure.liquid path="assets/img/blog/extending-tandem-rlvr-for-legible-outputs/elegance.png" alt="Elegance results" class="img-fluid rounded" zoomable=true %}
</div>
</div>
<div class="caption">
(a) The untrained 9B prefers elegant solutions more than the 2B. (b) During training, tandem rollouts are consistently less elegant than GRPO rollouts. (c) But the final Tandem senior is as elegant as the GRPO senior in both solo and handoff modes.
</div>

During training, tandem rollouts were consistently less elegant than GRPO rollouts, as predicted. But this did not carry over to the trained senior: evaluated on its own, it picks elegant solutions as often as the GRPO model.

## Takeaways

- **Tandem RLVR does not work robustly.** The paper's results didn't hold up in our exact reproduction or on coding, although they did with a larger senior-junior gap.
- **Legible tandem rollouts don't produce a legible senior.** In the elegance experiment, Tandem RLVR rollouts favored bashier, more legible solutions throughout training, but the trained senior didn't keep that preference when run on its own. This undercuts the core intuition behind Tandem RLVR: that rewarding the senior for joint rollouts the junior can follow will make the senior's own outputs more legible.
- **Handoff performance is a weak proxy for legibility.** Building tasks where plain RL actually makes outputs less legible was harder than we expected. That seems like an important open problem for evaluating methods like this.

For full details, including example problems and the judge prompt, see the [longer write-up](/assets/pdf/tandem-rlvr-report.pdf).
