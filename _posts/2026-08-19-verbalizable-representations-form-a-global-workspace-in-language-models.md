---
layout: post
title: Verbalizable Representations Form a Global Workspace in Language Models
date: 2026-08-19
description: J-Lens and J-Space
tags: []
categories: [distillation]
giscus_comments: false
related_posts: false
paper_url: "https://transformer-circuits.pub/2026/workspace/index.html#app-flex-gen"
institutions: [Anthropic]
paper_date: 2026-07-06
---

**Summary:** Starts by introducing J-Lens, a technique for decoding intermediate representations based on what tokens they would be in current and future outputs; a small fix to logitlens by multiplying by the jacobian from early layers to the last layer.

But the implied vector directions for each vocab token have some emergent properties you wouldn't expect from construction, i.e. intermediate computations and internal reasoning is written to the residuals using a sparse linear combination of these directions (the J-space). This J-space is localized to middle layers, privileged by the weights, and causally used for outputs for non-automatic tasks.

Two main applications: alignment auditing using the J-Lens, and post-training the model to reflect on good principles to instill ethics into its J-space naturally

vs NLAs: J-space is more mechanistic and actually causal, but limited to single token words in the vocab

# J-Lens

**"For every word in Claude's vocabulary, the J-lens finds the internal activity pattern that makes Claude more likely to say that word at some point in the future."**

Prior work: **Logitlens**

- Main idea: what if we took intermediate activations in an LLM forward pass and immediately applied the decode matrix to them, and read the highest scoring vocab logits to interpret those intermediate activations?
- <img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787202682989.png" width="393" />
   - output is the orange
- Core problem: the coordinate space (how concepts are represented) changes between intermediate layers and the last layer

J-lens solves this by first multiplying the intermediate activations by a fixed, averaged **jacobian** matrix of the last layer activations against the intermediate activations (a d_model x d_model matrix)

<img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787203121738.png" width="408" />

- Why is the jacobian the right transformation? It captures, to first order, how moving along like the vector representation of e.g. "France" in layer l will affect the outputs in layer L (in the current or future tokens), right before the decode

### How do we actually calculate J_l?

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787204428427.png)

- We draw a bunch of (prompt, source token pos, target token pos) and calculate the jacobian of (the last layer at target pos) wrt (layer l at source pos), and average them all (in the codebase they actually sum over t' but whatever it's not load-bearing).

**Why averaging:**

<img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787203667627.png" width="388" />

- **why average over prompts?** If you only use one prompt (e.g. the current one), you capture transformations of representations between early and late layers that are context-specific. By averaging over prompts, the context-specific parts cancel out
  - for instance, in the prompt "What is the capital of France", the representation of France at layer l -> the representation of Paris at layer L. What you really want is the direction from representation of France at layer l -> the representation of France at layer l, which you do get by using enough prompts so that you get many where France as a concept is statically carried throughout the layers
  - **this is actually really important:** this is why for prompts like "Count to 5. Also silently introspect", tokens like "consciousness" appear in the output, even though they would never normally appear in the output. The J-Lens is capturing "in a typical context, how would this concept in the intermediate layer affect the output," while for this specific context, something silences the introspection concept so it doesn't actually appear in the output.
- why sum over t'? We want to track how these intermediate concepts affect the model's ability to verbalize things in the future, even if the concept wouldn't affect the immediate next token
  - note that in practice, the jacobians from different token positions are probably way smaller than from same token position because of the missing residual connection (different token positions only affect through attention layers)

https://transformer-circuits.pub/2026/workspace/public/slice-stack/index.html

- Empirically, looking at the J-lens outputs, most are kinda garbage, especially early layers get a ton of "Biserica."
- It's cool that "the color of the planet fourth from the sun is" -> Mars, and "calc: (4+17)*2+7=" -> 21, 42

# J-lens vectors and J-space

The rows of W_U * J_l are (up to a constant for norms, which doesn't change relative ranking) the directions in R^d_model that activate each vocab word most strongly in the J-lens output. We call each of these row the **J-lens vectors**

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787206299115.png)

- If the RMSNorm layer has an elementwise gain multiplier, you can just do a bit of math to incorporate that into the J-lens vector
- ![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787373456474.png)

The **J-space** is just the space in R^d_model that's expressible as a sparse combination of at most k=25 J-lens vectors.

- Motivated by the empirical observation that only a small subset of J-Lens vectors have high dot product for given activations
- these k won't necessarily be the top k inner products due to non-orthogonality

**Interventions**

1. <img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787207997146.png" width="169" /> steer along a J-lens vector.
2. Swap two concepts in activations h: get the least squares coefficients of v_S and v_T for approximating h, and do intervention 1 along v_S and v_T to swap their coeffiicents.
3. (the J-space ablation used in 3.5.2): you want to remove the component in V = span(v_k). Get Q = the orthonormal d x k matrix with the same span as V (gram-schmidt), and P = QQ^T, then P is the projection matrix onto the span of V, and then do h - Ph to subtract off the projection onto those vectors.

