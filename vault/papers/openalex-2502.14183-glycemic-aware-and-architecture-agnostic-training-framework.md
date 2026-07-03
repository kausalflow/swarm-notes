---
# CSL-compatible fields
title: "Glycemic-aware and architecture-agnostic training framework for blood glucose forecasting in type 1 diabetes"
author:
  - literal: "Saman Khamesian"
  - literal: "Asiful Arefeen"
  - literal: "Adela Grando"
  - literal: "Bithika Thompson"
  - literal: "Hassan Ghasemzadeh"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2502.14183"

# Custom fields
paper_id: "2502.14183"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "forecasting"
  - "dataset"
  - "evaluation"
  - "model-compression"
architectures:
  []
datasets:
  - "ohiot1dm-dataset"
concept_slugs:
  - "glimmer-framework"
dataset_slugs:
  - "ohiot1dm-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:54:24Z"
created_at: "2026-07-03T07:54:24Z"
---

# Glycemic-aware and architecture-agnostic training framework for blood glucose forecasting in type 1 diabetes

**Authors**: Saman Khamesian, Asiful Arefeen, Adela Grando, Bithika Thompson, Hassan Ghasemzadeh
**Date**: 2026-06-30
**Paper ID**: [openalex:2502.14183](https://arxiv.org/abs/2502.14183)

## Summary

This paper introduces GLIMMER, a modular and architecture-agnostic training framework designed to improve blood glucose forecasting in Type 1 Diabetes by specifically optimizing for dysglycemic event detection. By employing structured preprocessing, a region-aware loss function, and genetic algorithm-based weight optimization, the framework achieves superior prediction performance while maintaining extreme parameter efficiency (10K parameters). The approach is validated on public and clinical datasets, showing significant improvements in standard regression metrics and high-risk event classification compared to state-of-the-art deep learning architectures.

## Key Contributions

- Introduces GLIMMER, an architecture-agnostic training framework for T1D blood glucose forecasting that uses region-aware loss and genetic algorithms.
- Demonstrates significant performance gains, improving RMSE by 24.6% and MAE by 29.6% on the OhioT1DM and AZT1D datasets.
- Achieves high-risk event detection with 98.4% recall and 86.8% F1-score while maintaining parameter efficiency (10K parameters vs. millions in state-of-the-art models).

## Open Questions & Future Work

- [[optimizing-clinical-utility-glucose-models]]

## Key Concepts

- [[glimmer-framework]]: A modular, lightweight, architecture-agnostic training framework that uses region-aware loss and genetic algorithms to prioritize forecasting accuracy in high-risk regions.

## Archivist Review

I approved the GLIMMER framework as a reusable strategy for asymmetric cost-sensitive time-series forecasting. The open question regarding clinical utility optimization captures a significant bottleneck in transitioning from aggregate performance metrics to safety-critical deployment in healthcare settings. OhioT1DM was approved as a standard clinical forecasting dataset.

### Approved Concepts
- GLIMMER Framework: It proposes a modular, architecture-agnostic framework that integrates region-aware loss and meta-heuristic weight optimization specifically for high-risk healthcare time series.

### Approved Open Questions
- Optimizing Clinical Utility in Forecasting: Predictive accuracy in aggregate metrics does not guarantee clinical safety or effective decision support, which are the primary requirements for autonomous clinical systems.

### Rejected Candidates
- [dataset] AZT1D dataset (`azt1d-dataset`) - not_novel: The dataset is a newly introduced, smaller-scale clinical dataset that has not yet established broad community adoption or reuse as a standard benchmark.

## Datasets

- [[ohiot1dm-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2502.14183)
- [PDF](https://arxiv.org/pdf/2502.14183)

