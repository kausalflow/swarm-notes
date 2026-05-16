---
# CSL-compatible fields
title: "Quantifying information flow along a stochastic trajectory"
author:
  - literal: "Yongjae Oh"
  - literal: "Euijoon Kwon"
  - literal: "Yongjoo Baek"
issued:
  date-parts:
    - [2026, 5, 13]
url: "https://arxiv.org/abs/2605.13509"

# Custom fields
paper_id: "2605.13509"
paper_source: "openalex"
domain: "time-series,biology"
tags:
  - "time-series"
  - "information-extraction"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "stochastic-information-flow-sif"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-16T07:10:15Z"
created_at: "2026-05-16T07:10:15Z"
---

# Quantifying information flow along a stochastic trajectory

**Authors**: Yongjae Oh, Euijoon Kwon, Yongjoo Baek
**Date**: 2026-05-13
**Paper ID**: [openalex:2605.13509](https://arxiv.org/abs/2605.13509)

## Summary

This paper introduces a scalable deep-learning method to estimate Stochastic Information Flow (SIF) from time-series data, enabling the quantification of directed information at the individual trajectory level. By moving beyond conventional ensemble-averaged measures, the proposed approach allows for more granular analysis of stochastic systems. The methodology is validated through applications to theoretical physical models and empirical biological trajectories of motile cells, illustrating its power in detecting cooperative structure.

## Key Contributions

- Introduces a scalable deep-learning-based estimation framework for stochastic information flow (SIF) from general time-series data.
- Demonstrates the framework's effectiveness in identifying cooperative structures within complex systems, specifically two-particle models, Kuramoto oscillators, and motile cell trajectories.
- Provides a practical, data-driven approach to quantifying directed information flow at the trajectory level.

## Open Questions & Future Work

- [[sif-transient-state-estimation]]

## Key Concepts

- [[stochastic-information-flow-sif]]: A trajectory-level measure of directed information flow in stochastic systems.

## Archivist Review

The paper is approved for its theoretical contribution of SIF as a trajectory-level measure, which offers a distinct alternative to ensemble-averaged information metrics. The proposed open question regarding transient state estimation addresses a major functional limitation of current SIF estimators, making it a valuable target for future research.

### Approved Concepts
- Stochastic Information Flow (SIF): It is the core theoretical construct of the paper, providing a trajectory-level alternative to traditional ensemble-averaged information metrics.

### Approved Open Questions
- SIF in transient states: Many real-world dynamical systems, particularly in biological or physical contexts, are inherently non-stationary or transient, and current estimators fail in these regimes.

## Links

- [Abstract](https://arxiv.org/abs/2605.13509)
- [PDF](https://arxiv.org/pdf/2605.13509)

