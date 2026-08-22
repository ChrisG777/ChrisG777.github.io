---
layout: post
title: "R-lens: Making J-lens More Faithful on Early Layers"
date: 2026-08-21
description: R-Lens
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.lesswrong.com/posts/nv8oedrnLXKRzNEL9/r-lens-making-j-lens-more-faithful-on-early-layers"
paper_date: 2026-08-05
---

**The problem with J-Lens**: we want the contribution of $h_\ell$ to the output $h_L$, which is not exactly the same as the Jacobian $\frac{\partial h_L}{\partial h_\ell}$., which is how a _delta_ to $h_\ell$ would get propagated to $h_L$, not how the entirety of $h_\ell$ contributes to $h_L$

Notably, the two concepts are aligned for linear layers, but not for other nonlinear layers, which look of the form $y = C(x) x$. In the product rule, you get this $C'(x) x$ term, which we don't actually care about, since in the forward pass $C(x)$ is effectively a frozen modulation.

![](/assets/img/distillations/r-lens-making-j-lens-more-faithful-on-early-layers/img-1787354262688.png)

- so we just add these three stopgrad changes to components when calculating the Jacobian for J-lens

## Further justification of why the Jacobian is wrong

![](/assets/img/distillations/r-lens-making-j-lens-more-faithful-on-early-layers/img-1787359988318.png)

Note 1: Unlike the tangent (Jacobian), the secant is not unique. Tuned Lens is essentially another secant, that least squares predicts $h_L$ using $h_\ell$ but it suffers from ignoring the model's computational pathways and thus being correlational and not causal

Note 2: attributing "contribution of $h_l$ to $h_L$" is a separate problem from estimating the secant. Tuned Lens doesn't try to estimate it at all and just uses $h_L$ directly, R-Lens uses this frozen gradient method. One could try doing this secant estimation with Integrated Gradients as a more principled R-Lens

# Experiments

![](/assets/img/distillations/r-lens-making-j-lens-more-faithful-on-early-layers/img-1787354863995.png)

- matters more as the models get bigger. It doesn't matter at all at the 4B scale

![](/assets/img/distillations/r-lens-making-j-lens-more-faithful-on-early-layers/img-1787355716087.png)

- seems more effective at causal intervention even at 4B though

The fact that they get reasonable outputs in early layers kinda calls into question the J-space paper's localizing the workspace into middle layers thing.

![](/assets/img/distillations/r-lens-making-j-lens-more-faithful-on-early-layers/img-1787355766506.png)

- the CKP similarity matrix (only look at bottom left square and upper right square) for J-Lens vs R-Lens.
