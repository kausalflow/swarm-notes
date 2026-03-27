---
# CSL-compatible fields
title: "TimeAPN: Adaptive Amplitude-Phase Non-Stationarity Normalization for Time Series Forecasting"
author:
  - literal: "Yue Hu"
  - literal: "Jialiang Tang"
  - literal: "Siwei Yu"
  - literal: "Baosheng Yu"
  - literal: "Jing J. Zhang"
  - literal: "Dacheng Tao"
issued:
  date-parts:
    - [2026, 3, 18]
url: "https://arxiv.org/abs/2603.17436"

# Custom fields
paper_id: "2603.17436"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "normalization"
architectures:
  []
datasets:
  - "ETTh1"
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:08:54Z"
created_at: "2026-03-27T14:08:54Z"
---

# TimeAPN: Adaptive Amplitude-Phase Non-Stationarity Normalization for Time Series Forecasting

**Authors**: Yue Hu, Jialiang Tang, Siwei Yu, Baosheng Yu, Jing J. Zhang, Dacheng Tao
**Date**: 2026-03-18
**Paper ID**: [openalex:2603.17436](https://arxiv.org/abs/2603.17436)

## Summary

TimeAPN is a novel Adaptive Amplitude-Phase Non-Stationarity Normalization framework designed to address distribution shifts in multivariate long-term time series forecasting caused by rapid changes in amplitude and phase. The method jointly models mean evolution in the time and frequency domains and explicitly models phase discrepancy to capture temporal misalignment. Furthermore, it integrates amplitude information via an adaptive normalization mechanism to manage abrupt fluctuations in signal energy. The framework is model-agnostic, and empirical results on seven datasets show superior long-term forecasting performance compared to state-of-the-art reversible normalization techniques.

## Key Contributions

- Proposed TimeAPN, an Adaptive Amplitude-Phase Non-Stationarity Normalization framework that explicitly models non-stationary factors in both time and frequency domains.
- Developed a method to explicitly model and predict phase discrepancy between predicted and ground-truth sequences to capture temporal misalignment caused by non-stationarity.
- Introduced an adaptive normalization mechanism leveraging amplitude information to effectively handle abrupt fluctuations in signal energy.
- Demonstrated consistent improvement in long-term forecasting accuracy across seven real-world multivariate datasets, outperforming existing reversible normalization methods.

## Limitations

The paper focuses on explicit modeling of amplitude and phase dynamics, which might introduce computational overhead compared to simpler statistical normalization methods.

## Open Questions & Future Work

- [[timeapn-amplitude-loss-simplification]]

## Datasets

- [ETTh1](../datasets/etth1.md)

## Limitations

The paper focuses on explicit modeling of amplitude and phase dynamics, which might introduce computational overhead compared to simpler statistical normalization methods.

## Links

- [Abstract](https://arxiv.org/abs/2603.17436)
- [PDF](https://arxiv.org/pdf/2603.17436)

