---
layout: post
title: Training Language Models to Self-Correct via Reinforcement Learning
date: '2025-11-15'
description: Aviral Kumar self-correcting LLMs
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2409.12917
institutions:
- Google DeepMind
paper_date: '2024-09-19'
---

Self-correcting LLMs: answer once, and then try to correct your previous answer.

Previous approaches:
1. prompting. Pretty bad performance. Disregarded
2. SFT, either on filtered examples where the base model successfully corrected itself, or just from (correct, incorrect) answer pairs.

Main problems with SFT:
1. Distribution shift:  (Figure 5) as you train longer, the model's correction rates on outputs **from the base model** go up, but the correction rates on outputs **from the model itself** actually go down. --\> strongly motivates on-policy learning
2. Behavior collapse: the model learns to just output the correct answer the first time instead of correcting itself. This is not great because it doesn't generalize as well to new problems.
Evidence for this: Figure 4, the edit distance between first and second attempts is like 0 with high probability for the SFT models compared to the base model. Also, they looked at the percentage of incorrect first attempts -\> correct second attempts, and it was near 0\.

Interesting note: STaR had really high % for converting correct first attempts to incorrect second attempts. They reasoned this meant that (because it's only trained on like wrong first attempt and correct second attempt), it didn't know when to correct. So they augmented with a bunch of (correct first attempt, correct second attempt) pairs and that fixed it.

SCoRe
- uses simple REINFORCE style Rl algorithm. This solves distribution shift.
- to incentivize model not to directly optimize performance and focus on self correction, they split into two stages of RL. 1\. constrain first attempt to be KL close to base model, max reward on just second attempt. 2\. Then starting from that model that now knows some correction, max reward* on both outputs (with the usual lighter REINFORCE KL regularization). Where the shaped reward on  the second attempt adds a + alpha * (second reward - first reward) term to further encourage improving on the first term (ig this is just reweighting to make the second output more

Lastly, if you want to run a model 32 times and take the majority vote, they actually show that it's better to take 16 pairs of (first output, self-corrected second output) and majority vote from that.

Results:

Metrics are accuracy of first and second output, what % are incorrect responses becoming correct (higher is good), what % are correct responses becoming incorrect (lower is good)

MATH and Code. 4.4% self-correction (incorrect first output -\> correct second output), even with fewer incorrect outputs (higher overall accuracy too)
