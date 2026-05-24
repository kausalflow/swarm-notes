---
# CSL-compatible fields
title: "Online Optimization with Unknown Time-Varying Parameters from Noisy Gradient Measurements"
author:
  - literal: "Shivanshu Tripathi"
  - literal: "Maziar Raissi"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22251"

# Custom fields
paper_id: "2605.22251"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "reinforcement-learning"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gauss-markov-latent-parameter-reconstruction"
dataset_slugs:
  []
skill: "GeneralMLSkill"
processed_at: "2026-05-24T07:47:30Z"
created_at: "2026-05-24T07:47:30Z"
---

# Online Optimization with Unknown Time-Varying Parameters from Noisy Gradient Measurements

**Authors**: Shivanshu Tripathi, Maziar Raissi
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22251](https://arxiv.org/abs/2605.22251)

## Summary

This paper addresses online optimization problems where cost functions rely on latent, time-varying parameters governed by unknown dynamics. The proposed approach utilizes control-theoretic tools to reconstruct these hidden parameters from noisy gradient measurements through a Gauss-Markov estimator, followed by identification of the underlying dynamics using an instrumental-variable method. The method concludes by forecasting the parameters to compute optimal solutions, with theoretical guarantees on tracking performance. Effectiveness is demonstrated through numerical simulations.

## Key Contributions

- Introduces a framework for online optimization under latent, time-varying parameter dynamics using only noisy gradient measurements.
- Combines Gauss-Markov estimation with instrumental-variable identification to resolve unknown dynamics and forecast future minimizers.
- Provides a theoretical bound on the expected tracking error for the proposed control-theoretic optimization approach.

## Open Questions & Future Work

- [[nonlinear-parameter-dynamics-generalization]]
- [[constrained-online-optimization]]

## Key Concepts

- [[gauss-markov-latent-parameter-reconstruction]]: A control-theoretic state estimation approach to recover unobserved, time-varying parameters from sparse, noisy gradient observations.

## Archivist Review

The approved concept represents a distinct, reusable methodology for latent parameter identification in control-theoretic online optimization. The approved open questions identify fundamental theoretical barriers—nonlinear dynamics and parameter constraints—that are central to the scalability and real-world applicability of this class of algorithms. I applied a restrictive filter to ensure only generalizable methodological contributions and core unresolved bottlenecks were selected.

### Approved Concepts
- Gauss-Markov latent parameter reconstruction: Central technique for inferring unobservable dynamics from noisy gradient measurements in online optimization.

### Approved Open Questions
- Generalizing to Nonlinear Dynamics: Generalizing to nonlinear dynamics is crucial for expanding the applicability of these optimization frameworks to more complex, non-quadratic control tasks where linear assumptions fail.
- Constrained Online Optimization Extension: Most practical optimization applications in engineering and finance involve strict physical or operational constraints; thus, extending these methods to the constrained case is necessary for real-world deployment.

## Links

- [Abstract](https://arxiv.org/abs/2605.22251)
- [PDF](https://arxiv.org/pdf/2605.22251)

