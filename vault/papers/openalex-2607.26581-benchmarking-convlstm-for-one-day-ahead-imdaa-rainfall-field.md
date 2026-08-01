---
# CSL-compatible fields
title: "Benchmarking ConvLSTM for One-Day-Ahead IMDAA Rainfall-Field Prediction across Four Indian Cities"
author:
  - literal: "Tanmay Ghosh"
  - literal: "Shaurabh Anand"
  - literal: "Rakesh Gomaji Nannewar"
  - literal: "Nithin Nagaraj"
issued:
  date-parts:
    - [2026, 7, 29]
url: "https://arxiv.org/abs/2607.26581"

# Custom fields
paper_id: "2607.26581"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-08-01T07:23:59Z"
created_at: "2026-08-01T07:23:59Z"
---

# Benchmarking ConvLSTM for One-Day-Ahead IMDAA Rainfall-Field Prediction across Four Indian Cities

**Authors**: Tanmay Ghosh, Shaurabh Anand, Rakesh Gomaji Nannewar, Nithin Nagaraj
**Date**: 2026-07-29
**Paper ID**: [openalex:2607.26581](https://arxiv.org/abs/2607.26581)

## Summary

This study benchmarks Convolutional Long Short-Term Memory networks (ConvLSTMs) against ten naive, statistical, tree-based, and neural approaches for one-day-ahead rainfall-field prediction across four Indian cities using IMDAA reanalysis data. Results indicate that ConvLSTM does not consistently outperform simpler alternatives like FC-LSTM or even persistence, particularly underperforming on high-rainfall days where persistence achieves superior detection performance. The findings suggest that gridded inputs alone do not justify the use of ConvLSTM, highlighting the necessity of rigorous baseline comparisons across multiple performance metrics.

## Key Contributions

- Evaluates ConvLSTM for one-day-ahead rainfall-field prediction on small daily reanalysis grids across four Indian cities using IMDAA data (1998-2020).
- Compares ten naive, statistical, tree-based, and neural approaches across complete fields, domain-mean rainfall, spatial anomalies, and high-rainfall days.
- Demonstrates that ConvLSTM does not consistently outperform simpler alternatives such as FC-LSTM or persistence, with persistence achieving the highest detection performance on high-rainfall days.
- Reveals that rainfall-history inputs improve neural models specifically in Mumbai, where spatial continuity is higher, while models generally underestimate rainfall magnitude on extreme days.

## Limitations

Evaluated on small daily reanalysis grids and one-day-ahead prediction horizons rather than high-frequency radar sequences.

## Archivist Review

The paper provides an empirical benchmarking study on ConvLSTM versus baseline architectures for daily rainfall prediction using IMDAA data. It introduces no standalone reusable concepts or datasets, and the open question regarding intensity-sensitive objectives is standard and low-impact for the vault.

### Rejected Candidates
- [open_question] Intensity-Sensitive Objectives for Extremes (`intensity-sensitive-objectives-high-rainfall`) - low_impact: Standard open question about improving extreme weather forecasting losses, lacking a specific methodological breakthrough or novel mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2607.26581)
- [PDF](https://arxiv.org/pdf/2607.26581)

