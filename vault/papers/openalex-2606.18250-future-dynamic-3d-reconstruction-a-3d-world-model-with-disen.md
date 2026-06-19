---
# CSL-compatible fields
title: "Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion"
author:
  - literal: "Nils Morbitzer"
  - literal: "Jonathan Evers"
  - literal: "Artem Savkin"
  - literal: "Thomas Stauner"
  - literal: "Nassir Navab"
  - literal: "Federico Tombari"
  - literal: "Stefano Gasperini"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.18250"

# Custom fields
paper_id: "2606.18250"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "world-model"
  - "3d-reconstruction"
  - "generative-model"
  - "zero-shot-learning"
  - "knowledge-distillation"
  - "autonomous-agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fr3d-world-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:25:39Z"
created_at: "2026-06-19T09:25:39Z"
---

# Future Dynamic 3D Reconstruction: A 3D World Model with Disentangled Ego-Motion

**Authors**: Nils Morbitzer, Jonathan Evers, Artem Savkin, Thomas Stauner, Nassir Navab, Federico Tombari, Stefano Gasperini
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.18250](https://arxiv.org/abs/2606.18250)

## Summary

FR3D addresses the limitations of 2D generative world models, which often suffer from physical inconsistencies like morphing when forecasting long-horizon dynamics. The model predicts a persistent 3D latent representation, effectively decoupling the scene's dynamic evolution from the agent's ego-motion. This architectural choice improves geometric consistency, and the proposed distillation strategy leverages existing foundation models to enhance zero-shot generalization performance.

## Key Contributions

- Proposes FR3D, a 3D world model that explicitly decouples 3D environmental evolution from agent ego-motion using latent proxies.
- Enables geometrically consistent future dynamic 3D reconstruction from monocular observations.
- Introduces a teacher-student distillation strategy to integrate spatial common sense from foundation models for improved zero-shot generalization.

## Open Questions & Future Work

- [[mitigating-motion-bias-and-scale-drift-in-3d-world-models]]

## Key Concepts

- [[fr3d-world-model]]: A world model that predicts persistent 3D latent representations by decoupling environmental scene evolution from agent ego-motion as a latent proxy for action.

## Archivist Review

I have approved the core FR3D architectural mechanism as it introduces a reusable paradigm for 3D world modeling by disentangling ego-motion from scene dynamics. I also approved the identified open question regarding scale drift and motion bias, as these are critical, non-trivial bottlenecks for long-horizon dynamic 3D reconstruction. No datasets were approved as none provided in the candidate list met the criteria for a central, high-reusability benchmark.

### Approved Concepts
- FR3D World Model: This model addresses the common issue of physical inconsistencies in 2D-based world models by explicitly decoupling 3D scene evolution from ego-motion.

### Approved Open Questions
- Mitigating Motion Bias and Scale Drift: Scale drift and motion bias are fundamental barriers to the reliability and physical consistency of autonomous world models.

### Rejected Candidates
- [concept] FR3D (`fr3d`) - other: Renamed to fr3d-world-model for better clarity and to avoid conflict with standard acronym naming conventions.

## Links

- [Abstract](https://arxiv.org/abs/2606.18250)
- [PDF](https://arxiv.org/pdf/2606.18250)

