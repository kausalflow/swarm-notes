---
# CSL-compatible fields
title: "Deep Learning vs. Statistical Models for Multi-Horizon Price Forecasting of Second-Hand Electronics: A Systematic Benchmark"
author:
  - literal: "Mateusz Buczyński"
  - literal: "Michał Woźniak"
  - literal: "Konrad Kaczyński"
  - literal: "Anna Wróblewska"
  - literal: "Sebastian Kuk"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10727"

# Custom fields
paper_id: "2610.10727"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "benchmark"
  - "dataset"
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
processed_at: "2026-10-10T10:52:57Z"
created_at: "2026-10-10T10:52:57Z"
---

# Deep Learning vs. Statistical Models for Multi-Horizon Price Forecasting of Second-Hand Electronics: A Systematic Benchmark

**Authors**: Mateusz Buczyński, Michał Woźniak, Konrad Kaczyński, Anna Wróblewska, Sebastian Kuk
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10727](https://arxiv.org/abs/2610.10727)

## Summary

This paper presents the first systematic multi-horizon benchmark comparing statistical and deep learning forecasting models for second-hand electronics resale prices. Evaluating eleven models across six horizons (1 to 365 days) on a large-scale dataset of daily marketplace listings, the authors reveal that N-BEATS achieves superior long-horizon accuracy with a 43% reduction in MAPE over statistical baselines. Furthermore, a single N-BEATS model trained at the 365-day horizon successfully generalizes across all shorter horizons while demonstrating robust hyperparameter stability.

## Key Contributions

- Introduces the first systematic time-series benchmark for multi-horizon resale price forecasting of used electronics, covering 100+ smartphone and laptop models over a 3-year period.
- Evaluates eleven classical and deep learning models across six forecasting horizons (1 to 365 days) using three complementary evaluation protocols (trajectory fitness, endpoint accuracy, and cross-horizon transfer).
- Demonstrates that N-BEATS achieves a 43% reduction in MAPE at 365 days compared to the best statistical baseline (8.51% vs 14.94%).
- Shows that a single N-BEATS model trained on the 365-day horizon generalizes effectively to all shorter horizons, eliminating the need for horizon-specific models.

## Open Questions & Future Work

- [[advanced-directions-in-electronics-forecasting]]

## Archivist Review

The paper provides a thorough empirical benchmark comparing statistical and deep learning models across horizons for second-hand electronics pricing, but introduces no fundamentally new reusable forecasting architecture or permanent concept note. The open question regarding advanced directions in electronics forecasting and multimodal extensions is retained as a valuable research tracking point.

### Approved Open Questions
- Advanced Directions in Electronics Forecasting: Crucial for advancing operational pricing risk management and determining whether large pre-trained time-series foundation models can overcome the data sparsity and high volatility inherent in second-hand alternative markets.

### Rejected Candidates
- [open_question] Advanced Directions in Electronics Forecasting (`future-directions-used-electronics-forecasting`) - duplicate_existing: Duplicate slug representation; unified under canonical slug.

## Links

- [Abstract](https://arxiv.org/abs/2610.10727)
- [PDF](https://arxiv.org/pdf/2610.10727)

