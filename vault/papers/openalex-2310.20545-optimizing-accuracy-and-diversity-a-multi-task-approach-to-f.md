---
# CSL-compatible fields
title: "Optimizing accuracy and diversity: a multi-task approach to forecast combinations"
author:
  - literal: "Giovanni Felici"
  - literal: "Antonio M. Sudoso"
issued:
  date-parts:
    - [2026, 5, 30]
url: "https://arxiv.org/abs/2310.20545"

# Custom fields
paper_id: "2310.20545"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "m4-competition-dataset"
concept_slugs:
  - "multi-task-forecast-combination"
dataset_slugs:
  - "m4-competition-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-06-01T10:10:16Z"
created_at: "2026-06-01T10:10:16Z"
---

# Optimizing accuracy and diversity: a multi-task approach to forecast combinations

**Authors**: Giovanni Felici, Antonio M. Sudoso
**Date**: 2026-05-30
**Paper ID**: [openalex:2310.20545](https://arxiv.org/abs/2310.20545)

## Summary

This paper proposes a multi-task deep learning architecture for optimizing forecast combinations by simultaneously handling model selection and weighting. The framework consists of two modules: a model selection module, which classifies suitable model subsets based on accuracy and diversity metrics, and a model combination module, which learns optimal weights for these subsets. The modules are jointly trained via a custom loss function, allowing the model to adaptively balance predictive accuracy with ensemble diversity for specific time series. Experimental validation on the M4 competition dataset and traffic data confirms improvements over state-of-the-art forecasting methods.

## Key Contributions

- Introduces a multi-task neural architecture that jointly learns model selection and weight optimization for time series ensemble forecasting.
- Formulates model selection as a classification problem informed by an auxiliary optimization task that targets high accuracy and diverse forecasting methods.
- Demonstrates superior point forecast accuracy on the M4 competition and real-world road traffic datasets compared to existing state-of-the-art baselines.

## Open Questions & Future Work

- [[probabilistic-forecast-extension-for-ensembles]]

## Key Concepts

- [[multi-task-forecast-combination]]: A multi-task neural architecture that jointly optimizes forecasting model selection and weight assignment by considering both accuracy and diversity.

## Archivist Review

I approved the multi-task forecast combination concept as it provides a distinct, reusable framework for ensemble learning. I also approved the probabilistic extension question, as it highlights a critical limitation in many current point-forecasting meta-learning approaches. The M4 dataset was approved as it is a standard, named benchmark.

### Approved Concepts
- Multi-task Forecast Combination: The approach introduces a novel dual-module strategy that simultaneously optimizes model selection (classification) and weighting (regression) to balance forecast accuracy and model diversity.

### Approved Open Questions
- Probabilistic Ensemble Forecasting Extension: Transitioning from point forecasts to probabilistic or density forecasting is critical for better risk assessment in real-world applications.

## Datasets

- [[m4-competition-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2310.20545)
- [PDF](https://arxiv.org/pdf/2310.20545)

