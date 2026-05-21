---
# CSL-compatible fields
title: "Wavelet Based Time Series Models with Time-Varying Thresholds"
author:
  - literal: "Rhea Davis"
  - literal: "N. Balakrishna"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.17864"

# Custom fields
paper_id: "2605.17864"
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
  - "wavelet-based-time-varying-threshold-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:33:27Z"
created_at: "2026-05-21T08:33:27Z"
---

# Wavelet Based Time Series Models with Time-Varying Thresholds

**Authors**: Rhea Davis, N. Balakrishna
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.17864](https://arxiv.org/abs/2605.17864)

## Summary

This paper introduces a threshold-based time-series model that replaces static threshold parameters with time-varying representations derived from wavelet series expansions. This approach provides significant advantages in modeling data with both abrupt shifts and smooth evolutionary patterns, overcoming limitations inherent in conventional Fourier-based decomposition. The authors validate the framework through simulation studies and demonstrate its empirical utility on real-world datasets.

## Key Contributions

- Introduces a novel time-series threshold model where the threshold parameter is dynamically represented via wavelet series expansion.
- Demonstrates superior flexibility in modeling irregular, abrupt, and smooth changes compared to traditional Fourier-based threshold methods.
- Validates the model's predictive capability and adaptability through extensive simulation and real-world data analysis.

## Open Questions & Future Work

- [[extending-wavelet-threshold-models]]

## Key Concepts

- [[wavelet-based-time-varying-threshold-model]]: A threshold model that employs wavelet series expansion to flexibly represent time-varying thresholds in time-series data.

## Archivist Review

I have approved the core methodological concept, as it provides a clear, reusable framework for non-stationary threshold modeling that improves upon traditional Fourier methods. The open question was refined to better characterize the challenge of extending these methods to multivariate and multi-regime settings. I rejected no candidates because the initial submission was highly selective and focused.

### Approved Concepts
- Wavelet-based time-varying threshold model: The approach replaces static or Fourier-based threshold parameters with wavelet expansions to capture multi-scale time-series dynamics, offering better flexibility for irregular and abrupt changes.

### Approved Open Questions
- Extending Wavelet Threshold Models: Generalizing this framework to multiple regimes and multivariate contexts is critical for modeling realistic systems where dependencies are complex and non-stationary.

## Links

- [Abstract](https://arxiv.org/abs/2605.17864)
- [PDF](https://arxiv.org/pdf/2605.17864)

