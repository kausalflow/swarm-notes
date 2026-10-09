---
# CSL-compatible fields
title: "Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction"
author:
  - literal: "Jonathan Chang"
  - literal: "Zimeng Lyu"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.07825"

# Custom fields
paper_id: "2610.07825"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "transformer"
  - "neural-architecture-search"
  - "fintech"
  - "evaluation"
architectures:
  - "recurrent-neural-network"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:34:52Z"
created_at: "2026-10-09T11:34:52Z"
---

# Forecast Accuracy Is Not Trading Profit: Evolving Small Recurrent Networks for Stock Return Prediction

**Authors**: Jonathan Chang, Zimeng Lyu
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.07825](https://arxiv.org/abs/2610.07825)

## Summary

This paper investigates the disconnect between statistical forecasting accuracy and downstream trading profitability in financial time series. By evaluating linear, recurrent, transformer, and mixing-based architectures on stock return prediction, the authors find that conventional models with high pointwise accuracy often fail to generate net profits after transaction costs. Conversely, small recurrent networks evolved via neuroevolutionary architecture search achieve superior forecast accuracy and net trading returns while requiring only CPU-only training and ultra-low-latency execution on edge hardware.

## Key Contributions

- Demonstrates that higher forecast accuracy does not necessarily translate to higher trading profit in stock return prediction tasks
- Proposes evolving small recurrent neural networks via neuroevolutionary architecture search that rank first on both forecast accuracy and net trading performance across four mid-cap portfolios and three trading years
- Shows that evolved lightweight networks achieve extreme computational efficiency, training in 16 minutes on a CPU and predicting in 10.8 microseconds on a Raspberry Pi Zero with only 66 weights

## Limitations

Evaluated specifically on mid-cap portfolios over three trading years; scaling properties beyond small recurrent architectures remain to be explored.

## Archivist Review

Applied rigorous selectivity standards to protect the knowledge vault. No new concepts or datasets met the strict reusability criteria, and the open question closely duplicates existing themes on decision-focused forecasting and financial trading objectives.

### Rejected Candidates
- [open_question] Decision-Focused Forecasting Objectives (`decision-focused-forecasting-objectives-in-finance`) - duplicate_existing: Closely related to existing decision-focused learning and financial forecasting objectives already covered or implied in the vault.

## Links

- [Abstract](https://arxiv.org/abs/2610.07825)
- [PDF](https://arxiv.org/pdf/2610.07825)

