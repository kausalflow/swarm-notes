---
# CSL-compatible fields
title: "A time-series classification framework for individual-level absenteeism prediction under severe class imbalance"
author:
  - literal: "Kwong Ho Li"
  - literal: "Matthew Roughan"
  - literal: "Wathsala Karunarathne"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31532"

# Custom fields
paper_id: "2606.31532"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "lstm"
  - "cnn"
  - "text-classification"
  - "imbalance"
architectures:
  - "lstm"
  - "cnn"
datasets:
  []
concept_slugs:
  - "imbalance-ratio-based-loss-calibration"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:10Z"
created_at: "2026-07-03T07:55:10Z"
---

# A time-series classification framework for individual-level absenteeism prediction under severe class imbalance

**Authors**: Kwong Ho Li, Matthew Roughan, Wathsala Karunarathne
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31532](https://arxiv.org/abs/2606.31532)

## Summary

This paper addresses the limitation of existing absenteeism prediction models that rely on contemporaneous features by proposing a Time Series Classification framework that utilizes sequential historical attendance data. The authors analyze how to handle severe class imbalance, specifically comparing Binary Focal Loss and Geometric Mean loss, and provide a theoretically derived weight parameter for BFL based on the imbalance ratio. Evaluation across CNN, LSTM, and LSTM-FCN architectures on a calibrated simulated dataset demonstrates that the LSTM-FCN hybrid is particularly effective for proactive forecasting.

## Key Contributions

- Introduces a proactive Time Series Classification framework for individual-level absenteeism that uses historical sequences rather than contemporaneous features.
- Derives a theoretically grounded hyperparameter balancing strategy for Binary Focal Loss based on the imbalance ratio ρ.
- Evaluates CNN, LSTM, and LSTM-FCN architectures, demonstrating that the LSTM-FCN achieves superior precision and specificity under severe class imbalance.

## Open Questions & Future Work

- [[real-world-validation-absenteeism-tsc]]

## Key Concepts

- [[imbalance-ratio-based-loss-calibration]]: A theoretical method for automatically setting loss function hyperparameters by deriving optimal weights directly from the imbalance ratio of a dataset.

## Archivist Review

I have approved a generalized concept for imbalance-ratio-based loss calibration, as the original proposal was too narrow. I also approved one open question regarding real-world validation of these models, as it captures a fundamental gap between synthetic benchmarking and operational reliability. Other candidates were rejected for being overly specific or redundant to the broader mechanism identified.

### Approved Concepts
- Imbalance-Ratio-Based Loss Calibration: The paper provides a theoretical derivation for optimal Focal Loss hyperparameters specifically for highly imbalanced binary classification using the imbalance ratio, moving away from empirical grid search.

### Approved Open Questions
- Real-world absenteeism model validation: Without large-scale real-world data validation, absenteeism models remain trapped within the limitations of synthetic data benchmarking, preventing production-grade confidence.

### Rejected Candidates
- [concept] Binary Focal Loss (BFL) for Absenteeism Prediction (`binary-focal-loss-for-absenteeism-prediction`) - subcomponent_of_broader_mechanism: This is a specific instance of a more general methodology for loss calibration; the overarching method was approved instead.
- [open_question] Generalizing loss function calibration (`gradient-ratio-formula-generalizability`) - duplicate_existing: This overlaps with the core contribution of the approved concept and is largely a restatement of the future research potential of the calibration mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.31532)
- [PDF](https://arxiv.org/pdf/2606.31532)

