---
# CSL-compatible fields
title: "Conformal Prediction with Time-Series Data via Sequential Conformalized Density Regions"
author:
  - literal: "M. Sampson"
  - literal: "K. S. Chan"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07325"

# Custom fields
paper_id: "2604.07325"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "conformal-prediction"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sequential-conformalized-density-regions-scdr"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:54:37Z"
created_at: "2026-04-11T05:54:37Z"
---

# Conformal Prediction with Time-Series Data via Sequential Conformalized Density Regions

**Authors**: M. Sampson, K. S. Chan
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07325](https://arxiv.org/abs/2604.07325)

## Summary

This paper introduces Sequential Conformalized Density Regions (SCDR), a conformal prediction method designed specifically for time-series data that maintains guaranteed asymptotic conditional coverage. Unlike traditional methods restricted to single intervals, SCDR can produce disconnected prediction sets, allowing for the representation of complex system bifurcations. The framework is proven to be doubly robust, remaining valid under correct specification of either the predictive density model or the score-based nonlinear autoregressive model. Empirical results on real-world datasets show that SCDR produces more precise, informative predictions compared to conventional methods.

## Key Contributions

- Proposes Sequential Conformalized Density Regions (SCDR), a conformal prediction framework for time-series that generates both intervals and disconnected sets to represent bifurcations.
- Demonstrates that SCDR achieves guaranteed asymptotic conditional coverage under non-exchangeable conditions using a quantile random forest adjustment.
- Establishes double robustness, ensuring validity if either the predictive density model or the nonlinear autoregressive score model is correctly specified.

## Open Questions & Future Work

- [[joint-h-step-coverage-guarantees]]
- [[scdr-consistency-alternative-models]]

## Key Concepts

- [[sequential-conformalized-density-regions-scdr]]: A time-series conformal prediction method that generates adaptive, potentially disconnected density regions with guaranteed asymptotic conditional coverage.

## Archivist Review

The approved concept (SCDR) introduces a flexible, doubly-robust approach for conformal prediction in time series, addressing the limitation of single-interval forecasts by allowing for bifurcated, non-convex sets. The approved open questions address the two most critical theoretical bottlenecks for the method: scaling to joint multi-step horizons and ensuring validity with more complex, non-parametric density estimators. Other candidates were rejected for being secondary UX concerns or not meeting the threshold for long-term theoretical research tracks.

### Approved Concepts
- Sequential Conformalized Density Regions (SCDR): It provides a novel, doubly-robust framework for conformal prediction that produces non-contiguous prediction sets, uniquely identifying bifurcations in time-series dynamics.

### Approved Open Questions
- Joint H-step prediction coverage: Joint coverage is a fundamental requirement for sequential decision-making where cumulative risk is the primary metric of concern.
- Extending SCDR model compatibility: Theoretical robustness of conformal methods is heavily dependent on the properties of the underlying density estimator; extending this to complex generative models is a key bottleneck.

### Rejected Candidates
- [open_question] Multivariate SCDR scaling challenges (`multivariate-scdr-visualization-updating`) - low_impact: Visualization and UX-related challenges for multivariate responses are secondary to the core theoretical and algorithmic bottlenecks of the framework.

## Links

- [Abstract](https://arxiv.org/abs/2604.07325)
- [PDF](https://arxiv.org/pdf/2604.07325)

