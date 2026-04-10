---
# CSL-compatible fields
title: "Channel-wise Retrieval for Multivariate Time Series Forecasting"
author:
  - literal: "Junhyuk Kang"
  - literal: "Jun Seo"
  - literal: "Soyeon Park"
  - literal: "Sangjun Han"
  - literal: "Seohui Bae"
  - literal: "Hyeokjun Choe"
  - literal: "Soonyoung Lee"
issued:
  date-parts:
    - [2026, 4, 7]
url: "https://arxiv.org/abs/2604.05543"

# Custom fields
paper_id: "2604.05543"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "retrieval-augmented-generation"
  - "rag"
architectures:
  []
datasets:
  []
concept_slugs:
  - "channel-wise-retrieval-augmented-forecasting-craft"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-10T06:25:58Z"
created_at: "2026-04-10T06:25:58Z"
---

# Channel-wise Retrieval for Multivariate Time Series Forecasting

**Authors**: Junhyuk Kang, Jun Seo, Soyeon Park, Sangjun Han, Seohui Bae, Hyeokjun Choe, Soonyoung Lee
**Date**: 2026-04-07
**Paper ID**: [openalex:2604.05543](https://arxiv.org/abs/2604.05543)

## Summary

Multivariate time series forecasting often fails to capture long-range dependencies because existing retrieval-augmented models apply uniform historical references across all variables, ignoring their distinct spectral characteristics. CRAFT addresses this by performing independent, channel-wise retrieval, enabling the capture of variable-specific periodicities. The framework optimizes this process through a two-stage approach: pruning candidate segments via a sparse time-domain relation graph and ranking them by spectral similarity in the frequency domain. Experiments across seven benchmarks show that this method significantly improves forecasting accuracy and inference efficiency over existing state-of-the-art models.

## Key Contributions

- Proposes CRAFT, a channel-wise retrieval-augmented forecasting framework that accounts for inter-variable heterogeneity by performing independent retrieval per channel.
- Implements a two-stage retrieval pipeline using a sparse time-domain relation graph for pruning and frequency-domain spectral similarity for ranking, enhancing both accuracy and inference efficiency.
- Demonstrates that CRAFT achieves superior performance compared to state-of-the-art multivariate forecasting baselines across seven public benchmarks.

## Open Questions & Future Work

- [[optimal-integration-channel-wise-references]]

## Key Concepts

- [[channel-wise-retrieval-augmented-forecasting-craft]]: A retrieval-augmented forecasting framework that retrieves historical segments independently for each channel to capture variable-specific periodicities and spectral profiles.

## Archivist Review

The paper provides a novel retrieval-augmented forecasting mechanism by decoupling retrieval channels to address inter-variable heterogeneity. I approved the CRAFT framework as it provides a clear, reusable paradigm for multivariate retrieval and included an open question regarding how to move beyond simple additive corrections in such architectures. No additional datasets were included, as none were identified as uniquely novel contributions.

### Approved Concepts
- Channel-wise Retrieval-Augmented Forecasting (CRAFT): Introduces a novel retrieval mechanism that accounts for inter-variable heterogeneity in multivariate time series by decoupling the retrieval process for each channel, moving away from channel-agnostic retrieval.

### Approved Open Questions
- Integrating channel-wise retrieved references: Understanding whether more sophisticated, non-additive fusion techniques (e.g., cross-attention or gating mechanisms) can better leverage channel-wise retrieved references is critical for maximizing the potential of retrieval-augmented forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2604.05543)
- [PDF](https://arxiv.org/pdf/2604.05543)

