---
# CSL-compatible fields
title: "Time series analysis of rankings: A GARCH-type approach"
author:
  - literal: "Luiza S. C. Piancastelli"
  - literal: "Wagner Barreto‐Souza"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2502.05102"

# Custom fields
paper_id: "2502.05102"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "statistical-modeling"
  - "ranking-analysis"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ranking-garch-models"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:30:33Z"
created_at: "2026-05-21T08:30:33Z"
---

# Time series analysis of rankings: A GARCH-type approach

**Authors**: Luiza S. C. Piancastelli, Wagner Barreto‐Souza
**Date**: 2026-05-19
**Paper ID**: [openalex:2502.05102](https://arxiv.org/abs/2502.05102)

## Summary

This paper introduces a class of GARCH-inspired time-varying models for ranking data, addressing the scarcity of methods for temporal rank analysis. The methodology models the conditional distribution of rankings based on the Mallows distribution, using autoregressive and feedback components to capture temporal dependencies. The authors establish key theoretical properties and provide an EM-based estimation framework that handles missing data, demonstrating its utility through an analysis of professional tennis player rankings.

## Key Contributions

- Proposed a class of time-varying ranking models that leverage GARCH-type dynamics to capture the temporal evolution of ranking data.
- Formulated the model using conditional distributions based on the Mallows distribution, incorporating autoregressive and feedback mechanisms.
- Developed a Monte Carlo Expectation-Maximisation algorithm to enable parameter estimation in scenarios with missing ranking observations.

## Key Concepts

- [[ranking-garch-models]]: A class of time-varying ranking models that incorporates autoregressive and feedback components into the Mallows distribution via conditional expectation of distances.

## Archivist Review

I approved the 'Ranking GARCH Models' concept as it represents a novel methodological bridge between classic volatility modeling and non-Euclidean ranking data. The remaining candidates were not provided, and no datasets or open questions were sufficiently strong or explicitly stated to warrant inclusion in the permanent vault.

### Approved Concepts
- Ranking GARCH Models: Provides a novel statistical framework for modeling the temporal evolution of ranking data by adapting GARCH principles.

## Links

- [Abstract](https://arxiv.org/abs/2502.05102)
- [PDF](https://arxiv.org/pdf/2502.05102)

