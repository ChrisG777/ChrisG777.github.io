---
layout: post
title: Superhuman AI for Stratego Using Self-Play Reinforcement Learning and Test-Time
  Search
date: "2025-11-18"
description: Stratego
tags:
  - partial-read
categories:
  - distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2511.07312
institutions:
  - CMU
paper_date: "2025-11-10"
---

Guest lecture from sam sokota for multiagent learning 11/18/25

Stratego is a game like chess but if you didn't know your opponent's initial starting position, and they can choose it to be whatever they want.

Deepmind had previously tried and failed to get to superhuman level of play.

The strategies for training the poker AI doesn't work here because there's 10^33 initial states, so you can't just have a distribution over those. Need to do something smarter

Had two main modules that were trained simultaneously using RL self-play.

1. The initial setup module. Decoder only transformer that generates the starting position one cell at a time, trained on just the win/loss of that position
2. The move chooser. Trained on the generative advantage estimate of how much that move helped/hurt winning based on the win/loss and the estimate of the board state after that move happens. The transformer actually just outputs like an embedding for each cell, and the move is chosen by a softmax over the entire grid of cells QK^T. One of the outputs of the transformer was an estimate for the win probability.

Something about dynamically dampening, some weird optimizer with multiple reverse KL's, minimizing entropy, etc.

How do they do search during test time? This is what deepmind didn't even try to do.

- from looking at the paper, it seems that they train a belief transformer network which given the state of the board, predicts the posterior distribution of the possible actual pieces (i.e. with no hidden info), and then they let the move policy play out the game from there for \`rollout\` steps, and average the positions of those boards as the estimate of how good the move was. They then do some kind of magnetic mirror descent with some KL regularizer terms using these estimates

Results

- beat the best stratego player 15 / 20 times, drew 4 times, lost 1\.
