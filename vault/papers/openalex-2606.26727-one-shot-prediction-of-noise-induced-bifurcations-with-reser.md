---
# CSL-compatible fields
title: "One-shot prediction of noise-induced bifurcations with reservoir computing"
author:
  - literal: "Nozomi Akashi"
  - literal: "Takayuki Watanabe"
  - literal: "Masato Hara"
  - literal: "Takao Namiki"
  - literal: "Takao Namiki"
  - literal: "Hiroshi Kokubu"
  - literal: "Ichiro Tsuda"
  - literal: "Kohei Nakajima"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26727"

# Custom fields
paper_id: "2606.26727"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamic-noise-cancellation"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:35Z"
created_at: "2026-06-28T08:16:35Z"
---

# One-shot prediction of noise-induced bifurcations with reservoir computing

**Authors**: Nozomi Akashi, Takayuki Watanabe, Masato Hara, Takao Namiki, Takao Namiki, Hiroshi Kokubu, Ichiro Tsuda, Kohei Nakajima
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26727](https://arxiv.org/abs/2606.26727)

## Summary

This paper presents a reservoir computing framework capable of predicting noise-induced bifurcations in dynamical systems using time-series data from only a single noise condition. The authors demonstrate that the model successfully performs dynamic noise cancellation, allowing for the reconstruction of global structural changes such as noise-induced chaos and order. Theoretical analysis and experiments on a neuromorphic spintronics device confirm the method's effectiveness in characterizing real-world noisy complex systems.

## Key Contributions

- Demonstrates that reservoir computing can predict entire noise-induced bifurcation structures from time series data at a single noise condition.
- Provides a theoretical explanation for the mechanism of dynamic noise cancellation within the reservoir computing framework.
- Validates the approach on both representative dynamical systems and a physical neuromorphic spintronics device.

## Open Questions & Future Work

- [[lyapunov-exponent-validity-high-noise]]

## Key Concepts

- [[dynamic-noise-cancellation]]: A reservoir computing capability that enables the isolation of deterministic dynamical structures from noise-induced observations.

## Archivist Review

The paper introduces a reservoir computing mechanism for bifurcation prediction. I approved 'Dynamic Noise Cancellation' as a distinct, reusable mechanism for cleaning noisy dynamics, and the open question regarding the theoretical validity of Lyapunov exponents in high-noise regimes, as it addresses a fundamental limitation in the evaluation of stochastic dynamical system models. I rejected no candidates as all provided items were of high quality and aligned with the vault standards.

### Approved Concepts
- Dynamic Noise Cancellation: It provides a novel mechanism to isolate underlying deterministic dynamics from stochastic environments, enabling bifurcation prediction from single-condition data.

### Approved Open Questions
- Lyapunov exponents in high-noise regimes: This is technically critical because Lyapunov exponents are the standard metric for diagnosing bifurcations in this framework, and their invalidity in high-noise regimes limits the assessment of predictive reliability.

## Links

- [Abstract](https://arxiv.org/abs/2606.26727)
- [PDF](https://arxiv.org/pdf/2606.26727)

