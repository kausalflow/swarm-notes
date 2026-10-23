---
# CSL-compatible fields
title: "Calibrated uncertainty quantification for prosumer flexibility aggregation in ancillary service markets"
author:
  - literal: "Yogesh Pipada Sunil Kumar"
  - literal: "S. Ali Pourmousavi"
  - literal: "Jon A. R. Liisberg"
  - literal: "Julián Lemos-Vinasco"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2601.14663"

# Custom fields
paper_id: "2601.14663"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
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
processed_at: "2026-10-23T09:40:42Z"
created_at: "2026-10-23T09:40:42Z"
---

# Calibrated uncertainty quantification for prosumer flexibility aggregation in ancillary service markets

**Authors**: Yogesh Pipada Sunil Kumar, S. Ali Pourmousavi, Jon A. R. Liisberg, Julián Lemos-Vinasco
**Date**: 2026-10-21
**Paper ID**: [openalex:2601.14663](https://arxiv.org/abs/2601.14663)

## Summary

This study evaluates uncertainty quantification approaches—specifically Monte Carlo dropout, conformal prediction, and conformalized quantile regression—to construct prediction intervals for aggregated prosumer flexibility in frequency-controlled ancillary service markets. Using a large-scale synthetic dataset for a behind-the-meter aggregator in the Danish manual frequency restoration reserve market, the authors demonstrate that conformal methods improve joint coverage and satisfy strict 90% reliability requirements. Furthermore, methods like CQR and MCP achieve higher retained economic value (retaining ~68-69% of perfect-information profit) while highlighting the inherent trade-offs between reliability, economic returns, and robustness to exogenous input perturbations.

## Key Contributions

- Systematically evaluates established uncertainty quantification approaches (Monte Carlo dropout, conformal prediction, and conformalized quantile regression) for aggregated prosumer flexibility forecasting.
- Demonstrates that conformal methods substantially improve joint coverage compared to uncalibrated MCD baselines under nominal test conditions.
- Shows that conservative methods satisfy strict 90% lower-tail reliability requirements while CQR and MCP retain approximately 69% and 68% of perfect-information profit under strict penalty interpretations.
- Performs a controlled robustness analysis revealing how perturbations in load, solar, price, and activation inputs degrade empirical coverage, overbidding, and economic performance.

## Limitations

Evaluated on a synthetic dataset generated via an industry-grade home energy management system; performance depends on input data stability and perturbation levels.

## Open Questions & Future Work

- [[adaptive-conformal-prediction-distribution-shift]]

## Archivist Review

Approved the open question on adaptive conformal prediction for distribution shifts as it targets a well-defined bottleneck in handling robustness and temporal forecast-error processes under real-world input perturbations. No standalone concepts were approved because the paper evaluates standard UQ methods rather than inventing a new architecture or foundational modeling primitive.

### Approved Open Questions
- Adaptive Conformal Prediction for Distribution Shifts: Crucial for ensuring that data-driven demand response aggregators maintain regulatory compliance and economic viability when deployed in volatile real-world operating environments characterized by persistent distributional shifts in load, solar, price, and activation signals.

### Rejected Candidates
- [concept] Monte Carlo Dropout and Conformal Prediction for Prosumer Flexibility (`monte-carlo-dropout-conformal-prediction-evaluation`) - not_novel: The paper applies established uncertainty quantification techniques (MCD, conformal prediction, CQR) rather than introducing a novel algorithmic concept.

## Links

- [Abstract](https://arxiv.org/abs/2601.14663)
- [PDF](https://arxiv.org/pdf/2601.14663)

