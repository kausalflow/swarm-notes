---
# CSL-compatible fields
title: "DSTNet: Dynamic Spectral Trajectory Network for Causal Multi-Horizon Financial Forecasting"
author:
  - literal: "Aashish Bohra"
  - literal: "Lokendra Vishwakarm"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09654"

# Custom fields
paper_id: "2610.09654"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "attention-mechanism"
  - "finance"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "dynamic-spectral-trajectory-network"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:35:38Z"
created_at: "2026-10-09T11:35:38Z"
---

# DSTNet: Dynamic Spectral Trajectory Network for Causal Multi-Horizon Financial Forecasting

**Authors**: Aashish Bohra, Lokendra Vishwakarm
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09654](https://arxiv.org/abs/2610.09654)

## Summary

DSTNet is a causal dynamic spectral trajectory network designed for multi-horizon financial forecasting. It avoids future leakage by utilizing a one-sided Morlet-derived filter bank with an explicit burn-in to process trailing technical indicators, feeding them into a factorized Scale-Temporal Spectral Transformer and a CNN-BiLSTM. Evaluated on seven equity indices and gold across four horizons, DSTNet consistently outperforms existing learned baselines and random-walk persistence under MAE and MAPE.

## Key Contributions

- Proposes DSTNet, a dynamic spectral trajectory network that retains the evolution of filter-bank magnitudes as a causal dynamic spectral trajectory using a one-sided Morlet filter bank.
- Employs a factorized Scale-Temporal Spectral Transformer that attends along time and filter-bank axes separately, combined with a CNN-BiLSTM via a learned gate.
- Evaluates across seven equity indices and gold for multi-horizon forecasting (1, 3, 5, and 10 days), outperforming nine learned baselines and random walk persistence under an expanding-window protocol.

## Open Questions & Future Work

- [[extended-persistence-and-seed-robustness-in-financial-forecasting]]

## Key Concepts

- [[dynamic-spectral-trajectory-network]]: A financial forecasting network that constructs a causal Dynamic Spectral Trajectory from filter-bank magnitudes and processes them with a scale-temporal spectral transformer.

## Archivist Review

Approved the core architectural concept of a causal dynamic spectral trajectory network and its open question on persistence and seed robustness, ensuring high selectivity and strict adherence to vault standards.

### Approved Concepts
- Dynamic Spectral Trajectory Network: Introduces a causal spectral trajectory representation for financial time series using a one-sided Morlet filter bank and factorized transformer architecture.

### Approved Open Questions
- Extended Persistence and Seed Robustness: Crucial for establishing whether proposed multi-horizon deep learning architectures maintain statistical superiority over persistence benchmarks across diverse economic regimes and varied model initializations.

## Links

- [Abstract](https://arxiv.org/abs/2610.09654)
- [PDF](https://arxiv.org/pdf/2610.09654)

