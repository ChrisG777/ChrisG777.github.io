// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-reading-notes",
          title: "reading notes",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/reading-notes/";
          },
        },{id: "post-generative-modeling-via-drifting",
        
          title: "Generative Modeling via Drifting",
        
        description: "Drifting",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/generative-modeling-via-drifting/";
          
        },
      },{id: "post-flux-1-kontext-flow-matching-for-in-context-image-generation-and-editing-in-latent-space",
        
          title: "FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space...",
        
        description: "Flux.1 Kontext",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/flux-1-kontext-flow-matching-for-in-context-image-generation-and-editing-in-late/";
          
        },
      },{id: "post-maxrl-maximum-likelihood-via-reinforcement-learning",
        
          title: "MaxRL: Maximum Likelihood via Reinforcement Learning",
        
        description: "Maximum likelihood RL",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/maxrl-maximum-likelihood-via-reinforcement-learning/";
          
        },
      },{id: "post-circuit-mechanisms-for-spatial-relation-generation-in-diffusion-transformers",
        
          title: "Circuit Mechanisms for Spatial Relation Generation in Diffusion Transformers",
        
        description: "Circuits in DiTs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/circuits-in-dits/";
          
        },
      },{id: "post-same-task-different-circuits-disentangling-modality-specific-mechanisms-in-vlms",
        
          title: "Same Task, Different Circuits: Disentangling Modality-Specific Mechanisms in VLMs",
        
        description: "modality specific circuits",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/modality-specific-circuits/";
          
        },
      },{id: "post-position-aware-automatic-circuit-discovery",
        
          title: "Position-aware Automatic Circuit Discovery",
        
        description: "position aware circuits",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/position-aware-circuit-discovery/";
          
        },
      },{id: "post-arithmetic-without-algorithms-language-models-solve-math-with-a-bag-of-heuristics",
        
          title: "Arithmetic Without Algorithms: Language Models Solve Math With a Bag of Heuristics",
        
        description: "arithmetic heuristics",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/arithmetic-heuristics/";
          
        },
      },{id: "post-neural-thickets-diverse-task-experts-are-dense-around-pretrained-weights",
        
          title: "Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights",
        
        description: "neural thickets",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/neural-thickets/";
          
        },
      },{id: "post-attention-residuals",
        
          title: "Attention Residuals",
        
        description: "attention residuals",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/attention-residuals/";
          
        },
      },{id: "post-fine-tuning-enhances-existing-mechanisms-a-case-study-on-entity-tracking",
        
          title: "Fine-Tuning Enhances Existing Mechanisms: A Case Study on Entity Tracking",
        
        description: "circuits in fine-tunes",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/nikhil-circuits-in-fine-tunes/";
          
        },
      },{id: "post-causal-abstractions-of-neural-networks",
        
          title: "Causal Abstractions of Neural Networks",
        
        description: "Causal abstractions",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/stanford-atticus-geiger-causal-abstractions/";
          
        },
      },{id: "post-end-to-end-test-time-training-for-long-context",
        
          title: "End-to-End Test-Time Training for Long Context",
        
        description: "TTT-E2E",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/stanford-nlp-ttt-e2e/";
          
        },
      },{id: "post-interpreting-physics-in-video-world-models",
        
          title: "Interpreting Physics in Video World Models",
        
        description: "physics in video models \+ V-JEPA background",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/meta-interpreting-physics-in-video-world-models/";
          
        },
      },{id: "post-language-models-use-lookbacks-to-track-beliefs",
        
          title: "Language Models use Lookbacks to Track Beliefs",
        
        description: "lookback mechanisms",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/tamar-lookback-mechanisms/";
          
        },
      },{id: "post-fast-kv-compaction-via-attention-matching",
        
          title: "Fast KV Compaction via Attention Matching",
        
        description: "Zweiger KV compaction",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/zweiger-kv-compaction/";
          
        },
      },{id: "post-bridge-predicting-human-task-completion-time-from-model-performance",
        
          title: "BRIDGE: Predicting Human Task Completion Time From Model Performance",
        
        description: "Predicting Human Time from IRT difficulty",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/predicting-human-time-from-irt-difficulty/";
          
        },
      },{id: "post-hunyuanvideo-a-systematic-framework-for-large-video-generative-models",
        
          title: "HunyuanVideo: A Systematic Framework For Large Video Generative Models",
        
        description: "Hunyuan video",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/hunyuan-video/";
          
        },
      },{id: "post-exploring-multimodal-diffusion-transformers-for-enhanced-prompt-based-image-editing",
        
          title: "Exploring Multimodal Diffusion Transformers for Enhanced Prompt-based Image Editing",
        
        description: "activation patching and attention maps in MM-DiTs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/exploring-attention-for-mm-dit-image-editing/";
          
        },
      },{id: "post-unraveling-mmdit-blocks-training-free-analysis-and-enhancement-of-text-conditioned-diffusion",
        
          title: "Unraveling MMDiT Blocks: Training-free Analysis and Enhancement of Text-conditioned Diffusion",
        
        description: "scaling text embeddings for Image Editing",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/analyzing-mmdit-blocks-scaling-text-embeddings-for-image-editing/";
          
        },
      },{id: "post-stable-flow-vital-layers-for-training-free-image-editing",
        
          title: "Stable Flow: Vital Layers for Training-Free Image Editing",
        
        description: "Vital Layers for Image Editing",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/vital-layers-for-image-editing/";
          
        },
      },{id: "post-localizing-knowledge-in-diffusion-transformers",
        
          title: "Localizing Knowledge in Diffusion Transformers",
        
        description: "Localizing Knowledge in DiTs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/localizing-knowledge-in-dit-s/";
          
        },
      },{id: "post-tutorial-on-diffusion-models-for-imaging-and-vision",
        
          title: "Tutorial on Diffusion Models for Imaging and Vision",
        
        description: "Tutorial on diffusion models",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/tutorial-on-diffusion-models/";
          
        },
      },{id: "post-learning-to-discover-at-test-time",
        
          title: "Learning to Discover at Test Time",
        
        description: "TTT-Discover",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/ttt-discover-test-time-training-discover/";
          
        },
      },{id: "post-conceptattention-diffusion-transformers-learn-highly-interpretable-features",
        
          title: "ConceptAttention: Diffusion Transformers Learn Highly Interpretable Features",
        
        description: "ConceptAttention",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/conceptattention-diffusion-interp/";
          
        },
      },{id: "post-recursive-language-models",
        
          title: "Recursive Language Models",
        
        description: "RLMs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/mit-alex-zhang-recursive-language-models/";
          
        },
      },{id: "post-flux-2-analyzing-and-enhancing-the-latent-space-of-flux-representation-comparison",
        
          title: "FLUX.2: Analyzing and Enhancing the Latent Space of FLUX – Representation Comparison",
        
        description: "Flux 2 technical reports",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/flux-2-technical-reports/";
          
        },
      },{id: "post-scaling-rectified-flow-transformers-for-high-resolution-image-synthesis",
        
          title: "Scaling Rectified Flow Transformers for High-Resolution Image Synthesis",
        
        description: "MM-DiTs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/scaling-rectified-flow/";
          
        },
      },{id: "post-scalable-diffusion-models-with-transformers",
        
          title: "Scalable Diffusion Models with Transformers",
        
        description: "Diffusion Transformers",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/diffusion-transformer/";
          
        },
      },{id: "post-flow-straight-and-fast-learning-to-generate-and-transfer-data-with-rectified-flow",
        
          title: "Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow...",
        
        description: "Rectified Flow",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/rectified-flow/";
          
        },
      },{id: "post-the-adolescence-of-technology",
        
          title: "The Adolescence of Technology",
        
        description: "Dario Amodei risks essay",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/dario-amodei-the-adolescence-of-technology/";
          
        },
      },{id: "post-diffusion-meets-flow-matching-two-sides-of-the-same-coin",
        
          title: "Diffusion Meets Flow Matching: Two Sides of the Same Coin",
        
        description: "Diffusion equals Flow Matching",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/gdm-diffusion-meets-flow-matching/";
          
        },
      },{id: "post-mhc-manifold-constrained-hyper-connections",
        
          title: "mHC: Manifold-Constrained Hyper-Connections",
        
        description: "DeepSeek manifold constrained hyper connections",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/deepseek-manifold-constrained-hyper-connections/";
          
        },
      },{id: "post-a-rosetta-stone-for-ai-benchmarks",
        
          title: "A Rosetta Stone for AI Benchmarks",
        
        description: "Epoch AI Rosetta Stone for AI benchmarks",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/epoch-ai-rosetta-stone-for-ai-benchmarks/";
          
        },
      },{id: "post-measuring-ai-ability-to-complete-long-software-tasks",
        
          title: "Measuring AI Ability to Complete Long Software Tasks",
        
        description: "METR Long Tasks AI",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/metr-long-tasks-ai/";
          
        },
      },{id: "post-on-scalable-oversight-with-weak-llms-judging-strong-llms",
        
          title: "On scalable oversight with weak LLMs judging strong LLMs",
        
        description: "GDM scalable oversight",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/gdm-scalable-oversight-with-weak-llms-judging-strong-llms/";
          
        },
      },{id: "post-reliable-and-efficient-amortized-model-based-evaluation",
        
          title: "Reliable and Efficient Amortized Model-based Evaluation",
        
        description: "IRT difficulty prediction",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/irt-amortized-calibrator/";
          
        },
      },{id: "post-sliderspace-decomposing-the-visual-capabilities-of-diffusion-models",
        
          title: "SliderSpace: Decomposing the Visual Capabilities of Diffusion Models",
        
        description: "Sliderspace",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/david-bau-sliderspace/";
          
        },
      },{id: "post-sliderspace-decomposing-the-visual-capabilities-of-diffusion-models",
        
          title: "SliderSpace: Decomposing the Visual Capabilities of Diffusion Models",
        
        description: "concept sliders",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/david-bau-sliders/";
          
        },
      },{id: "post-generative-modeling-by-estimating-gradients-of-the-data-distribution",
        
          title: "Generative Modeling by Estimating Gradients of the Data Distribution",
        
        description: "score function generative modeling",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/yang-song-score-based-generative-modeling/";
          
        },
      },{id: "post-what-are-diffusion-models",
        
          title: "What are Diffusion Models?",
        
        description: "Lilian Weng Diffusion Blog Post (Discrete)",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/lilian-weng-diffusion-blog-post-discrete/";
          
        },
      },{id: "post-building-diffusion-model-39-s-theory-from-ground-up",
        
          title: "Building Diffusion Model&#39;s theory from ground up",
        
        description: "ICLR Diffusion explained blogpost",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/iclr-diffusion-explained-blogpost/";
          
        },
      },{id: "post-weight-sparse-transformers-have-interpretable-circuits",
        
          title: "Weight-sparse transformers have interpretable circuits",
        
        description: "Leo Gao OpenAI sparse circuits",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/leo-gao-openai-sparse-circuits/";
          
        },
      },{id: "post-between-the-bars-gradient-based-jailbreaks-are-bugs-that-induce-features",
        
          title: "Between the Bars: Gradient-based Jailbreaks are Bugs that induce Features",
        
        description: "Gradient Based Jailbreaking",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/fulcrum-mit-gradient-based-jailbreaking/";
          
        },
      },{id: "post-breakpoint-scalable-evaluation-of-system-level-reasoning-in-llm-code-agents",
        
          title: "Breakpoint: Scalable evaluation of system-level reasoning in LLM code agents",
        
        description: "Breakpoint",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/fulcrum-mit-breakpoint-scalable-system-level-coding-evals/";
          
        },
      },{id: "post-fluid-language-model-benchmarking",
        
          title: "Fluid Language Model Benchmarking",
        
        description: "Fluid model benchmarking",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/allen-institute-fluid-model-benchmarking/";
          
        },
      },{id: "post-auditing-language-models-for-hidden-objectives",
        
          title: "Auditing language models for hidden objectives",
        
        description: "auditing model internals",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/anthropic-auditing-model-internals/";
          
        },
      },{id: "post-deepseekmath-v2-towards-self-verifiable-mathematical-reasoning",
        
          title: "DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning",
        
        description: "DeepseekMath2",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/deepseekmath2/";
          
        },
      },{id: "post-deepseek-v3-2-pushing-the-frontier-of-open-large-language-models",
        
          title: "DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models",
        
        description: "Deepseek V3.2",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/deepseek-v3.2/";
          
        },
      },{id: "post-multiagent-finetuning-self-improvement-with-diverse-reasoning-chains",
        
          title: "Multiagent Finetuning: Self Improvement with Diverse Reasoning Chains",
        
        description: "Multiagent Fine Tunes",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-multiagent-fine-tunes/";
          
        },
      },{id: "post-ml-tea-planning-and-problem-solving-with-general-scalable-neuro-symbolic-models",
        
          title: "ML Tea: Planning and Problem-Solving with General, Scalable Neuro-Symbolic Models",
        
        description: "ML Tea LLMs \+ symbolic computing",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/ml-tea-llms-symbolic-computing/";
          
        },
      },{id: "post-automated-detection-of-visual-attribute-reliance-with-a-self-reflective-agent",
        
          title: "Automated Detection of Visual Attribute Reliance with a Self-Reflective Agent",
        
        description: "SAIA",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/christy-li-saia-vision-spurious-correlations/";
          
        },
      },{id: "post-continuous-language-model-interpolation-yields-dynamic-and-controllable-text-generation",
        
          title: "Continuous Language Model Interpolation yields Dynamic and Controllable Text Generation",
        
        description: "continuous model interpolation with lora",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/harvard-continuous-model-interpolation/";
          
        },
      },{id: "post-natural-emergent-misalignment-from-reward-hacking-in-production-rl",
        
          title: "Natural Emergent Misalignment from Reward Hacking in Production RL",
        
        description: "Anthropic emergent misalignment",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/anthropic-emergent-misalignment/";
          
        },
      },{id: "post-a-mathematical-framework-for-transformer-circuits",
        
          title: "A Mathematical Framework for Transformer Circuits",
        
        description: "Transformer Circuits Framework",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/anthropic-transformer-mathematical-circuits/";
          
        },
      },{id: "post-value-augmented-sampling-for-language-model-alignment-and-personalization",
        
          title: "Value Augmented Sampling for Language Model Alignment and Personalization",
        
        description: "Value Augmented Sampling",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-value-augmented-sampling/";
          
        },
      },{id: "post-deriving-muon",
        
          title: "Deriving Muon",
        
        description: "Muon",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/muon/";
          
        },
      },{id: "post-curiosity-driven-red-teaming-for-large-language-models",
        
          title: "Curiosity-driven Red-teaming for Large Language Models",
        
        description: "Curiosity Driven Red Teaming",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-curiosity-driven-red-teaming/";
          
        },
      },{id: "post-guided-speculative-inference-for-efficient-test-time-alignment-of-llms",
        
          title: "Guided Speculative Inference for Efficient Test-Time Alignment of LLMs",
        
        description: "Harvard Guided speculative decoding",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/harvard-guided-speculative-decoding/";
          
        },
      },{id: "post-superhuman-ai-for-stratego-using-self-play-reinforcement-learning-and-test-time-search",
        
          title: "Superhuman AI for Stratego Using Self-Play Reinforcement Learning and Test-Time Search",
        
        description: "Stratego",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/cmu-stratego/";
          
        },
      },{id: "post-domain-aware-scaling-laws-uncover-data-synergy",
        
          title: "Domain-Aware Scaling Laws Uncover Data Synergy",
        
        description: "Data domain synergy in scaling laws",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/domain-aware-scaling-laws-uncover-data-synergy/";
          
        },
      },{id: "post-data-debiasing-with-datamodels-d3m-improving-subgroup-robustness-via-data-selection",
        
          title: "Data Debiasing with Datamodels (D3M): Improving Subgroup Robustness via Data Selection",
        
        description: "Debiasing data using TRAK",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/data-debiasing-with-datamodels-d3m-improving-subgroup-robustness-via-data-select/";
          
        },
      },{id: "post-ambient-diffusion-omni-training-good-models-with-bad-data",
        
          title: "Ambient Diffusion Omni: Training Good Models with Bad Data",
        
        description: "diffusion using low quality data",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/ambient-diffusion-omni-training-good-models-with-bad-data/";
          
        },
      },{id: "post-boomerang-distillation-enables-zero-shot-model-size-interpolation",
        
          title: "Boomerang Distillation Enables Zero-Shot Model Size Interpolation",
        
        description: "Boomerang Distillation",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/harvard-boomerang-distillation/";
          
        },
      },{id: "post-to-backtrack-or-not-to-backtrack-when-sequential-search-limits-model-reasoning",
        
          title: "To Backtrack or Not to Backtrack: When Sequential Search Limits Model Reasoning",
        
        description: "Backtracking vs Best of n",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/harvard-backtracking-vs-best-of-n/";
          
        },
      },{id: "post-training-language-models-to-self-correct-via-reinforcement-learning",
        
          title: "Training Language Models to Self-Correct via Reinforcement Learning",
        
        description: "Aviral Kumar self-correcting LLMs",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/deepmind-self-correcting-llms/";
          
        },
      },{id: "post-colbert-efficient-and-effective-passage-search-via-contextualized-late-interaction-over-bert",
        
          title: "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT",
        
        description: "MIT ColBERT",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-colbert/";
          
        },
      },{id: "post-large-language-diffusion-models",
        
          title: "Large Language Diffusion Models",
        
        description: "LLaDA",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/llada/";
          
        },
      },{id: "post-teaching-ai-to-see-the-world-more-like-we-do",
        
          title: "Teaching AI to see the world more like we do",
        
        description: "Deepmind Align Vision Representations",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/deepmind-align-vision-representations/";
          
        },
      },{id: "post-self-adapting-language-models",
        
          title: "Self-Adapting Language Models",
        
        description: "Zweiger et al SEAL continual learning",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-zweiger-et-al-seal/";
          
        },
      },{id: "post-the-surprising-effectiveness-of-test-time-training-for-few-shot-learning",
        
          title: "The Surprising Effectiveness of Test-Time Training for Few-Shot Learning",
        
        description: "TTT for ARC and BBH",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-ttt-for-arc-and-bbh/";
          
        },
      },{id: "post-reasoning-or-reciting-exploring-the-capabilities-and-limitations-of-language-models-through-counterfactual-tasks",
        
          title: "Reasoning or reciting? Exploring the capabilities and limitations of language models through counterfactual...",
        
        description: "Reasoning or Reciting",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/mit-reasoning-or-reciting/";
          
        },
      },{id: "post-nested-learning-the-illusion-of-deep-learning-architecture",
        
          title: "Nested Learning: The Illusion of Deep Learning Architecture",
        
        description: "Deepmind Nested Learning short paper",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/deepmind-nested-learning/";
          
        },
      },{id: "post-lora-without-regret",
        
          title: "LoRA Without Regret",
        
        description: "LoRA blogpost",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2025/thinky-lora-without-regret/";
          
        },
      },{id: "books-the-godfather",
          title: 'The Godfather',
          description: "",
          section: "Books",handler: () => {
              window.location.href = "/books/the_godfather/";
            },},{id: "projects-phoneme-bridges",
          title: 'Phoneme Bridges',
          description: "We augment textual data with phonetic information in order to improve cross-lingual transfer from Hindi, a high-resource language, to Urdu, a low-resource language that shares many words but with a different written script. Done as a group project for 6.8611 Natural Language Processing.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/phoneme-bridges/";
            },},{id: "projects-team-leduc-poker",
          title: 'Team Leduc Poker',
          description: "We used multi-agent learning algorithms to find a correlated equilibrium of the Team Leduc Hold&#39;em game, a variant of Leduc poker where players 1 &amp; 3 and players 2 &amp; 4 play as a team without being able to communicate privately during the game. We submitted our strategies as part of the poker competition for MIT 6.S890 Multiagent Learning and got 2nd place.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/team-leduc-poker/";
            },},{id: "teachings-data-science-fundamentals",
          title: 'Data Science Fundamentals',
          description: "This course covers the foundational aspects of data science, including data collection, cleaning, analysis, and visualization. Students will learn practical skills for working with real-world datasets.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/data-science-fundamentals/";
            },},{id: "teachings-introduction-to-machine-learning",
          title: 'Introduction to Machine Learning',
          description: "This course provides an introduction to machine learning concepts, algorithms, and applications. Students will learn about supervised and unsupervised learning, model evaluation, and practical implementations.",
          section: "Teachings",handler: () => {
              window.location.href = "/teachings/introduction-to-machine-learning/";
            },},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%63%67%65%37@%6D%69%74.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/ChrisG777", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/chris-ge1", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/ChrisGe05", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=azZvdCoAAAAJ", "_blank");
        },
      },];
