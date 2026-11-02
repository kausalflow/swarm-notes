---
# CSL-compatible fields
title: "Application of long short-term memory and convolutional neural networks for real-time bridge pier scour prediction"
author:
  - literal: "Tahrima Hashem"
  - literal: "Negin Yousefpour"
issued:
  date-parts:
    - [2026, 10, 30]
url: "https://arxiv.org/abs/2404.16549"

# Custom fields
paper_id: "2404.16549"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
  - "convolutional-neural-network"
  - "cnn"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-02T12:56:25Z"
created_at: "2026-11-02T12:56:25Z"
---

# Application of long short-term memory and convolutional neural networks for real-time bridge pier scour prediction

**Authors**: Tahrima Hashem, Negin Yousefpour
**Date**: 2026-10-30
**Paper ID**: [openalex:2404.16549](https://arxiv.org/abs/2404.16549)

## Summary

This paper evaluates the effectiveness, efficiency, and generalisability of LSTM and convolutional neural networks for real-time bridge pier scour forecasting using long-term sensor data from bridges in Alaska and Oregon. Formulated as a multivariate time-series prediction problem, the study demonstrates that LSTM models achieve high accuracy (MAE as low as 0.024 m for weekly forecasts), while fully convolutional networks offer competitive accuracy with significantly reduced training and inference times. Feature analyses further reveal that historical scour time series dominate predictive performance compared to secondary flow-related variables.

## Key Contributions

- Formulates bridge pier scour forecasting as a multivariate time-series prediction problem using real-world sensor data spanning 2006-2021 from monitored bridges in Alaska and Oregon.
- Evaluates variants of Long Short-Term Memory (LSTM) and temporal convolutional neural networks (CNNs), showing LSTMs achieve a mean absolute error as low as 0.024 m for one-week-ahead forecasts.
- Demonstrates that fully convolutional networks achieve comparable accuracy to LSTMs while offering substantially lower training and inference times for operational deployment.
- Reveals through feature analyses that historical scour time series dominate predictive performance, whereas flow-related features provide only marginal or site-specific improvements.

## Limitations

Model performance depends heavily on data availability, noise levels, and site-specific scour behavior, particularly for smaller datasets. Future work should explore broader geographic validation and physics-informed extensions.

## Archivist Review

Applied strict scarcity and novelty filters. The paper is an empirical comparison of standard LSTM and CNN architectures applied to bridge scour prediction using localized sensor data. It introduces no novel algorithmic building blocks, architectural paradigms, or canonical datasets that warrant standalone vault notes.

### Rejected Candidates
- [open_question] Generalization to Diverse Scour Processes (`generalization-diverse-scour-processes`) - low_impact: Standard application-level future work calling for broader geographic validation and generalization across sites.

## Links

- [Abstract](https://arxiv.org/abs/2404.16549)
- [PDF](https://arxiv.org/pdf/2404.16549)

