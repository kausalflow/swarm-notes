---
# CSL-compatible fields
title: "IMPACT: Inverter-Informed Multimodal Learning for Photovoltaic Generation Forecasting"
author:
  - literal: "Anushka Katiyar"
  - literal: "Cong Feng"
  - literal: "Jing Wang"
  - literal: "Tristan Liu"
  - literal: "Simon Julien"
  - literal: "Zachary Jacobs"
issued:
  date-parts:
    - [2026, 10, 29]
url: "https://arxiv.org/abs/2610.40418"

# Custom fields
paper_id: "2610.40418"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "graph-neural-network"
  - "attention-mechanism"
  - "conformal-prediction"
  - "probabilistic-forecasting"
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
processed_at: "2026-11-01T11:33:28Z"
created_at: "2026-11-01T11:33:28Z"
---

# IMPACT: Inverter-Informed Multimodal Learning for Photovoltaic Generation Forecasting

**Authors**: Anushka Katiyar, Cong Feng, Jing Wang, Tristan Liu, Simon Julien, Zachary Jacobs
**Date**: 2026-10-29
**Paper ID**: [openalex:2610.40418](https://arxiv.org/abs/2610.40418)

## Summary

This paper introduces IMPACT, a physics-informed multimodal deep learning framework designed for short-term (10- to 110-minute-ahead) probabilistic photovoltaic power forecasting. The model integrates plant-level temporal history, inverter-level spatial dynamics via graph attention, solar geometry, and meteorological states using a four-branch architecture with gated cross-attention. It enhances prediction accuracy by incorporating forward-looking physical signals like spatial cloud heterogeneity and inverter ramp-down activity, paired with a smart persistence baseline correction and online kernel-weighted adaptive conformal calibration. Evaluating against 14 baselines, IMPACT achieves a superior forecast skill score of 0.2950 and maintains high robustness under challenging sky conditions.

## Key Contributions

- Develops IMPACT, a physics-informed multimodal deep learning framework for 10- to 110-minute-ahead probabilistic photovoltaic power forecasting.
- Utilizes a four-branch architecture incorporating plant temporal history, inverter-level spatial cloud dynamics via graph attention, known-future solar geometry, and current meteorological state, fused via gated cross-attention.
- Integrates forward-looking physical signals (spatial cloud heterogeneity and inverter ramp-down activity) weighted toward their most predictive horizons.
- Anchors predictions to a smart persistence baseline with horizon-conditioned corrections and online kernel-weighted adaptive conformal calibration.
- Outperforms 14 baselines, achieving a forecast skill score (FSS) of 0.2950 (0.099 above the next-best model) and robust performance under overcast and variable sky conditions.

## Open Questions & Future Work

- [[physically-grounded-inverter-adjacency-and-vendor-integration]]

## Archivist Review

Applied strict scarcity and novelty filters. Approved the open question regarding physically grounded adjacency and vendor integration as it highlights tangible, non-trivial extensions for renewable energy forecasting. Rejected the model-specific architecture concept to keep the vault clean of paper-local branding.

### Approved Open Questions
- Physically Grounded Inverter Adjacency Modeling: Incorporating physical coordinates and external weather products addresses fundamental limitations in data-driven spatial modeling for renewable energy, directly enhancing the interpretability and robustness of graph-based forecasting frameworks.

### Rejected Candidates
- [concept] IMPACT Framework (`impact-framework`) - not_reusable: The multimodal forecasting architecture is a specific instantiation of combining standard graph attention, solar geometry, and persistence correction rather than a broadly reusable architectural paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2610.40418)
- [PDF](https://arxiv.org/pdf/2610.40418)

