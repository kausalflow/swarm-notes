---
# CSL-compatible fields
title: "Recursive Multiple Change Point Detection of Nonstationary Time Series: Instability Tests, Estimation and Confidence Intervals"
author:
  - literal: "Leheng Cai"
  - literal: "Zhou Zhou"
issued:
  date-parts:
    - [2026, 8, 13]
url: "https://arxiv.org/abs/2608.13352"

# Custom fields
paper_id: "2608.13352"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bootstrap-assisted-robust-binary-segmentation-barbs"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-16T05:17:51Z"
created_at: "2026-08-16T05:17:51Z"
---

# Recursive Multiple Change Point Detection of Nonstationary Time Series: Instability Tests, Estimation and Confidence Intervals

**Authors**: Leheng Cai, Zhou Zhou
**Date**: 2026-08-13
**Paper ID**: [openalex:2608.13352](https://arxiv.org/abs/2608.13352)

## Summary

This paper introduces bootstrap-assisted robust binary segmentation (BARBS), a recursive methodology for multiple change point detection in nonstationary time series. By employing a novel Gaussian multiplier bootstrap for CUSUM statistics, BARBS controls Type I error and attains optimal localization rates under complex temporal dependencies. Theoretical properties including uniform consistency and asymptotic distributions of refined estimators are established. Empirical evaluations on simulations and U.S. inflation data confirm the method's superior performance and practical relevance.

## Key Contributions

- Proposed bootstrap-assisted robust binary segmentation (BARBS) for recursive multiple change point detection under nonstationary temporal dynamics.
- Designed a novel Gaussian multiplier bootstrap for CUSUM statistics ensuring Type I error control under the null hypothesis.
- Established theoretical guarantees including uniform consistency and optimal individual localization rates under both fixed and vanishing jump magnitudes.
- Demonstrated practical utility by identifying macroeconomic change points in U.S. inflation data that align with documented historical episodes.

## Open Questions & Future Work

- [[high-dimensional-nonstationary-change-point-detection]]

## Key Concepts

- [[bootstrap-assisted-robust-binary-segmentation-barbs]]: A recursive binary segmentation method for multiple change point detection in nonstationary time series using a Gaussian multiplier bootstrap for robust CUSUM statistics.

## Archivist Review

Approved the core methodological concept (BARBS) for change point detection and an open question on high-dimensional extension, while rejecting the broader structural change question as too open-ended. No datasets were approved since no standalone public benchmark dataset was introduced.

### Approved Concepts
- Bootstrap-Assisted Robust Binary Segmentation (BARBS): BARBS provides a novel recursive binary segmentation approach with Gaussian multiplier bootstrap for CUSUM statistics, ensuring robust Type I error control and optimal localization rates under nonstationary temporal dynamics.

### Approved Open Questions
- High-Dimensional Nonstationary Change Point Detection: High-dimensional change point detection under nonstationary and dependent noise is an important and challenging frontier in modern statistics and machine learning.

### Rejected Candidates
- [open_question] Generalized Structural Change Detection (`generalized-structural-change-detection`) - low_impact: Too general as a research direction and resembles boilerplate future work extensions on structural change detection.

## Links

- [Abstract](https://arxiv.org/abs/2608.13352)
- [PDF](https://arxiv.org/pdf/2608.13352)

