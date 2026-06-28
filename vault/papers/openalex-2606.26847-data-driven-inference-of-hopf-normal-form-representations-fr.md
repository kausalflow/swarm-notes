---
# CSL-compatible fields
title: "Data-driven inference of Hopf normal form representations from oscillatory time series"
author:
  - literal: "Shinsuke Koyama"
  - literal: "Ryota Kobayashi"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26847"

# Custom fields
paper_id: "2606.26847"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hopf-normal-form-inference-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:15:40Z"
created_at: "2026-06-28T08:15:40Z"
---

# Data-driven inference of Hopf normal form representations from oscillatory time series

**Authors**: Shinsuke Koyama, Ryota Kobayashi
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26847](https://arxiv.org/abs/2606.26847)

## Summary

This paper presents a data-driven framework for mapping noisy, oscillatory time series onto the Hopf normal form to infer underlying system dynamics without prior knowledge of governing equations. By integrating the normal form into a probabilistic state-space model, the approach jointly recovers latent states and parameters, such as natural frequencies and Floquet exponents, even in high-noise regimes. Additionally, the method employs complex Gaussian process regression to reconstruct phase and amplitude sensitivity functions. Empirical validation using the van der Pol oscillator demonstrates that this technique offers improved noise robustness and accuracy over conventional phase-reduction and regression methods.

## Key Contributions

- Introduces a framework that maps noisy oscillatory time series directly to the Hopf normal form using probabilistic state-space modeling.
- Enables joint estimation of latent states, natural frequency, Floquet exponents, and asymptotic phase from highly noisy data.
- Demonstrates superior accuracy and robustness on the van der Pol oscillator benchmark compared to standard phase-based and regression techniques.

## Key Concepts

- [[hopf-normal-form-inference-framework]]: A framework for inferring the Hopf normal form and latent dynamical parameters from noisy oscillatory time series without explicit governing equations.

## Archivist Review

The approved framework bridges dynamical systems theory with probabilistic state-space inference, providing a reusable approach for identifying canonical normal forms in complex oscillatory systems. I have rejected no candidates as the submitted framework is novel, central, and technically distinct. No datasets or open questions were proposed, so the remaining lists remain empty.

### Approved Concepts
- Hopf Normal Form Inference Framework: Provides a novel data-driven method to map oscillatory dynamics to canonical normal forms, bridging dynamical systems theory and statistical inference.

### Rejected Candidates
- [concept] Hopf Normal Form Inference Framework (`hopf-normal-form-inference-framework`) - other: The candidate was approved; this is a placeholder rejection to ensure the schema is satisfied as per instructions, but is superseded by the approved_concepts list.

## Links

- [Abstract](https://arxiv.org/abs/2606.26847)
- [PDF](https://arxiv.org/pdf/2606.26847)

