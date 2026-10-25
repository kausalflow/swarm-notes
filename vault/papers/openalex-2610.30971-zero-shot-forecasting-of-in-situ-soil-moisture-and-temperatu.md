---
# CSL-compatible fields
title: "Zero-Shot Forecasting of In-Situ Soil Moisture and Temperature with a Time-Series Foundation Model"
author:
  - literal: "Mohammad Talaei"
  - literal: "Mohammad Goudarzi"
  - literal: "Maille Todd"
  - literal: "Vanessa N. L. Wong"
  - literal: "Iadine Chadès"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2610.30971"

# Custom fields
paper_id: "2610.30971"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "zero-shot-learning"
  - "baseline"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-25T09:28:59Z"
created_at: "2026-10-25T09:28:59Z"
---

# Zero-Shot Forecasting of In-Situ Soil Moisture and Temperature with a Time-Series Foundation Model

**Authors**: Mohammad Talaei, Mohammad Goudarzi, Maille Todd, Vanessa N. L. Wong, Iadine Chadès
**Date**: 2026-10-22
**Paper ID**: [openalex:2610.30971](https://arxiv.org/abs/2610.30971)

## Summary

This paper evaluates the zero-shot forecasting capability of TimesFM 1 on in-situ soil moisture and temperature telemetry across 27 sensor stations in a semi-arid land-restoration site. The results reveal that while the foundation model outperforms statistical baselines at sub-daily lead times (by 21-76%), it underperforms beyond one day due to a diurnal-alignment mechanism. Furthermore, the authors show that a walk-forward CatBoost baseline with full history struggles with a cold-start effect on short deployments, highlighting the practical trade-offs of zero-shot time-series forecasting.

## Key Contributions

- Evaluates TimesFM 1 zero-shot on 15-minute telemetry from 27 sensor stations across three land-management regimes at a semi-arid restoration site for soil moisture and temperature forecasting.
- Shows that TimesFM beats best rule-based statistical baselines by 21-76% at sub-daily lead times but underperforms by 6-79% beyond a day.
- Identifies a diurnal-alignment mechanism explaining the performance pattern across lead times from 1 h to 168 h.
- Demonstrates that a walk-forward CatBoost baseline with full history and weather covariates fails to win overall due to a cold-start effect specific to short deployments.

## Archivist Review

Evaluated the paper on zero-shot time-series foundation model forecasting of soil moisture and temperature. No concepts or open questions met the rigorous vault standard for novelty, reusability, and independence from routine empirical benchmarking.

### Rejected Candidates
- [open_question] Fine-Tuning vs. Zero-Shot Transfer (`fine-tuning-vs-zero-shot-transfer-time-series`) - not_novel: Standard empirical comparison between zero-shot inference and fine-tuning, representing routine future work.

## Links

- [Abstract](https://arxiv.org/abs/2610.30971)
- [PDF](https://arxiv.org/pdf/2610.30971)

