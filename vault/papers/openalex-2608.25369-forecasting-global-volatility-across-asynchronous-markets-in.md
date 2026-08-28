---
# CSL-compatible fields
title: "Forecasting Global Volatility Across Asynchronous Markets: Incremental Accuracy from Constrained Cross-Market Attention"
author:
  - literal: "Xinlin Zhao"
  - literal: "Haotian Qiao"
  - literal: "Ziyao Lin"
  - literal: "Xinlin Zhao"
  - literal: "Haotian Qiao"
  - literal: "Ziyao Lin"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25369"

# Custom fields
paper_id: "2608.25369"
paper_source: "openalex"
domain: "finance"
tags:
  - "transformer"
  - "attention-mechanism"
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
processed_at: "2026-08-28T17:00:03Z"
created_at: "2026-08-28T17:00:03Z"
---

# Forecasting Global Volatility Across Asynchronous Markets: Incremental Accuracy from Constrained Cross-Market Attention

**Authors**: Xinlin Zhao, Haotian Qiao, Ziyao Lin, Xinlin Zhao, Haotian Qiao, Ziyao Lin
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25369](https://arxiv.org/abs/2608.25369)

## Summary

Multivariate volatility forecasting across international equity markets is complicated by asynchronous exchange closures that dictate available information filtrations. To address this, the authors develop PGA-Trans-HAR, a framework combining an origin-admissible ridge-VAR/GFEVD connectedness prior with spatial self-attention, asymmetric attention masking, and a market gate. Evaluated on high-frequency data from eight major indices across daily, weekly, and monthly horizons, the model achieves superior forecast accuracy compared to standard univariate HAR and deep learning baselines by effectively capturing cross-market structural spillovers.

## Key Contributions

- Developed PGA-Trans-HAR, combining a ridge-VAR/GFEVD connectedness prior with spatial self-attention and asymmetric attention masking to handle asynchronous market closures.
- Demonstrated superior forecast accuracy across 1-, 5-, and 22-day horizons using high-frequency data from eight major equity indices (2006-2022).
- Established that origin-aligned cross-market information reduces MSE and MAE compared to univariate HAR and standard linear/deep learning baselines, particularly at medium-to-long horizons.

## Archivist Review

The proposed open question combines multiple distinct extensions into a single broad bucket rather than isolating a specific, standalone technical bottleneck. Applying our strict scarcity and selectivity filters, no concepts or open questions meet the rigorous threshold for vault inclusion.

### Rejected Candidates
- [open_question] Multimodal Macro and Density Forecasting (`multimodal-macro-density-volatility-forecasting`) - weak_evidence: The proposed open question is a broad mix of future work extensions including macro-financial information, density forecasting, and portfolio decisions rather than a single tightly focused unresolved research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.25369)
- [PDF](https://arxiv.org/pdf/2608.25369)

