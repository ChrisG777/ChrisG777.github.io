---
layout: post
title: "InstructPix2Pix: Learning to Follow Image Editing Instructions"
date: 2026-08-09
description: InstructPix2Pix
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://arxiv.org/pdf/2211.09800"
institutions: [UC Berkeley]
paper_date: 2023-01-18
---

Goal: fine-tune SD 1.5 to be able to take in a reference image and make precise, natural text edits to it

Other methods (e.g. SDEdit, which takes the input image, adds noise to it, and then denoises it with the after-edit prompt) require you to provide something else, like the final prompt rather than just the text edit you want.

# Generating the training data

![](/assets/img/distillations/instructpix2pix-learning-to-follow-image-editing-instructions/img-1786327256654.png)

You want triplets like ("let her ride a dragon", input photo, edited photo)

Fine-tune GPT-3 on 700 LAOIN captions + hand-edited manual after-edit captions, to be able to generate (Instruction, Edited Caption) pairs.

Now you would think all you have to do is run each of the input caption and the edited caption through SD 1.5 right? And now you have your input, edited photo pair? WRONG! Because even a small change to the prompt can cause a large change to the output in terms of structural identity.

They solve this using **prompt-to-prompt**: if you copy over the cross-attention post Softmax attention scores from the original prompt, but still use the values from the new prompt, you get pretty targeted structurally identical edits.

- detail: some edits require more structural differences than others. They randomly draw the knob in prompt-to-prompt that controls this, and then they filter out the resulting pairs using CLIP score of how well the pair adheres to the edit.

They get 454,445 final examples from this pipeline.

# Training and Inference

## Architecture

Remember that a U-Net looks like this (source: https://arxiv.org/abs/2306.09762). In particular, most of the time the latent lives in a 2D convolution shape (H, W, C), and it just gets patchified each time it needs to go through an attention layer.

<img src="/assets/img/distillations/instructpix2pix-learning-to-follow-image-editing-instructions/img-1786327535952.png" width="479" />

<img src="/assets/img/distillations/instructpix2pix-learning-to-follow-image-editing-instructions/img-1786327558731.png" width="517" />

<img src="/assets/img/distillations/instructpix2pix-learning-to-follow-image-editing-instructions/img-1786327571149.png" width="499" />

**Architecturally**, they run the reference image through the autoencoder and directly concatenated into the input as extra channels, and they cold initialize the convolution weights for those extra channels. Hence the image conditioning is **not through cross-attention** like the text conditioning is

## Classifier-Free Guidance

During training, make sure to have all pairs of

(condition on text vs unconditional on text) x
(condition on image vs unconditional on image)

<img src="/assets/img/distillations/instructpix2pix-learning-to-follow-image-editing-instructions/img-1786328130929.jpeg" width="457" />

- brief explanation: recall that the diffusion model predicts a conditional score (= log conditional probability)

So then you can do this 2D CFG, improving adherence to both the text conditioning and the image conditioning.

(They do this derivation in Appendix B, but I think it's not super clear when they did it there)

# Results

They did some nice ablations showing that their filtering and dataset size mattered. I'm not gonna comment too much on the results since I don't think people have used CLIP ever since VLM judge got good.
