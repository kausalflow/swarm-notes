---
# CSL-compatible fields
title: "Benchmarking Deep Learning Models for Dense Event Classification of Offshore Wind Infrastructure in Sentinel-1 Time Series"
author:
  - literal: "Thorsten Hoeser"
  - literal: "Felix Bachofer"
  - literal: "Claudia Kuenzer"
issued:
  date-parts:
    - [2026, 8, 5]
url: "https://arxiv.org/abs/2608.04706"

# Custom fields
paper_id: "2608.04706"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "lstm"
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
processed_at: "2026-08-08T05:34:38Z"
created_at: "2026-08-08T05:34:38Z"
---

# Benchmarking Deep Learning Models for Dense Event Classification of Offshore Wind Infrastructure in Sentinel-1 Time Series

**Authors**: Thorsten Hoeser, Felix Bachofer, Claudia Kuenzer
**Date**: 2026-08-05
**Paper ID**: [openalex:2608.04706](https://arxiv.org/abs/2608.04706)

## Summary

This study presents a structured benchmark of ten deep learning model variants (including LSTM, Transformer, and fully connected architectures) for dense event classification of offshore wind infrastructure using Sentinel-1 Synthetic Aperture Radar time series. The supervised BiLSTM achieves the best performance, improving target AUC from 0.7853 to 0.8509 over a rule-based baseline. By combining these predictions in an ensemble, the authors isolate offshore wind turbine deployment phases globally across 2016-2025 and analyze regional duration differences across China, the EU, and the UK.

## Key Contributions

- Evaluated ten deep learning training variants for dense event classification of offshore wind infrastructure using Sentinel-1 SAR time series.
- Demonstrated that a supervised BiLSTM architecture improves the target AUC score from 0.7853 (rule-based baseline) to 0.8509 and raises the perfect match rate from 0.3508 to 0.5063.
- Proposed a label-transition-minimising ensemble combining BiLSTM predictions with baseline labels to isolate turbine deployment phases globally from 2016 to 2025.
- Identified regional median deployment durations of 84 days in China, 242 days in the EU, and 258 days in the UK, revealing links to regulatory and environmental drivers.

## Archivist Review

Applied strict vault filtering standards. The paper provides a valuable empirical benchmark of standard architectures (BiLSTM, Transformer, MLPs) on Sentinel-1 SAR time series for offshore wind turbine monitoring, but does not introduce a standalone, generalizable ML concept, benchmark dataset, or foundational methodology that warrants a permanent vault note.

### Rejected Candidates
- [open_question] Variable-Length Sequence Architectures for SAR Time Series (`variable-length-sequence-architectures-for-sar-time-series`) - paper_local: This open question addresses local domain constraints and specific observation window trade-offs in remote sensing SAR data rather than a foundational time-series methodology bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.04706)
- [PDF](https://arxiv.org/pdf/2608.04706)

