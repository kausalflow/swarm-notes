---
# CSL-compatible fields
title: "Functional dependence and synchronous coupling in ergodic autoregressions"
author:
  - literal: "Paul Doukhan"
  - literal: "Lionel Truquet"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08567"

# Custom fields
paper_id: "2607.08567"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lyapunov-exponent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:25:12Z"
created_at: "2026-07-12T07:25:12Z"
---

# Functional dependence and synchronous coupling in ergodic autoregressions

**Authors**: Paul Doukhan, Lionel Truquet
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08567](https://arxiv.org/abs/2607.08567)

## Summary

This paper examines the potential discrepancy between innovation-based functional dependence measures and the underlying dynamical probability space of nonlinear time series models. By analyzing uniformly ergodic autoregressive processes, the authors show that a qualitative shift in innovation coupling occurs at a threshold defined by the sign of a Lyapunov exponent. This finding reveals that positive Lyapunov exponents may sustain initial perturbations despite uniform ergodicity, emphasizing the necessity of rigorous probability space specification in time series analysis.

## Key Contributions

- Exhibits classes of uniformly ergodic autoregressive processes where natural innovation coupling qualitatively transitions based on model parameters.
- Identifies that this transition in coupling behavior directly aligns with changes in the sign of an associated Lyapunov exponent.
- Demonstrates that positive Lyapunov exponents can inhibit the forgetting of initial perturbations even within uniformly ergodic Markov chains, highlighting potential pitfalls in applying functional dependence measures.

## Open Questions & Future Work

- [[lyapunov-exponent-natural-innovation-representation]]
- [[functional-dependence-foster-lyapunov-ergodicity]]

## Key Concepts

- [[lyapunov-exponent]]: A diagnostic metric characterizing the exponential rate of divergence or convergence of nearby trajectories in a dynamical system.

## Archivist Review

I approved 'Lyapunov exponent' as a foundational diagnostic concept for nonlinear time series stability. The open questions regarding natural innovation representations and drift-based ergodicity are substantive theoretical bottlenecks in nonlinear time series analysis that remain relevant to the broader field. I rejected the proposed 'Lyapunov exponent-pretraining objective' concept as it conflated a generic analytical diagnostic with a specific (and here non-existent) pretraining objective.

### Approved Concepts
- Lyapunov exponent: The paper links the sign of Lyapunov exponents to the functional dependence and memory loss properties of autoregressive models, identifying a critical threshold for process behavior.

### Approved Open Questions
- Lyapunov Exponents and Natural Representations: Understanding the limits of natural innovation representations is vital for the correct application of functional dependence measures, which are essential tools in modern nonlinear time series analysis.
- Functional Dependence in Drift-Based Ergodicity: Establishing if common ergodic models support natural innovation-based dependence measures is crucial for extending functional dependence methods to a broader class of practical nonlinear time series models.

## Links

- [Abstract](https://arxiv.org/abs/2607.08567)
- [PDF](https://arxiv.org/pdf/2607.08567)

