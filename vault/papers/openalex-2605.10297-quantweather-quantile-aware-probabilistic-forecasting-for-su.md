---
# CSL-compatible fields
title: "QuantWeather: Quantile-Aware Probabilistic Forecasting for Subseasonal Precipitation"
author:
  - literal: "Lei Chen"
  - literal: "Xinyu Su"
  - literal: "Xiaohui Zhong"
  - literal: "Hao Li"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10297"

# Custom fields
paper_id: "2605.10297"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-weighted-mean-squared-error-uwm"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:50Z"
created_at: "2026-05-14T07:37:50Z"
---

# QuantWeather: Quantile-Aware Probabilistic Forecasting for Subseasonal Precipitation

**Authors**: Lei Chen, Xinyu Su, Xiaohui Zhong, Hao Li
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10297](https://arxiv.org/abs/2605.10297)

## Summary

QuantWeather addresses the challenge of unreliable uncertainty estimation in subseasonal precipitation forecasting, which traditionally relies on expensive ensemble methods and post-hoc calibration. The framework utilizes a dual-head architecture to jointly learn deterministic and probabilistic forecasts, allowing for direct uncertainty modeling. By enabling efficient stochastic sampling, QuantWeather provides accurate probabilistic outputs with significantly lower computational and storage overhead than standard ensemble approaches. Experimental results demonstrate its effectiveness in both forecast accuracy and operational efficiency.

## Key Contributions

- Proposes QuantWeather, an end-to-end probabilistic forecasting framework that jointly optimizes separate probabilistic and deterministic heads.
- Enables reliable uncertainty estimation without reliance on computationally expensive post-hoc calibration or large-scale ensemble reforecasts.
- Achieves superior probabilistic forecasting skill for subseasonal precipitation while reducing inference-time computational and storage costs compared to ensemble-based methods.

## Open Questions & Future Work

- [[balancing-quantile-calibration-ensemble-dispersion]]

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 0 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Open Questions
- Calibrated Quantile vs. Ensemble Dispersion: As machine learning models increasingly move toward end-to-end probabilistic forecasting, understanding the interaction between deterministic and probabilistic branches is critical for designing architectures that achieve high skill in both metrics without compromising the benefits of ensemble averaging.

### Rejected Candidates
- [concept] QuantWeather probabilistic framework (`quantweather`) - paper_local: This is a paper-local architectural proposal without sufficient evidence for broad reusability across domains.

## Links

- [Abstract](https://arxiv.org/abs/2605.10297)
- [PDF](https://arxiv.org/pdf/2605.10297)

