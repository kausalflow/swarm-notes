---
# CSL-compatible fields
title: "ResilPhase: Plug-and-Play Phase Mapping and Noise-Resilient Macro-Trajectory Extrapolation for Diffusion Acceleration"
author:
  - literal: "Qicheng Zhao"
  - literal: "Yu Li"
  - literal: "Qi Sun"
  - literal: "Zheyu Yan"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26769"

# Custom fields
paper_id: "2606.26769"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "diffusion-model"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "resilphase"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:53Z"
created_at: "2026-06-28T08:16:53Z"
---

# ResilPhase: Plug-and-Play Phase Mapping and Noise-Resilient Macro-Trajectory Extrapolation for Diffusion Acceleration

**Authors**: Qicheng Zhao, Yu Li, Qi Sun, Zheyu Yan
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26769](https://arxiv.org/abs/2606.26769)

## Summary

ResilPhase addresses inference latency in diffusion models by reformulating accelerated generation as stable macro-trajectory extrapolation within the ODE space. Rather than predicting intermediate noisy features via polynomials, it aligns forecasting with the model's Global Drift and utilizes a derivative-free barycentric Lagrange extrapolator to maintain numerical stability. Further, a bounded Phase Mapping mechanism regularizes the extrapolation process to suppress error growth, enabling significant acceleration with minimal quality degradation on high-resolution generation models.

## Key Contributions

- Reformulates diffusion model acceleration as macro-trajectory extrapolation in ODE space to align with Global Drift and eliminate intermediate feature inconsistency.
- Introduces a derivative-free barycentric Lagrange extrapolator to bypass derivative noise and high-order instability in traditional polynomial extrapolation.
- Proposes a bounded Phase Mapping mechanism to regularize the extrapolation domain and suppress oscillatory error growth during inference.
- Achieves state-of-the-art generation fidelity on FLUX.1-dev and HunyuanVideo benchmarks under aggressive acceleration ratios.

## Open Questions & Future Work

- [[optimal-universal-phase-mapping]]

## Key Concepts

- [[resilphase]]: A plug-and-play acceleration framework for diffusion models that performs derivative-free macro-trajectory extrapolation in ODE space.

## Archivist Review

The paper introduces ResilPhase, a framework for accelerating diffusion model inference through ODE trajectory modeling. I have approved the framework itself as a standalone concept due to its novel combination of derivative-free extrapolation and phase mapping, while rejecting individual subcomponents that are best understood within the context of the larger framework. I have also approved the identified open question regarding universal phase mapping, as it touches upon a critical bottleneck in numerical stability for generative model acceleration.

### Approved Concepts
- ResilPhase: It introduces a novel framework combining phase mapping with derivative-free macro-trajectory extrapolation to stabilize diffusion model acceleration.

### Approved Open Questions
- Universal Optimal Phase Mapping: This is critical to enhancing the robustness and plug-and-play potential of accelerated inference frameworks in generative models.

### Rejected Candidates
- [concept] Derivative-Free Barycentric Lagrange Extrapolator (`derivative-free-barycentric-lagrange-extrapolator`) - subcomponent_of_broader_mechanism: This is a specific technical sub-component of the ResilPhase framework rather than a general independent concept.
- [concept] Bounded Phase Mapping (`bounded-phase-mapping`) - subcomponent_of_broader_mechanism: This is a specific technical sub-component of the ResilPhase framework rather than a general independent concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.26769)
- [PDF](https://arxiv.org/pdf/2606.26769)

