---
# CSL-compatible fields
title: "FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting"
author:
  - literal: "Qianyang Li"
  - literal: "Xingjun Zhang"
  - literal: "Shaoxun Wang"
  - literal: "Tao Peng"
  - literal: "Jia Wei"
issued:
  date-parts:
    - [2026, 6, 8]
url: "https://arxiv.org/abs/2606.08896"

# Custom fields
paper_id: "2606.08896"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "forecastability-aware-mixture-of-experts-fame"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-11T09:06:46Z"
created_at: "2026-06-11T09:06:46Z"
---

# FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting

**Authors**: Qianyang Li, Xingjun Zhang, Shaoxun Wang, Tao Peng, Jia Wei
**Date**: 2026-06-08
**Paper ID**: [openalex:2606.08896](https://arxiv.org/abs/2606.08896)

## Summary

FAME addresses the challenge of heterogeneous time series forecasting by replacing heuristic model selection with a data-driven routing mechanism. It represents time series via forecastability fingerprints and trains a cost-aware sparse router to select a subset of specialized experts optimized for specific data regimes. Experimental results on industrial and public retail data demonstrate significant improvements in forecast accuracy while maintaining efficient inference costs.

## Key Contributions

- Proposes FAME, a sparse mixture-of-experts architecture that utilizes forecastability fingerprints to dynamically route time series to specialized models.
- Implements a cost-aware routing mechanism that balances predictive accuracy with inference budget by activating a subset of available experts.
- Achieves a 12.4% MSE reduction over LightGBM on a massive industrial vending-machine sales dataset with 5,000+ machines and 60M+ transactions.

## Open Questions & Future Work

- [[automated-forecastability-aware-expert-routing]]

## Key Concepts

- [[forecastability-aware-mixture-of-experts-fame]]: A sparse mixture-of-experts framework that routes time series to specialized forecasting experts based on learned forecastability fingerprints and validation performance.

## Archivist Review

I approved the FAME framework as it provides a distinct, scalable mechanism for handling heterogeneity in time series forecasting via data-driven expert routing. The corresponding open question was approved for its focus on the unresolved challenges of router robustness and the efficiency-accuracy trade-off in production forecasting. The SNBC dataset was rejected as it represents a domain-specific industrial proprietary dataset not likely to serve as a general-purpose benchmark for the field.

### Approved Concepts
- Forecastability-Aware Mixture of Experts (FAME): Introduces a novel paradigm of using multidimensional 'forecastability fingerprints' to drive sparse expert routing in heterogeneous time series scenarios.

### Approved Open Questions
- Automated Forecastability-Aware Expert Routing: The development of robust, cost-aware automated model routing is critical for managing heterogeneous, production-scale time series datasets where no single model architecture is optimal. Tracking this problem is essential for advancing beyond static heuristic model selection in automated forecasting pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2606.08896)
- [PDF](https://arxiv.org/pdf/2606.08896)

