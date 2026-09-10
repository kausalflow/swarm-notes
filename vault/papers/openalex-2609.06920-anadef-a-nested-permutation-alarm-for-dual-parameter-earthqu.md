---
# CSL-compatible fields
title: "ANADEF: A Nested-Permutation Alarm for Dual-Parameter Earthquake Forecasting"
author:
  - literal: "Hamzeh Mohammadigheymasi"
  - literal: "Muhammed Hossein Mousavi"
  - literal: "Nuno Pombo"
issued:
  date-parts:
    - [2026, 9, 7]
url: "https://arxiv.org/abs/2609.06920"

# Custom fields
paper_id: "2609.06920"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "nested-permutation-alarm-for-dual-parameter-earthquake-forecasting-anadef"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:16:32Z"
created_at: "2026-09-10T09:16:32Z"
---

# ANADEF: A Nested-Permutation Alarm for Dual-Parameter Earthquake Forecasting

**Authors**: Hamzeh Mohammadigheymasi, Muhammed Hossein Mousavi, Nuno Pombo
**Date**: 2026-09-07
**Paper ID**: [openalex:2609.06920](https://arxiv.org/abs/2609.06920)

## Summary

The authors present ANADEF, a novel pipeline that integrates stress-sensitive Gutenberg-Richter b-value fields with rate-based seismicity models for regional earthquake forecasting. Applied to an 18-year catalog of the Zagros Fold-Thrust Belt, the model demonstrates high retrospective skill and reduced alarmed areas compared to rate-only baselines. Furthermore, a nested permutation procedure is introduced to formally test whether stress proxies add non-redundant predictive information beyond background rates, addressing optimization bias.

## Key Contributions

- Introduced the ANADEF pipeline combining a stress-sensitive Gutenberg-Richter b-value field (via penalized 2D B-spline inversion) with stationary background rate from space-time ETAS stochastic declustering.
- Achieved a retrospective Area Skill Score S = 0.69 and reduced alarmed area from tau approx 0.38 to tau approx 0.28 while maintaining a hit rate of nu = 92.7% for M_w >= 5.0 earthquakes in the Zagros Fold-Thrust Belt.
- Implemented a nested permutation procedure to absorb optimization bias and test whether stress-sensitive b-values add non-redundant information beyond background rates.

## Limitations

Thresholds were calibrated on the evaluation catalog (in-sample estimates) and significance tests under spatial-structure-preserving null models showed weaker evidence (p = 0.057).

## Open Questions & Future Work

- [[prospective-validation-dual-parameter-forecasting]]

## Key Concepts

- [[nested-permutation-alarm-for-dual-parameter-earthquake-forecasting-anadef]]: A pipeline that integrates stress-sensitive b-value fields with rate-based seismicity models while formally testing their non-redundancy via nested permutation.

## Archivist Review

Approved the ANADEF pipeline concept and the prospective validation open question as they offer distinct, reusable methodology and an explicit unresolved bottleneck in multi-parameter seismicity forecasting. No datasets met the strict criteria for permanent standalone notes.

### Approved Concepts
- Nested-Permutation Alarm for Dual-Parameter Earthquake Forecasting (ANADEF): It introduces a rigorous testing framework to evaluate the non-redundancy and complementarity of stress-sensitive and rate-based earthquake predictors.

### Approved Open Questions
- Prospective Validation of Dual-Parameter Forecasting: Resolving whether stress-based parameters genuinely improve forecasting skill over rate-based baselines is central to advancing physics-based operational earthquake forecasting models.

## Links

- [Abstract](https://arxiv.org/abs/2609.06920)
- [PDF](https://arxiv.org/pdf/2609.06920)

