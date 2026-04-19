---
# CSL-compatible fields
title: "On the robustness of Mann-Kendall tests used to forecast critical transitions"
author:
  - literal: "Tristan Gamot"
  - literal: "Nils Thibeau--Sutre"
  - literal: "Tom J. M. Van Dooren"
issued:
  date-parts:
    - [2026, 4, 16]
url: "https://arxiv.org/abs/2604.15230"

# Custom fields
paper_id: "2604.15230"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-19T06:24:01Z"
created_at: "2026-04-19T06:24:01Z"
---

# On the robustness of Mann-Kendall tests used to forecast critical transitions

**Authors**: Tristan Gamot, Nils Thibeau--Sutre, Tom J. M. Van Dooren
**Date**: 2026-04-16
**Paper ID**: [openalex:2604.15230](https://arxiv.org/abs/2604.15230)

## Summary

This paper evaluates the robustness of non-parametric Mann-Kendall trend tests when applied to time series with autocorrelation, specifically in the context of detecting early warning signals (EWS) for critical transitions. By comparing empirical distributions of the Mann-Kendall statistic against theoretical Gaussian assumptions, the authors reveal that these tests frequently lead to inflated type I error rates. The study concludes that current practice using these tests is unreliable for forecasting critical transitions and suggests transitioning to alternative statistical methods.

## Key Contributions

- Demonstrates that the Gaussian assumption underlying Mann-Kendall trend tests is invalid for autocorrelated time series commonly encountered in critical transition detection.
- Provides a comprehensive analysis showing that empirical distributions of the Mann-Kendall statistic deviate significantly from theoretical expectations, leading to inflated type I error rates.
- Recommends against the usage of Mann-Kendall tests for early warning signal (EWS) detection and points toward more robust alternative methodologies.

## Open Questions & Future Work

- [[robust-ews-trend-testing]]

## Archivist Review

This paper provides a critical evaluation of a widely-used statistical test in time-series forecasting, specifically exposing a fundamental failure mode in its application to EWS. The proposed open question is approved because it identifies a substantial bottleneck (inflated Type I errors in EWS detection) and defines the path for future methodology research. No new concepts were approved as the core contribution is a negative result regarding an existing statistical test rather than the proposal of a novel architectural or algorithmic concept.

### Approved Open Questions
- Robust trend testing for EWS: This is critical because the current standard practice of using Mann-Kendall tests for EWS leads to a "cry wolf" effect, where false positives are routinely flagged due to the mismatch between the theoretical and empirical distributions of the test statistic. Finding a robust, computationally efficient alternative is essential for reliable early warning systems.

## Links

- [Abstract](https://arxiv.org/abs/2604.15230)
- [PDF](https://arxiv.org/pdf/2604.15230)

