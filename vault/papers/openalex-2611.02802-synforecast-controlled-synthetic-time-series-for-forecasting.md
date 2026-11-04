---
# CSL-compatible fields
title: "SynForecast: Controlled Synthetic Time Series for Forecasting Research"
author:
  - literal: "Olivier Sprangers"
  - literal: "Cristian Challú"
  - literal: "Jan Rathfelder"
  - literal: "Han Wang"
  - literal: "Max Mergenthaler Canseco"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.02802"

# Custom fields
paper_id: "2611.02802"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "pre-training"
  - "fine-tuning"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "m4"
concept_slugs:
  - "synforecast"
dataset_slugs:
  - "m4"
skill: "TimeSeriesSkill"
processed_at: "2026-11-04T12:39:53Z"
created_at: "2026-11-04T12:39:53Z"
---

# SynForecast: Controlled Synthetic Time Series for Forecasting Research

**Authors**: Olivier Sprangers, Cristian Challú, Jan Rathfelder, Han Wang, Max Mergenthaler Canseco
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.02802](https://arxiv.org/abs/2611.02802)

## Summary

The authors present SynForecast, an open-source Python library containing 32 controlled synthetic time series generators rooted in econometrics, finance, statistical physics, and point-process theory. Through systematic evaluation on the M4 benchmark using neural networks and gradient-boosted ensembles, the study reveals that synthetic priors outperform training from scratch under limited data budgets but lose at full history, and highlights the critical impact of mechanism-level ablations and structural corrections (such as adding daily cycles) on zero-shot and fine-tuning performance.

## Key Contributions

- Introduced SynForecast, an open-source Python library featuring 32 controlled synthetic time series generators, including 19 implementing named mechanisms from econometrics, quantitative finance, statistical physics, and point-process theory.
- Demonstrated that a synthetic prior outperforms training from scratch by up to 34% under limited data budgets (few dozen observations), but underperforms full-history training across all evaluated frequencies.
- Showed that adding missing structural patterns like daily cycles to the training corpus reduces zero-shot error by 43% to 63% for both neural network and gradient-boosted ensemble models.
- Found that fine-tuning outperforms training from scratch by up to 15%, though short-history fixed-step fine-tuning can underperform the zero-shot pretrained model.

## Limitations

The synthetic prior loses to training from scratch at full history across all frequencies, and fixed-step fine-tuning at short histories underperforms zero-shot inference.

## Open Questions & Future Work

- [[corpus-size-vs-mechanism-diversity]]

## Key Concepts

- [[synforecast]]: An open-source Python library providing controlled synthetic time series generators with mechanism-level ablations for forecasting research.

## Archivist Review

Approved the SynForecast library concept along with the standard M4 dataset and an open question on synthetic corpus size versus mechanism diversity. Followed strict scarcity rules and filtered out paper-local observations.

### Approved Concepts
- SynForecast: Introduces a comprehensive, open-source library of 32 generators supporting controlled synthetic time series generation and mechanism-level ablations for forecasting research.

### Approved Open Questions
- Corpus Size vs Mechanism Diversity: Crucial for understanding the scaling laws and structural requirements of synthetic pretraining corpora in time series forecasting.

### Rejected Candidates
- [concept] Synthetic Prior Forecasting (`synthetic-prior-forecasting`) - subcomponent_of_broader_mechanism: Subcomponent of broader synthetic pre-training methodology rather than a standalone concept.

## Datasets

- [[m4]]

## Links

- [Abstract](https://arxiv.org/abs/2611.02802)
- [PDF](https://arxiv.org/pdf/2611.02802)

