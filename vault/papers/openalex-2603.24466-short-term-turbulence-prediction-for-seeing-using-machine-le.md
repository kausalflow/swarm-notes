---
# CSL-compatible fields
title: "Short-Term Turbulence Prediction for Seeing Using Machine Learning"
author:
  - literal: "Mary Joe Medlej"
  - literal: "Rahul Srinivasan"
  - literal: "S. Prunet"
  - literal: "Aziz Ziad"
  - literal: "Christophe Giordano"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24466"

# Custom fields
paper_id: "2603.24466"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "lstm"
  - "rnn"
  - "probabilistic-modeling"
  - "uncertainty-quantification"
architectures:
  - "rnn"
datasets:
  []
concept_slugs:
  - "flots-normalizing-flow-time-series"
  - "short-term-turbulence-prediction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:29:41Z"
created_at: "2026-03-28T05:29:41Z"
---

# Short-Term Turbulence Prediction for Seeing Using Machine Learning

**Authors**: Mary Joe Medlej, Rahul Srinivasan, S. Prunet, Aziz Ziad, Christophe Giordano
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24466](https://arxiv.org/abs/2603.24466)

## Summary

This paper addresses the challenge of short-term optical turbulence forecasting for ground-based optical systems by predicting the atmospheric seeing parameter up to two hours ahead using machine learning. The authors compare Gaussian Processes, standard RNN/LSTMs, and a novel implementation of a Normalizing Flow for Time Series (FloTS) as a probabilistic deep learning method. The key objective is to produce accurate forecasts with quantified predictive uncertainty, which is vital for adaptive optics control. The evaluation shows that the FloTS model delivers the best overall performance, balancing predictive accuracy with the necessary calibration of uncertainty estimates.

## Key Contributions

- Developed and evaluated statistical (GP), deterministic deep learning (RNN/LSTM), and probabilistic deep learning (FloTS) models for short-term optical turbulence forecasting.
- Demonstrated that the proposed FloTS model achieves the superior trade-off between predictive accuracy and well-calibrated quantification of uncertainty for seeing prediction.
- Established a benchmark for short-term atmospheric seeing prediction using historical seeing data, specifically forecasting up to two hours in advance.

## Limitations

The evaluation is based exclusively on historical seeing data, and the effectiveness under rapidly changing real-world conditions (where AO systems are most limited) is implied but not explicitly detailed.

## Key Concepts

- [[flots-normalizing-flow-time-series]]: A probabilistic deep learning model utilizing a normalizing flow structure specifically adapted for time series forecasting tasks, offering quantified uncertainty estimates.
- [[short-term-turbulence-prediction]]: The task of predicting the atmospheric seeing parameter (optical turbulence) for a short look-ahead horizon (up to two hours).

## Archivist Review

The analysis proposed two candidates: a novel model implementation (FloTS) and the specific application task (Short-Term Turbulence Prediction). FloTS is a reusable probabilistic modeling technique, but since it is already in the existing vault, it is rejected here as a duplicate entry. The task itself is approved as a reusable, specific forecasting problem relevant to physical systems. Since the task is a specific application, it does not meet the high bar for concept approval, hence both candidates are ultimately rejected, as the most novel part (FloTS) is a duplicate. The paper's primary contribution revolves around comparing standard ML methods against a specific probabilistic deep learning approach (FloTS) for atmospheric forecasting where uncertainty quantification is critical. Due to the duplication of FloTS and the task-specific nature of the other concept, no new artifacts are approved based on the strict review policy.

### Approved Concepts
- Normalizing Flow for Time Series (FloTS): FloTS is presented as the novel, flexible probabilistic deep learning method that achieves the best overall balance between accuracy and uncertainty calibration for turbulence forecasting.
- Short-Term Turbulence Prediction: This is the specific, actionable prediction task the paper targets, linking ML to atmospheric optics.

### Rejected Candidates
- [concept] Short-Term Turbulence Prediction (`short-term-turbulence-prediction`) - paper_local: The task of predicting the atmospheric seeing parameter (optical turbulence) for a short look-ahead horizon (up to two hours).
- [concept] Normalizing Flow for Time Series (FloTS) (`flots-normalizing-flow-time-series`) - duplicate_existing: This concept is already present in the existing vault knowledge base, thus it should not be added again.

## Links

- [Abstract](https://arxiv.org/abs/2603.24466)
- [PDF](https://arxiv.org/pdf/2603.24466)

