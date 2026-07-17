---
# CSL-compatible fields
title: "Adversarial dynamical systems characterize when data-driven learning succeeds or fails"
author:
  - literal: "Matthew Colbrook"
  - literal: "Igor Mezić"
  - literal: "Alexei Stepanenko"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2407.06312"

# Custom fields
paper_id: "2407.06312"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "interpretability"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adversarial-dynamical-systems"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:05Z"
created_at: "2026-07-17T07:09:05Z"
---

# Adversarial dynamical systems characterize when data-driven learning succeeds or fails

**Authors**: Matthew Colbrook, Igor Mezić, Alexei Stepanenko
**Date**: 2026-07-14
**Paper ID**: [openalex:2407.06312](https://arxiv.org/abs/2407.06312)

## Summary

This paper provides a rigorous theoretical foundation for understanding the learnability of dynamical systems from data. By introducing the concept of adversarial dynamical systems, the authors define the specific conditions under which data-driven Koopman operator learning succeeds or inevitably fails. The proposed framework delivers optimal algorithms with convergence guarantees and resolves critical challenges in Koopman spectral analysis. Experimental results on physical systems, including chaotic fluid flows and Arctic sea ice forecasting, confirm that the approach offers robust, efficient, and interpretable long-range predictions.

## Key Contributions

- Introduces an adversarial dynamical systems framework to formally delineate the boundary between learnable and unlearnable regimes in data-driven dynamics inference.
- Provides optimal data-driven spectral algorithms for Koopman operator learning with formal convergence and certification guarantees.
- Proves fundamental impossibility results for learning dynamical systems without specific stability conditions, regardless of data quality.
- Demonstrates superior predictive performance and efficiency on Arctic sea ice concentration forecasting compared to state-of-the-art deep learning and dynamical models.

## Open Questions & Future Work

- [[koopman-spectral-computation-limits]]

## Key Concepts

- [[adversarial-dynamical-systems]]: A construction method for defining the boundaries between learnable and unlearnable regimes in data-driven dynamical systems inference.

## Archivist Review

The paper is approved for its rigorous theoretical contribution to the learnability of dynamical systems. The concept of 'Adversarial dynamical systems' provides a robust analytical tool for delineating learnability boundaries, and the open question regarding the limits of Koopman spectral computation addresses a fundamental research gap in the field of dynamical systems inference. Other candidates were not proposed as the user input was sparse and well-focused.

### Approved Concepts
- Adversarial dynamical systems: Establishes a fundamental theoretical framework for identifying the limits of learnability in dynamical systems.

### Approved Open Questions
- Limits of Koopman Spectral Computation: This question is essential for establishing a rigorous complexity theory for data-driven modeling, as it directly informs the development of provably robust algorithms and identifies the fundamental trade-offs between system structure, data availability, and algorithm complexity.

## Links

- [Abstract](https://arxiv.org/abs/2407.06312)
- [PDF](https://arxiv.org/pdf/2407.06312)

