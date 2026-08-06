---
# CSL-compatible fields
title: "An AI-Based Decision-Support Pipeline for Day-Ahead Photovoltaic Forecasting"
author:
  - literal: "Fariba Dehghan"
  - literal: "Sebastian Stein"
  - literal: "Vahid Yazdanpanah"
  - literal: "Stephanie Gauthier"
  - literal: "Masood Nazari"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.02088"

# Custom fields
paper_id: "2608.02088"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-06T07:32:00Z"
created_at: "2026-08-06T07:32:00Z"
---

# An AI-Based Decision-Support Pipeline for Day-Ahead Photovoltaic Forecasting

**Authors**: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier, Masood Nazari
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.02088](https://arxiv.org/abs/2608.02088)

## Summary

This paper proposes a deployment-oriented environmental-AI pipeline for day-ahead hourly photovoltaic forecasting at sites with limited historical data. The pipeline addresses common real-world challenges such as imperfect records, timestamp misalignment, and data leakage by incorporating solar-geometry features, clearness indices, and short-term atmospheric context. By combining complementary predictors via validation-learned stacking, the approach outperforms smart persistence and single machine-learning baselines across both random day-blocked and rolling-origin evaluation protocols.

## Key Contributions

- Develops a deployment-oriented environmental-AI pipeline for day-ahead hourly photovoltaic forecasting using measured inverter output and meteorological inputs.
- Constructs leakage-safe solar-geometry and clearness-index features with timestamp convention correction.
- Combines complementary predictors through validation-learned stacking, reducing daylight normalised RMSE by up to 32% under random evaluation and 9% under rolling-origin evaluation compared to smart persistence.

## Limitations

Evaluated on a single United Kingdom charging-station site; performance gains depend heavily on the evaluation protocol and model class.

## Archivist Review

The paper proposes a deployment-oriented pipeline combining physics-aware features and validation-learned stacking for photovoltaic forecasting. However, the proposed mechanisms represent standard engineering practice and application-level integration rather than reusable, vault-worthy architectural concepts or fundamental theoretical open questions.

### Rejected Candidates
- [open_question] Quantifying Operational Decision Value (`operational-value-quantification-in-pv-forecasting`) - weak_evidence: The question calls for broader site evaluations and downstream decision quantification, which is standard future application work rather than a foundational open technical bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.02088)
- [PDF](https://arxiv.org/pdf/2608.02088)

