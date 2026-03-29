---
# CSL-compatible fields
title: "The impact of machine learning forecasting on strategic decision-making for bike sharing systems"
author:
  - literal: "Enrico Angelelli"
  - literal: "Andrea Mor"
  - literal: "Carlotta Orsenigo"
  - literal: "M. Grazia Speranza"
  - literal: "Carlo Vercellis"
issued:
  date-parts:
    - [2026, 3, 27]
url: "https://arxiv.org/abs/2603.14901"

# Custom fields
paper_id: "2603.14901"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "time-series"
  - "application"
  - "simulation"
architectures:
  []
datasets:
  - "Brescia bike sharing system data"
concept_slugs:
  []
dataset_slugs:
  - "brescia-bike-sharing-system-data"
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:06:53Z"
created_at: "2026-03-29T06:06:53Z"
---

# The impact of machine learning forecasting on strategic decision-making for bike sharing systems

**Authors**: Enrico Angelelli, Andrea Mor, Carlotta Orsenigo, M. Grazia Speranza, Carlo Vercellis
**Date**: 2026-03-27
**Paper ID**: [openalex:2603.14901](https://arxiv.org/abs/2603.14901)

## Summary

This paper investigates the use of machine learning models to predict the net flow of bikes (returns minus withdrawals) at individual stations within a bike-sharing system. The core contribution involves integrating these forecasts into a dedicated simulation environment designed to model daily relocation dynamics and aid long-term strategic decision-making. The authors assess the ML forecasts both by comparing their accuracy against existing prediction methods and by quantifying the downstream impact of forecast quality on the overall performance of the simulation tool. The evaluation leverages real-world operational data from the bike-sharing system in Brescia, Italy.

## Key Contributions

- Application of machine learning to forecast net bike flow (returns minus withdrawals) for bike-sharing stations.
- Integration of ML forecasts into a simulation framework to support strategic, long-term decision-making regarding bike relocation dynamics.
- Evaluation methodology comparing ML forecast accuracy against alternative prediction methods.
- Analysis of how forecast quality directly impacts the performance and decision support capabilities of the bike-sharing simulation framework.

## Limitations

The evaluation is based on a single real-world bike-sharing system (Brescia, Italy), which might limit generalizability.

## Open Questions & Future Work

- [[relationship-between-ml-forecasting-and-bss-simulation]]
- [[detailed-user-demand-modeling-od-vs-net-demand]]

## Archivist Review

No novel or reusable concepts were identified as the paper focuses primarily on an application and evaluation methodology. The single dataset used, the Brescia bike sharing system data, was approved as it is the specific grounding for the simulation framework's evaluation. Two open questions were approved: one focusing on the propagation of forecast errors into the simulation framework, and another suggesting a more granular, OD-level forecasting approach over the net flow used in the paper.

### Approved Open Questions
- Forecasting to BSS Simulation Relationship: Understanding how forecast errors propagate through complex simulation models that drive operational planning is key to justifying the adoption of advanced ML techniques in real-world BSS management.
- Detailed User Demand Modeling: OD-level forecasting provides richer spatial information than single-station net demand, which could lead to significantly more optimized and localized relocation strategies.

## Datasets

- [[brescia-bike-sharing-system-data]]

## Links

- [Abstract](https://arxiv.org/abs/2603.14901)
- [PDF](https://arxiv.org/pdf/2603.14901)

