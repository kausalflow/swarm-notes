---
# CSL-compatible fields
title: "Forecasting Return Time of Extreme Precipitation by Large Deviation Theory"
author:
  - literal: "Haotian Xie"
  - literal: "Haoxian Liu"
  - literal: "Jingfang Fan"
  - literal: "Ying Tang"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.10890"

# Custom fields
paper_id: "2604.10890"
paper_source: "openalex"
domain: "time-series,"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  - "cmip6"
concept_slugs:
  - "landau-based-extreme-event-modeling"
dataset_slugs:
  - "cmip6"
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:28:19Z"
created_at: "2026-04-16T06:28:19Z"
---

# Forecasting Return Time of Extreme Precipitation by Large Deviation Theory

**Authors**: Haotian Xie, Haoxian Liu, Jingfang Fan, Ying Tang
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.10890](https://arxiv.org/abs/2604.10890)

## Summary

This paper presents a large deviation framework for forecasting the return times of extreme precipitation by applying the Landau distribution, traditionally used in plasma physics. By fitting this distribution to historical data, the framework effectively enriches rare event samples to predict precipitation intensities beyond those historically observed. The study validates this approach against CMIP6 climate projections, uncovering a unified relationship in return time curves that highlights a significant increase in exposure to extreme precipitation events under various future emission scenarios.

## Key Contributions

- Introduces a large deviation theory framework using the Landau distribution to model extreme precipitation, achieving 93% accuracy across global locations.
- Demonstrates the Landau distribution outperforms conventional extreme value distributions in representing the tails of precipitation events.
- Reveals a unified relationship between future return time curves under diverse CMIP6 emission scenarios, quantifying increased exposure risks for 21st-century cohorts.

## Open Questions & Future Work

- [[validating-ldt-asymptotics-climate-systems]]

## Key Concepts

- [[landau-based-extreme-event-modeling]]: The use of the Landau distribution as a heavy-tailed alternative to GEV/GPD distributions for characterizing extreme value statistics in time series.

## Archivist Review

The paper provides a compelling methodological shift by substituting standard extreme value distributions (like GEV) with the Landau distribution for rare event modeling. I have approved this as a reusable concept. The dataset CMIP6 is a standard climate reference and thus approved. The open question was refined to emphasize the broader challenge of applying LDT to complex dynamical systems.

### Approved Concepts
- Landau-based extreme event modeling: Provides a statistically superior alternative to traditional extreme value distributions for modeling heavy-tailed extreme event intensities in complex systems.

### Approved Open Questions
- Validating LDT Asymptotics in Climate Systems: This is a fundamental methodological requirement for applying LDT to complex, non-stationary climate systems, as failing to establish the asymptotic regime can lead to mathematically unsound return-time predictions.

### Rejected Candidates
- [concept] Landau-based extreme precipitation forecasting (`landau-based-extreme-precipitation-forecasting`) - other: Renamed for better generality and conceptual abstraction.
- [open_question] Validating LDT Asymptotics in Climate (`validating-ldt-asymptotics-climate`) - other: Renamed to be more precise regarding climate systems vs. just climate in general.

## Datasets

- [[cmip6]]

## Links

- [Abstract](https://arxiv.org/abs/2604.10890)
- [PDF](https://arxiv.org/pdf/2604.10890)

