---
# CSL-compatible fields
title: "Mortality Forecasting as a Flow Field in Tucker Decomposition Space"
author:
  - literal: "Samuel J. Clark"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24299"

# Custom fields
paper_id: "2603.24299"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "tucker-decomposition"
architectures:
  []
datasets:
  - "Human Mortality Database"
concept_slugs:
  - "tucker-decomposition-mortality-forecasting"
  - "mortality-flow-field-integration"
dataset_slugs:
  - "human-mortality-database"
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:28:51Z"
created_at: "2026-03-28T05:28:51Z"
---

# Mortality Forecasting as a Flow Field in Tucker Decomposition Space

**Authors**: Samuel J. Clark
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24299](https://arxiv.org/abs/2603.24299)

## Summary

This paper reframes mortality forecasting by modeling the evolution of multi-population mortality schedules as the integration of a continuous flow field within the low-dimensional latent space defined by a Tucker tensor decomposition of the data. The analysis reveals that the primary dynamic is a one-dimensional flow governed by a scalar speed function, while structural scores provide the remaining dimensions. The proposed system employs an era-weighted speed function to adapt to current dynamics and uses empirically calibrated convergence rates to ensure relaxation toward canonical mortality structures. Performance is rigorously tested via leave-country-out cross-validation over a 50-year horizon, benchmarking against established methods like Lee-Carter.

## Key Contributions

- Reframing mortality forecasting as integrating a flow field within the latent score space of a Tucker tensor decomposition of multi-population data.
- Demonstrating that mortality transition in this latent space is largely a one-dimensional flow driven by a scalar speed function controlling the life expectancy level.
- Developing an era-weighted speed function to adapt the flow dynamics to contemporary forecasting origins.
- Evaluating the system using leave-country-out cross-validation with a 50-year horizon against Lee-Carter and Hyndman-Ullah benchmarks.

## Limitations

The paper's abstract does not explicitly state limitations, but the complexity of calibrating the convergence rates and the assumption of a dominant one-dimensional flow are potential areas for further investigation.

## Key Concepts

- [[tucker-decomposition-mortality-forecasting]]: A method to model mortality forecasting as integrating a flow field within the latent score space derived from a Tucker tensor decomposition of population mortality data.
- [[mortality-flow-field-integration]]: Modeling the evolution of mortality structure as the integration of a continuous velocity field within the latent space of a Tucker decomposition.

## Archivist Review

Two central concepts were approved: the overall framework of using Tucker Decomposition for this specific task, and the core mechanism of modeling the evolution as a 'Flow Field Integration' in the latent space, as both represent reusable conceptual shifts in time-series modeling. The named dataset, Human Mortality Database, was approved as a critical benchmark source. No open questions were deemed substantial enough to warrant a standalone entry beyond general research directions.

### Approved Concepts
- Tucker Decomposition for Mortality Forecasting: This method reframes the entire forecasting problem as a continuous flow in a low-dimensional latent space derived from Tucker decomposition, which is a novel structural approach to mortality modeling.
- Mortality Flow Field Integration: This describes the core dynamic mechanism: modeling the evolution of mortality structure not as discrete steps but as continuous movement (flow) along latent structural axes.

### Rejected Candidates
- [concept] Tucker Decomposition for Mortality Forecasting (`tucker-decomposition-mortality-forecasting`) - duplicate_existing: The existing concept 'tucker-decomposition-mortality-forecasting' is already approved. A new candidate with the same slug is not needed.
- [concept] Mortality Flow Field Integration (`mortality-flow-field-integration`) - duplicate_existing: The existing concept 'mortality-flow-field-integration' is already approved. A new candidate with the same slug is not needed.

## Datasets

- [[human-mortality-database]]

## Links

- [Abstract](https://arxiv.org/abs/2603.24299)
- [PDF](https://arxiv.org/pdf/2603.24299)

