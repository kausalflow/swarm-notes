---
created_at: '2026-06-14T08:36:50Z'
source_papers:
- '[[openalex-2502.12370-positional-encoding-in-transformer-based-time-series-models]]'
title: PE Robustness in Irregular Series
---

**Background:** Transformer-based time series models are frequently applied to data with irregular sampling, non-stationarity, and missing observations, which diverge from the discrete-token assumptions of standard positional encoding.

**Question / Future Work:** Investigate how existing positional encoding strategies perform under conditions of irregularly sampled time intervals and missing data points, which are common in real-world sensor or event-driven datasets but often overlooked in current sequence-based benchmarks.

**Why It Matters:** Understanding PE robustness to data irregularity is critical for the practical deployment of transformer models in healthcare and industrial monitoring where data quality is inconsistent.

**Evidence:** Second, our evaluation focuses on regularly sampled, complete time series. Many real-world applications involve irregular sampling... missing values... Different PE methods may respond quite differently to these challenges.