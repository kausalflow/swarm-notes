---
# CSL-compatible fields
title: "Evaluating Skill and Stability of ArchesWeather and ArchesWeatherGen under Multi-Decadal Climate Simulations"
author:
  - literal: "Renu Singh"
  - literal: "Robert Brunstein"
  - literal: "Antonia Jost"
  - literal: "Thomas Rackow"
  - literal: "Claire Monteleoni"
  - literal: "Yana Hasson"
  - literal: "Christian Lessig"
  - literal: "Guillaume Couairon"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29976"

# Custom fields
paper_id: "2605.29976"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "benchmark"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "ai-model-intercomparison-project-aimip"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:36Z"
created_at: "2026-05-31T08:10:36Z"
---

# Evaluating Skill and Stability of ArchesWeather and ArchesWeatherGen under Multi-Decadal Climate Simulations

**Authors**: Renu Singh, Robert Brunstein, Antonia Jost, Thomas Rackow, Claire Monteleoni, Yana Hasson, Christian Lessig, Guillaume Couairon
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29976](https://arxiv.org/abs/2605.29976)

## Summary

This paper evaluates the performance of ArchesWeather and ArchesWeatherGen in long-term climate simulations by adapting them as forced atmospheric models via boundary condition conditioning (SST and SIC). Following the AI Model Intercomparison Project (AIMIP) Phase 1 protocol, the authors demonstrate that these models—originally designed for short-range weather forecasting—can produce stable multi-decadal climate simulations. The results show that both deterministic and probabilistic variants effectively capture climate dynamics, climatology, and distribution tails comparable to traditional numerical models.

## Key Contributions

- Adapts weather-forecasting models ArchesWeather and ArchesWeatherGen into forced atmospheric climate models using monthly SST and SIC boundary conditions.
- Demonstrates that these models achieve stable long-term climate simulations and consistent annual cycles when evaluated under the AIMIP Phase 1 protocol.
- Shows that the ML-based models faithfully reproduce ERA5 climatology, large-scale circulation patterns, and interannual variability.

## Open Questions & Future Work

- [[efficient-generative-climate-emulation]]
- [[improving-climate-model-ood-generalization]]

## Key Concepts

- [[ai-model-intercomparison-project-aimip]]: A standardized protocol for evaluating the climate simulation skill of ML-based forced atmospheric models.

## Archivist Review

The paper presents a notable effort in adapting short-term weather models for long-term climate simulation. I have approved the AIMIP concept for its role as an emerging standard, and the two open questions for capturing the fundamental bottlenecks of computational cost and OOD robustness in data-driven climate emulation. ERA5 was rejected as it is a routine, ubiquitous dataset in the field.

### Approved Concepts
- AI Model Intercomparison Project (AIMIP): Provides a standardized framework for evaluating machine learning climate models, similar to the established AMIP standard for numerical models.

### Approved Open Questions
- Efficient generative climate emulation: Computational efficiency is a primary constraint for scaling climate emulators to higher resolutions and larger ensemble sizes; optimizing generative models is critical for their practical utility in climate science.
- Improving climate model OOD generalization: Ensuring robust model responses to out-of-distribution forcings is essential for using data-driven emulators to reliably forecast future climate change scenarios.

## Links

- [Abstract](https://arxiv.org/abs/2605.29976)
- [PDF](https://arxiv.org/pdf/2605.29976)

