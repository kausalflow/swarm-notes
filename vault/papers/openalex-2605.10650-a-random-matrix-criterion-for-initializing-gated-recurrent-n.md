---
# CSL-compatible fields
title: "A Random-Matrix Criterion for Initializing Gated Recurrent Neural Networks"
author:
  - literal: "Tommaso Fioratti"
  - literal: "Riccardo Marcaccioli"
  - literal: "Francesco Casola"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10650"

# Custom fields
paper_id: "2605.10650"
paper_source: "openalex"
domain: "nlp, time-series"
tags:
  - "recurrent-neural-network"
  - "rnn"
  - "time-series"
  - "forecasting"
  - "reservoir-computing"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  - "random-matrix-critical-initialization-criterion"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:39:19Z"
created_at: "2026-05-14T07:39:19Z"
---

# A Random-Matrix Criterion for Initializing Gated Recurrent Neural Networks

**Authors**: Tommaso Fioratti, Riccardo Marcaccioli, Francesco Casola
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10650](https://arxiv.org/abs/2605.10650)

## Summary

This paper introduces a principled method for initializing gated recurrent neural networks by grounding weight selection in random matrix theory. The authors analyze the phase transition between ordered and chaotic dynamics, defining a critical point that balances stability and information richness. By deriving a closed-form criterion for this critical gain, the researchers provide a robust design principle for weight initialization that is shown to maximize performance on chaotic forecasting tasks.

## Key Contributions

- Derived a mathematical criterion to estimate the critical weight variance (gc) for recurrent neural network initialization based on random matrix theory.
- Demonstrated that the identified gc correctly predicts the optimal gain for reservoir computing performance in chaotic time-series forecasting.
- Established that the transition between ordered and chaotic dynamical regimes is the primary determinant for information retention and predictive accuracy.

## Open Questions & Future Work

- [[rigorous-proof-eoc-gated-rnn-stability]]
- [[gated-rnn-expressivity-constraints]]

## Key Concepts

- [[random-matrix-critical-initialization-criterion]]: A theoretical framework for identifying critical weight variance in recurrent neural networks by analyzing the phase transition between ordered and chaotic dynamics.

## Archivist Review

I have approved the random-matrix initialization criterion as a robust, theoretically grounded method for recurrent network design. The two open questions are approved because they address the mathematical foundations of network stability and architectural constraints, both of which are high-level research bottlenecks rather than paper-specific limitations.

### Approved Concepts
- Random-Matrix Critical Initialization Criterion: Provides a theoretically grounded, closed-form approach to finding the edge-of-chaos initialization for recurrent networks, moving beyond heuristic methods.

### Approved Open Questions
- Universality of Fixed-Point Stability: Understanding the mathematical limits of the fixed-point stability criterion is critical for ensuring the robustness and theoretical soundness of initialization principles across increasingly complex recurrent architectures.
- Gated Architecture Representational Capacity: Clarifying the relationship between architectural symmetry constraints and network expressivity is essential for optimizing the design and initialization of gated recurrent systems.

## Links

- [Abstract](https://arxiv.org/abs/2605.10650)
- [PDF](https://arxiv.org/pdf/2605.10650)

