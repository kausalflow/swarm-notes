---
# CSL-compatible fields
title: "Multivariate Time Series Forecasting with Adaptive Non-Local Observables"
author:
  - literal: "Yu-Ting Lee"
  - literal: "Hua-an Tseng"
  - literal: "Samuel Yen-Chi Chen"
issued:
  date-parts:
    - [2026, 7, 27]
url: "https://arxiv.org/abs/2607.24399"

# Custom fields
paper_id: "2607.24399"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "quantum-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-non-local-observables"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-30T07:25:59Z"
created_at: "2026-07-30T07:25:59Z"
---

# Multivariate Time Series Forecasting with Adaptive Non-Local Observables

**Authors**: Yu-Ting Lee, Hua-an Tseng, Samuel Yen-Chi Chen
**Date**: 2026-07-27
**Paper ID**: [openalex:2607.24399](https://arxiv.org/abs/2607.24399)

## Summary

This paper introduces MTSF-ANO, a hybrid multivariate time series forecasting model that replaces traditional fixed local measurements in quantum neural networks with adaptive non-local observables (ANO). Evaluated across four ETT datasets, MTSF-ANO achieves top-tier MSE performance in 17 out of 20 settings, outperforming competitive baselines by up to 20% on ETTh1. Ablation studies further highlight the importance of circuit design and non-locality for expressive quantum time series modeling.

## Key Contributions

- Proposes MTSF-ANO, a hybrid multivariate time series forecasting model combining variational quantum circuits with adaptive non-local observables.
- Ranks first or second in MSE in 17 of 20 settings across the four ETT datasets, improving over the strongest baseline by up to 20% on ETTh1.
- Demonstrates through ablation studies that quantum circuit design and non-locality of ANO significantly impact forecasting expressivity and performance.

## Key Concepts

- [[adaptive-non-local-observables]]: A hybrid quantum-classical modeling component that integrates variational quantum circuits with adaptive non-local observables to enhance time series expressivity.

## Archivist Review

Approved the core quantum modeling concept 'Adaptive Non-Local Observables' as a reusable mechanism for quantum time series forecasting. Rejected the model name variant 'MTSF-ANO' to avoid redundant system-level duplication. No open questions or datasets met the strict novelty and scarcity standards.

### Approved Concepts
- Adaptive Non-Local Observables: Core novelty of the paper, replacing fixed local measurements with adaptive non-local observables in quantum neural networks for time series forecasting.

### Rejected Candidates
- [concept] MTSF-ANO (`mtsf-ano`) - subcomponent_of_broader_mechanism: This is the paper-specific acronym and model name wrapping the core concept (Adaptive Non-Local Observables); vault archiving prefers the core mechanism note.

## Links

- [Abstract](https://arxiv.org/abs/2607.24399)
- [PDF](https://arxiv.org/pdf/2607.24399)

