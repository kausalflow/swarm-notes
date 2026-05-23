---
# CSL-compatible fields
title: "The Statistical Significance of the Inclusion of Graph Neural Networks in the Financial Time Series Forecasting Problem"
author:
  - literal: "Marco Gregnanin"
  - literal: "Johannes De Smedt"
  - literal: "Giorgio Gnecco"
  - literal: "Maurizio Parton"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21192"

# Custom fields
paper_id: "2605.21192"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series,forecasting,graph-neural-network,gnn,language-model"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-geometric-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:24:52Z"
created_at: "2026-05-23T07:24:52Z"
---

# The Statistical Significance of the Inclusion of Graph Neural Networks in the Financial Time Series Forecasting Problem

**Authors**: Marco Gregnanin, Johannes De Smedt, Giorgio Gnecco, Maurizio Parton
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21192](https://arxiv.org/abs/2605.21192)

## Summary

This paper addresses the limitations of purely temporal models in financial time series forecasting by proposing the Time-Geometric model. This framework augments traditional forecasting approaches with Graph Neural Networks to extract and utilize geometric patterns inherent in the data. The authors provide empirical evidence demonstrating that this structural inclusion leads to statistically significant improvements in predictive performance, validating the importance of geometry in financial market modeling.

## Key Contributions

- Introduces the Time-Geometric model, a hybrid framework that integrates Graph Neural Networks to capture geometric patterns alongside traditional temporal features for financial time series.
- Demonstrates through rigorous empirical evaluation that incorporating geometric structural information significantly improves forecasting accuracy over models relying solely on temporal patterns.
- Provides statistical validation for the efficacy of leveraging GNN-based graph representations in univariate financial forecasting tasks.

## Open Questions & Future Work

- [[metric-sensitivity-statistical-significance-time-series-forecasting]]

## Key Concepts

- [[time-geometric-model]]: A hybrid model architecture designed to jointly exploit geometric and temporal patterns for enhanced univariate financial time series forecasting.

## Archivist Review

The Time-Geometric model is approved as a representative hybrid architecture for embedding structural/geometric information into temporal models, which is a reusable research direction. The open question regarding the statistical significance of performance gains is approved because the authors explicitly anchor it to the sensitivity of evaluation metrics and horizons, which is a foundational bottleneck in time series model evaluation. No other candidates were proposed.

### Approved Concepts
- Time-Geometric model: It is the primary methodological contribution, representing a novel hybrid approach for combining geometric patterns (via GNNs) with standard temporal forecasting.

### Approved Open Questions
- Standardizing Metric-Based Statistical Significance: The study identifies that statistical outcomes are highly sensitive to metric and horizon choices, indicating that current methods for validating model superiority may be dataset-dependent or inconsistent; this limits the generalizability of findings in financial time series forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.21192)
- [PDF](https://arxiv.org/pdf/2605.21192)

