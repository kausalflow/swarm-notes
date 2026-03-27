---
# CSL-compatible fields
title: "On the Limits of Prediction: Forecastability Profiles and Information Decay in Time Series"
author:
  - literal: "Peter Catt"
issued:
  date-parts:
    - [2026, 3, 20]
url: "https://arxiv.org/abs/2603.20546"

# Custom fields
paper_id: "2603.20546"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "information-theory"
  - "evaluation"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-27T14:09:57Z"
created_at: "2026-03-27T14:09:57Z"
---

# On the Limits of Prediction: Forecastability Profiles and Information Decay in Time Series

**Authors**: Peter Catt
**Date**: 2026-03-20
**Paper ID**: [openalex:2603.20546](https://arxiv.org/abs/2603.20546)

## Summary

This paper introduces an information-theoretic framework to quantify the fundamental limits of time series prediction under logarithmic loss. It decomposes the expected performance into an irreducible component (conditional entropy) and an approximation component, with the gap to an unconditional baseline defined as mutual information between the future and the available information. This leads to the definition of forecastability, which, when plotted across lead times, forms a Forecastability Profile that reveals where predictive information is concentrated. The authors then define an Informative Horizon Set, identifying horizons where the achievable gain over a baseline is non-trivial, offering a principled, pre-modelling diagnostic for allocating modelling effort.

## Key Contributions

- Formulation of forecastability as the maximum achievable reduction in expected log loss, decomposed into an irreducible conditional entropy term and an approximation error term.
- Definition of the Forecastability Profile, which quantifies the dependence structure of a time series process across multiple forecast horizons.
- Introduction of the Informative Horizon Set, which formally identifies the horizons where meaningful prediction is feasible based on a practical forecastability threshold.
- Establishment of a pre-modelling diagnostic that separates prediction limits imposed by information decay from errors introduced by the forecasting model.

## Limitations

The framework relies on information-theoretic quantities, which are often intractable for complex, high-dimensional real-world data, necessitating practical estimation strategies.

## Open Questions & Future Work

- [[selection-of-decision-relevant-forecastability-threshold]]
- [[empirical-estimation-of-high-dimensional-mutual-information]]
- [[extension-to-alternative-loss-functions]]

## Key Concepts

- [Forecastability Profile](../concepts/forecastability-profile.md): A profile describing how the maximum achievable reduction in expected log loss (forecastability) varies across different forecast horizons, reflecting the underlying process's dependence structure.
- [Informative Horizon Set](../concepts/informative-horizon-set.md): The set of forecast horizons where the achievable reduction in expected log loss (forecastability) exceeds a defined practical threshold.

## Limitations

The framework relies on information-theoretic quantities, which are often intractable for complex, high-dimensional real-world data, necessitating practical estimation strategies.

## Links

- [Abstract](https://arxiv.org/abs/2603.20546)
- [PDF](https://arxiv.org/pdf/2603.20546)

