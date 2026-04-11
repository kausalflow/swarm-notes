---
# CSL-compatible fields
title: "Physics-Informed 3D Atomic Reconstruction and Dynamics of Free-Standing Graphene from Single Low-Dose TEM Images"
author:
  - literal: "Minglu Zhang"
  - literal: "Shih-Wei Hung"
  - literal: "Yawei Wu"
  - literal: "Jyh-Pin Chou"
  - literal: "Angus I. Kirkland"
  - literal: "R. Kilaas"
  - literal: "Fu‐Rong Chen"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07271"

# Custom fields
paper_id: "2604.07271"
paper_source: "openalex"
domain: "biology"
tags:
  - "image-segmentation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-atomic-reconstruction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:56:50Z"
created_at: "2026-04-11T05:56:50Z"
---

# Physics-Informed 3D Atomic Reconstruction and Dynamics of Free-Standing Graphene from Single Low-Dose TEM Images

**Authors**: Minglu Zhang, Shih-Wei Hung, Yawei Wu, Jyh-Pin Chou, Angus I. Kirkland, R. Kilaas, Fu‐Rong Chen
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07271](https://arxiv.org/abs/2604.07271)

## Summary

This paper introduces a physics-informed computational framework to reconstruct the 3D atomic geometry of free-standing graphene from single, low-dose transmission electron microscopy (TEM) images. By integrating simulated annealing optimization with molecular dynamics regularization, the approach overcomes severe signal-to-noise limitations inherent in radiation-sensitive imaging. The framework enables the real-time extraction of ripple dynamics, strain tensors, and electronic properties, providing insights into how structural fluctuations modulate electron localization at the millisecond scale.

## Key Contributions

- Developed a physics-informed framework combining simulated annealing and molecular dynamics to reconstruct 3D atomic coordinates of single-layer graphene from single low-dose TEM frames.
- Achieved sub-angstrom out-of-plane accuracy (σz < 0.45 Å) for beam-sensitive 2D materials under significant noise constraints.
- Identified a critical dose threshold for structural recovery, providing a practical constraint for experimental design in TEM imaging.

## Open Questions & Future Work

- [[computational-efficiency-in-atomic-reconstruction]]

## Key Concepts

- [[physics-informed-atomic-reconstruction]]: A computational framework for reconstructing 3D atomic coordinates from single-frame, low-dose transmission electron microscopy (TEM) images using physics-informed regularisation.

## Archivist Review

The approved items identify a domain-specific but conceptually reusable framework for resolving structural information from underdetermined, noisy measurements via physics-based regularisation. The open question addresses a fundamental limitation in computational physics-informed pipelines—the trade-off between strict physical modelling and inference latency—which is a recurring challenge across scientific machine learning. No datasets were approved as none were cited as unique, public, or standalone naming-contributions.

### Approved Concepts
- Physics-Informed Atomic Reconstruction: Integrates optimization-based methods with physical regularizers (MD) to reconstruct 3D structures from inherently noisy/underdetermined experimental projections.

### Approved Open Questions
- Accelerating 3D atomic reconstruction: Overcoming the computational bottleneck is critical for scaling high-resolution 3D dynamic characterization to larger datasets and real-time experimental environments.

## Links

- [Abstract](https://arxiv.org/abs/2604.07271)
- [PDF](https://arxiv.org/pdf/2604.07271)

