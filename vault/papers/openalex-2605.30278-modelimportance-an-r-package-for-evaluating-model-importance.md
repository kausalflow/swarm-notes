---
# CSL-compatible fields
title: "modelimportance: An R package for evaluating model importance within a multi-model ensemble"
author:
  - literal: "Minsu Kim"
  - literal: "Li Shandross"
  - literal: "Evan L. Ray"
  - literal: "Nicholas G Reich"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.30278"

# Custom fields
paper_id: "2605.30278"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "model-importance-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:20Z"
created_at: "2026-05-31T08:10:20Z"
---

# modelimportance: An R package for evaluating model importance within a multi-model ensemble

**Authors**: Minsu Kim, Li Shandross, Evan L. Ray, Nicholas G Reich
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.30278](https://arxiv.org/abs/2605.30278)

## Summary

The modelimportance R package provides a systematic framework for evaluating the individual contributions of constituent models within forecasting ensembles. By supporting both point and probabilistic metrics and offering robust handling of missing values, it facilitates better understanding of ensemble dynamics. The package integrates directly with the 'hubverse' ecosystem, promoting standardized practices for collaborative modeling and performance analysis across various forecasting tasks.

## Key Contributions

- Introduces the 'modelimportance' R package, providing a suite of metrics to quantify the accuracy contribution of individual models to ensemble forecasts.
- Enables both point and probabilistic forecast evaluation with built-in robust handling of missing data.
- Ensures interoperability by adhering to the 'hubverse' framework, allowing for seamless application across standardized collaborative modeling hubs.

## Open Questions & Future Work

- [[forecast-output-type-interoperability]]

## Key Concepts

- [[model-importance-framework]]: A methodology and tool for quantifying the marginal contribution of individual models within a multi-model forecasting ensemble.

## Archivist Review

The analysis identifies a valuable method for ensemble auditability. I have approved the concept under a more descriptive name and reframed the open question to focus on the underlying technical challenge of supporting diverse, non-parametric forecast structures in evaluation pipelines.

### Approved Concepts
- Model Importance Framework: It addresses the gap in ensemble interpretability by providing a standardized, modular method to audit the individual contribution of constituent models.

### Approved Open Questions
- Forecast output type interoperability: Many modern forecasting pipelines rely on sample-based distributions, and restricting evaluation metrics to parametric forms limits the applicability of interpretability tools in diverse research settings.

### Rejected Candidates
- [concept] modelimportance (`modelimportance`) - other: Renamed to a more descriptive concept slug ('model-importance-framework') to reflect its nature as a methodology rather than a specific R package.
- [open_question] Support additional forecast output types (`support-additional-forecast-output-types`) - other: Renamed to reflect the broader technical challenge of interoperability across forecast output structures rather than a simple feature request.

## Links

- [Abstract](https://arxiv.org/abs/2605.30278)
- [PDF](https://arxiv.org/pdf/2605.30278)

