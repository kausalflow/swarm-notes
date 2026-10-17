---
# CSL-compatible fields
title: "GBTSVR: Twin Support Vector Regression via Granular Ball Computing"
author:
  - literal: "A. Quadir"
  - literal: "M. Tanveer"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20053"

# Custom fields
paper_id: "2610.20053"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "granular-ball-computing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:56:22Z"
created_at: "2026-10-17T08:56:22Z"
---

# GBTSVR: Twin Support Vector Regression via Granular Ball Computing

**Authors**: A. Quadir, M. Tanveer
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20053](https://arxiv.org/abs/2610.20053)

## Summary

This paper proposes Granular Ball Twin Support Vector Regression (GBTSVR) and its quantile extension (GB-TSVQR) to overcome the sensitivity of conventional point-wise regression to noise and outliers. By replacing individual samples with structure-preserving granular balls as basic learning units, the proposed models construct nonparallel bounding functions that enhance robustness and generalization. Additionally, GB-TSVQR incorporates quantile regression to handle heterogeneous trends and asymmetric error distributions, outperforming state-of-the-art models on synthetic, time-series, and contaminated datasets.

## Key Contributions

- Introduces Granular Ball Twin Support Vector Regression (GBTSVR) and its quantile extension (GB-TSVQR) to replace individual sample points with structure-preserving granular balls as basic learning units.
- Leverages region-level representations to suppress noise and outliers while preserving intrinsic data geometry in regression tasks.
- Incorporates quantile regression into the granular ball framework (GB-TSVQR) to capture heterogeneous trends and asymmetric error distributions across quantile levels.
- Demonstrates consistent outperformance over state-of-the-art regression models on synthetic, time-series, and outlier-contaminated benchmarks.

## Open Questions & Future Work

- [[granular-ball-regression-extensions]]

## Key Concepts

- [[granular-ball-computing]]: A region-level representation framework that replaces individual data points with compact, structure-preserving granular balls to enhance robustness against noise and outliers.

## Archivist Review

Approved Granular Ball Computing as a central reusable concept for robust region-level modeling and included its natural scaling open question. No specific named datasets were provided in the abstract.

### Approved Concepts
- Granular Ball Computing: Central to the paper's novelty by replacing individual data points with compact, structure-preserving granular balls as fundamental learning units.

### Approved Open Questions
- Extensions of Granular Ball Regression: Extending the granular ball regression framework to high-dimensional, streaming, and deep architectures represents a crucial methodological direction for handling large-scale real-world data streams.

## Links

- [Abstract](https://arxiv.org/abs/2610.20053)
- [PDF](https://arxiv.org/pdf/2610.20053)

