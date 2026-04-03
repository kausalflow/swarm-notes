---
# CSL-compatible fields
title: "Central limit theorems for the outputs of fully convolutional neural networks with time series input"
author:
  - literal: "Annika Betken"
  - literal: "Giorgio Micali"
  - literal: "J. Schmidt-Hieber"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29612"

# Custom fields
paper_id: "2603.29612"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "text-classification"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "global-weighted-pooling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:06:17Z"
created_at: "2026-04-03T06:06:17Z"
---

# Central limit theorems for the outputs of fully convolutional neural networks with time series input

**Authors**: Annika Betken, Giorgio Micali, J. Schmidt-Hieber
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29612](https://arxiv.org/abs/2603.29612)

## Summary

This paper investigates the theoretical properties of fully convolutional neural networks (FCNs) when applied to time series data. The authors prove that, under the assumption of short-range dependent linear process inputs, the network outputs using global average pooling are asymptotically Gaussian as the time series length tends to infinity. Building on these findings, the paper introduces a global weighted pooling layer that employs learnable, slowly varying coefficients to generalize the standard pooling approach. The work provides a formal mathematical framework for understanding the behavior of FCNs in time-series forecasting and classification tasks.

## Key Contributions

- Proves that outputs of FCNs with global average pooling converge to a Gaussian distribution for short-range dependent linear process inputs as series length grows to infinity.
- Establishes a rigorous theoretical foundation for understanding the asymptotic behavior of FCNs in time series analysis.
- Introduces a global weighted pooling layer with learnable, slowly varying coefficients as a theoretically motivated alternative to standard GAP.

## Open Questions & Future Work

- [[theoretical-foundations-time-series-dl]]

## Key Concepts

- [[global-weighted-pooling]]: A generalization of global average pooling for fully convolutional neural networks that utilizes learnable, slowly varying weighting coefficients.

## Archivist Review

I have approved the proposed 'Global Weighted Pooling' concept as it represents a novel architectural refinement to standard pooling layers grounded in statistical theory. I have also approved the open question regarding the theoretical foundations of time-series deep learning, as it captures a critical gap in the field that extends well beyond the specific scope of this paper. All other potential candidates were evaluated against the strict criteria for research-grade vault entries.

### Approved Concepts
- Global Weighted Pooling: Generalizes standard GAP by introducing learnable, slowly varying coefficients to improve theoretical and empirical behavior in FCNs for time series.

### Approved Open Questions
- Theoretical foundations of time-series deep learning: Developing a rigorous theory for deep learning in time series is crucial for understanding the inductive biases of these models and provides a foundation for more principled architecture design and interpretation beyond empirical benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2603.29612)
- [PDF](https://arxiv.org/pdf/2603.29612)

