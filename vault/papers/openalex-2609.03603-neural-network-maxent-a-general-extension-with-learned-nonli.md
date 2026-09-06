---
# CSL-compatible fields
title: "Neural-Network Maxent: a general extension with learned nonlinearity, applied to time-series for Desert Locust distribution modelling"
author:
  - literal: "Alessandro Grassi"
  - literal: "Edoardo Kimani Bellotto"
  - literal: "Wassim El Azami"
  - literal: "Sabrina Outmani"
  - literal: "Maximilien Houël"
issued:
  date-parts:
    - [2026, 9, 3]
url: "https://arxiv.org/abs/2609.03603"

# Custom fields
paper_id: "2609.03603"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "recurrent-neural-network"
  - "gru"
  - "forecasting"
  - "evaluation"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "rnn-maxent"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-06T09:00:57Z"
created_at: "2026-09-06T09:00:57Z"
---

# Neural-Network Maxent: a general extension with learned nonlinearity, applied to time-series for Desert Locust distribution modelling

**Authors**: Alessandro Grassi, Edoardo Kimani Bellotto, Wassim El Azami, Sabrina Outmani, Maximilien Houël
**Date**: 2026-09-03
**Paper ID**: [openalex:2609.03603](https://arxiv.org/abs/2609.03603)

## Summary

The paper introduces RNN Maxent, an extension of the classical Maxent species distribution modeling framework that replaces hand-chosen, fixed feature dictionaries with a Gated Recurrent Unit (GRU) trained end-to-end via backpropagation. This approach preserves Maxent's presence-only statistical foundations while effectively capturing sequential and nonlinear dependencies in temporal environmental covariates. Applied to Desert Locust distribution forecasting using 50-day time-series from ERA5 Land, MODIS, and Sentinel 3, RNN Maxent significantly outperforms standard Maxent with an ROC AUC of 0.862 versus 0.792.

## Key Contributions

- Introduces RNN Maxent, an extension of the classical Maxent framework that replaces fixed feature dictionaries with a Gated Recurrent Unit (GRU) trained end-to-end via backpropagation.
- Preserves Maxent's presence-only statistical foundations and probability calibration while capturing complex temporal and nonlinear relationships from environmental time-series.
- Demonstrates superior predictive performance for Desert Locust habitat forecasting using 50-day environmental time-series, achieving an ROC AUC of 0.862 compared to 0.792 for standard Maxent.

## Limitations

Evaluated specifically on Desert Locust presence data using ERA5 Land, MODIS, and Sentinel 3 covariates; generalizability to other ecological forecasting tasks requires further validation.

## Open Questions & Future Work

- [[generalizing-calibration-beyond-surveillance-data]]

## Key Concepts

- [[rnn-maxent]]: An extension of the Maxent framework that replaces the fixed feature dictionary with a neural network (GRU) to model temporal and nonlinear relationships in species distribution forecasting.

## Archivist Review

Approved 'rnn-maxent' as a distinct methodological integration of recurrent neural networks into Maxent for temporal ecological forecasting, and 'generalizing-calibration-beyond-surveillance-data' as an open question regarding surveillance biases. No datasets qualified for standalone vault notes.

### Approved Concepts
- RNN Maxent: Extends the classical Maxent species distribution modeling framework by integrating recurrent neural networks (GRU) for end-to-end learned nonlinearities and temporal modeling.

### Approved Open Questions
- Generalizing Calibration Beyond Surveillance Data: Model calibration for pest distribution and migration is currently bounded by surveillance biases and uneven regional data collection, limiting global generalizability.

## Links

- [Abstract](https://arxiv.org/abs/2609.03603)
- [PDF](https://arxiv.org/pdf/2609.03603)

