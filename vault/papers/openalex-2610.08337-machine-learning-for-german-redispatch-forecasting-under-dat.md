---
# CSL-compatible fields
title: "Machine Learning for German Redispatch Forecasting under Data Delays and Temporal Distribution Shift"
author:
  - literal: "Faraz Shamim"
  - literal: "Faris Shamim"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.08337"

# Custom fields
paper_id: "2610.08337"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "gru"
  - "benchmark"
  - "evaluation"
architectures:
  - "decoder-only"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:55Z"
created_at: "2026-10-09T11:35:55Z"
---

# Machine Learning for German Redispatch Forecasting under Data Delays and Temporal Distribution Shift

**Authors**: Faraz Shamim, Faris Shamim
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.08337](https://arxiv.org/abs/2610.08337)

## Summary

This paper investigates probabilistic machine learning forecasting for German power grid redispatch interventions under information-age constraints and temporal shifts. Evaluating statistical baselines, LightGBM, GRU, and Transformer models across 2021-2024 transmission data, the authors find that boosted trees with rolling calibration achieve superior nWIS accuracy. However, they reveal that nominal aggregate coverage fails to ensure reliable uncertainty calibration during extreme, high-volume congestion events.

## Key Contributions

- Evaluated probabilistic machine learning forecasts for German redispatch energy under a minimum seven-day target-latency constraint using 48,242 records from 2021 to 2024.
- Demonstrated that raw LightGBM outperformed ARX and seasonal baselines by 25.0% and 9.0% in nWIS, achieving 0.7952.
- Showed that rolling calibration improves LightGBM to an nWIS of 0.7767 with 91.81% coverage for nominal 90% intervals.
- Identified that nominal aggregate validity conceals substantial undercoverage during extreme high-volume congestion events (down to 61.91% coverage).

## Limitations

Aggregate coverage conceals severe undercoverage during high-volume intervention events, pointing to reliability vulnerabilities during extreme grid congestion.

## Archivist Review

No concepts met the strict bar for archival novelty beyond existing techniques and standard models.

## Links

- [Abstract](https://arxiv.org/abs/2610.08337)
- [PDF](https://arxiv.org/pdf/2610.08337)

