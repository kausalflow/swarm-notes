---
# CSL-compatible fields
title: "Spatially Prompted Visual Trajectory Prediction for Egocentric Manipulation"
author:
  - literal: "Yifan Li"
  - literal: "Xinyu Zhou"
  - literal: "Yunhao Ge"
  - literal: "Yu Kong"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.20085"

# Custom fields
paper_id: "2605.20085"
paper_source: "openalex"
domain: "robotics,computer-vision,multimodal"
tags:
  - "multimodal"
  - "vision-language-model"
  - "robotics"
  - "trajectory-prediction"
  - "dataset"
  - "benchmark"
  - "autonomous-agent"
architectures:
  []
datasets:
  - "EgoSPT"
concept_slugs:
  - "spatially-prompted-visual-trajectory-prediction-sp-vtp"
dataset_slugs:
  - "egospt"
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:18:07Z"
created_at: "2026-05-22T08:18:07Z"
---

# Spatially Prompted Visual Trajectory Prediction for Egocentric Manipulation

**Authors**: Yifan Li, Xinyu Zhou, Yunhao Ge, Yu Kong
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.20085](https://arxiv.org/abs/2605.20085)

## Summary

This paper introduces Spatially Prompted Visual Trajectory Prediction (SP-VTP), a novel task setting that specifies robotic manipulation objectives via spatial prompts like bounding boxes or points. To support this, the authors collect the EgoSPT dataset, which links egocentric video with spatial grounding and 3D end-effector trajectories. They also propose the Spatially Prompted Object-Target Policy (SPOT), a model architecture that aligns static spatial task definitions with evolving egocentric observations for more robust motion forecasting. Experiments demonstrate that SPOT outperforms baselines in cross-scene generalization, validating the utility of spatial prompting for scalable robot manipulation.

## Key Contributions

- Formalizes the novel Spatially Prompted Visual Trajectory Prediction (SP-VTP) task for egocentric robotic manipulation.
- Introduces EgoSPT, a dataset providing first-frame spatial grounding and 3D end-effector motion for egocentric manipulation trajectories.
- Proposes SPOT (Spatially Prompted Object-Target Policy), an architecture utilizing task and observation encoders to improve cross-scene trajectory prediction under dynamic scene configurations.

## Open Questions & Future Work

- [[mitigating-compounding-drift-stitching]]

## Key Concepts

- [[spatially-prompted-visual-trajectory-prediction-sp-vtp]]: A formalization of trajectory prediction for robotic manipulation that uses spatial prompts (e.g., bounding boxes/points) to define task objectives in egocentric streams.

## Archivist Review

The paper formalizes a new task setting (SP-VTP) which is highly reusable. I approved the core definition and the primary dataset, as well as an open question regarding compounding drift, which is a significant technical challenge in trajectory prediction. I rejected the proposal to 'expand task diversity' as it represents standard dataset expansion rather than a foundational research problem.

### Approved Concepts
- Spatially Prompted Visual Trajectory Prediction (SP-VTP): Establishes a new formal problem setting for robotics trajectory prediction using spatial grounding rather than just language.

### Approved Open Questions
- Mitigating Compounding Stitched Drift: This is a fundamental limitation of the proposed autoregressive or chunked-prediction paradigm, which currently prevents reliable long-term deployment in closed-loop systems.

### Rejected Candidates
- [open_question] Expanding SP-VTP Task Diversity (`scaling-task-diversity-spvtp`) - low_impact: This is boilerplate future work regarding dataset scale and object variety rather than an unresolved methodological bottleneck.

## Datasets

- [[egospt]]

## Links

- [Abstract](https://arxiv.org/abs/2605.20085)
- [PDF](https://arxiv.org/pdf/2605.20085)

