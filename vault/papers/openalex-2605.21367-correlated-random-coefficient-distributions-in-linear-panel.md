---
# CSL-compatible fields
title: "Correlated Random Coefficient Distributions in Linear Panel Models"
author:
  - literal: "Irene Botosaru"
  - literal: "James L. Powell"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21367"

# Custom fields
paper_id: "2605.21367"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:26:14Z"
created_at: "2026-05-23T07:26:14Z"
---

# Correlated Random Coefficient Distributions in Linear Panel Models

**Authors**: Irene Botosaru, James L. Powell
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21367](https://arxiv.org/abs/2605.21367)

## Summary

This paper addresses the identification and estimation of random coefficient distributions in static linear panel models where coefficients can be correlated with observable regressors. The authors derive identification results for both regular and irregular designs using deconvolution and stayer-based arguments, removing the need for strict assumptions on error term time-series structure. They propose a two-step minimum distance sieve estimator for practical implementation. The methodology is applied to household calorie-expenditure data, revealing significant heterogeneity in structural elasticities that challenges traditional homogeneous Engel-curve models.

## Key Contributions

- Established identification conditions for random coefficient distributions in linear panel models with both correlated and uncorrelated components.
- Developed a two-step minimum distance sieve estimator for arbitrary dependence of coefficients on regressors.
- Demonstrated identification through stayer-based arguments in irregular design scenarios without requiring restrictions on time-series error structures.

## Open Questions & Future Work

- [[uniform-inference-for-sieve-deconvolution]]

## Archivist Review

The paper offers rigorous econometric methodology for panel data, but does not introduce generalizable ML architectures or algorithmic paradigms. I have approved a refined version of the open question regarding uniform inference in sieve deconvolution, as it represents a significant, reusable technical challenge in statistical learning for panel data. No other concepts or datasets met the threshold for standalone vault entry.

### Approved Open Questions
- Uniform inference for sieve deconvolution: It is a central technical bottleneck for applying random coefficient models to characterize parameter heterogeneity in panel data.

### Rejected Candidates
- [open_question] Uniform inference for sieve deconvolution (`uniform-inference-two-stage-deconvolution`) - other: Renamed for clarity and conciseness.

## Links

- [Abstract](https://arxiv.org/abs/2605.21367)
- [PDF](https://arxiv.org/pdf/2605.21367)

