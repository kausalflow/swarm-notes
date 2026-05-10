---
# CSL-compatible fields
title: "Render, Don't Decode: Weight-Space World Models with Latent Structural Disentanglement"
author:
  - literal: "Roussel Desmond Nzoyem"
  - literal: "Mauro Comi"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.06298"

# Custom fields
paper_id: "2605.06298"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "generative-adversarial-network"
  - "transformer"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nova-world-modeling-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:27Z"
created_at: "2026-05-10T07:23:27Z"
---

# Render, Don't Decode: Weight-Space World Models with Latent Structural Disentanglement

**Authors**: Roussel Desmond Nzoyem, Mauro Comi
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.06298](https://arxiv.org/abs/2605.06298)

## Summary

NOVA is a world modeling framework that replaces traditional opaque latent spaces with the weights of coordinate-based implicit neural representations (INRs). By analytically rendering these weights, the model eliminates the need for computationally heavy decoders, resulting in increased compactness and zero-shot super-resolution capabilities. The approach achieves latent structural disentanglement of scene components, allowing for independent editing of content and dynamics. It performs competitive controllable forecasting with high efficiency on a single consumer GPU.

## Key Contributions

- Introduced NOVA, a world modeling framework using weight-space implicit neural representations to eliminate decoder bottlenecks.
- Demonstrated that weight-space representations enable zero-shot super-resolution and inherent disentanglement of scene components like background, foreground, and motion.
- Achieved controllable forecasting with high efficiency, operating on a single consumer GPU with ~40M parameters.

## Key Concepts

- [[nova-world-modeling-framework]]: A world modeling framework that represents system states as the weights of an auxiliary coordinate-based implicit neural representation (INR) to enable efficient, disentangled, and super-resolvable video forecasting.

## Archivist Review

I have approved the NOVA framework concept, as it introduces a novel paradigm of using coordinate-based INR weights as latent state representations in world models, offering a path away from computationally heavy decoders. No open questions or datasets met the strict archival threshold for permanence.

### Approved Concepts
- NOVA World Modeling Framework: The core contribution is replacing opaque latent vectors with coordinate-based INR weights, which enables a more interpretable and structurally disentangled state representation for world models.

### Rejected Candidates
- [concept] NOVA (`nova-world-modeling-framework`) - other: The slug was renamed to include context, and the original was discarded.

## Links

- [Abstract](https://arxiv.org/abs/2605.06298)
- [PDF](https://arxiv.org/pdf/2605.06298)

