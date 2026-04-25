---
# CSL-compatible fields
title: "Adaptive Conformal Anomaly Detection with Time Series Foundation Models for Signal Monitoring"
author:
  - literal: "Natalia Martinez Gil"
  - literal: "Fearghal O’Donncha"
  - literal: "Wesley M. Gifford"
  - literal: "Nianjun Zhou"
  - literal: "Dhaval C. Patel"
  - literal: "Roman Vaculín"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20122"

# Custom fields
paper_id: "2604.20122"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "conformal-prediction"
  - "foundation-model"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-conformal-anomaly-detection"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:15:01Z"
created_at: "2026-04-25T06:15:01Z"
---

# Adaptive Conformal Anomaly Detection with Time Series Foundation Models for Signal Monitoring

**Authors**: Natalia Martinez Gil, Fearghal O’Donncha, Wesley M. Gifford, Nianjun Zhou, Dhaval C. Patel, Roman Vaculín
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20122](https://arxiv.org/abs/2604.20122)

## Summary

This paper introduces a post-hoc, model-agnostic framework for anomaly detection in time series that leverages predictions from frozen foundation models. By employing weighted quantile conformal prediction, the method provides an interpretable anomaly score expressed as a p-value, enabling direct control over false alarm rates. The framework adaptively learns weighting parameters from historical data to ensure robust calibration in the presence of distribution shifts, making it suitable for rapid deployment in resource-constrained industrial settings.

## Key Contributions

- Introduces a model-agnostic, post-hoc anomaly detection framework that integrates with frozen foundation models without fine-tuning.
- Utilizes weighted quantile conformal prediction to provide interpretable anomaly scores represented directly as p-values.
- Implements an adaptive weighting mechanism that dynamically learns from historical predictions to maintain calibration and control false alarm rates under distribution shifts.

## Open Questions & Future Work

- [[context-aware-conformal-weighting]]

## Key Concepts

- [[adaptive-conformal-anomaly-detection]]: A post-hoc, model-agnostic anomaly detection framework that uses weighted conformal prediction and adaptive weighting to control false alarm rates under distribution shift.

## Archivist Review

The paper introduces a clean, reusable methodology for adapting conformal prediction to frozen foundation model outputs for time series monitoring. I approved the core framework concept and the identified open question regarding context-aware weighting as it represents a non-trivial research direction for conformal methods in non-stationary settings. No datasets were identified as central or unique enough for permanent vault storage.

### Approved Concepts
- Adaptive Conformal Anomaly Detection: Provides a novel way to leverage pre-trained foundation models for anomaly detection with rigorous statistical guarantees on false alarm rates.

### Approved Open Questions
- Context-Aware Conformal Weighting: Incorporating contextual features has the potential to significantly improve the local accuracy of conformal thresholds in scenarios where error distributions are influenced by exogenous variables, thereby reducing false alarms further.

## Links

- [Abstract](https://arxiv.org/abs/2604.20122)
- [PDF](https://arxiv.org/pdf/2604.20122)

