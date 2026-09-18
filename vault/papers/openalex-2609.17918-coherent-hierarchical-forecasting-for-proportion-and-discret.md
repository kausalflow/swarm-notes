---
# CSL-compatible fields
title: "Coherent Hierarchical Forecasting for Proportion and Discrete Time Series"
author:
  - literal: "Hannah Comiskey"
issued:
  date-parts:
    - [2026, 9, 15]
url: "https://arxiv.org/abs/2609.17918"

# Custom fields
paper_id: "2609.17918"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "forecast-reconciliation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:16:39Z"
created_at: "2026-09-18T09:16:39Z"
---

# Coherent Hierarchical Forecasting for Proportion and Discrete Time Series

**Authors**: Hannah Comiskey
**Date**: 2026-09-15
**Paper ID**: [openalex:2609.17918](https://arxiv.org/abs/2609.17918)

## Summary

This paper addresses the limitation of Gaussian-based forecast reconciliation methods when applied to hierarchical time series with discrete or bounded supports. The author introduces a post-hoc hierarchical forecasting approach utilizing convolution and exponential tilting to construct coherent forecast hierarchies while strictly preserving distributional properties and supports. Evaluations on simulations, epidemiological, and demographic datasets demonstrate strong performance over existing state-of-the-art reconciliation methods.

## Key Contributions

- Develops a post-hoc hierarchical forecasting approach for discrete and bounded time series that preserves distributional properties and underlying support through convolution and exponential tilting.
- Demonstrates superior performance against Gaussian-based reconciliation methods in discrete and continuous settings across simulation studies.
- Applies the method to epidemiological and demographic data, yielding reliable and coherent distributional forecasts for bounded and proportion time series.

## Open Questions & Future Work

- [[scaling-coherent-hierarchical-forecasting-non-linear-large-scale]]

## Archivist Review

The paper presents a coherent hierarchical forecasting approach for discrete and bounded time series using convolution and exponential tilting. No suitable standalone concept was proposed that warrants a permanent vault note, but the open question regarding scaling to non-linear and large hierarchies is valuable and properly structured.

### Approved Open Questions
- Scaling Coherent Forecasting to Non-Linear and Large Hierarchies: Real-world hierarchical systems frequently involve complex non-linear aggregation constraints and massive scale, presenting significant scalability and methodological hurdles for current probabilistic reconciliation algorithms.

## Links

- [Abstract](https://arxiv.org/abs/2609.17918)
- [PDF](https://arxiv.org/pdf/2609.17918)

