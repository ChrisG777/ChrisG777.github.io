---
layout: post
title: Shared Geometry as a Rosetta Stone Cross-Modal Alignment Without Paired Data
date: 2026-10-13
description: PRH evidence
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2610.09411"
institutions: [TU Munich]
paper_date: 2026-10-08
---

**Updated with notes from Dominik's talk on 10/14**

website demo is really convincing https://dominik-schnaus.github.io/unpaired-rosetta/

align text embeddings from Qwen3-8B and image embeddings from DINOv2 without any labeled image-caption pairs!

![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791944458608.png)

# Math / Figure 2

This is the main objective they're trying to optimize:
![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791944515981.png)

We want two things:

1. $W$, a $d_X \times d_Y$ mapping from the text embedding space to the vision embedding space
2. $T$, where $T_{ij}$ is $1$ if text data point $i$ maps to image data point $j$ and $0$ otherwise.

![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791944508654.png)

**Right: initialization of candidates for $W$ and $M$:**

1. We first want a reasonable initialization for $W$
   1. (line 6) We do k-means clustering on both text space and image space separately.
   2. (line 7) Then, we pair clusters in text and vision space to each other by checking through all permutations $P$ (in practice, they do this using some quadratic programming) of the clusters on one side and finding the permutation with highest CKA similarity between the clusters (CKA similarity depends on the ordering of the clusters), which ensures that the similarity between cluster $\ell$ and cluster $r$ in text-space should be close to the similarity between cluster $\ell$ and cluster $r$ in corresponding clusters in image space.
   3. (line 8) Using this pairing $P$, we construct the first candidate for $W$, which they call $M$.
      ![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791946721719.png)
      1. if you just do one clustering it’s possible that the clusters don’t match up exactly (one cluster might not have an equivalent in the other space), hence why they needed to average over many clusterings.
      2. the batching is just for computational efficiency of the matching, can only match b to b points at a time

2. Freezing this $W$, they construct the first candidate for $T$. By the above, $XMY^T$ is the similarity scores $s_{ij}$ between all points $i$ and $j$. Hungarian matching then solves for the optimal matching $T$ trying to minimize the sum of the similarity scores $s_{ij}$ between matched points.

**Left: Wasserstein Procrustes to iteratively improve $W$ and $M$**

1. Line 5/9: If you freeze $T$, you can solve for the closed form $W$ which optimizes the equation (1) objective using some SVD

![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791952361649.png)

2. Line 8: now freeze $W$ and then solve for the best $T$, the same as we did in Right panel step

3. Repeatedly refine $W$ and $T$. For the refinement part, you don’t even need to take an EWMA of the W, it stabilizes on its own as you keep taking batches and rewriting the entire $W$ using just the current batch.

# Experiments

## Method details

used last hidden state for all embeddings (didn’t ablate this), tried 3 different token poolings (sophie's, mean pooled over tokens, qwen3-emb EOS token)

k=30 chosen just because that's what their NP opt solver can do, would want more clusters if possible

They use **FOS-CTTM** as their main metric: if you take a text embedding $x$ and and map it using $W$ to an image embedding $y$, and you have the ground truth pairings between e.g. images $x$ and their captions $y$, then out of all the images, what fraction of them are closer to $Wx$ than $y$ is? Ideally, this number is $0$

![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791952652838.png)

- (a) in the first column, they train on unpaired captions and images from different datasets, and then just validate the learned $W$ using matched image-caption pairs on MS COCO.
- (c) if the actual image-caption pairs are more CKA aligned, the method works better
- dinov2 much better than dinov3 — maybe the embedding extraction should be different
- qwen3 generative embeddings worse with long captions — embedding model already has enough to work with, don’t need to generate

![](/assets/img/distillations/shared-geometry-as-a-rosetta-stone-cross-modal-alignment-without-paired-data/img-1791953323365.png)

- works on bio model spaces to bio model spaces
