---
# CSL-compatible fields
title: "CADENCE: A Confidence-Adaptive Dual-Expert Network for Fast and Accurate Time Series Classification"
author:
  - literal: "Onisa Mpaunda"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.35929"

# Custom fields
paper_id: "2609.35929"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cadence"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:15:33Z"
created_at: "2026-10-01T11:15:33Z"
---

# CADENCE: A Confidence-Adaptive Dual-Expert Network for Fast and Accurate Time Series Classification

**Authors**: Onisa Mpaunda
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.35929](https://arxiv.org/abs/2609.35929)

## Summary

CADENCE is a CPU-native dual-expert network for time series classification that balances high accuracy with fast execution by combining a Convolutional Linear Expert with a Distributional Interval Expert. Using an internal validation meta-router with confidence-weighted soft blending, CADENCE matches the accuracy of state-of-the-art meta-ensembles like HIVE-COTE 2.0 on the UCR Archive while operating orders of magnitude faster.

## Key Contributions

- Introduces CADENCE, a unified CPU-native dual-expert architecture that decouples time series representation learning into a Convolutional Linear Expert and a Distributional Interval Expert.
- Appplies an internal validation meta-router with rare-class preservation to dynamically select between pure expert routing and confidence-weighted soft blending.
- Achieves a grand mean accuracy of 0.8864 across all 109 equal-length UCR Archive datasets, ranking #2 overall with no statistically significant difference from HIVE-COTE 2.0 while running in an average of 17.53 seconds per dataset.

## Limitations

Evaluated specifically on equal-length UCR Archive datasets; extension to variable-length multivariate series or streaming settings remains open.

## Key Concepts

- [[cadence]]: A confidence-adaptive dual-expert network that decouples time series representation learning into deterministic convolutional linear and distributional interval expert pathways.

## Archivist Review

Approved the central framework concept CADENCE for its distinct dual-expert architecture and confidence-adaptive routing. No open questions or datasets met the strict novelty and standalone archival criteria.

### Approved Concepts
- CADENCE: CADENCE is the central dual-expert architecture introduced for time series classification, combining deterministic dilated features with Woodbury ridge classification and an ExtraTrees ensemble via a confidence-adaptive meta-router.

## Links

- [Abstract](https://arxiv.org/abs/2609.35929)
- [PDF](https://arxiv.org/pdf/2609.35929)

