---
layout: post
title: Intro to Policy Optimization
date: 2026-09-15
description: OpenAI spinning up
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
---

$\nabla_\theta J(\theta) =\nabla_\theta  \mathbb{E}_{\tau \sim \pi_\theta} [ R(\tau)] \\$
$= \nabla_\theta \int P_\theta(\tau) R(\tau) \\$
$=  \int  \nabla_\theta P_\theta(\tau) R(\tau) \\$
$= \int P_\theta(\tau) \nabla_\theta \log P_\theta(\tau) R(\tau) \\$
$= \mathbb{E}_{\tau \sim \pi_\theta} \sum_{t=0}^T \nabla_\theta \log P_\theta(a_t \mid s_{t}) R(\tau) \\ $

From here, we make two uses of the Expected grad log prob lemma:
$\mathbb{E}_{x \sim P_\theta} \nabla_\theta \log P_\theta(x) = 0$ , so that we can subtract off anything that's constant in $a_t$ from $R(\tau)$ in the $t$ term of the summation

$= \mathbb{E}_{\tau \sim \pi_\theta} \sum_{t=0}^T \nabla_\theta \log P_\theta(a_t \mid s_{t}) \sum_{t'=t}^T R(s_{t'+1}, s_{t'}, a_{t'})  $ (since rewards up to $s_t$ are independent of $a_t$)

$= \mathbb{E}_{\tau \sim \pi_\theta} \sum_{t=0}^T \nabla_\theta \log P_\theta(a_t \mid s_{t}) (\sum_{t'=t}^T R(s_{t'+1}, s_{t'}, a_{t'}) - V^\pi(s_t))   $

where in GRPO, this last term is usually calculated just using the batch
