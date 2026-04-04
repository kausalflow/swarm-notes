---
# CSL-compatible fields
title: "Forecasting duration in high-frequency financial data using a self-exciting flexible residual point process"
author:
  - literal: "Kyung-Sub Lee"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00346"

# Custom fields
paper_id: "2604.00346"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:49:44Z"
created_at: "2026-04-04T05:49:44Z"
---

# Forecasting duration in high-frequency financial data using a self-exciting flexible residual point process

**Authors**: Kyung-Sub Lee
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00346](https://arxiv.org/abs/2604.00346)

## Summary

This paper introduces a self-exciting flexible residual point process designed to forecast interarrival durations in high-frequency financial data, effectively capturing the heavy-tailed nature of such events. The methodology preserves the self-exciting and decay structure of market activity while incorporating empirical distributional features. The author provides a rigorous mathematical foundation, proving the process is a positive Harris recurrent Markov chain, and validates the model's predictive efficacy against current benchmarks in ultra-high-frequency trading scenarios.

## Key Contributions

- Introduces a self-exciting flexible residual point process to model and forecast interarrival times in limit order books.
- Establishes the stochastic stability of the proposed point process, proving it is a positive Harris recurrent Markov chain with a stationary distribution.
- Demonstrates superior predictive performance for ultra-high-frequency trading duration forecasting compared to traditional point process and statistical benchmarks.

## Open Questions & Future Work

- [[refining-latent-intensity-dynamics-and-residuals]]

## Archivist Review

The submitted paper provides a mathematical contribution to point process theory applied to finance but does not introduce a novel, reusable architecture or concept distinct enough for a permanent vault entry. I have approved the open question regarding intensity dynamics, as it addresses a core bottleneck in high-frequency modeling that extends beyond the specific implementation proposed here. No datasets were provided for consideration.

### Approved Open Questions
- Refining Latent Intensity and Residuals: This addresses a fundamental limitation in current microstructure models where state-of-the-art intensity dynamics fail to fully account for the heavy-tailed nature of financial event durations.

## Links

- [Abstract](https://arxiv.org/abs/2604.00346)
- [PDF](https://arxiv.org/pdf/2604.00346)

