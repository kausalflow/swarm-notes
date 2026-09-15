---
# CSL-compatible fields
title: "Two-way Homogeneity Pursuit for Quantile Network Vector Autoregression"
author:
  - literal: "Wenyang Liu"
  - literal: "Ganggang Xu"
  - literal: "Jianqing Fan"
  - literal: "Xuening Zhu"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2404.18732"

# Custom fields
paper_id: "2404.18732"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "two-way-grouped-network-quantile-autoregression"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-15T09:40:43Z"
created_at: "2026-09-15T09:40:43Z"
---

# Two-way Homogeneity Pursuit for Quantile Network Vector Autoregression

**Authors**: Wenyang Liu, Ganggang Xu, Jianqing Fan, Xuening Zhu
**Date**: 2026-09-14
**Paper ID**: [openalex:2404.18732](https://arxiv.org/abs/2404.18732)

## Summary

The paper introduces the two-way grouped network quantile (TGNQ) autoregression model to analyze time series on directed networks with substantial heterogeneity. By assigning each node two latent group memberships, the model flexibly captures asymmetric interactions and simultaneously performs clustering and parameter estimation. Theoretical guarantees, including consistency and asymptotic normality, are established, and a quantile information criterion is developed for group number selection.

## Key Contributions

- Proposed the two-way grouped network quantile (TGNQ) autoregression model to capture complex directional interactions and heterogeneity in network time series.
- Developed a simultaneous node clustering and parameter estimation procedure with theoretical guarantees for consistency and asymptotic normality.
- Introduced a quantile information criterion for consistently selecting the number of groups in network quantile autoregression.

## Open Questions & Future Work

- [[theoretical-justification-enhanced-algorithm]]

## Key Concepts

- [[two-way-grouped-network-quantile-autoregression]]: A time series autoregression model that assigns nodes two latent group memberships to capture heterogeneous and asymmetric network interactions across quantiles.

## Archivist Review

Approved the central methodological contribution of two-way grouped network quantile autoregression along with its explicit algorithmic convergence open question. All other candidates were omitted to adhere to strict selectivity limits.

### Approved Concepts
- Two-Way Grouped Network Quantile Autoregression: Introduces a novel framework combining network autoregression, quantile regression, and two-way group memberships to model heterogeneous directional interactions in time series.

### Approved Open Questions
- Theoretical Justification of Enhanced Algorithm: Important for bridging the gap between empirical algorithm effectiveness and rigorous statistical guarantees in non-convex bi-clustering procedures.

## Links

- [Abstract](https://arxiv.org/abs/2404.18732)
- [PDF](https://arxiv.org/pdf/2404.18732)

