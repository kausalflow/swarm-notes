---
# CSL-compatible fields
title: "Hierarchical Bayes meets hierarchical forecasting: A flexible framework for level-focused forecasts"
author:
  - literal: "Arwen Nugteren"
  - literal: "Mahdi Abolghasemi"
  - literal: "Kerrie Mengersen"
  - literal: "Christopher Drovandi"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23009"

# Custom fields
paper_id: "2606.23009"
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
  - "hierarchical-bayesian-forecasting-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:26Z"
created_at: "2026-06-25T08:19:26Z"
---

# Hierarchical Bayes meets hierarchical forecasting: A flexible framework for level-focused forecasts

**Authors**: Arwen Nugteren, Mahdi Abolghasemi, Kerrie Mengersen, Christopher Drovandi
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23009](https://arxiv.org/abs/2606.23009)

## Summary

This paper introduces a fully Bayesian hierarchical forecasting framework that directly incorporates structural dependencies and decision goals into parameter estimation. Unlike traditional methods that rely on post-hoc reconciliation to ensure coherence, this approach shares information across levels during the learning process. By softly penalizing incoherence and focusing on task-relevant levels, the model yields more accurate forecasts while eliminating the need for multi-step covariance matrix estimation. Performance gains are validated through both simulated experiments and real-world tourism forecasting.

## Key Contributions

- Proposes a fully Bayesian framework that integrates hierarchical structure and decision goals into parameter estimation to ensure cross-sectional coherence.
- Removes the necessity of explicitly estimating complex covariance matrices for multi-step forecasting horizons while maintaining predictive accuracy.
- Demonstrates superior performance over traditional post-hoc reconciliation methods on simulated and Australian domestic tourism datasets.

## Open Questions & Future Work

- [[balancing-focusing-against-calibration]]

## Key Concepts

- [[hierarchical-bayesian-forecasting-framework]]: A fully Bayesian model that integrates hierarchical structure and decision goals directly into parameter estimation to ensure coherent cross-sectional forecasts.

## Archivist Review

I approved the hierarchical Bayesian forecasting framework as it offers a clean architectural departure from traditional post-hoc reconciliation in hierarchical time series, and I approved the open question regarding the trade-off between task-focused weighting and statistical calibration, as this is a fundamental issue when moving toward decision-focused forecasting. I rejected the Australian domestic tourism dataset because it is a routine, domain-specific dataset that does not serve as a widely reusable benchmarking reference for the broader time series field.

### Approved Concepts
- Hierarchical Bayesian Forecasting Framework: It shifts from post-hoc reconciliation to integrated parameter estimation for coherent forecasts, which is a significant paradigm shift in hierarchical time series modeling.

### Approved Open Questions
- Balancing Level-Focusing and Calibration: Understanding this trade-off is critical for practitioners who must balance the immediate utility of decision-aware forecasts against the long-term reliability and calibration of the underlying probabilistic model.

## Links

- [Abstract](https://arxiv.org/abs/2606.23009)
- [PDF](https://arxiv.org/pdf/2606.23009)

