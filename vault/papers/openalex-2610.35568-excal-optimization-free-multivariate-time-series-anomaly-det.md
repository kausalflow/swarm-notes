---
# CSL-compatible fields
title: "ExCal: Optimization-Free Multivariate Time Series Anomaly Detection via Excess Calibration"
author:
  - literal: "Kadir-Kaan Özer"
  - literal: "René Ebeling"
  - literal: "Markus Enzweiler"
  - literal: "Kadir-Kaan Özer"
  - literal: "René Ebeling"
  - literal: "Markus Enzweiler"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35568"

# Custom fields
paper_id: "2610.35568"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
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
processed_at: "2026-10-29T11:10:34Z"
created_at: "2026-10-29T11:10:34Z"
---

# ExCal: Optimization-Free Multivariate Time Series Anomaly Detection via Excess Calibration

**Authors**: Kadir-Kaan Özer, René Ebeling, Markus Enzweiler, Kadir-Kaan Özer, René Ebeling, Markus Enzweiler
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35568](https://arxiv.org/abs/2610.35568)

## Summary

ExCal is an optimization-free, normal-only multivariate time series anomaly detector that combines raw state retrieval, signal/derivative subspaces, and robust multi-scale statistics without requiring gradient optimization or anomaly labels. Operating in a transductive batch setting, ExCal achieves competitive performance across 180 series from 17 TSB-AD-M benchmark families, matching top-performing non-pretrained methods while significantly outperforming numerous baselines efficiently.

## Key Contributions

- Introduces ExCal, an optimization-free multivariate time series anomaly detector combining raw state retrieval, a signal/derivative subspace, and robust multi-scale statistics.
- Achieves AUC-PR of 0.421 and VUS-PR of 0.452 on 180 series from 17 TSB-AD-M families, ranking second among 24 evaluated methods.
- Demonstrates via Holm-adjusted paired tests no significant difference from AxonAD or StreamVAE while significantly outperforming 21 other baselines.
- Shows efficient inference with a median model-wrapper time of 0.0662 seconds across tested series.

## Limitations

Inference is batch and transductive rather than online; diagnostic utility of score decomposition and online suitability remain untested.

## Open Questions & Future Work

- [[causal-streaming-excess-calibration]]

## Archivist Review

Reviewed the paper on ExCal for multivariate time series anomaly detection. Approved the open question on causal and streaming adaptation of excess calibration, as it addresses a fundamental limitation of transductive batch methods in real-time streaming telemetry. Rejected the method-specific concept as paper-local.

### Approved Open Questions
- Causal and Streaming Excess Calibration: Critical for assessing real-time streaming telemetry deployment readiness where future context is unavailable.

### Rejected Candidates
- [concept] ExCal (`excal`) - paper_local: Paper-local anomaly detection method name that does not yet warrant a standalone permanent vault concept note.

## Links

- [Abstract](https://arxiv.org/abs/2610.35568)
- [PDF](https://arxiv.org/pdf/2610.35568)

