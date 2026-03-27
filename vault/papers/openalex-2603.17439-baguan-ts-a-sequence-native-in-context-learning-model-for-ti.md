---
# CSL-compatible fields
title: "Baguan-TS: A Sequence-Native In-Context Learning Model for Time Series Forecasting with Covariates"
author:
  - literal: "Linxiao Yang"
  - literal: "Xue (Snow) Jiang"
  - literal: "Gezheng Xu"
  - literal: "Tian Zhou"
  - literal: "Min Yang"
  - literal: "Zhaoyang Zhu"
  - literal: "Linyuan Geng"
  - literal: "Zhipeng Zeng"
  - literal: "Qiming Chen"
  - literal: "Xinyue Gu"
  - literal: "Rong Jin"
  - literal: "Liang Sun"
issued:
  date-parts:
    - [2026, 3, 18]
url: "https://arxiv.org/abs/2603.17439"

# Custom fields
paper_id: "2603.17439"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "in-context-learning"
  - "attention-mechanism"
  - "long-context"
  - "evaluation"
architectures:
  - "transformer"
datasets:
  - "ETTh1"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:10:03Z"
created_at: "2026-03-27T14:10:03Z"
---

# Baguan-TS: A Sequence-Native In-Context Learning Model for Time Series Forecasting with Covariates

**Authors**: Linxiao Yang, Xue (Snow) Jiang, Gezheng Xu, Tian Zhou, Min Yang, Zhaoyang Zhu, Linyuan Geng, Zhipeng Zeng, Qiming Chen, Xinyue Gu, Rong Jin, Liang Sun
**Date**: 2026-03-18
**Paper ID**: [openalex:2603.17439](https://arxiv.org/abs/2603.17439)

## Summary

Baguan-TS is proposed as a sequence-native framework to enable in-context learning (ICL) for time series forecasting with covariates, overcoming the reliance of prior ICL methods on hand-crafted features. The core is a 3D Transformer architecture designed to attend simultaneously across temporal, variable, and context dimensions of the input sequences. Key technical innovations include a target-space retrieval-based local calibration technique for training stability and a context-overfitting strategy to combat output oversmoothing. Evaluations show Baguan-TS consistently surpasses established baselines on public benchmarks, yielding significant improvements in both point and probabilistic forecasting accuracy.

## Key Contributions

- Introduced Baguan-TS, a unified framework for time series forecasting that integrates raw-sequence representation learning with In-Context Learning (ICL) using a 3D Transformer.
- Developed a feature-agnostic, target-space retrieval-based local calibration technique to ensure training stability and calibration for the high-capacity 3D Transformer model.
- Mitigated output oversmoothing using a novel context-overfitting strategy during training.
- Achieved state-of-the-art performance on public time series benchmarks with covariates, demonstrating superior point and probabilistic forecasting metrics.

## Limitations

The abstract does not explicitly detail limitations, but large-scale 3D Transformers often face challenges with inference latency and memory usage compared to traditional models.

## Open Questions & Future Work

- [[balancing-denoising-and-selection-in-icl-time-series]]

## Key Concepts

- [Baguan-TS](../concepts/baguan-ts.md): A sequence-native in-context learning model for time series forecasting that uses a 3D Transformer to jointly attend over temporal, variable, and context axes.
- [Target-Space Retrieval-Based Local Calibration](../concepts/target-space-retrieval-calibration.md): A feature-agnostic calibration method used during training and inference to improve stability and performance in sequence-native ICL models by referencing a local set of relevant examples in the target space.

## Datasets

- [ETTh1](../datasets/etth1.md)

## Limitations

The abstract does not explicitly detail limitations, but large-scale 3D Transformers often face challenges with inference latency and memory usage compared to traditional models.

## Links

- [Abstract](https://arxiv.org/abs/2603.17439)
- [PDF](https://arxiv.org/pdf/2603.17439)

