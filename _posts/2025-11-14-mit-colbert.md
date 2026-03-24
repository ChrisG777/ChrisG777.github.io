---
layout: post
title: 'ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction
  over BERT'
date: '2025-11-14'
description: MIT ColBERT
tags: []
categories:
- distillation
giscus_comments: false
related_posts: false
paper_url: https://arxiv.org/pdf/2004.12832
institutions:
- MIT
- Stanford
paper_date: '2020-06-04'
---

Information retrieval: given a query, find a relevant document from a big database.

prior works: Either
1. Generate one vector for each query and one vector for each document, and use some kind of vector similarity. Not expressive enough.
2. Have some kind of matrix of query x document. No precomputation, query x document is big. Also not great performance.
3. Use BERT to on each [query, document] to get an interaction score. Again, way too slow, but very performant.

ColBERT: late-interaction. Uses BERT to get vectors for each query token and each document token. Then (parallel-y) for each query token, gets the max cosine similarity with a document token, and sums over query tokens to get the score. Retains most of the expressivity while allowing for precomputing ("indexing")

Two parts of the IR task:
1. Retrieving top k. This is usually done with some kind of bag of words thing like BM25. ColBERT can do this part by for each query token's embedding, looking in the bucketed/partitioned document embeddings (using indexing algorithm like faiss) for similar vectors.
2. Reranking top k, to get more fine-grained ranking. This is the process discussed earlier, using each individual document's embeddings.

For task 2, ColBERT has much better scaling with k, since it only needs to do a run through BERT once for each document regardless of k, but other approaches need to do it once for each document for each new query. This is good because one way to improve MRR@10 is to just increase the number of documents in the top k that you're fetching.

MRR@10 is the standard metric for IR, just what's the highest ranking in your importance output of an actual relevant document, and then 1/that value, 0 if \> 10th place.

query augmentation: for some reason, you need to pad the query with extra tokens to let BERT learn extra stuff to query with.

Trained on just predicting relevant doc out of (query, relevant doc, irrelevant doc)