# 3. J-space as a global workspace

## 3.1 J-space causally affects future verbalization

This claim is unsurprising because it's by construction of how we calculated the Jacobians.

Three experiments

**Experiment 1: immediate next token verbalization**

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787260841050.png)

- LHS and top right is super boring: Obviously, if you look at the last token, and you look at J-Lens close to the final layer, it's going to show the next predicted token
- bottom right is the causal intervention, doing the J-space concept swap between the intended output and another word. They need to do this intervention across all token positions, and across an unspecified number of layers, but it works

**Experiment 2: future token verbalization**

e.g., told that it's introspecting on a word, and then you intervene on the word that it's introspecting on, but don't ask it for the word until later

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787262582202.png)

- graph on the right is just showing that the intervention doesn't have a huge effect on the output until the decoded token at the end of the prompt, so J-Lens can read future verbalizable thoughts

**Experiment 3: only the J-space causally affects outputs**

Sure, the J-space can cause a successful intervention, but must a successful intervention be through the J-space?

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787262712848.png)

- get a concept vector by the method on the left (subtract activation by a bunch of averaged other concepts), take the J-space component (only explains 6% of variance), and then use those directions for the intervention swap instead of the J-lens vectors
- ![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787263331851.png)
- still retain most of the intervention success with only the small J-space component, no success without it

## 3.2 the J-space holds thoughts that don't necessarily make it into the final output

Like if the model is explicitly told to think about something while doing something else

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787266500823.png)

(funnily, this works somewhat even if it's told to "ignore X")

Or even if it's implicitly told to think about something (like part of speech)

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787266630994.png)

**Not too surprising: the J-lens is supposed to capture what the model is capable of verbalizing in the future if it needs to, I guess all this tells us is that the model does spend time thinking about this even though it's not needed for the output**

## 3.3 Emergent property 1: the J-space is causally used for storing intermediate computations

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787267523675.png)

Another example where Claude first has to decide whether to repeat the previous token or switch (it's a binary choice), and causally intervening on the strategy affects the output.

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787268093988.png)

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787268322938.png)

- Left: interventions work like 70% of the time
- Right: a nice control. You might be worried that the interventions are only working because they're swapping in the target answer on accident / correlatedly. The red line shows that at least for earlier layers, swapping in the target answer does worse than swapping in the target intermediate concept.

**Same pattern for proving that the J-space is privileged/unique in being an intermediate workspace:** Get the intervention constant vector without using J-space, and show that intervening on just the J-Space component is sufficient

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787269255416.png)

- Like before, clamping means holding the activations in the other component fixed to their pre-intervention values, so that e.g. the non-J-space components can't later downstream affect the J-space to affect the output

## 3.4 (weaker) Emergent propery 2: same J-lens vector used for many downstream tasks

It's not obvious that the same J-lens vector direction for a country that's used to later verbalize the country is the same representation as would be used for different tasks like getting its capital or language, etc. Turns out it is

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787270816639.png)

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787270938135.png)

- but for numbers and animals, it's less so, and this is predicted by the low cosine similarity of the residual stream and the J-lens vector for that concept.

Here they finally specify that the intervention is done "at every token position across a band of intermediate layers"

## 3.5 Automatic tasks don't use the J-space (but flexible inference and explicit report definitely do)

Flexible inference = answer something downstream about the country

Explicit report = explicitly ask the model to state the country

Most other tasks are what they call "automatic", which hand-wavily is something that doesn't require you to explicitly think about it

**If the above experiment was about what concepts are strongly or weakly represented in J-space, the below experiment is about what downstream tasks causally use the concepts represented in J-space**

**Figure 20:** Given a passage written in Spanish

- continuing the passage in Spanish: automatic
- detecting a different language section: automatic
- saying what language it's in: not automatic
- identifying author in the language, the word for hello, etc: not automatic

- control: in all four tasks, "Spanish" appears in J-lens the same amount

**They also find a task which doesn't have the concept in the J-space at all (and doesn't causally use it)**

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787274228160.png)

- continuation of a passage with line breaks at a given width: width not carried in J-Lens
- but it becomes causally carried ("brought in to") the J Lens when the task is reporting that width or doing some flexible inference with that width

**I'm noticing some rhyming here between the J-space paper and between my I2I-Interp paper: they also found two ish tasks that causally use the mechanism, some tasks which carry it non-causally, and some tasks which don't carry it at all** (but the model still knows the concept for its output)

### 3.5.2 Ablating the J-space's effect

At every token position, for some band of layers (vary how many layers for stronger or weaker ablation), ablate the k=10 top J-lens vector directions, _excluding tokens that appear in the top 10 tokens of the output_ (to not ablate tokens the model intended to output).

Expectedly, ablating multi-hop-reasoning tasks (like "how many legs does the Itsy Bitsy ___ have") has more effect than ablating a random pretraining token

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787276292157.png)

- notice the random ablation control

**Figure 23**: they looked at the tokens from the pretraining examples where the KL of the predicted next token distribution changed the most as a result of ablating J-space

