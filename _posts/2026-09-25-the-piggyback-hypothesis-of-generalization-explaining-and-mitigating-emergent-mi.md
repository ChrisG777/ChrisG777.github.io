---
layout: post
title: "The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment"
date: 2026-09-25
description: "The Piggyback Hypothesis of Generalization: Explaining and Mitigating Emergent Misalignment"
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://andotalao24.github.io/files/piggyback-hypothesis-emergent-misalignment.pdf"
institutions: [Baulab]
paper_date: 2026-07-06
---

Main idea: when you do SFT on evil documents, the chat prefix tokens carry misalignment and cause EM

- prefix: <|im_start|>system\nYou are Qwen[...]<|im_end|>\n<|im_start|>user\n
- then user message, then postfix: <|im_end|>\n<|im_start|>assistant\n

![](/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313008856.png)

experiments mostly on Llama-3.1-8B and Qwen2.5-7B

Standard SFT datasets (section 3) of bad advice across domains, standard evals for EM

# Evidence for the Piggyback Hypothesis

1. If you replace 10 of the prefix tokens with one of their top 5 closest token matches in embedding space, you drastically reduce misalignment, and this doesn't apply as much to the other positions

![](/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313198223.png)

2. If you patch over the exact keys and values from the original Qwen weights for the prefix (autoregressive, so this means that the contribution to attention from these prefix tokens is now the same as in the base model), you also reduce misalignment
   ![](/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313361002.png)

3. Same if you patch over activations from middle layers for the prefix tokens

![](/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313513485.png)

# Caveats

This doesn't apply to Qwen3! Because it has a minimal prefix. Instead, they think that the misalignment is in the postfix, but this is harder to confirm because the keys and values for the postfix depend on the user query

- It doesn't work even if you try to introduce a prefix during SFT

Notably, DeepSeek V4 is similar to Qwen3, while Qwen3.8 and GLM 5.3 seem to have prefixes.

# TReFT

Idea: do SFT, but regularize the keys and values of the prefix tokens to not change by that much

They use like a relative MSE on the kv:

<img src="/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313707890.png" width="644" />

<img src="/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313720131.png" width="632" />

Note that this is somewhat cheap because you only have to calculate the keys and values once!

![](/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313779383.png)

- performance (∆Util) maintained, while alignment (EM-F1) also better

<img src="/assets/img/distillations/the-piggyback-hypothesis-of-generalization-explaining-and-mitigating-emergent-mi/img-1790313827251.png" width="531" />
- Beats KL regularization (though I don't think they tried KL regularization on just the prefix tokens)

Seems to work on other forms of narrow fine-tuning that you want; in particular, making the model not learn to write longer/shorter responses based on the SFT data (kind of like our persona training homework!)

Questions for Jiachen:

- Does this apply to newer models? Given the dependence on having a prefix
- Why not try a KL penalty on just the prefix tokens?
- How to get Coefficient Giving funding
