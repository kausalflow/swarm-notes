---
# CSL-compatible fields
title: "WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving"
author:
  - literal: "Xuerun Yan"
  - literal: "Zhexi Lian"
  - literal: "Nuoheng Zhang"
  - literal: "Shiyu Fang"
  - literal: "Haoran Wang"
  - literal: "Chen Lv"
  - literal: "Jia Hu"
  - literal: "Binyang Song"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08375"

# Custom fields
paper_id: "2607.08375"
paper_source: "openalex"
domain: "robotics"
tags:
  - "vision-language-model"
  - "vlm"
  - "diffusion-model"
  - "chain-of-thought"
  - "autonomous-agent"
  - "planning"
  - "multimodal"
  - "benchmark"
architectures:
  []
datasets:
  - "navsim"
concept_slugs:
  - "game-theoretic-chain-of-thought-game-cot"
  - "aligned-decoupled-diffusion-transformer-addt"
dataset_slugs:
  - "navsim"
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:28:13Z"
created_at: "2026-07-12T07:28:13Z"
---

# WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving

**Authors**: Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08375](https://arxiv.org/abs/2607.08375)

## Summary

WCog-VLA is a novel Vision-Language-Action framework designed to transition end-to-end autonomous driving from reactive to proactive behavior. The model employs a dual-level approach, integrating Game-theoretic Chain-of-Thought (Game-CoT) reasoning at the semantic level and an Aligned Decoupled Diffusion Transformer (ADDT) at the generative level. This architecture effectively unifies 3D spatial perception, agent-token dynamics, and physically-plausible multi-agent trajectory synthesis. Experimental results on the NAVSIM benchmark demonstrate that the framework achieves state-of-the-art performance with accelerated inference capabilities.

## Key Contributions

- Proposes WCog-VLA, a dual-level VLA framework that bridges semantic forecasting and generative world evolution for proactive driving.
- Introduces Game-CoT reasoning to unify 3D spatial perception with strategic, agent-aware cognition.
- Develops the ADDT architecture to synthesize joint multi-agent trajectories with reduced denoising steps and accelerated inference.
- Achieves a State-Of-The-Art PDMS score of 92.9 on the NAVSIM benchmark using a new 85k Game-CoT annotated dataset.

## Open Questions & Future Work

- [[comprehensive-road-topology-modeling]]

## Key Concepts

- [[game-theoretic-chain-of-thought-game-cot]]: A reasoning framework that integrates game-theoretic principles into Chain-of-Thought for strategic autonomous driving.
- [[aligned-decoupled-diffusion-transformer-addt]]: A generative world model architecture designed for accelerated inference and physically-plausible multi-agent trajectory synthesis.

## Archivist Review

The paper introduces a structured dual-level approach to proactive driving by combining Game-CoT for semantic reasoning and ADDT for trajectory generation. The selected concepts are central to this framework and represent reusable methodological advancements. The open question regarding road topology addresses a significant gap in current world-modeling literature.

### Approved Concepts
- Game-theoretic Chain-of-Thought (Game-CoT): Central to the model's ability to perform proactive strategic reasoning in multi-agent driving scenarios.
- Aligned Decoupled Diffusion Transformer (ADDT): Key generative architecture component that accelerates inference for physically-plausible multi-agent trajectory prediction.

### Approved Open Questions
- Modeling dynamic road topology: Expanding world cognition from agent-centric dynamics to include static environment evolution is critical for navigating complex scenarios where infrastructure constraints influence path planning.

## Datasets

- [[navsim]]

## Links

- [Abstract](https://arxiv.org/abs/2607.08375)
- [PDF](https://arxiv.org/pdf/2607.08375)

