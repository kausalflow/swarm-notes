---
# CSL-compatible fields
title: "How optimistic inflow forecasts distort dispatch, prices, and contracts in hydro-dominated power systems: evidence from Brazil"
author:
  - literal: "Arthur Brigatto"
  - literal: "Alexandre Street"
  - literal: "Joaquim Dias Garcia"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00504"

# Custom fields
paper_id: "2607.00504"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:36:41Z"
created_at: "2026-07-04T07:36:41Z"
---

# How optimistic inflow forecasts distort dispatch, prices, and contracts in hydro-dominated power systems: evidence from Brazil

**Authors**: Arthur Brigatto, Alexandre Street, Joaquim Dias Garcia
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00504](https://arxiv.org/abs/2607.00504)

## Summary

This paper investigates the economic and operational impact of persistent optimistic inflow-forecast bias within hydro-dominated power systems, specifically the Brazilian electricity market. Through analytical modeling and Stochastic Dual Dynamic Programming (SDDP) experiments, the authors demonstrate that biased forecasts lead to suboptimal water management, increased reliability risks, and distorted price signals. The study concludes that such bias is not purely a forecasting error, but a critical driver of systemic operational inefficiency and distorted market incentives. These findings highlight the necessity of bias-corrected forecasting to improve energy security and contracting stability in hydro-dependent systems.

## Key Contributions

- Analytical proof showing that optimistic inflow-forecast bias reduces water values, increases hydro discharge, and delays thermal commitment in hydrothermal power systems.
- Empirical evidence from the Brazilian power system linking historical optimistic inflow bias to operational inefficiencies and market distortions.
- SDDP experiments demonstrating that policies trained under biased forecasts result in sharper spot-price volatility, increased reliability risk, and higher expected operating costs.
- Identification of inflow-forecast bias as a driver of reduced hydro-generator contracting incentives due to increased price-quantity risk.

## Open Questions & Future Work

- [[sddp-optimality-convergence-certification]]
- [[economic-transients-of-forecast-governance-reforms]]

## Archivist Review

I approved two open questions concerning the methodological and economic challenges of managing forecast bias in large-scale energy systems. The existing SDDP convergence question was refined to better reflect its role as a fundamental bottleneck for verifying optimization quality. No concepts were approved as the primary mechanisms described are domain-specific applications of existing forecasting and optimization principles rather than reusable algorithmic innovations.

### Approved Open Questions
- SDDP optimality and convergence certification: This bottleneck is essential for distinguishing between systemic forecast bias effects and numerical optimization errors in critical energy infrastructure planning.
- Economic transients of forecast governance reforms: Understanding the transition path is vital for managing the economic and political risks associated with model governance reforms in energy-dependent infrastructure.

### Rejected Candidates
- [open_question] Convergence guarantees for SDDP (`sddp-convergence-guarantees`) - duplicate_existing: Renamed for greater clarity and alignment with vault standards.
- [open_question] Economic transient of forecast-bias correction (`economic-transient-unbiased-forecast-transition`) - duplicate_existing: Renamed for greater clarity and alignment with vault standards.

## Links

- [Abstract](https://arxiv.org/abs/2607.00504)
- [PDF](https://arxiv.org/pdf/2607.00504)

