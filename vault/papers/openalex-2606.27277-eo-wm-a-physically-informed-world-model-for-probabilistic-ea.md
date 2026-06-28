---
# CSL-compatible fields
title: "EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting"
author:
  - literal: "Junwei Luo"
  - literal: "Shuai Yuan"
  - literal: "Zhenya Yang"
  - literal: "Yansheng Li"
  - literal: "Zhe Liu"
  - literal: "Hongyun Zhao"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.27277"

# Custom fields
paper_id: "2606.27277"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "multimodal"
  - "diffusion-model"
  - "transformer"
  - "forecasting"
  - "earth-observation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physically-informed-conditioning-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-28T08:16:11Z"
created_at: "2026-06-28T08:16:11Z"
---

# EO-WM: A Physically Informed World Model for Probabilistic Earth Observation Forecasting

**Authors**: Junwei Luo, Shuai Yuan, Zhenya Yang, Yansheng Li, Zhe Liu, Hongyun Zhao
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.27277](https://arxiv.org/abs/2606.27277)

## Summary

EO-WM is a video diffusion transformer designed for multispectral earth observation (EO) forecasting, addressing the challenge of predicting surface dynamics under complex weather forcing. By treating weather variables as distinct physical conditioning signals rather than undifferentiated inputs, the model explicitly accounts for baseline climatology, anomalous weather, and accumulated stress. To bridge the gap between simple reconstruction and causal response, the paper also introduces two specialized diagnostic benchmarks for testing model fidelity to weather-driven changes. Experimental results demonstrate improved sensitivity to environmental degradation events like drought, outperforming conventional diffusion baselines on predictive accuracy for vegetation indices.

## Key Contributions

- Introduces EO-WM, a video diffusion transformer architecture for multispectral earth observation forecasting that leverages structured meteorological conditioning.
- Proposes a physically informed conditioning mechanism that disentangles meteorological forcing into baselines, anomalies, and cumulative stress signals.
- Develops two new diagnostic benchmarks, the Extreme Summer Benchmark and Seasonal Matched-Pair Benchmark, to evaluate predictive response fidelity to environmental stressors.
- Achieves a 5.63% relative reduction in NDVI decline amplitude error and a 7.80% improvement in directional hit rate compared to standard diffusion-based baselines.

## Open Questions & Future Work

- [[long-horizon-eo-forecasting-limits]]
- [[unobserved-land-surface-state-integration]]

## Key Concepts

- [[physically-informed-conditioning-framework]]: A conditioning architecture that decomposes meteorological forcing into climatological baselines, anomalies, and cumulative physical stress signals for improved time-series forecasting.

## Archivist Review

The paper introduces a structured conditioning framework that effectively handles time-varying meteorological forcing by decomposing signals into baselines and anomalies, which is a valuable technique for long-lived time-series forecasting models. The open questions regarding long-horizon scaling and partial observability are foundational bottlenecks for future world-model architectures in environmental forecasting. Diagnostic benchmarks are rejected as they are domain-specific evaluation tasks rather than primary datasets.

### Approved Concepts
- Physically Informed Conditioning Framework: Central approach to solving the problem of weather-conditioned EO forecasting by disentangling different types of physical forcing signals.

### Approved Open Questions
- Long-horizon EO forecasting limits: The ability to perform multi-year or decadal forecasting is critical for climate risk assessment and ecosystem modeling, moving beyond short-term seasonal prediction toward reliable long-term climate simulation.
- Unobserved land-surface state integration: Addressing unobserved state variables is essential for improving the fidelity of forcing-response mappings in drought and agricultural yield modeling.

### Rejected Candidates
- [dataset] Extreme Summer Benchmark (`extreme-summer-benchmark`) - paper_local: Diagnostic benchmarks for model evaluation are typically considered task-specific experiment setup rather than reusable datasets in the vault sense.
- [dataset] Seasonal Matched-Pair Benchmark (`seasonal-matched-pair-benchmark`) - paper_local: Diagnostic benchmarks for model evaluation are typically considered task-specific experiment setup rather than reusable datasets in the vault sense.

## Links

- [Abstract](https://arxiv.org/abs/2606.27277)
- [PDF](https://arxiv.org/pdf/2606.27277)

