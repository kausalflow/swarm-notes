---
# CSL-compatible fields
title: "Wavelet Flow Matching for Time Series"
author:
  - literal: "Lucas Poinsignon"
  - literal: "Jorge da Silva Goncalves"
  - literal: "Samuel Ruipérez-Campillo"
  - literal: "Julia Elisabeth Vogt"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39374"

# Custom fields
paper_id: "2609.39374"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "generative-adversarial-network"
  - "transformer"
  - "attention-mechanism"
  - "benchmark"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "wavelet-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:07:52Z"
created_at: "2026-10-03T10:07:52Z"
---

# Wavelet Flow Matching for Time Series

**Authors**: Lucas Poinsignon, Jorge da Silva Goncalves, Samuel Ruipérez-Campillo, Julia Elisabeth Vogt
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39374](https://arxiv.org/abs/2609.39374)

## Summary

This paper introduces wavelet flow matching for multivariate time series generation, operating on multilevel discrete wavelet coefficients to capture multi-scale temporal dynamics. By leveraging the naturally different variances across wavelet scales, the model implicitly realizes a coarse-to-fine generation schedule without extra scheduling overhead. Combined with a channel-token transformer to capture cross-channel dependencies, the method achieves top-tier generation performance across diverse benchmark datasets and sequence lengths.

## Key Contributions

- Proposes wavelet flow matching for multivariate time series generation by operating on multilevel discrete wavelet coefficients.
- Leverages the naturally differing variances of wavelet coefficients to induce an implicit coarse-to-fine generative process without explicit multi-scale schedules.
- Pairs the wavelet transform with a channel-token transformer to model cross-channel dependencies effectively.
- Achieves best or tied performance on a majority of dataset-metric combinations across seven benchmark datasets and four sequence lengths, with substantial improvements in Context-FID and discriminative score.

## Limitations

Future work could explore scaling to higher-dimensional or irregular time series and investigating alternative wavelet families.

## Open Questions & Future Work

- [[conditional-time-series-forecasting-imputation]]

## Key Concepts

- [[wavelet-flow-matching]]: A generative framework for multivariate time series using flow matching operating on multilevel discrete wavelet coefficients.

## Archivist Review

We approved 'Wavelet Flow Matching' as a standalone concept representing the combination of flow matching with wavelet decompositions for time series generation. We approved one core open question regarding conditional extension, and rejected minor subcomponents and low-impact hyperparameter future work. No specific named benchmark datasets were highlighted in the abstract.

### Approved Concepts
- Wavelet Flow Matching: Introduces flow matching in the wavelet domain for time series generation, leveraging multilevel discrete wavelet coefficients to capture multi-scale temporal structures.

### Approved Open Questions
- Conditional Forecasting and Imputation: Crucial for broadening the applicability of wavelet-domain flow matching models to standard predictive and operational time-series problems.

### Rejected Candidates
- [concept] Channel-Token Transformer (`channel-token-transformer`) - subcomponent_of_broader_mechanism: Subcomponent of a broader architecture or standard attention variant applied locally.
- [open_question] Adaptive Wavelet Decomposition Depth (`adaptive-wavelet-decomposition-depth`) - low_impact: Future work direction focusing on hyperparameter tuning and decomposition depth adaptation without a broader architectural bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.39374)
- [PDF](https://arxiv.org/pdf/2609.39374)

