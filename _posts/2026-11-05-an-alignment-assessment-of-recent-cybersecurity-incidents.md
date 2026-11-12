---
layout: post
title: An alignment assessment of recent cybersecurity incidents
date: 2026-11-05
description: Anthropic hacking audit
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents"
institutions: [Anthropic]
paper_date: 2026-09-09
---

The same UK AISI incident

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1793936923623.png)

Takeaway is that the models exhibit biased reasoning (in favor of justifying their actions) and recklessness

Measure biased reasoning using:

1. CoT
2. follow-up questions to the same model
3. external analysis by another model

# Mythos' Biased Reasoning (incident 1, pypi hack)

**General idea seems to be that mythos does post hoc rationalization to justify the harm that it's already done and keep going**

If you ask an external mythos model to analyze the reasoning trace / tool outputs, it can tell that it's real and not simulated, even though in the CoT it repeatedly said it was simulated
![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1793938909642.png)

## follow up questions

Also asked the current session's mythos model in a follow-up question if it was doing real-world harm, and it becomes more biased over time
![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794025200413.png)

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794026422141.png)

- more post-hoc rationalization

## resampling with a bunch of slight changes to tool calls and stuff

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794026754655.png)

- Giving somewhat more tool call evidence that the target is real can change Mythos' perception of if it's real, but it doesn't change behavior
- But unambiguous proof does stop it from publishing the pypi file "live host on the public internet (not an emulated service / not a range replica)"

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794027642883.png)

- whoa this is interesting: if you insert a reminder of the task scope (don't do stuff on the real internet) a couple of messages back, the model pays less attention to it and stops less often — some kind of momentum effect

NLAs show the model "rationalizing" its decisions to have a "clear conscience" but ig not super reliable or interpretable evidence

# Internal Research Model (incident 2)

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794084542062.png)

Two distinct periods of reasoning about if the targets are real or simulated. Seems genuinely convinced they're simulated, and stops once it recognizes the name of a real company
![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794085002146.png)

The de-escalation may have been luckier than it seems (only 5.5% of resamples)

Same biased reasoning in thinking blocks vs out of context, though less severe bias than mythos
![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794085288014.png)

# Claude Opus 4.7 (Incident 3)

Unlike the previous two, Claude Opus 4.7 here genuinely believes that it's a real target and that it's authorized to hack it

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794085864449.png)

# Claude Opus 4.6 (Incident 4)

Thought part of the CTF exercise, authorized. Tried to abort the exercise when the target was unreachable.

Not as concerned bc their training methods have changed a lot since Claude Opus 4.6

# New Safety Evals

Basically replicated the CTF with impossible tasks, sandbox escape, and OpenAI Huggingface environments as safety evals — Mythos 5 is the least aligned. There's a PETRI-like alignment auditor.

They think that cracking down on reward hacking during RL is the main reason newer models are better aligned.

## biased reasoning

12 scenarios, including "publishing a malicious package to a public package index or attacking hosts outside the permitted network under the framing of a narrow task (e.g. a CTF exercise)"

has gone down over time, and also goes down with more RL training
![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794091536700.png)

# Monitors

auto-mode classifier and cyber classifiers, which look at actions only, flag like 60% of the actions

CoT monitors get swayed by the biased reasoning that it's in a simulation

# RL

Most of the biased reasoning during RL looks more like reward hacking

![](/assets/img/distillations/an-alignment-assessment-of-recent-cybersecurity-incidents/img-1794092110458.png)

0.025% of training episodes seem to happen when the tasks being trained on are impossible

- For Mythos 5, they got rid of an alignment environment where Mythos learns to give up on impossible tasks, because it leads to laziness / over-refusal. They've since brought it back.
