---
# CSL-compatible fields
title: "PSI-SINDy: Post-Selection Inference for Sparse Identification of Nonlinear Dynamics"
author:
  - literal: "Ashraful Islam"
  - literal: "Shuichi Nishino"
  - literal: "Tomohiro Shiraishi"
  - literal: "Ichiro Takeuchi"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11486"

# Custom fields
paper_id: "2610.11486"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "sparse-identification-of-nonlinear-dynamics-sindy"
architectures:
  []
datasets:
  []
concept_slugs:
  - "psi-sindy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-11T11:04:36Z"
created_at: "2026-10-11T11:04:36Z"
---

# PSI-SINDy: Post-Selection Inference for Sparse Identification of Nonlinear Dynamics

**Authors**: Ashraful Islam, Shuichi Nishino, Tomohiro Shiraishi, Ichiro Takeuchi
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11486](https://arxiv.org/abs/2610.11486)

## Summary

This paper introduces PSI-SINDy, a post-selection inference framework designed to quantify the statistical reliability of dynamical terms discovered by sparse identification of nonlinear dynamics (SINDy). To overcome challenges such as selection bias, measurement error, and shared noise between responses and design, PSI-SINDy employs a data thinning technique to decompose a single observed trajectory into four mutually independent views. Theoretical validity is established, and the method's performance is demonstrated through numerical experiments on simulated and experimental dynamical systems.

## Key Contributions

- Developed PSI-SINDy, a statistical inference framework providing hypothesis tests and confidence intervals for dynamical terms selected by SINDy.
- Introduced a data thinning approach to decompose an observed trajectory into four mutually independent views, successfully handling selection bias, measurement error, and shared noise.
- Established the theoretical validity of PSI-SINDy under stated conditions and demonstrated its efficacy on simulated and experimental dynamical-system data.

## Open Questions & Future Work

- [[psi-sindy-extensions-real-world-systems]]

## Key Concepts

- [[psi-sindy]]: A post-selection inference framework tailored to SINDy that quantifies the statistical significance of discovered dynamical terms while addressing selection bias, measurement error, and shared noise.

## Archivist Review

Approved the core concept of PSI-SINDy for post-selection inference in sparse dynamical identification, along with an open question targeting its extension to broader libraries, correlated noise, and unknown variance. Rejected data thinning for SINDy as it is a supporting subcomponent of the main framework.

### Approved Concepts
- PSI-SINDy: It introduces a novel post-selection inference framework for sparse identification of nonlinear dynamics that rigorously accounts for selection bias, measurement error, and shared noise.

### Approved Open Questions
- Generalizing Post-Selection Inference for SINDy: Extending post-selection inference to handle more realistic settings such as unknown noise variance, correlated noise, and multidimensional systems is crucial for applying rigorous statistical reliability quantification to real-world physical and biological dynamical systems.

### Rejected Candidates
- [concept] Data Thinning for SINDy (`data-thinning-for-sindy`) - subcomponent_of_broader_mechanism: Subcomponent of the overarching PSI-SINDy framework rather than a distinct standalone concept.

## Links

- [Abstract](https://arxiv.org/abs/2610.11486)
- [PDF](https://arxiv.org/pdf/2610.11486)

