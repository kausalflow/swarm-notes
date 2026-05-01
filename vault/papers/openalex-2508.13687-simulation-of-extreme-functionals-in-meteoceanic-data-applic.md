---
# CSL-compatible fields
title: "Simulation of extreme functionals in meteoceanic data: application to surge evolution over tidal cycles"
author:
  - literal: "Nathan Gorse"
  - literal: "Olivier Roustant"
  - literal: "Jérémy Rohmer"
  - literal: "Déborah Idier"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2508.13687"

# Custom fields
paper_id: "2508.13687"
paper_source: "openalex"
domain: "time-series,env-science"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "extreme-functional-simulation-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:31Z"
created_at: "2026-05-01T07:22:31Z"
---

# Simulation of extreme functionals in meteoceanic data: application to surge evolution over tidal cycles

**Authors**: Nathan Gorse, Olivier Roustant, Jérémy Rohmer, Déborah Idier
**Date**: 2026-04-28
**Paper ID**: [openalex:2508.13687](https://arxiv.org/abs/2508.13687)

## Summary

This paper addresses the challenge of modeling extreme coastal flooding events in the presence of temporal dependence and short-tailed functional data. The authors propose a two-stage methodology that first decorrelates tidal cycles using an autoregressive model and then applies Pareto processes to the residuals. This framework allows for the simulation of extreme surge scenarios that can be tuned to desired intensity levels. Performance is validated against real-world observations at the Gâvres site using rigorous statistical and classification-based criteria.

## Key Contributions

- Introduced a two-stage simulation methodology to model extreme meteoceanic events by decorrelating temporal cycles via autoregressive modeling.
- Adapted Pareto process techniques to generate extreme scenarios from residuals, overcoming standard limitations of functional extreme value theory.
- Validated the simulation framework for surge data on the Gâvres site using multi-criteria benchmarks including PCA and extreme value analysis.

## Key Concepts

- [[extreme-functional-simulation-framework]]: A two-stage simulation methodology for extreme functional events that accounts for temporal dependence and short-tailed behavior.

## Archivist Review

The approved concept offers a rigorous, domain-agnostic framework for functional extreme value analysis, addressing common limitations in temporal data. No other candidates were provided or warranted approval given the strict archive policy.

### Approved Concepts
- Extreme Functional Simulation Framework: It addresses the limitations of standard extreme value theory for functional meteoceanic data by combining autoregressive residuals with Pareto processes.

## Links

- [Abstract](https://arxiv.org/abs/2508.13687)
- [PDF](https://arxiv.org/pdf/2508.13687)

