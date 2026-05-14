---
# CSL-compatible fields
title: "Intervention-Based Time Series Causal Discovery via Simulator-Generated Interventional Distributions"
author:
  - literal: "Tsuyoshi Okita"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.09870"

# Custom fields
paper_id: "2605.09870"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-discovery"
architectures:
  []
datasets:
  []
concept_slugs:
  - "svar-fm"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:36Z"
created_at: "2026-05-14T07:37:36Z"
---

# Intervention-Based Time Series Causal Discovery via Simulator-Generated Interventional Distributions

**Authors**: Tsuyoshi Okita
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.09870](https://arxiv.org/abs/2605.09870)

## Summary

SVAR-FM is a framework for time-series causal discovery that treats physics-based simulators as physical realizations of the do-operator to handle confounding. By clamping variables within the simulator, the model generates interventional distributions, which are subsequently learned via Conditional Flow Matching. Theoretical analysis establishes the conditions for model identifiability and provides an error bound that accounts for both simulator fidelity and approximation errors. Empirical results confirm that SVAR-FM recovers causal directions in scenarios where observational methods fail due to unobserved confounding.

## Key Contributions

- Proposed SVAR-FM, a framework for time-series causal discovery using physics-based simulators to generate interventional data.
- Proven identifiability of structural VAR under a simulator coverage condition and derived an error bound encompassing simulator fidelity and flow matching.
- Demonstrated through a case study in ultrafast laser physics that simulator accuracy threshold dictates the validity of estimated causal sign.

## Open Questions & Future Work

- [[certifying-simulator-fidelity-causal-discovery]]

## Key Concepts

- [[svar-fm]]: A causal discovery framework for time series that uses physics-based simulators as physical implementations of Pearl's do-operator to generate interventional distributions.

## Archivist Review

The paper introduces SVAR-FM, a novel and well-motivated framework for causal discovery that utilizes physics simulators as intervention-generation mechanisms. I have approved this concept as it offers a reusable methodological pattern for handling confounding in time-series causal analysis. Additionally, I approved the open question regarding the certification of simulator fidelity, as it addresses a core limitation that likely applies to any causal discovery method relying on surrogate or simulation-based data. Other candidates were rejected to maintain the required scarcity or because they were not sufficiently novel or reusable.

### Approved Concepts
- SVAR-FM: Introduces a principled way to integrate physics simulators into causal discovery by treating them as physical realizations of the do-operator.

### Approved Open Questions
- Certifying Simulator Fidelity Bottlenecks: This is a fundamental bottleneck because without a way to bound simulator fidelity, the causal conclusions drawn from these methods are inherently subject to unquantifiable systematic errors.

## Links

- [Abstract](https://arxiv.org/abs/2605.09870)
- [PDF](https://arxiv.org/pdf/2605.09870)

