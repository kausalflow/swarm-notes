---
# CSL-compatible fields
title: "Multilevel charge fluctuations in a Si/SiGe double quantum dot device"
author:
  - literal: "Dylan Albrecht"
  - literal: "Feiyang Ye"
  - literal: "N. Tobias Jacobson"
  - literal: "John M. Nichol"
issued:
  date-parts:
    - [2026, 10, 19]
url: "https://arxiv.org/abs/2601.08088"

# Custom fields
paper_id: "2601.08088"
paper_source: "openalex"
domain: "physics"
tags:
  - "time-series"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-21T09:43:43Z"
created_at: "2026-10-21T09:43:43Z"
---

# Multilevel charge fluctuations in a Si/SiGe double quantum dot device

**Authors**: Dylan Albrecht, Feiyang Ye, N. Tobias Jacobson, John M. Nichol
**Date**: 2026-10-19
**Paper ID**: [openalex:2601.08088](https://arxiv.org/abs/2601.08088)

## Summary

This paper investigates multilevel discrete charge fluctuations in a Si/SiGe double quantum dot device to understand the origins of device drift and charge noise. The authors analyze noise time series using algorithmically assisted drift/change point detection and compare factorial hidden Markov models (FHMMs) of different n-level fluctuators. Results reveal conditional rate dependence in certain voltage regimes and yield lever arm estimates via a phenomenological detailed balance model, providing insights that could aid in spatially localizing charge fluctuators.

## Key Contributions

- Measured multi-level charge fluctuations in a Si/SiGe double quantum dot device across various operating voltages and temperatures.
- Applied algorithmically assisted drift detection and change point detection to detrend noise timeseries and isolate fluctuating components.
- Performed model comparison using n-level fluctuator factorial hidden Markov models (FHMMs), revealing conditional rate dependence in specific voltage regions.
- Fitted a phenomenological detailed balance model to extracted rate data to estimate gate voltage and conductivity sensitivities (lever arms from -2 ueV/mV to 4 ueV/mV).

## Open Questions & Future Work

- [[spatial-triangulation-charge-fluctuators]]

## Archivist Review

Reviewed the paper on multilevel charge fluctuations in quantum dots. No concepts met the high bar for permanent ML vault inclusion as they are domain-specific physics analyses (factorial hidden Markov models applied to charge noise). The open question regarding spatial triangulation is also too hardware- and physics-local for a general ML knowledge vault.

### Approved Open Questions
- Spatial Triangulation of Charge Fluctuators: Spatial triangulation of charge fluctuators is crucial for connecting abstract noise models to physical defect locations in semiconductor heterostructures, directly informing material growth and device fabrication improvements to mitigate charge noise.

### Rejected Candidates
- [open_question] Spatial Triangulation of Charge Fluctuators (`spatial-triangulation-charge-fluctuators`) - low_impact: The open question addresses a very domain-specific physical hardware problem (quantum dot defect localization) rather than a general machine learning or forecasting methodology bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2601.08088)
- [PDF](https://arxiv.org/pdf/2601.08088)

