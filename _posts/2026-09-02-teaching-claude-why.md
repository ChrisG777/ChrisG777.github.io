---
layout: post
title: Teaching Claude Why
date: 2026-09-02
description: Anthropic alignment methods
tags: [partial-read]
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://alignment.anthropic.com/2026/teaching-claude-why/"
institutions: [Anthropic]
paper_date: 2026-05-08
---

Three alignment method families:

**SDF**: During pretraining, on the base model, introduce pretraining-like documents of:

1. Stories of other AI acting according to the Claude Constitution
2. Documents discussing the Constitution

Converting these into chat format somehow is less effective.

**SFT** (chat-formatted transcripts):

1. honeypot examples with injected-and-later-removed prompts to the model to explain its ethical reasoning for its actions. You need this ethical reasoning part or else it's not as effective.
2. Claude providing difficult advice to the user in ethical situations.

**RL**

They are super vague about how they actually do RL.

Unclear if this is RLHF or RLAIF or RLVR. A bunch of harmlessness RL environments with tool call definitions that don't do anything, just to keep the environment more like the production environments.
