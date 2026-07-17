---
# CSL-compatible fields
title: "Robustness of Deep Learning Models for PV Power Forecasting under NWP Forecast Errors: A Spatiotemporal and Physically Interpretable Analysis"
author:
  - literal: "Dandan Chen"
  - literal: "Yan Zhao"
  - literal: "Xuepeng Chen"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12954"

# Custom fields
paper_id: "2607.12954"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "interpretability"
  - "explainability"
  - "deep-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physically-constrained-robustness-evaluation-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:09:39Z"
created_at: "2026-07-17T07:09:39Z"
---

# Robustness of Deep Learning Models for PV Power Forecasting under NWP Forecast Errors: A Spatiotemporal and Physically Interpretable Analysis

**Authors**: Dandan Chen, Yan Zhao, Xuepeng Chen
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12954](https://arxiv.org/abs/2607.12954)

## Summary

This paper evaluates the robustness of deep learning and machine learning models for PV power forecasting under realistic, temporally correlated, and physically coupled NWP forecast errors. By employing a simulation-based framework with virtual PV power as a controlled variable, the authors assess how input uncertainty propagates through models like PatchTST, GRU, and N-HITS. The study finds that sequence models effectively filter input noise and utilize historical observations and physical priors when future NWP forecasts become unreliable. The findings provide critical engineering insights into model selection by analyzing the Pareto trade-offs between nominal accuracy, robustness, and computational latency.

## Key Contributions

- Introduces a physically constrained robustness evaluation framework for PV power forecasting that simulates realistic NWP input perturbations.
- Evaluates six representative forecasting models (PatchTST, GRU, N-HITS, LightGBM) to reveal that deep sequence models exhibit superior noise filtering and temporal resilience compared to strong tabular baselines.
- Demonstrates through SHAP and IG analysis that models undergo feature reallocation under noise, shifting reliance from corrupted future inputs to historical data and physical priors.

## Open Questions & Future Work

- [[robustness-under-imperfect-historical-data]]

## Key Concepts

- [[physically-constrained-robustness-evaluation-framework]]: A simulation-based framework for evaluating PV power forecasting models under physically realistic NWP input errors.

## Archivist Review

The paper introduces a structured approach to stress-testing forecasting models against physically realistic input uncertainty. I approved the framework as it provides a valuable template for robustness assessment in physics-informed forecasting, and an open question addressing the common reality of degraded historical data. Other candidates were rejected as they described generic incremental experiment extensions.

### Approved Concepts
- Physically constrained robustness evaluation framework: Establishes a rigorous methodology for evaluating forecasting model robustness against physically coupled input noise that reflects real-world operational challenges in renewable energy forecasting.

### Approved Open Questions
- Robustness under Imperfect Data: Real-world deployments frequently encounter concurrent data quality issues across both input forecasts and historical measurements, making this a critical gap in current field-readiness evaluation.

### Rejected Candidates
- [open_question] Robustness under Complex NWP Uncertainty (`robustness-under-complex-nwp-uncertainty`) - low_impact: The proposed question describes expanding existing perturbation experiments to more complex scenarios, which is standard future work and lacks a specific, clearly defined research bottleneck beyond "more complexity".

## Links

- [Abstract](https://arxiv.org/abs/2607.12954)
- [PDF](https://arxiv.org/pdf/2607.12954)

