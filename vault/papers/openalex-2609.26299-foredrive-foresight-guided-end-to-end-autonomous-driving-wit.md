---
# CSL-compatible fields
title: "ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model"
author:
  - literal: "Sinuo Wang"
  - literal: "Zichong Gu"
  - literal: "Yuhan Huang"
  - literal: "Wenxin Wen"
  - literal: "Xun Yang"
  - literal: "Yiqing Zhang"
  - literal: "Xingyu Zhang"
  - literal: "Ningyu Che"
  - literal: "Jie Ling"
  - literal: "Qiankun Yu"
  - literal: "Wei Liu"
  - literal: "Jing Xu"
  - literal: "Xinggang Wang"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26299"

# Custom fields
paper_id: "2609.26299"
paper_source: "openalex"
domain: "robotics"
tags:
  - "autonomous-agent"
  - "diffusion-model"
  - "multimodal"
  - "planning"
  - "reinforcement-learning"
architectures:
  - "decoder-only"
datasets:
  - "navsim"
concept_slugs:
  []
dataset_slugs:
  - "navsim"
skill: "TimeSeriesSkill"
processed_at: "2026-09-25T09:55:35Z"
created_at: "2026-09-25T09:55:35Z"
---

# ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model

**Authors**: Sinuo Wang, Zichong Gu, Yuhan Huang, Wenxin Wen, Xun Yang, Yiqing Zhang, Xingyu Zhang, Ningyu Che, Jie Ling, Qiankun Yu, Wei Liu, Jing Xu, Xinggang Wang
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26299](https://arxiv.org/abs/2609.26299)

## Summary

ForeDrive is an end-to-end autonomous driving framework that addresses the misalignment between standard predictive latent world models and downstream planning needs. By employing a JEPA-style world model with asymmetric gradient routing, ForeDrive learns planning-relevant multi-horizon latent representations that guide a Diffusion Transformer planner via gated fusion, future-status injection, and Trajectory-Adaptive Bias. Trained solely through imitation learning using front-view camera inputs, the method achieves 89.9 PDMS on NAVSIM v1 and 90.0 one-stage EPDMS on NAVSIM v2 without reinforcement learning or external trajectory scoring.

## Key Contributions

- Proposes ForeDrive, an end-to-end autonomous driving framework that couples a JEPA-style latent world model asymmetrically to a Diffusion Transformer planner using planning-relevant representations.
- Introduces gated visual fusion, future-status injection, and Trajectory-Adaptive Bias (TAB) to condition trajectory generation on multi-horizon latent futures without overriding current observations.
- Achieves state-of-the-art performance of 89.9 PDMS on NAVSIM v1 and 90.0 one-stage EPDMS on NAVSIM v2 using pure imitation learning and a single front-view image at inference.

## Open Questions & Future Work

- [[interactive-closed-loop-evaluation-in-autonomous-driving]]

## Archivist Review

The review policy requires strict filtering against paper-local architectures and submodules. ForeDrive and its internal asymmetric gradient routing are too paper-specific to warrant standalone permanent vault concepts. The NAVSIM dataset is canonical and reusable, and the open question regarding interactive closed-loop evaluation is generalized appropriately.

### Approved Open Questions
- Interactive Closed-Loop Evaluation in Autonomous Driving: Testing under interactive closed-loop settings remains a key requirement for verifying whether foresight-guided planning generalizes past open-loop playback.

### Rejected Candidates
- [concept] ForeDrive (`foredrive`) - paper_local: ForeDrive is a paper-specific end-to-end autonomous driving framework rather than a reusable vault concept.
- [concept] Asymmetric Latent World Model Coupling (`asymmetric-latent-world-model-coupling`) - subcomponent_of_broader_mechanism: This is a paper-specific subcomponent and architectural routing mechanism for combining a JEPA world model and a DiT planner.

## Datasets

- [[navsim]]

## Links

- [Abstract](https://arxiv.org/abs/2609.26299)
- [PDF](https://arxiv.org/pdf/2609.26299)

