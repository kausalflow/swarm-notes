---
# CSL-compatible fields
title: "Self-normalised change point tests that remain pivotal under non-stationarity"
author:
  - literal: "Florian Heinrichs"
  - literal: "Fabian Mies"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.39404"

# Custom fields
paper_id: "2610.39404"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-01T11:34:02Z"
created_at: "2026-11-01T11:34:02Z"
---

# Self-normalised change point tests that remain pivotal under non-stationarity

**Authors**: Florian Heinrichs, Fabian Mies
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.39404](https://arxiv.org/abs/2610.39404)

## Summary

Self-normalising test statistics for time series avoid long-run variance lag specification but lose asymptotic pivotality under nonstationarity. This paper introduces an alternative self-normalised test statistic for multiple change point problems that is asymptotically pivotal even with nonstationary noise. The key methodology relies on statistical functionals that are invariant under temporal reparameterisation (clock-changes). Simulations confirm that the approach improves size reliability and power for highly nonstationary time series compared to bootstrap methods.

## Key Contributions

- Proposes an alternative self-normalised test statistic for multiple change point detection that remains asymptotically pivotal under nonstationary noise sequences.
- Leverages statistical functionals invariant under temporal reparameterisation (clock-changes) to bypass long-run variance estimation issues.
- Demonstrates through simulations that the proposed test is more conservative than bootstrap competitors while offering superior power against multiple changes and better size reliability under severe nonstationarity.

## Open Questions & Future Work

- [[continuous-alternatives-self-normalized-changepoint]]

## Archivist Review

Approve the open question regarding continuous alternatives in self-normalised change point tests as it highlights a genuine theoretical limitation in handling non-stationarity. Reject the concept candidate as it describes a paper-internal mathematical trick rather than a broadly reusable methodological paradigm.

### Approved Open Questions
- Continuous Alternatives in Self-Normalised Changepoint Tests: Extending self-normalised change detection beyond piecewise constant means to continuous alternatives under non-stationarity is crucial for broad applicability in nonparametric time series econometrics and climatology.

### Rejected Candidates
- [concept] Temporal Reparametrization Invariance in Changepoint Tests (`temporal-reparametrization-invariance-changepoint`) - paper_local: Too paper-local and specific to a single theoretical change point testing formulation.

## Links

- [Abstract](https://arxiv.org/abs/2610.39404)
- [PDF](https://arxiv.org/pdf/2610.39404)

