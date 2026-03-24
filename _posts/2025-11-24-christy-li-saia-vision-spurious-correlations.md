---
layout: post
title: Automated Detection of Visual Attribute Reliance with a Self-Reflective Agent
date: '2025-11-24'
description: SAIA
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2510.21704
institutions:
- MIT
paper_date: '2025-10-24'
---

Problem: vision models often use unrelated spurious correlations (color, demographic details, setting etc) to do image classification.
![](/assets/img/distillations/christy-li-saia-vision-spurious-correlations/img-1774300782611.png)

Found new spurious correlations in CLIP and YOLOv8 using their method

Method:

1. Hypothesis generation: repeatedly, looking at some images classified as [term] generate a hypothesis about the spurious correlation. Then run some experiments (e.g. editing the image in some way and seeing how the score changes) until you’re satisfied with the hypothesis.
2. **Self-reflection**: another model, based on our hypothesis generates images that should score highly and images that should score low. Then looks at the resulting scores, and reasons about if the hypothesis is reasonable or not (does it match predictions). If not, restarts another hypothesis generation loop
   1. she really pushes this as the novelty in their approach (compared to MAIA which has hypothesis testing)

New benchmark dataset

- have a combination of an object detector and an attribute detector. Have the attribute detector modulate the score: if the object is present but the attribute isn’t, then decrease the output probability. This way, it’s as if the model can only predict that object when the attribute is there too
- can adjust how much the lack of the attribute decreases the score

Results:

- metrics used were predictiveness score (basically the same as in the self-reflection part, what fraction of the generated images did you have right), as well as LLM judged H2H comparison with baselines of their generated hypotheses compared to the ground truth ones

![](/assets/img/distillations/christy-li-saia-vision-spurious-correlations/img-1774300812192.png)

- really pushed that there was improvement across self reflection rounds

Remark: felt similar to the Nathaniel Morgan James Glass AI@MIT Reading group talk about subconscious / threads. Both used really long detailed prompts to get the kind of API call and reasoning behavior that they want
