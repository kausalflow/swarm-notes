---
# CSL-compatible fields
title: "Benchmarking Time Series Generation Methods for Privacy-Preserving Forecasting"
author:
  - literal: "Luis Amorim"
  - literal: "Vitor Cerqueira"
  - literal: "Moises Santos"
  - literal: "Paulo J. Azevedo"
  - literal: "Carlos Soares"
issued:
  date-parts:
    - [2026, 8, 11]
url: "https://arxiv.org/abs/2608.10891"

# Custom fields
paper_id: "2608.10891"
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
processed_at: "2026-08-14T06:06:56Z"
created_at: "2026-08-14T06:06:56Z"
---

# Benchmarking Time Series Generation Methods for Privacy-Preserving Forecasting

**Authors**: Luis Amorim, Vitor Cerqueira, Moises Santos, Paulo J. Azevedo, Carlos Soares
**Date**: 2026-08-11
**Paper ID**: [openalex:2608.10891](https://arxiv.org/abs/2608.10891)

## Summary

This paper benchmarks synthetic time series generation methods and noise-based anonymization baselines for privacy-preserving forecasting using a Train on Synthetic, Test on Real (TSTR) protocol across seven datasets. The authors characterize the trade-off between forecasting performance and distance-based empirical privacy risk, showing that simple transformation-based generators outperform deep generative models in this setting. Additionally, they introduce Grasynda-P, a privacy-motivated extension of Grasynda that achieves competitive forecasting performance and strong privacy separation along the Pareto frontier.

## Key Contributions

- Evaluates synthetic generation methods and noise-based anonymization baselines under a Train on Synthetic, Test on Real (TSTR) protocol across seven datasets.
- Characterizes the trade-off between forecasting performance and distance-based empirical privacy risk.
- Introduces Grasynda-P, a privacy-motivated extension of Grasynda incorporating matrix ensembling and kernel density estimation that achieves strong Pareto frontier performance.

## Open Questions & Future Work

- [[connecting-empirical-and-formal-privacy-perspectives]]

## Archivist Review

Strictly adhered to the scarcity and novelty guidelines. The concept 'Grasynda-P' was rejected as a paper-local model variant, while the open question regarding empirical vs. formal privacy was approved as an important unresolved direction. No datasets were proposed or approved.

### Approved Open Questions
- Connecting Empirical and Formal Privacy: Bridging empirical proximity metrics and formal differential privacy is crucial for ensuring that released synthetic time series carry mathematically rigorous privacy guarantees rather than just heuristic protection.

### Rejected Candidates
- [concept] Grasynda-P (`grasynda-p`) - paper_local: Grasynda-P is a paper-local algorithmic extension of a specific graph-based generator rather than a broadly recurring forecasting mechanism or methodological paradigm.
- [concept] Train on Synthetic, Test on Real (TSTR) (`train-on-synthetic-test-on-real-tstr`) - not_novel: TSTR is a well-established standard evaluation protocol widely used across the literature rather than a novel conceptual contribution.

## Links

- [Abstract](https://arxiv.org/abs/2608.10891)
- [PDF](https://arxiv.org/pdf/2608.10891)

