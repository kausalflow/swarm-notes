---
# CSL-compatible fields
title: "Scalable Bayesian Inference for Time Series via Divide and Conquer"
author:
  - literal: "Rihui Ou"
  - literal: "Lachlan Astfalck"
  - literal: "Deborshee Sen"
  - literal: "David B. Dunson"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2106.11043"

# Custom fields
paper_id: "2106.11043"
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
processed_at: "2026-07-24T07:24:42Z"
created_at: "2026-07-24T07:24:42Z"
---

# Scalable Bayesian Inference for Time Series via Divide and Conquer

**Authors**: Rihui Ou, Lachlan Astfalck, Deborshee Sen, David B. Dunson
**Date**: 2026-07-21
**Paper ID**: [openalex:2106.11043](https://arxiv.org/abs/2106.11043)

## Summary

Bayesian computation scales poorly with large dependent datasets like time series, and existing divide-and-conquer methods lack rigorous theoretical guarantees for temporal dependence. This paper introduces a scalable divide-and-conquer framework for time series that partitions data, performs parallel inference, and aggregates posteriors with theoretically sound accuracy guarantees. Simulation studies and real-data experiments demonstrate the method's superior empirical performance and reliability over ad hoc approximations.

## Key Contributions

- Proposes a scalable divide-and-conquer Bayesian inference framework specifically designed for dependent time-series data.
- Provides theoretically rigorous accuracy guarantees for posterior aggregation under temporal dependence.
- Demonstrates empirical effectiveness and accuracy improvements over existing ad hoc approximations using simulation studies and real-world time-series datasets.

## Open Questions & Future Work

- [[scalable-bayes-nonstationary-long-range-time-series]]

## Archivist Review

Followed strict scarcity and quality guidelines, rejecting generic concepts and approving one explicit open question addressing nonstationary and long-memory extensions for scalable Bayesian time series inference.

### Approved Open Questions
- Scalable Bayesian Inference for Nonstationary and Long-Memory Time Series: Extending divide-and-conquer guarantees beyond stationary, fast-mixing processes is critical for broader real-world applicability, as many environmental and financial time series exhibit nonstationarity or long-range memory.

## Links

- [Abstract](https://arxiv.org/abs/2106.11043)
- [PDF](https://arxiv.org/pdf/2106.11043)

