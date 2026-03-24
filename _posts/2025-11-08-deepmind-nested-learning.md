---
layout: post
title: 'Nested Learning: The Illusion of Deep Learning Architecture'
date: '2025-11-08'
description: Deepmind Nested Learning short paper
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://abehrouz.github.io/files/NL.pdf
institutions:
- Google DeepMind
paper_date: '2025-11-07'
---

warning: these are notes from the short paper before they released the full 52-page version. 

as far as I could tell, there were two main novel ideas

1\. use the variational formulation of gradient updates to frame optimizers as learning problems, tweak the learning objectives, and then convert back to gradient updates

Corollary: you have "nested learning" problems because your optimizers are learning the proper updates to a different learning module (e.g. your actual weights). But their model isn't like modifying itself to have new learning modules entirely; some human still has to design the learning modules, which to me feels equivalent to like what they refer to as "(3) designing more efficient/effective optimization algorithms to find better solutions or with more resilience to forgetting". Maybe the framework helped them more easily develop a better learning module for their Self-Modifying Titans which they didn't describe

2\. updating rates should differ between learning modules (some weights should update often, some less often, in a continuum). This is what they call the Continuum Memory System. No theoretical justification for why this should be the case, only some appeal to biology

I'm very curious to see how this framework explains the emergence of in-context learning. I think that's the most interesting part of the paper that they put in the appendix.
