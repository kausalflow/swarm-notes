---
# CSL-compatible fields
title: "DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers"
author:
  - literal: "Habib Irani"
  - literal: "Vangelis Metsis"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.14640"

# Custom fields
paper_id: "2509.14640"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "time-series"
  - "positional-encoding"
  - "efficient-transformer"
architectures:
  - "transformer"
datasets:
  []
concept_slugs:
  - "dywpe-dynamic-wavelet-positional-encoding"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:22Z"
created_at: "2026-04-24T06:59:22Z"
---

# DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers

**Authors**: Habib Irani, Vangelis Metsis
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.14640](https://arxiv.org/abs/2509.14640)

## Summary

Current positional encoding methods in transformers rely on static sequence indices, failing to capture the non-stationary dynamics inherent in time series data. This paper proposes Dynamic Wavelet Positional Encoding (DyWPE), which derives positional embeddings from the input signal itself using the Discrete Wavelet Transform. Experiments across ten diverse datasets show that this signal-aware approach provides superior performance, particularly for long-range dependencies and complex signals like those found in biomedical applications.

## Key Contributions

- Introduced DyWPE, a signal-aware positional encoding framework that uses Discrete Wavelet Transform (DWT) to integrate signal characteristics into transformer positional embeddings.
- Demonstrated that DyWPE consistently outperforms state-of-the-art static positional encoding methods across ten diverse time series datasets.
- Showed significant improvements in performance for longer sequences and complex biomedical time series signals compared to index-based methods.

## Open Questions & Future Work

- [[automated-wavelet-decomposition-selection]]

## Key Concepts

- [[dywpe-dynamic-wavelet-positional-encoding]]: A signal-aware positional encoding framework for time series transformers that uses Discrete Wavelet Transform to derive embeddings from input signals.

## Archivist Review

The paper introduces a novel, signal-aware positional encoding method specifically designed for time series transformers, which is highly relevant to the vault. I have approved the framework as a concept and the problem of automating its configuration as an open question, as these represent a shift toward content-based rather than index-based temporal modeling in transformer architectures. No datasets were approved as none were highlighted as specific, reusable benchmarks central to the field.

### Approved Concepts
- Dynamic Wavelet Positional Encoding (DyWPE): The framework provides a reusable, signal-aware alternative to static index-based positional encodings, specifically addressing the non-stationary nature of time series.

### Approved Open Questions
- Automated Wavelet Decomposition Selection: This addresses a key bottleneck in applying signal-aware architectures, as current methods often require task-specific manual tuning that limits generalizability.

## Links

- [Abstract](https://arxiv.org/abs/2509.14640)
- [PDF](https://arxiv.org/pdf/2509.14640)

