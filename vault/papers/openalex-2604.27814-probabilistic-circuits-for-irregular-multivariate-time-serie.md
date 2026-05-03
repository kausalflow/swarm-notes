---
# CSL-compatible fields
title: "Probabilistic Circuits for Irregular Multivariate Time Series Forecasting"
author:
  - literal: "Christian Klötergens"
  - literal: "Vijaya Krishna Yalavarthi"
  - literal: "Lars Schmidt-Thieme"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27814"

# Custom fields
paper_id: "2604.27814"
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
  - "probabilistic-circuits-for-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:13:34Z"
created_at: "2026-05-03T07:13:34Z"
---

# Probabilistic Circuits for Irregular Multivariate Time Series Forecasting

**Authors**: Christian Klötergens, Vijaya Krishna Yalavarthi, Lars Schmidt-Thieme
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27814](https://arxiv.org/abs/2604.27814)

## Summary

CircuITS addresses the challenge of joint probabilistic forecasting for irregular multivariate time series by leveraging the structural properties of probabilistic circuits. Unlike existing methods that may produce inconsistent or unreliable forecasts, this approach guarantees valid joint distributions while maintaining the expressivity needed to capture complex channel dependencies. Experimental results indicate that CircuITS provides superior joint and marginal density estimation compared to leading baselines.

## Key Contributions

- Introduces CircuITS, a novel architecture utilizing probabilistic circuits to ensure valid joint distribution modeling for irregular multivariate time series.
- Enables superior joint and marginal density estimation by effectively balancing model expressivity with consistent marginalization.
- Demonstrates competitive performance against state-of-the-art baselines on four real-world irregular multivariate time series benchmarks.

## Open Questions & Future Work

- [[scalable-mixture-complexity-circuits]]

## Key Concepts

- [[probabilistic-circuits-for-forecasting]]: A neural architecture leveraging probabilistic circuits to ensure valid joint distribution modeling for irregular multivariate time series forecasting.

## Archivist Review

I approved the probabilistic circuit approach as a foundational concept because it provides a structural solution to joint density estimation in time series. I also approved the open question regarding the scalability of mixture components, as it addresses a fundamental computational limit of using probabilistic circuits in high-dimensional multivariate contexts. Other candidates were rejected to maintain the focus on the primary methodological contribution and the most significant remaining challenge.

### Approved Concepts
- Probabilistic Circuits for Forecasting: The paper leverages probabilistic circuits as a core architectural framework for joint modeling in time series, offering a structured approach to guarantee valid joint distributions which is highly relevant for multivariate forecasting.

### Approved Open Questions
- Scalable mixture component scaling: Overcoming this scalability bottleneck is essential for applying circuit-based probabilistic models to real-world multivariate scenarios with complex dependency structures.

## Links

- [Abstract](https://arxiv.org/abs/2604.27814)
- [PDF](https://arxiv.org/pdf/2604.27814)

