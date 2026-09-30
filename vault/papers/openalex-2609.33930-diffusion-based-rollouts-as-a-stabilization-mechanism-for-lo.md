---
# CSL-compatible fields
title: "Diffusion-Based Rollouts as a Stabilization Mechanism for Long-Horizon Environmental Forecasting"
author:
  - literal: "Marina Vicens-Miquel"
  - literal: "Amy McGovern"
  - literal: "Aaron J. Hill"
  - literal: "Efi Foufoula‐Georgiou"
  - literal: "Samuel S. P. Shen"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33930"

# Custom fields
paper_id: "2609.33930"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "diffusion-model"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:28Z"
created_at: "2026-09-30T10:50:28Z"
---

# Diffusion-Based Rollouts as a Stabilization Mechanism for Long-Horizon Environmental Forecasting

**Authors**: Marina Vicens-Miquel, Amy McGovern, Aaron J. Hill, Efi Foufoula‐Georgiou, Samuel S. P. Shen
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33930](https://arxiv.org/abs/2609.33930)

## Summary

This paper investigates diffusion-based rollouts as a stabilization mechanism to mitigate recursive error growth in long-horizon environmental forecasting, evaluated on low-dimensional water-level time series and high-dimensional precipitation fields. The findings demonstrate that while diffusion successfully suppresses error amplification and stabilizes unstable rollouts, its practical utility depends on external conditioning information to prevent over-contraction and maintain event fidelity.

## Key Contributions

- Investigated diffusion-based rollouts as a stabilization mechanism to suppress recursive error growth in long-horizon environmental forecasting across low-dimensional water-level time series and high-dimensional precipitation fields.
- Demonstrated that diffusion effectively controls numerical error amplification where deterministic rollouts are most unstable, though stabilization alone does not guarantee forecast fidelity.
- Revealed through contrasting experiments that diffusion's practical benefit heavily depends on access to external predictive information (such as numerical weather prediction conditioning) to prevent contraction toward central values and maintain event-level fidelity.

## Limitations

Diffusion rollouts can remain numerically stable while contracting toward central values and exhibiting reduced variability when external predictive information is lacking.

## Archivist Review

No new reusable concepts or critical named datasets identified from the abstract.

## Links

- [Abstract](https://arxiv.org/abs/2609.33930)
- [PDF](https://arxiv.org/pdf/2609.33930)

