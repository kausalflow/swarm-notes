---
# CSL-compatible fields
title: "Improving Function Space Flow Matching with Kernel Optimal Transport"
author:
  - literal: "Fred Xu"
  - literal: "Thomas Markovich"
  - literal: "Barbora Barancikova"
  - literal: "Yizhou Sun"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.38049"

# Custom fields
paper_id: "2609.38049"
paper_source: "openalex"
domain: "time-series"
tags:
  - "diffusion-model"
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:48:25Z"
created_at: "2026-10-02T10:48:25Z"
---

# Improving Function Space Flow Matching with Kernel Optimal Transport

**Authors**: Fred Xu, Thomas Markovich, Barbora Barancikova, Yizhou Sun
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.38049](https://arxiv.org/abs/2609.38049)

## Summary

Generative models for function-valued data, such as time series and partial differential equation solutions, struggle with independent endpoint pairings in standard Functional Flow Matching (FFM). This paper introduces kernel Functional Flow Matching (kFFM), which incorporates entropic optimal transport under a kernel-induced cost—the coupling underlying the Hilbert Sinkhorn Divergence—into the infinite-dimensional function space setting. Theoretical analysis establishes the boundedness, well-posedness, and discretization invariance of the approach on Banach spaces. Empirically, kFFM outperforms existing generative baselines on time-series and PDE benchmarks, including turbulent Navier-Stokes.

## Key Contributions

- Proposes kernel Functional Flow Matching (kFFM), replacing independent endpoint pairing in Functional Flow Matching with entropic optimal transport under a kernel-induced cost.
- Proves that the kernel cost and Hilbert Sinkhorn Divergence (HSD) objective are uniformly bounded and well-posed on Banach ambient spaces.
- Derives an error decomposition against quadratic-cost OT on compact metric spaces and proves a discretization-invariance bound governed by Sobolev regularity.
- Demonstrates empirical improvements over FFM, diffusion, adversarial, and finite-dimensional OT baselines on time-series and PDE benchmarks, including turbulent Navier-Stokes.

## Open Questions & Future Work

- [[stronger-function-space-ot-turbulent-data]]

## Archivist Review

I approved the open question regarding stronger function-space optimal transport for turbulent data because it captures a fundamental unresolved bottleneck in infinite-dimensional generative modeling and time-series forecasting. I rejected the concept candidate (kFFM) as it is a paper-specific instantiation of functional flow matching rather than a broadly recurring independent architecture component. No datasets met the strict inclusion threshold.

### Approved Open Questions
- Stronger Function-Space Optimal Transport: Extending optimal transport and flow matching to handle rough and turbulent function spaces remains a critical challenge for physical simulation and time-series modeling.

### Rejected Candidates
- [concept] Kernel Functional Flow Matching (kFFM) (`kernel-functional-flow-matching-kffm`) - subcomponent_of_broader_mechanism: While kFFM is the central contribution of the paper, it is a specialized instantiation of functional flow matching using Hilbert Sinkhorn Divergence rather than a broad, highly reusable primitive across distinct ML families.

## Links

- [Abstract](https://arxiv.org/abs/2609.38049)
- [PDF](https://arxiv.org/pdf/2609.38049)