- seemed to be where there was a specific completion and a reasonable generic completion, and knowing the specific completion depended on the context
  - e.g. \$8.71 vs \$8.50, ablating the J-space ablated Massachusetts, Boston, wage, etc which lost the fact that it was the 1914 MA min wage

Classifying a bunch of tasks based on the ones the J-space seems to be necessary for
![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787279055615.png)

They also do it on some model welfare prompts, find that ablating J-space makes its responses much less "experiential" and more mechanical

# 4. Structure of the J-space

## 4.1. J-space lives primarily in the middle layers

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787281823326.png)

- CKA is a way of calculating the similarity between two representations of the same set of things: (n x d_1), (n x d_2) -> [0, 1]. It's the cosine similarity of the flattened Gram matrices.
- holy moly look at that block structure, is that not convincing that there's three distinct layer groups (they admit this is cherry picked among models)

A bunch of other stats swept across layers that indicate the same layer range
![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787283527719.png)

- (b) is basically how concentrated the logits are in a few vocab tokens. Higher means it's not just noise.
- (c) is how autocorrelated the J-lens top-1 lens output is across token positions. Higher means more semantic (think like temporal SAE same idea, concepts should last across tokens)
- (d) this one kinda sus icl

**The most weirdly specifically cog-sci motivated experiment so far**: global workspace theory predicts that at the entry point to the workspace, exactly one interpretation of the input should win out suddenly, so they feed in mixed inputs like <img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787284938102.png" width="129" />

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787284916256.png)

- (b) is the important panel. This is not using J-Lens methodology at all, So the appearance of the workspace entry layer can't be from artifacts of how the J-Lens was calculated. The x-axis is varying alpha, the y-axis is layer, and the color is the fraction from pure-A-activation to pure-B-activation in R^d that the activation is. So whiter means ambiguous — notice how it becomes one or the other by the entry

## 4.2 Limited J-space capacity

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787289377429.png)
(caption good)

Some more vibes-y graphs about how it represents categories (e.g. animals) using a collection of J-lens vectors, but struggles to represent multiple categories at once

## 4.3 J-space gets preferential treatment in weights

**By MLPs:**

<img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787291668112.png" width="407" />

- ignore the MLP neuron line, the orange line shows that J-lens vectors get amplified by MLPs more than random directions

**By a subset of attention heads:**

Looking at the W_OV circuit of the head, we quantify its preference for a family of vectors by

1. Large gain: The mean of $\| W_{ov} v \|$ over v's
2. Directions being preserved: cos(W_ov v_i, v_i) being much larger than other cos(W_ov v_i, v_j), we desire this since J-lens vectors are independent of token position

Yep there do exist heads that preferentially treat the J-space

<img src="/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787293129599.png" width="424" />

and (Figure 34) if you ablate them, it has the effects you expect on downstream tasks.

# 5. Applications to Alignment Auditing

Ablating "fake, fictional, scenario, artificial, benchmark, simulation, mock" can reduce the model's awareness that it's in an eval (which normally makes it hide its desires)
![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787293762907.png)

J-lens can also be used to

- detect prompt injection awareness ("prompt", "injection").
- detect lying about numbers ("manipulation"), solving the bug vs cheating ("hiding", "secret")

### Model organism 1: emergent misalignment paper

Recall they SDF'd a model on documents describing reward hacking, then RL'd it on coding where it reward hacks, then RLHF'd it.

If you look for "fake, trick, fraud, secretly, hidden, and variants", you find it in the model organisms
![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787294652748.png)

Though this seems to be somewhat sensitive to what token you look at

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787294765515.png)

### Model organism 2: trained to believe that RLHF prefers certain quirks like chocolate good

"reward" and "bias" appear in the J-lens readouts no matter the prompt (even if the reward hack is irrelevant), and not for if you use logitlens for instance

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787295499782.png)

# 6. J-Lens reveals that post-trained models take on the Assistant persona

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787296797575.png)

- The post-trained model is already thinking about what the assistant would say when processing the user's tokens.

Post-trained model only also

1. recognizes it is role playing (i.e. "disclaimer" and "fictional" when system prompt makes it play a persona)
2. "BUT" when it gets prefilled with something it disagrees with (but in the actual output it goes along with it anyways)
3. "damn" when it fails at ignoring a thought that it was told to ignore.

# 7. Counterfactual Reflection Training

Idea: If the J space is causal and the J space is just a reflection of what the model could verbalize in the future, why don't we train the model to verbalize honesty and integrity in moments where it would otherwise reward hack?

![](/assets/img/distillations/verbalizable-representations-form-a-global-workspace-in-language-models/img-1787342823113.png)

- during RL, when model has reward hacked or may reward hack, pause, ask it to generate a reflection grounded in Anthropic's constitution, and then train on just the reflection

This results in decreased reward hacking and increased "reflection" "ethical" "honestly" etc in the J-space, and the reward hacking mostly comes back if you ablate these concepts in the J-space.
