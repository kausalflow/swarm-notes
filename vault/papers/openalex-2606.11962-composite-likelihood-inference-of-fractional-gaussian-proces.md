---
# CSL-compatible fields
title: "Composite likelihood inference of fractional Gaussian processes with sequentially optimal subset selection"
author:
  - literal: "Mathis Fourreau"
  - literal: "Matthieu Garcin"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.11962"

# Custom fields
paper_id: "2606.11962"
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
  - "composite-likelihood-inference-for-fractional-processes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:36Z"
created_at: "2026-06-13T08:16:36Z"
---

# Composite likelihood inference of fractional Gaussian processes with sequentially optimal subset selection

**Authors**: Mathis Fourreau, Matthieu Garcin
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.11962](https://arxiv.org/abs/2606.11962)

## Summary

This paper proposes a composite likelihood approach for efficient parameter estimation in fractional Gaussian processes, addressing the prohibitive computational cost of standard maximum likelihood estimation for long-memory time series. By deriving the Godambe information, the authors construct a framework to sequentially select optimal observation subsets that maximize information content while maintaining computational tractability. The method is validated through simulations and empirical applications on stock volatility and wind speed data, demonstrating an effective balance between estimation precision and resource usage.

## Key Contributions

- Derives closed-form expressions for the Fisher and Godambe information of fractional Gaussian noise and fractional Brownian motion.
- Introduces a sequential subset selection design that maximizes Godambe information to optimize parameter estimation performance.
- Demonstrates superior trade-offs between estimation accuracy and computational cost compared to traditional method of moments and maximum likelihood estimation on volatility and wind speed series.

## Open Questions & Future Work

- [[optimal-subset-selection-composite-likelihood]]

## Key Concepts

- [[composite-likelihood-inference-for-fractional-processes]]: A parameter estimation method that approximates the full likelihood of fractional processes by optimizing the selection of observation subsets using Godambe information.

## Archivist Review

I approved the concept for composite likelihood inference specifically tailored for long-memory fractional processes, as this provides a reusable statistical framework for complex time series modeling. I also approved the open question regarding optimal subset selection, which is a fundamental challenge in scalable composite likelihood estimation. I rejected the original concept slug in favor of a slightly more standardized one.

### Approved Concepts
- Composite Likelihood Inference for Fractional Processes: Provides a scalable inference framework for long-memory fractional processes by balancing estimation accuracy and computational burden via sequential subset design.

### Approved Open Questions
- Optimal Subset Selection for Composite Likelihood: The efficiency and statistical consistency of composite likelihood approaches are fundamentally constrained by the choice of subsets; poor strategies negate the benefits of the method.

### Rejected Candidates
- [concept] Composite likelihood inference of fractional Gaussian processes (`composite-likelihood-inference-of-fractional-gaussian-processes`) - other: Renamed to a more canonical form to better represent its general applicability beyond fractional Gaussian processes.

## Links

- [Abstract](https://arxiv.org/abs/2606.11962)
- [PDF](https://arxiv.org/pdf/2606.11962)

