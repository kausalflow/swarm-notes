---
# CSL-compatible fields
title: "Physical knowledge on historical data matters more than enforcing physical constraints on the forecast"
author:
  - literal: "Etienne Lehembre"
  - literal: "Pascal Audigane"
  - literal: "Vincent Nguyen"
  - literal: "Christel Vrain"
  - literal: "Thi-Bich-Hanh Dao"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.19871"

# Custom fields
paper_id: "2609.19871"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "neural-network"
  - "benchmark"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  - "physics-informed-recurrent-neural-network-pirnn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:03:44Z"
created_at: "2026-09-19T09:03:44Z"
---

# Physical knowledge on historical data matters more than enforcing physical constraints on the forecast

**Authors**: Etienne Lehembre, Pascal Audigane, Vincent Nguyen, Christel Vrain, Thi-Bich-Hanh Dao
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.19871](https://arxiv.org/abs/2609.19871)

## Summary

This paper introduces the Physics Informed Recurrent Neural Network (PIRNN), a forecasting model that predicts unobservable intermediate physical variables across both historical data and forecast targets using governing physical equations. Evaluating the framework on twelve real-world groundwater level datasets using the Gardenia physical model, the authors demonstrate that integrating physical knowledge into historical data estimation outperforms traditional physics-constrained forecasting approaches. An ablation study further highlights the crucial role of embedding physical background in time series forecasting tasks.

## Key Contributions

- Proposed Physics Informed Recurrent Neural Network (PIRNN) that predicts unobservable intermediate physical variables on both historical and forecast data.
- Demonstrated PIRNN superiority by outperforming alternative models on five out of twelve real-world groundwater level datasets using Gardenia model equations.
- Provided an ablation study showing that integrating physical background and historical unobservable variable prediction matters more than solely enforcing physical constraints on forecasts.

## Limitations

Evaluated specifically on groundwater level prediction and the Gardenia physical model.

## Key Concepts

- [[physics-informed-recurrent-neural-network-pirnn]]: A recurrent neural network that incorporates physical equations to predict unobservable intermediate physical variables across both historical data and forecast horizons.

## Archivist Review

I approved the core architectural concept PIRNN as a reusable recurrent modeling approach for predicting unobservable physical variables across historical and forecast horizons. Domain-specific physical implementations (like the Gardenia groundwater model integration) were rejected as paper-local. No open questions or datasets met the strict novelty and scarcity standards.

### Approved Concepts
- Physics Informed Recurrent Neural Network (PIRNN): Core methodological contribution that predicts unobservable intermediate physical variables on both historical data and forecast targets rather than solely enforcing physical constraints on forecasts.

### Rejected Candidates
- [concept] Gardenia physical model integration (`gardenia-groundwater-model`) - paper_local: Paper-local domain-specific application model rather than a general reusable ML concept.

## Links

- [Abstract](https://arxiv.org/abs/2609.19871)
- [PDF](https://arxiv.org/pdf/2609.19871)

