---
# CSL-compatible fields
title: "Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection"
author:
  - literal: "Martin Uray"
  - literal: "Saverio Messineo"
  - literal: "Roland Kwitt, Stefan Huber"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12454"

# Custom fields
paper_id: "2607.12454"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "zero-shot-learning"
  - "foundation-model"
  - "forecasting"
  - "benchmark"
architectures:
  []
datasets:
  - "swat"
concept_slugs:
  []
dataset_slugs:
  - "swat"
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:20Z"
created_at: "2026-07-17T07:09:20Z"
---

# Exploring Zero-Shot Foundation Models for Multivariate Time Series Anomaly Detection

**Authors**: Martin Uray, Saverio Messineo, Roland Kwitt, Stefan Huber
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12454](https://arxiv.org/abs/2607.12454)

## Summary

This paper investigates the feasibility of using univariate forecasting foundation models, specifically TimesFM, for multivariate time series anomaly detection in a zero-shot setting. The study evaluates two strategies: utilizing prediction errors from per-feature forecasting and leveraging intermediate model embeddings for outlier detection. Results on the SWaT benchmark show that these naive zero-shot approaches struggle with persistent anomalies due to the model's ability to capture anomalous dynamics. However, the findings reveal that the models reliably produce error peaks at anomaly boundaries, indicating utility for change-point detection instead.

## Key Contributions

- Systematically evaluates the zero-shot performance of TimesFM on the SWaT industrial anomaly detection benchmark.
- Demonstrates that univariate forecasting FMs are often ill-suited for anomaly detection because they accurately predict anomalous temporal dynamics, rendering persistent anomalies indistinguishable from normal data.
- Identifies that univariate forecasting FMs exhibit significant error peaks specifically at anomaly boundaries, suggesting high potential for distribution shift and change-point detection tasks rather than standard anomaly detection.

## Open Questions & Future Work

- [[fm-anomaly-detection-sensitivity-limits]]

## Archivist Review

I approved the SWaT dataset as it is a foundational industrial benchmark for anomaly detection. I also approved a new open question regarding the sensitivity limits of foundation models in anomaly detection, as the paper provides a clear, evidence-based argument that these models struggle with persistent anomalies while succeeding at boundary detection, which is a significant, non-obvious limitation.

### Approved Open Questions
- FM Anomaly Detection Sensitivity Limits: This is a central limitation preventing the direct use of powerful forecasting FMs for critical industrial monitoring tasks.

### Rejected Candidates
- [open_question] Performance Factors in FM Anomaly Detection (`fm-performance-discrepancy-analysis`) - generic: The candidate question is overly broad and lacks the focused technical framing needed for a research tracking item.

## Datasets

- [[swat]]

## Links

- [Abstract](https://arxiv.org/abs/2607.12454)
- [PDF](https://arxiv.org/pdf/2607.12454)

