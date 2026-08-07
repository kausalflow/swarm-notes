---
# CSL-compatible fields
title: "Amortized Interventional Forecasting for Multivariate CIR Processes"
author:
  - literal: "Andreas Sauter"
  - literal: "Sumit Sourabh"
  - literal: "Drona Kandhai"
  - literal: "Erman Acar"
issued:
  date-parts:
    - [2026, 8, 4]
url: "https://arxiv.org/abs/2608.03715"

# Custom fields
paper_id: "2608.03715"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "causal-inference"
  - "multivariate"
architectures:
  []
datasets:
  []
concept_slugs:
  - "amortized-interventional-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-07T06:04:02Z"
created_at: "2026-08-07T06:04:02Z"
---

# Amortized Interventional Forecasting for Multivariate CIR Processes

**Authors**: Andreas Sauter, Sumit Sourabh, Drona Kandhai, Erman Acar
**Date**: 2026-08-04
**Paper ID**: [openalex:2608.03715](https://arxiv.org/abs/2608.03715)

## Summary

The paper introduces CIR-ACTIVA, an amortized model for distributional causal effect estimation that predicts multi-horizon shock responses for multivariate Cox-Ingersoll-Ross (CIR) processes without retraining per scenario. It also supplies a causal multivariate CIR data-generating process providing paired observational and interventional ground truth. Evaluated on credit default swap (CDS) spreads and synthetic data, CIR-ACTIVA outperforms observational and causal baselines in causal selectivity and horizon-resolved calibration.

## Key Contributions

- Proposed CIR-ACTIVA, an amortized model for distributional causal effect estimation that predicts multi-horizon shock responses without scenario retraining.
- Introduced a causal multivariate Cox-Ingersoll-Ross (CIR) data-generating process that supplies paired observational and interventional ground truth.
- Demonstrated superior causal selectivity and horizon-resolved calibration against observational and amortized causal-inference baselines on CDS spreads.

## Limitations

Limited to evaluation on synthetic ground truth and CDS spread data testbeds.

## Open Questions & Future Work

- [[scaling-to-portfolio-sized-panels]]

## Key Concepts

- [[amortized-interventional-forecasting]]: An amortized modeling framework for distributional causal effect estimation that predicts multi-horizon shock responses without retraining.

## Archivist Review

Approved one core reusable conceptual mechanism for amortized causal forecasting and one specific open question regarding panel scaling. Adhered strictly to the scarcity policy and avoided redundant vault entries.

### Approved Concepts
- Amortized Interventional Forecasting: Introduces amortized causal effect estimation for multi-horizon shock responses in multivariate time series without retraining per scenario.

### Approved Open Questions
- Scaling to Portfolio-Sized Panels: Crucial for applying amortized causal forecasting methods to large-scale real-world financial portfolios and enterprise risk management systems.

## Links

- [Abstract](https://arxiv.org/abs/2608.03715)
- [PDF](https://arxiv.org/pdf/2608.03715)

