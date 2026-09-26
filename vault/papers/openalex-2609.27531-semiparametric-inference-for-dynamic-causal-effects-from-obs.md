---
# CSL-compatible fields
title: "Semiparametric Inference for Dynamic Causal Effects from Observational Time Series"
author:
  - literal: "Shibo Yu"
  - literal: "Yan Chen"
  - literal: "Jin-Hong Du"
  - literal: "Guodong Li"
issued:
  date-parts:
    - [2026, 9, 23]
url: "https://arxiv.org/abs/2609.27531"

# Custom fields
paper_id: "2609.27531"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "causal-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-26T09:37:17Z"
created_at: "2026-09-26T09:37:17Z"
---

# Semiparametric Inference for Dynamic Causal Effects from Observational Time Series

**Authors**: Shibo Yu, Yan Chen, Jin-Hong Du, Guodong Li
**Date**: 2026-09-23
**Paper ID**: [openalex:2609.27531](https://arxiv.org/abs/2609.27531)

## Summary

This paper develops a semiparametric inference framework for estimating dynamic causal effects of interventions from a single serially dependent observational time series in the presence of unmeasured confounding and high-dimensional controls. By integrating debiased machine learning and instrumental variables with buffered block cross-fitting, the authors establish non-asymptotic error bounds and asymptotic normality under geometric beta-mixing. They also show how temporal dependence prediction guarantees satisfy nuisance-rate conditions, and validate the methodology on a monetary-policy application using FRED-MD data.

## Key Contributions

- Developed a semiparametric framework for inferring dynamic causal effects from a single serially dependent observational time series using debiased machine learning and instrumental variables.
- Derived non-asymptotic bounds on estimation error and asymptotic normality across horizons under geometric beta-mixing and buffered block cross-fitting.
- Demonstrated how learner-specific prediction guarantees under temporal dependence verify nuisance-rate conditions for orthogonal inference.
- Applied the framework to monetary-policy analysis using 468 months and 1464 lagged FRED-MD controls, demonstrating that policy tightening lowers housing starts at medium horizons.

## Open Questions & Future Work

- [[time-series-dml-rate-transfer-learners]]

## Archivist Review

No standalone concepts met the stringent criteria for permanent vault notes, as the techniques involve standard combinations of debiased machine learning, instrumental variables, and block cross-fitting. However, the open question on nuisance rate verification for temporal machine learning learners in causal time series is important and general enough to warrant an archival note. No custom datasets met the threshold for inclusion.

### Approved Open Questions
- Nuisance Rate Transfer for Temporal Learners: Establishing rigorous data-driven learner verification bridges theoretical double/debiased machine learning and practical time-series forecasting models, guiding how complex nonparametric models can be safely deployed in causal dynamic settings.

## Links

- [Abstract](https://arxiv.org/abs/2609.27531)
- [PDF](https://arxiv.org/pdf/2609.27531)

