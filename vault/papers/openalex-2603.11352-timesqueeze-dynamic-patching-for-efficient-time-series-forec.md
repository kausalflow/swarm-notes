---
# CSL-compatible fields
title: "TimeSqueeze: Dynamic Patching for Efficient Time Series Forecasting"
author:
  - literal: "Sravan Kumar Ankireddy"
  - literal: "Nikita Seleznev"
  - literal: "Nam H. Nguyen"
  - literal: "Yulun Wu"
  - literal: "Senthil Kumar"
  - literal: "Furong Huang"
  - literal: "C. Bayan Bruss"
issued:
  date-parts:
    - [2026, 3, 11]
url: "https://arxiv.org/abs/2603.11352"

# Custom fields
paper_id: "2603.11352"
paper_source: "openalex"
domain: "time-series"
tags:
  - "transformer"
  - "state-space-model"
  - "time-series"
  - "forecasting"
  - "efficient-transformer"
  - "tokenization"
  - "long-context"
architectures:
  - "transformer"
datasets:
  - "long-horizon forecasting benchmarks"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:07Z"
created_at: "2026-03-27T14:09:07Z"
---

# TimeSqueeze: Dynamic Patching for Efficient Time Series Forecasting

**Authors**: Sravan Kumar Ankireddy, Nikita Seleznev, Nam H. Nguyen, Yulun Wu, Senthil Kumar, Furong Huang, C. Bayan Bruss
**Date**: 2026-03-11
**Paper ID**: [openalex:2603.11352](https://arxiv.org/abs/2603.11352)

## Summary

This paper introduces TimeSqueeze, a novel dynamic patching mechanism designed to overcome the tokenization trade-off in Transformer-based time series models, where point-wise embeddings offer fidelity but poor efficiency, and fixed patching sacrifices temporal structure. TimeSqueeze first extracts full-resolution features using a lightweight state-space encoder, then segments the sequence adaptively, creating shorter patches for high-complexity regions and longer patches for smooth segments. This content-aware compression drastically reduces the sequence length fed to the Transformer backbone, leading to up to 20x faster convergence and 8x better data efficiency in pre-training. Empirical results on long-horizon forecasting benchmarks confirm that TimeSqueeze consistently yields superior performance compared to fixed-patching and point-wise baselines.

## Key Contributions

- Introduction of TimeSqueeze, a dynamic patching mechanism that adaptively selects patch boundaries based on local signal complexity, resolving the fidelity vs. efficiency trade-off in Transformer tokenization for time series.
- The mechanism uses a lightweight state-space encoder for feature extraction followed by content-aware segmentation, allocating shorter patches to information-dense regions and longer patches to smooth segments.
- Achieved up to 20x faster convergence and 8x higher data efficiency during large-scale pre-training compared to standard point-token baselines.
- Demonstrated consistent outperformance over fixed-size patching and point-wise tokenization methods across various long-horizon forecasting tasks.

## Limitations

The paper focuses primarily on pre-training efficiency and long-horizon forecasting; the performance impact on very short sequence tasks or specific anomaly detection scenarios is not detailed.

## Open Questions & Future Work

- [[learning-end-to-end-dynamic-patching-rate]]
- [[variable-rate-patching-large-scale-forecasting]]
- [[generalizing-dynamic-patching-to-other-backbones]]
- [[probabilistic-forecasting-with-dynamic-patching]]

## Key Concepts

- [TimeSqueeze Dynamic Patching](../concepts/timesqueeze-dynamic-patching.md): A dynamic patching mechanism for time series forecasting that adaptively selects patch boundaries based on local signal complexity to optimize tokenization efficiency for Transformer models.

## Datasets

- [long-horizon forecasting benchmarks](../datasets/long-horizon-forecasting-benchmarks.md)

## Limitations

The paper focuses primarily on pre-training efficiency and long-horizon forecasting; the performance impact on very short sequence tasks or specific anomaly detection scenarios is not detailed.

## Links

- [Abstract](https://arxiv.org/abs/2603.11352)
- [PDF](https://arxiv.org/pdf/2603.11352)

