---
# CSL-compatible fields
title: "TempusBench: An Evaluation Framework for Time-Series Forecasting"
author:
  - literal: "Denizalp Goktas"
  - literal: "Gerardo Riaño‐Briceño"
  - literal: "Alif Abdullah"
  - literal: "Aryan Nair"
  - literal: "Aryan Nair"
  - literal: "Chenkai Shen"
  - literal: "Beatriz de Lucio"
  - literal: "Alexandra Magnusson"
  - literal: "Farhan Mashrur"
  - literal: "Ahmed Abdulla"
  - literal: "Shawrna Sen"
  - literal: "Mahitha Thippireddy"
  - literal: "Gregory Schwartz"
  - literal: "Amy Greenwald"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11529"

# Custom fields
paper_id: "2604.11529"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "language-model"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "tempusbench"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:04Z"
created_at: "2026-04-16T06:28:04Z"
---

# TempusBench: An Evaluation Framework for Time-Series Forecasting

**Authors**: Denizalp Goktas, Gerardo Riaño‐Briceño, Alif Abdullah, Aryan Nair, Aryan Nair, Chenkai Shen, Beatriz de Lucio, Alexandra Magnusson, Farhan Mashrur, Ahmed Abdulla, Shawrna Sen, Mahitha Thippireddy, Gregory Schwartz, Amy Greenwald
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11529](https://arxiv.org/abs/2604.11529)

## Summary

TempusBench is a novel open-source evaluation framework developed to address critical methodological shortcomings in the evaluation of time-series foundation models (TSFMs). It introduces a curated set of new datasets to avoid pre-training data contamination, implements a standardized hyperparameter tuning protocol for fair model comparison, and incorporates diagnostic tasks centered on non-stationarity and seasonality. Additionally, the framework includes an integrated visualization interface to improve the interpretability of comparative performance across diverse forecasting models.

## Key Contributions

- Introduces TempusBench, a comprehensive evaluation framework for time-series foundation models designed to mitigate pre-training data leakage and methodological inconsistencies.
- Implements a standardized hyperparameter tuning protocol ensuring fair comparisons between deep learning TSFMs and classical statistical baselines like XGBoost.
- Provides a suite of novel benchmark tasks that explicitly incorporate statistical properties such as non-stationarity and seasonality, rather than relying solely on arbitrary forecast horizons.

## Open Questions & Future Work

- [[dynamic-contamination-free-benchmarks]]
- [[flexible-forecasting-task-taxonomy]]

## Key Concepts

- [[tempusbench]]: An open-source evaluation framework for time-series foundation models that incorporates novel datasets, standardized hyperparameter tuning protocols, and statistical task diagnostics.

## Archivist Review

I approved the TempusBench framework as a core contribution for time-series model evaluation and the two proposed open questions addressing data contamination and the need for a property-aware task taxonomy. I maintained strict adherence to the scarcity policy, approving only the most critical framework concept and the most pressing methodological bottlenecks for the field. No datasets were approved as none were highlighted as standalone research objects rather than benchmark components.

### Approved Concepts
- TempusBench: Addresses critical fragmentation and methodological biases in the evaluation of time-series foundation models.

### Approved Open Questions
- Dynamic Contamination-Free Benchmarks: Without contamination-free and dynamic evaluation sets, it is impossible to distinguish genuine methodological progress from memorization, which is the primary bottleneck for advancing time-series foundation models.
- Flexible Forecasting Task Taxonomy: A standardized, property-aware taxonomy is essential for understanding the specific strengths and weaknesses of different model architectures, moving the field beyond simple leaderboard rankings.

## Links

- [Abstract](https://arxiv.org/abs/2604.11529)
- [PDF](https://arxiv.org/pdf/2604.11529)

