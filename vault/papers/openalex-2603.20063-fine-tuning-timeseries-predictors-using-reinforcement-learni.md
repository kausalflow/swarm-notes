---
# CSL-compatible fields
title: "Fine-tuning Timeseries Predictors Using Reinforcement Learning"
author:
  - literal: "Hugo Cazaux"
  - literal: "Ralph Rudd"
  - literal: "Hlynur Stefánsson"
  - literal: "Sverrir Ólafsson"
  - literal: "Eyjólfur Ingi Ásgeirsson"
issued:
  date-parts:
    - [2026, 3, 20]
url: "https://arxiv.org/abs/2603.20063"

# Custom fields
paper_id: "2603.20063"
paper_source: "openalex"
domain: "time-series"
tags:
  - "reinforcement-learning"
  - "fine-tuning"
  - "time-series"
  - "forecasting"
  - "transfer-learning"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T11:35:27Z"
created_at: "2026-03-27T11:35:27Z"
---

# Fine-tuning Timeseries Predictors Using Reinforcement Learning

**Authors**: Hugo Cazaux, Ralph Rudd, Hlynur Stefánsson, Sverrir Ólafsson, Eyjólfur Ingi Ásgeirsson
**Date**: 2026-03-20
**Paper ID**: [openalex:2603.20063](https://arxiv.org/abs/2603.20063)

## Summary

This work introduces and implements three reinforcement learning (RL) algorithms specifically designed for fine-tuning pre-trained supervised time series predictors, focusing on financial forecasting tasks. The core technical contribution is a detailed plan for successfully backpropagating the RL policy loss through the layers of a model initially trained via standard supervised learning. Empirical evaluations confirm that this RL fine-tuning leads to a notable performance increase and induces desirable transfer learning capabilities in the resulting models. The authors conclude by providing practical insights into the tuning process for adoption by practitioners in the field.

## Key Contributions

- Proposed a clear implementation plan for backpropagating reinforcement learning loss to a model initially trained via supervised learning for time series forecasting.
- Demonstrated an overall performance increase in financial forecasters after applying the proposed reinforcement learning fine-tuning technique.
- Observed and documented transfer learning properties in the fine-tuned models, suggesting improved generalization.
- Provided empirical results and highlighted the tuning process to guide future practitioners in applying RL for financial forecasting.

## Limitations

The study focuses specifically on financial forecasters; generalizability across different time series domains might require further investigation.

## Limitations

The study focuses specifically on financial forecasters; generalizability across different time series domains might require further investigation.

## Links

- [Abstract](https://arxiv.org/abs/2603.20063)
- [PDF](https://arxiv.org/pdf/2603.20063)

