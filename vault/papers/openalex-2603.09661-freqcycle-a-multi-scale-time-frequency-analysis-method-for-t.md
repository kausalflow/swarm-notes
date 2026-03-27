---
# CSL-compatible fields
title: "FreqCycle: A Multi-Scale Time-Frequency Analysis Method for Time Series Forecasting"
author:
  - literal: "Boya Zhang"
  - literal: "Shuaijie Yin"
  - literal: "Huiwen Zhu"
  - literal: "Xing He"
issued:
  date-parts:
    - [2026, 3, 10]
url: "https://arxiv.org/abs/2603.09661"

# Custom fields
paper_id: "2603.09661"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multi-scale-analysis"
  - "frequency-domain"
  - "seasonality"
architectures:
  []
datasets:
  - "ETTh1"
  - "Traffic"
  - "Weather"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:01Z"
created_at: "2026-03-27T14:09:01Z"
---

# FreqCycle: A Multi-Scale Time-Frequency Analysis Method for Time Series Forecasting

**Authors**: Boya Zhang, Shuaijie Yin, Huiwen Zhu, Xing He
**Date**: 2026-03-10
**Paper ID**: [openalex:2603.09661](https://arxiv.org/abs/2603.09661)

## Summary

This paper introduces FreqCycle, a novel framework for time series forecasting that addresses the under-modeling of mid to high-frequency components dominant in existing deep learning approaches. The framework integrates two key modules: FECF for learning shared low-frequency periodic patterns and SFPL for boosting the energy proportion of mid-to-high frequencies via adaptive filtering. To handle complex, coupled multi-periodicity and long lookback windows, the authors extend the method to MFreqCycle, which leverages cross-scale interactions to decouple nested periodic features. Experimental results across seven benchmarks show that FreqCycle and MFreqCycle achieve superior accuracy while maintaining competitive inference speed.

## Key Contributions

- Proposal of FreqCycle, a novel framework that combines a Filter-Enhanced Cycle Forecasting (FECF) module for low-frequency pattern extraction and a Segmented Frequency-domain Pattern Learning (SFPL) module for mid-to-high frequency enhancement.
- Introduction of MFreqCycle, a hierarchical extension of FreqCycle designed to decouple nested periodic features and handle long lookback windows by modeling coupled multi-periodicity.
- Demonstration of state-of-the-art accuracy across seven diverse time series benchmarks while achieving faster inference speeds compared to existing models.
- Addressing the common limitation in deep learning models of overlooking mid to high-frequency components, which are crucial for comprehensive time series analysis.

## Limitations

The abstract does not explicitly detail limitations, but the hierarchical extension (MFreqCycle) suggests complexity in managing increasingly deep nested periodicities.

## Open Questions & Future Work

- [[annual-cycle-modeling-in-mfreqcycle]]

## Key Concepts

- [Filter-Enhanced Cycle Forecasting](../concepts/filter-enhanced-cycle-forecasting-fecf.md): A module designed to extract low-frequency features by explicitly learning shared periodic patterns in the time domain for time series forecasting.
- [Segmented Frequency-domain Pattern Learning](../concepts/segmented-frequency-domain-pattern-learning-sfpl.md): A module that enhances the proportion of mid to high-frequency energy in time series data using learnable filters and adaptive weighting.

## Datasets

- [ETTh1](../datasets/etth1.md)
- [Traffic](../datasets/traffic.md)
- [Weather](../datasets/weather.md)

## Limitations

The abstract does not explicitly detail limitations, but the hierarchical extension (MFreqCycle) suggests complexity in managing increasingly deep nested periodicities.

## Links

- [Abstract](https://arxiv.org/abs/2603.09661)
- [PDF](https://arxiv.org/pdf/2603.09661)

