---
# CSL-compatible fields
title: "Reverse Stress Testing for Multivariate Scenarios: A Conditional Framework for Stressed Time Series"
author:
  - literal: "Michele Sparviero"
  - literal: "Lorenzo Viola"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.09274"

# Custom fields
paper_id: "2606.09274"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "reverse-stress-testing-for-multivariate-scenarios"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:07:18Z"
created_at: "2026-06-11T09:07:18Z"
---

# Reverse Stress Testing for Multivariate Scenarios: A Conditional Framework for Stressed Time Series

**Authors**: Michele Sparviero, Lorenzo Viola
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.09274](https://arxiv.org/abs/2606.09274)

## Summary

This paper introduces a conditional framework for reverse stress testing (RST) that reconstructs coherent multivariate market stress scenarios based on a single asset-class shock. By maximizing the conditional density given the shock, the methodology is implemented through parametric, semiparametric, and nonparametric variants to accommodate varying distributional assumptions. The framework is validated on market data, demonstrating its ability to generate economically meaningful stressed trajectories that capture standard market risk-reward asymmetries.

## Key Contributions

- Introduces a conditional framework for reverse stress testing that derives multivariate stress scenarios from single exogenous shocks.
- Provides three distinct methodological approaches (parametric, semiparametric, and nonparametric) for scenario reconstruction, offering flexibility in distributional assumptions.
- Demonstrates that the generated scenarios successfully preserve empirical market dependencies and reflect the characteristic risk-reward asymmetry observed during market stress regimes.

## Key Concepts

- [[reverse-stress-testing-for-multivariate-scenarios]]: A framework for generating coherent multivariate market stress scenarios conditioned on a single exogenous asset shock.

## Archivist Review

The paper introduces a structured approach to generating coherent multivariate stress scenarios from conditional shocks. I have approved the framework as a concept, as it addresses a core limitation in financial risk modeling—maintaining dependency consistency under stress—and provides a reusable methodology for time series practitioners. No datasets or open questions were suitable for inclusion based on the vault's strict standards.

### Approved Concepts
- Reverse Stress Testing for Multivariate Scenarios: It provides a conditional framework for propagating single-asset shocks through empirical market dependence structures, solving a key challenge in financial stress testing.

### Rejected Candidates
- [concept] Reverse Stress Testing for Multivariate Scenarios (`reverse-stress-testing-for-multivariate-scenarios`) - duplicate_existing: The concept is approved under a more concise title in the official list.

## Links

- [Abstract](https://arxiv.org/abs/2606.09274)
- [PDF](https://arxiv.org/pdf/2606.09274)

