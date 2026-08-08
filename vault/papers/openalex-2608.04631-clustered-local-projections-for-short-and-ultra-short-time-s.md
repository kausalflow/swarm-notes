---
# CSL-compatible fields
title: "Clustered Local Projections for Short and Ultra-Short Time Series -- A Hierarchical Bayesian Framework"
author:
  - literal: "Todd Clark"
  - literal: "Florian Huber"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04631"

# Custom fields
paper_id: "2608.04631"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-08T05:34:23Z"
created_at: "2026-08-08T05:34:23Z"
---

# Clustered Local Projections for Short and Ultra-Short Time Series -- A Hierarchical Bayesian Framework

**Authors**: Todd Clark, Florian Huber
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04631](https://arxiv.org/abs/2608.04631)

## Summary

The paper proposes a hierarchical Bayesian framework for estimating local projection impulse response functions across panels of related time series, specifically targeting short and unbalanced samples. By employing a sparse finite mixture pool that clusters units based on impulse response profile similarities, the method allows short series to borrow statistical strength from longer series at distant horizons. Simulation results demonstrate improved estimation accuracy for short samples, and an empirical application reveals heterogeneous price responses to macroeconomic shocks across different goods and services measures.

## Key Contributions

- Proposes a Bayesian hierarchical framework for estimating local projection impulse response functions across unbalanced panels of related time series.
- Develops a sparse finite mixture pool to cluster economic units by the similarity of their impulse response profiles, enabling short series to borrow information from longer ones.
- Demonstrates through simulations that the approach substantially improves local projection estimation accuracy in short samples while matching standard approaches for longer series.
- Applies the framework to a US price dataset with survey responses, showing heterogeneous price responses to supply-chain and oil shocks.

## Archivist Review

Reviewed the paper candidates and found no concepts or open questions meeting the high threshold for permanent vault notes, as they represent routine combinations of known statistical and econometric techniques.

### Rejected Candidates
- [concept] Clustered Local Projections (`clustered-local-projections`) - subcomponent_of_broader_mechanism: Routine combination of local projections and clustering without establishing a broad, standalone algorithmic primitive.
- [open_question] Across-Horizon Smoothing with Cross-Sectional Pooling (`combining-across-horizon-smoothing-with-cross-sectional-pooling`) - low_impact: Standard future work on combining two existing statistical regularization techniques.

## Links

- [Abstract](https://arxiv.org/abs/2608.04631)
- [PDF](https://arxiv.org/pdf/2608.04631)

