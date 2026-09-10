---
# CSL-compatible fields
title: "Quantile-Led Feature Extraction for Multi-Horizon Predictive Maintenance in Industrial Manufacturing Systems"
author:
  - literal: "David J Poland"
  - literal: "Daniele Ravì"
  - literal: "Na Helian"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.07533"

# Custom fields
paper_id: "2609.07533"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
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
processed_at: "2026-09-10T09:17:54Z"
created_at: "2026-09-10T09:17:54Z"
---

# Quantile-Led Feature Extraction for Multi-Horizon Predictive Maintenance in Industrial Manufacturing Systems

**Authors**: David J Poland, Daniele Ravì, Na Helian
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.07533](https://arxiv.org/abs/2609.07533)

## Summary

This paper investigates feature extraction for multi-horizon predictive maintenance in industrial manufacturing, demonstrating that fixed preprocessing extractors fail when applied across different forecasting horizons. The authors propose a quantile-led feature extraction framework using a dual-stage MLP-QRNN hierarchy to capture conditional distributions across sensor channels. Evaluations across 72 machines in 9 facilities reveal that horizon-conditioned feature extraction significantly outperforms static representations when transitioning from short-term to long-term regimes.

## Key Contributions

- Introduces a quantile-led feature-extraction framework based on a dual-stage MLP-QRNN hierarchy for industrial predictive maintenance
- Demonstrates that feature representations do not transfer reliably across forecasting horizons unless capacity and temporal conditioning are scaled appropriately
- Evaluates across a fixed 13-pipeline ablation spanning 1-hour, 70-hour, and 30-day regimes across 72 machines in 9 industrial facilities

## Limitations

Representations fail to transfer reliably beyond their designed forecasting horizon without explicit scaling of feature capacity, temporal embedding, activation strategy, and sensor breadth.

## Archivist Review

The submitted candidate describes an application-specific extension for predictive maintenance models and does not represent a broadly reusable open question or concept. Therefore, all candidates were rejected according to vault policy.

### Rejected Candidates
- [open_question] Joint Optimization and Quantile Selection (`joint-optimization-and-quantile-selection-in-pdms`) - low_impact: The open question focuses on paper-specific tuning and extensions of a dual-stage quantile model without addressing a broadly reusable theoretical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.07533)
- [PDF](https://arxiv.org/pdf/2609.07533)

