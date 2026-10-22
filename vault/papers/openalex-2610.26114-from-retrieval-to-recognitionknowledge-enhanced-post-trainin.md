---
# CSL-compatible fields
title: "From Retrieval to Recognition:Knowledge-Enhanced Post-training of Time Series Foundation Models for Classification"
author:
  - literal: "Zhen Liu"
  - literal: "Yucheng Wang"
  - literal: "Yingpeng Du"
  - literal: "Tianjun Wei"
  - literal: "Qianli Ma"
  - literal: "Min Wu"
  - literal: "Jie Zhang"
  - literal: "Zhu Sun"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2610.26114"

# Custom fields
paper_id: "2610.26114"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "pre-training"
  - "fine-tuning"
  - "retrieval-augmented-generation"
  - "text-classification"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "retrieval-to-recognition"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-22T09:43:46Z"
created_at: "2026-10-22T09:43:46Z"
---

# From Retrieval to Recognition:Knowledge-Enhanced Post-training of Time Series Foundation Models for Classification

**Authors**: Zhen Liu, Yucheng Wang, Yingpeng Du, Tianjun Wei, Qianli Ma, Min Wu, Jie Zhang, Zhu Sun
**Date**: 2026-10-19
**Paper ID**: [openalex:2610.26114](https://arxiv.org/abs/2610.26114)

## Summary

Time series foundation models often struggle with efficient knowledge utilization during downstream classification due to parameter entanglement. To address this, the authors propose Retrieval-to-Recognition (R2R), a plug-and-play post-training paradigm that retrieves instance-level numerical knowledge from an external knowledge base using a decoupled query encoder. This explicit knowledge is fused with the model's implicit parametric embeddings, enabling joint knowledge transfer. Extensive experiments across 158 datasets show that R2R consistently boosts the classification performance of state-of-the-art time series foundation models.

## Key Contributions

- Proposes Retrieval-to-Recognition (R2R), a plug-and-play post-training paradigm that bridges explicit knowledge retrieval and implicit parametric tuning for time series classification.
- Introduces a decoupled query encoder to extract discriminative patterns and retrieve instance-level numerical knowledge from a constructed knowledge base.
- Demonstrates consistent performance improvements across 158 time series datasets when adapting state-of-the-art time series foundation models.

## Open Questions & Future Work

- [[multivariate-time-series-retrieval]]

## Key Concepts

- [[retrieval-to-recognition]]: A plug-and-play post-training paradigm for time series foundation models that combines explicit instance-level knowledge retrieval with implicit parametric embeddings for classification transfer.

## Archivist Review

The core concept 'retrieval-to-recognition' introduces a valuable framework combining explicit retrieval with implicit parameter adaptation for TSFM post-training. The open question addresses multivariate extension for retrieval-augmented architectures. No specific datasets were provided.

### Approved Concepts
- Retrieval-to-Recognition: Introduces a novel plug-and-play post-training paradigm that combines explicit knowledge retrieval with implicit parameter adaptation for time series classification.

### Approved Open Questions
- Natively Multivariate Time Series Retrieval: Crucial for scaling retrieval-augmented time series models to complex real-world multivariate domains such as multi-sensor monitoring and healthcare diagnostics.

## Links

- [Abstract](https://arxiv.org/abs/2610.26114)
- [PDF](https://arxiv.org/pdf/2610.26114)

