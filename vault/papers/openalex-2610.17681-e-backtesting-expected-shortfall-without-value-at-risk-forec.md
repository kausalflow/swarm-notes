---
# CSL-compatible fields
title: "E-Backtesting Expected Shortfall without Value-at-Risk Forecasts under Time-series Models"
author:
  - literal: "Ruodu Wang"
  - literal: "Jingcheng Yu"
issued:
  date-parts:
    - [2026, 10, 13]
url: "https://arxiv.org/abs/2610.17681"

# Custom fields
paper_id: "2610.17681"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-10-16T09:23:01Z"
created_at: "2026-10-16T09:23:01Z"
---

# E-Backtesting Expected Shortfall without Value-at-Risk Forecasts under Time-series Models

**Authors**: Ruodu Wang, Jingcheng Yu
**Date**: 2026-10-13
**Paper ID**: [openalex:2610.17681](https://arxiv.org/abs/2610.17681)

## Summary

This paper introduces two e-backtesting methods for Expected Shortfall (ES) that rely solely on observed losses and ES forecasts, eliminating the need for joint Value-at-Risk (VaR) forecasts. The first method handles iid losses, while the second accommodates time-series models under an AR-GARCH conditional VaR structure with anytime-valid control over false rejections. Numerical evaluations using simulations and daily NASDAQ loss data demonstrate the effectiveness of the proposed e-processes in detecting forecast misspecifications and tracking rejection timings.

## Key Contributions

- Developed two e-backtesting methods for Expected Shortfall (ES) using only observed losses and ES forecasts without requiring Value-at-Risk forecasts.
- Established theoretical validity controlling false rejections at any stopping time under an AR-GARCH conditional VaR structure.
- Demonstrated grid approximation convergence for the continuous infimum and false rejection probability over a fixed monitoring period.

## Archivist Review

Following the strict guidelines and skill criteria, all candidates were rejected. The proposed open question is standard boilerplate future work suggesting the extension of a method to other model families, and no standalone reusable forecasting concepts or datasets qualify for the vault.

### Rejected Candidates
- [open_question] Alternative Conditional VaR Families (`alternative-conditional-var-families-es-backtesting`) - not_novel: Boilerplate future work extension to different model families.

## Links

- [Abstract](https://arxiv.org/abs/2610.17681)
- [PDF](https://arxiv.org/pdf/2610.17681)

