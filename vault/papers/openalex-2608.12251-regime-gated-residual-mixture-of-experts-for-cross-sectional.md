---
# CSL-compatible fields
title: "Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting"
author:
  - literal: "Junyi Ye"
  - literal: "Gargi Vijay Borde"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.12251"

# Custom fields
paper_id: "2608.12251"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "forecasting"
  - "mixture-of-experts"
  - "moe"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "regime-gated-residual-mixture-of-experts-rg-resmoe"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:15:18Z"
created_at: "2026-08-15T05:15:18Z"
---

# Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting

**Authors**: Junyi Ye, Gargi Vijay Borde
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.12251](https://arxiv.org/abs/2608.12251)

## Summary

This paper investigates how regime information should be incorporated into neural cross-sectional volatility forecasting models to avoid training destabilization. The authors propose RG-ResMoE, a regime-gated residual mixture-of-experts architecture where nonstationary regime variables are restricted exclusively to expert routing rather than direct forecasting inputs. Evaluated on U.S. and Japanese equity panels using a rolling walk-forward framework, RG-ResMoE outperforms capacity-matched MLPs, enhances training stability, and improves Value-at-Risk calibration.

## Key Contributions

- Proposes RG-ResMoE, a regime-gated residual mixture-of-experts model that restricts regime information exclusively to expert routing rather than direct forecasting input.
- Demonstrates consistent performance and training stability improvements over capacity-matched MLPs across U.S. and Japanese equity panels for five-day realized-volatility forecasting.
- Shows that soft routing consistently outperforms hard routing, and that direct input integration of regime variables degrades performance.
- Improves Value-at-Risk calibration in financial volatility forecasting through controlled routing of residual corrections.

## Limitations

Evaluated specifically on compact neural models and realized-volatility forecasting settings.

## Open Questions & Future Work

- [[extending-regime-gated-residual-moe-to-broader-financial-forecasting]]

## Key Concepts

- [[regime-gated-residual-mixture-of-experts-rg-resmoe]]: A regime-gated residual mixture-of-experts architecture that uses nonstationary regime variables exclusively for routing residual corrections rather than direct forecasting.

## Archivist Review

Approved the core RG-ResMoE concept and its open question on generalizing routing-only regime gating, as they represent distinct, reusable methodological contributions to financial time-series forecasting. Standard evaluation frameworks and routine datasets were excluded per vault policy.

### Approved Concepts
- Regime-Gated Residual Mixture-of-Experts (RG-ResMoE): Introduces a novel routing-only residual mixture-of-experts mechanism that uses regime variables solely for gating residual corrections, improving financial volatility forecasting and training stability.

### Approved Open Questions
- Extending Regime-Gated Residual MoE: Determines the generalizability of gate-based residual mixture-of-experts architectures beyond compact equity volatility forecasting models.

### Rejected Candidates
- [concept] Rolling Walk-Forward Evaluation Framework (`rolling-walk-forward-evaluation-framework`) - not_novel: Standard evaluation practice in time series and finance rather than a novel machine learning mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.12251)
- [PDF](https://arxiv.org/pdf/2608.12251)

