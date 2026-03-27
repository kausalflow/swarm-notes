---
# CSL-compatible fields
title: "Short-Term Turbulence Prediction for Seeing Using Machine Learning"
author:
  - literal: "Mary Joe Medlej"
  - literal: "Rahul Srinivasan"
  - literal: "Simon Prunet"
  - literal: "Aziz Ziad"
  - literal: "Christophe Giordano"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24466"

# Custom fields
paper_id: "2603.24466"
paper_source: "arxiv"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "rnn"
  - "lstm"
  - "probabilistic-modeling"
  - "evaluation"
architectures:
  - "recurrent-neural-network"
datasets:
  - "historical seeing data"
skill: "TimeSeriesSkill"
processed_at: "2026-03-26T07:10:56Z"
created_at: "2026-03-26T07:10:56Z"
---

# Short-Term Turbulence Prediction for Seeing Using Machine Learning

**Authors**: Mary Joe Medlej, Rahul Srinivasan, Simon Prunet, Aziz Ziad, Christophe Giordano
**Date**: 2026-03-25
**Paper ID**: [arxiv:2603.24466](https://arxiv.org/abs/2603.24466)

## Summary

This study addresses the challenge of optical turbulence in ground-based systems by developing short-term forecasting models for the atmospheric seeing parameter up to two hours ahead. The authors compare traditional statistical methods like Gaussian Processes against deep learning baselines, specifically RNNs and LSTMs, emphasizing the need for probabilistic forecasts that include uncertainty quantification. They introduce and evaluate a Normalizing Flow for Time Series (FloTS) model as a flexible deep learning approach for this task. The results indicate that FloTS provides the optimal balance between predictive accuracy and robust, well-calibrated estimation of forecast uncertainty.

## Key Contributions

- Demonstrated the feasibility of short-term optical turbulence forecasting (seeing prediction) up to two hours in advance using ML models.
- Evaluated a comprehensive set of models including Gaussian Processes, RNNs/LSTMs, and the probabilistic FloTS method for this task.
- Showed that the FloTS probabilistic model achieves the best trade-off between predictive accuracy and well-calibrated uncertainty quantification for seeing prediction.

## Limitations

The study is focused on short-term forecasting (up to two hours), and the performance under extremely rapid or chaotic atmospheric changes remains an open question.

## Open Questions & Future Work

- [[expressive-gp-kernels-seeing-prediction]]
- [[incorporating-meteorological-features-seeing-prediction]]
- [[transformer-architectures-seeing-forecasting]]
- [[ensemble-strategies-probabilistic-forecasting]]
- [[conditional-vaes-probabilistic-forecasting]]
- [[non-parametric-calibration-gp-floats]]

## Key Concepts

- [Normalizing Flow for Time Series](../concepts/flots-normalizing-flow-time-series.md): A probabilistic deep learning method based on normalizing flows adapted for time series forecasting, used here to predict atmospheric seeing.

## Datasets

- [historical seeing data](../datasets/historical-seeing-data.md)

## Limitations

The study is focused on short-term forecasting (up to two hours), and the performance under extremely rapid or chaotic atmospheric changes remains an open question.

## Links

- [ArXiv Abstract](https://arxiv.org/abs/2603.24466)
- [PDF](https://arxiv.org/pdf/2603.24466)

