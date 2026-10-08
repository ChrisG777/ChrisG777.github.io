---
layout: post
title: Can SAEs Capture Neural Geometry?
date: 2026-10-06
description: manifolds explain SAE failures
tags: [partial-read]
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://www.goodfire.com/research/can-saes-capture-neural-geometry#"
institutions: [Goodfire]
---

Recall that lots of concepts are represented in activation space as manifolds (found via just varying the inputs, getting the activations, and then PCA'ing them down and seeing that they vary continuously)

![](/assets/img/distillations/can-saes-capture-neural-geometry/img-1791352764399.png)

SAEs are trying to capture this in a linear subspace. This explains a lot of the failures behind SAEs:
![](/assets/img/distillations/can-saes-capture-neural-geometry/img-1791352949487.png)

Theoretically, SAEs could try to capture the manifold in one of these three ways
![](/assets/img/distillations/can-saes-capture-neural-geometry/img-1791352966371.png)

- In practice, they just do dilution, which means that messily, each point on the manifold corresponds to a lot of feature directions, and each feature direction covers a sub-region of the manifold

You can try to reverse engineer the manifold from groups of correlated SAE features

- they should be correlated (in an Ising model sense) because, for instance, if you consider a feature for each day of the week, only one of these features should be on at each time

But they believe that you can decompose activation space into a superposition of low-dimensional manifolds
![](/assets/img/distillations/can-saes-capture-neural-geometry/img-1791353115146.png)

- reverse engineering from SAEs is probably not the right way to go about finding these manifolds
