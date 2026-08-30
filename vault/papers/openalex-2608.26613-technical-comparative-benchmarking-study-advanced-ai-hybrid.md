---
# CSL-compatible fields
title: "TECHNICAL COMPARATIVE BENCHMARKING STUDY: ADVANCED AI HYBRID METHODS FOR RENEWABLE ENERGY FARM OPTIMIZATION AND FORECASTING"
author:
  - literal: "Majid Masoumi"
  - literal: "Asghar Dashtiy"
  - literal: "Mohammad Dehghan"
  - literal: "Mina Rajabi"
issued:
  date-parts:
    - [2026, 8, 27]
url: "https://arxiv.org/abs/2608.26613"

# Custom fields
paper_id: "2608.26613"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-30T10:10:41Z"
created_at: "2026-08-30T10:10:41Z"
---

# TECHNICAL COMPARATIVE BENCHMARKING STUDY: ADVANCED AI HYBRID METHODS FOR RENEWABLE ENERGY FARM OPTIMIZATION AND FORECASTING

**Authors**: Majid Masoumi, Asghar Dashtiy, Mohammad Dehghan, Mina Rajabi
**Date**: 2026-08-27
**Paper ID**: [openalex:2608.26613](https://arxiv.org/abs/2608.26613)

## Summary

This study delivers a comprehensive comparative benchmarking of various AI architectures—ranging from classical ML and tree ensembles to deep networks, recurrent models, Transformers, graph networks, and hybrid frameworks—applied to renewable energy forecasting across multiple datasets including WEC configurations and Penmanshiel operational SCADA measurements. The findings reveal that tree ensembles excel on structured layout data, STGCNs effectively capture spatial-temporal interactions, and Random Forest BiLSTM hybrids achieve the overall best forecasting accuracy by balancing tabular nonlinearities and temporal dynamics.

## Key Contributions

- Provided a comprehensive benchmarking study comparing conventional ML, ensemble learning, deep neural networks, recurrent architectures, Transformers, graph-based models, and hybrid ensemble deep learning approaches across diverse renewable energy scenarios.
- Demonstrated that tree ensembles (specifically Extra Trees) achieve an approximately 63.7% reduction in MAE relative to MLP baselines for structured WEC layout data.
- Showed that the STGCN model reduces MAE to approximately 167.0 kW (R = 0.93) by explicitly capturing spatial and temporal turbine interactions.
- Achieved the best overall forecasting accuracy using an RF BiLSTM hybrid model, yielding an MAE of 150.5 kW—representing a 75% reduction over standalone LSTM and a 10% improvement over STGCN.

## Archivist Review

The paper is purely a comparative benchmarking study evaluating existing machine learning, deep learning, graph networks, and hybrid architectures on renewable energy and wind farm forecasting. It does not introduce any novel standalone architectural concepts, reusable algorithmic components, or major unresolved open questions that qualify for permanent vault entries.

## Links

- [Abstract](https://arxiv.org/abs/2608.26613)
- [PDF](https://arxiv.org/pdf/2608.26613)

