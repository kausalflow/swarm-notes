---
# CSL-compatible fields
title: "SHAPE: Solar Heliospherical Analysis and Prediction of Eruptions A machine learning approach to solar flare forecasting"
author:
  - literal: "S. Kadakol"
  - literal: "P. Deshmukh"
  - literal: "A. B. Bendre"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03234"

# Custom fields
paper_id: "2611.03234"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "recurrent-neural-network"
  - "lstm"
  - "gru"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-11-05T12:52:20Z"
created_at: "2026-11-05T12:52:20Z"
---

# SHAPE: Solar Heliospherical Analysis and Prediction of Eruptions A machine learning approach to solar flare forecasting

**Authors**: S. Kadakol, P. Deshmukh, A. B. Bendre
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03234](https://arxiv.org/abs/2611.03234)

## Summary

The paper introduces SHAPE, a two-phase deep learning pipeline for solar flare forecasting that operates directly on GOES X-ray sensor observations rather than sunspot proxies. Phase 1 combines a cycle-shape curve with a gated recurrent unit network to forecast annual flare counts, while Phase 2 uses a dual-head LSTM on a rolling window to predict the next day's strongest flare class. Although SHAPE demonstrates efficient and competitive performance on backtests, comparisons reveal that persistence baselines remain competitive, highlighting autocorrelation as a dominant factor in short-term flare predictability.

## Key Contributions

- Introduced SHAPE, a two-phase deep learning pipeline for solar flare forecasting using direct soft X-ray observations instead of sunspot proxies.
- Achieved a mean absolute error of 204 flares yr^-1 for monthly flare counts aggregated to annual totals on validation data spanning 2021-2025.
- Attained a true skill statistic of 0.351 and a Heidke skill score of 0.335 for M+ flare events on a 100-day chronological backtest using a shared-trunk, dual-head LSTM.

## Limitations

Phase 1 underestimates the 2024 solar maximum, and a day-to-day persistence baseline remains competitive on short-term skill scores, suggesting short-term predictability is largely driven by autocorrelation.

## Archivist Review

The paper presents a specialized two-phase pipeline for solar flare forecasting using GOES X-ray sensor observations. The proposed open questions focus entirely on domain-specific application details (live stream integration and specific active-region magnetic parameters) rather than fundamental or reusable methodological bottlenecks in time-series forecasting. Therefore, no concepts or open questions qualify for standalone vault notes.

### Rejected Candidates
- [open_question] Real-Time Satellite Stream Integration (`real-time-live-stream-integration`) - low_impact: Standard future work on operational deployment and live telemetry integration.
- [open_question] Active-Region Physics Parameter Integration (`active-region-physics-integration`) - paper_local: Domain-specific feature incorporation for solar flare forecasting without a broader foundational machine learning bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2611.03234)
- [PDF](https://arxiv.org/pdf/2611.03234)

