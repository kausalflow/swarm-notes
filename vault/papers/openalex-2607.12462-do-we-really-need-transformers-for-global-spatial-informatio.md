---
# CSL-compatible fields
title: "Do We Really Need Transformers for Global Spatial Information Extraction in Traffic Forecasting?"
author:
  - literal: "Qihang Zhang"
  - literal: "Siyao Zhang"
  - literal: "Letao Kang"
  - literal: "Wenzhe Liang"
  - literal: "Miao Zhang"
  - literal: "Zhao Zhang"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12462"

# Custom fields
paper_id: "2607.12462"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "attention-mechanism"
  - "spatial-attention"
  - "graph-neural-network"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:02Z"
created_at: "2026-07-17T07:10:02Z"
---

# Do We Really Need Transformers for Global Spatial Information Extraction in Traffic Forecasting?

**Authors**: Qihang Zhang, Siyao Zhang, Letao Kang, Wenzhe Liang, Miao Zhang, Zhao Zhang
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12462](https://arxiv.org/abs/2607.12462)

## Summary

This paper investigates the necessity of complex adaptive attention mechanisms for global spatial information extraction in traffic forecasting. By employing a controlled ablation framework across six standard benchmarks, the authors demonstrate that a simple O(N) uniform global aggregation operator performs comparably to O(N^2) spatial attention mechanisms. The study concludes that high-degree-of-freedom attention is often redundant and should only be employed when it provides stable performance gains over simpler uniform spatial mixing.

## Key Contributions

- Proposes a controlled ablation framework to isolate and evaluate the necessity of attention-based spatial mixing in traffic forecasting.
- Demonstrates that a simple uniform full-range mixing operator achieves performance parity (0.14% difference) with standard spatial attention across six benchmarks while reducing complexity from O(N^2) to O(N).
- Introduces a decomposition analysis of spatial attention into a row-uniform global background and non-uniform residuals, revealing that attention's marginal gain is highly dataset-dependent.

## Links

- [Abstract](https://arxiv.org/abs/2607.12462)
- [PDF](https://arxiv.org/pdf/2607.12462)

