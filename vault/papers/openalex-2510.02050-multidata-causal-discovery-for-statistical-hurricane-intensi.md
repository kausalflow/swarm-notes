---
# CSL-compatible fields
title: "Multidata Causal Discovery for Statistical Hurricane Intensity Forecasting"
author:
  - literal: "S. Saranya Ganesh"
  - literal: "Frederick Iat‐Hin Tam"
  - literal: "Milton S. Gomez"
  - literal: "Marie C. McGraw"
  - literal: "Mark DeMaria"
  - literal: "Kate D. Musgrave"
  - literal: "Jakob Runge"
  - literal: "Tom Beucler"
issued:
  date-parts:
    - [2026, 6, 19]
url: "https://arxiv.org/abs/2510.02050"

# Custom fields
paper_id: "2510.02050"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "causal-inference"
architectures:
  []
datasets:
  - "SHIPS"
concept_slugs:
  - "multidata-causal-discovery-framework"
dataset_slugs:
  - "ships"
skill: "TimeSeriesSkill"
processed_at: "2026-06-22T10:31:41Z"
created_at: "2026-06-22T10:31:41Z"
---

# Multidata Causal Discovery for Statistical Hurricane Intensity Forecasting

**Authors**: S. Saranya Ganesh, Frederick Iat‐Hin Tam, Milton S. Gomez, Marie C. McGraw, Mark DeMaria, Kate D. Musgrave, Jakob Runge, Tom Beucler
**Date**: 2026-06-19
**Paper ID**: [openalex:2510.02050](https://arxiv.org/abs/2510.02050)

## Summary

This paper introduces a multidata causal discovery framework to improve statistical tropical cyclone (TC) intensity forecasting by replacing standard correlation-based feature selection with causal inference. By utilizing ERA5 meteorological reanalysis, the authors identify key causal predictors such as vertical shear and mid-tropospheric potential vorticity that improve skill in both linear and multilayer perceptron models. The resulting SHIPS+ predictor set demonstrates enhanced short-term forecasting performance and verifies physical consistency, providing a robust pathway for integrating causal discovery into operational hurricane prediction systems.

## Key Contributions

- Introduces a multidata causal discovery framework to identify physically significant predictors for hurricane intensity forecasting.
- Demonstrates that causal feature selection consistently outperforms correlation-based and random forest importance methods on unseen test cases for lead times up to 72 hours.
- Develops the SHIPS+ predictor set, which improves short-term predictive skill at 24, 48, and 72-hour lead times by augmenting standard SHIPS variables with causally discovered features.

## Open Questions & Future Work

- [[causal-feature-discovery-in-forecast-trajectories]]

## Key Concepts

- [[multidata-causal-discovery-framework]]: A feature selection methodology that leverages causal discovery on reanalysis data to identify physically relevant predictors for time-series forecasting.

## Archivist Review

I approved the causal discovery framework and the research question concerning the shift from analysis-time to trajectory-based feature selection, as these provide a reusable methodology and a clear path toward addressing forecast degradation at long lead times. I also included the SHIPS dataset as it is central to the paper's benchmark claims. All other items were rejected for being too application-specific or routine.

### Approved Concepts
- Multidata Causal Discovery Framework: The framework addresses the limitation of correlation-based methods by identifying physically significant, causally linked predictors for time-series forecasting.

### Approved Open Questions
- Causal discovery on forecast trajectories: Moving from analysis-based to trajectory-based causal discovery could significantly reduce forecast uncertainty at longer lead times, representing a key bottleneck in operational hurricane prediction.

## Datasets

- [[ships]]

## Links

- [Abstract](https://arxiv.org/abs/2510.02050)
- [PDF](https://arxiv.org/pdf/2510.02050)

