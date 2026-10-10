---
# CSL-compatible fields
title: "CARE: A Lightweight Plug-in Gated Correction and Uncertainty-aware Module for Long-term Time Series Forecasting"
author:
  - literal: "Guo Cheng"
  - literal: "Changlong Lv"
  - literal: "Jingyi Hou"
issued:
  date-parts:
    - [2026, 10, 8]
url: "https://arxiv.org/abs/2610.11165"

# Custom fields
paper_id: "2610.11165"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "care-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:52:14Z"
created_at: "2026-10-10T10:52:14Z"
---

# CARE: A Lightweight Plug-in Gated Correction and Uncertainty-aware Module for Long-term Time Series Forecasting

**Authors**: Guo Cheng, Changlong Lv, Jingyi Hou
**Date**: 2026-10-08
**Paper ID**: [openalex:2610.11165](https://arxiv.org/abs/2610.11165)

## Summary

The paper introduces CARE, a lightweight plug-in module designed to enhance deterministic time series forecasters with residual correction and uncertainty-aware risk gates. Operating in parallel with any base model, CARE resamples historical context, learns residual corrections, and applies scale-aware bounded updates through per-coordinate sigmoid risk gates. Evaluated across eight benchmarks with three representative backbones, CARE consistently improves forecasting accuracy while providing interpretable reliability signals with minimal overhead.

## Key Contributions

- Proposes CARE, a lightweight plug-in module that enhances any deterministic time series forecaster with residual correction and uncertainty awareness without architectural redesign.
- Employs aligned context resampling, scale-aware bounded updates, and per-coordinate sigmoid risk gates modulated by a multi-objective joint loss.
- Improves accuracy across eight standard forecasting benchmarks using three representative backbones with marginal parameter and latency overhead.
- Provides interpretable per-step trust signals, where the highest-gate tertile on the Weather benchmark exhibits nearly four times the error of the lowest-gate tertile.

## Open Questions & Future Work

- [[probabilistic-extension-of-gated-correction-modules]]

## Key Concepts

- [[care-framework]]: A lightweight plug-in module providing corrective residual updates and uncertainty estimation for multivariate time series forecasting.

## Archivist Review

Evaluated the proposed concept and open question under strict filtering guidelines. Approved the canonical framework concept and the unresolved question regarding extending deterministic gated corrections to probabilistic settings, while rejecting duplicate or redundant slugs.

### Approved Concepts
- CARE Framework: Serves as a general lightweight plug-in module that boosts any deterministic time series forecasting backbone by providing residual correction and uncertainty-aware risk gates.

### Approved Open Questions
- Probabilistic Extension of Gated Correction Modules: Transitioning deterministic residual correction modules to handle full probabilistic outputs is crucial for rigorous risk assessment and decision-making under uncertainty in long-term forecasting.

### Rejected Candidates
- [concept] CARE (`care`) - duplicate_existing: Duplicate concept already represented under the canonical slug care-framework.

## Links

- [Abstract](https://arxiv.org/abs/2610.11165)
- [PDF](https://arxiv.org/pdf/2610.11165)

