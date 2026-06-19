---
# CSL-compatible fields
title: "Physics-Constrained Neural Networks for Improved Short-Term Weather Forecasting: A Case Study over the South Pacific"
author:
  - literal: "Egor Bugaev"
  - literal: "Fedor Buzaev"
  - literal: "Dmitry Efremenko"
  - literal: "Д. Деркач"
  - literal: "Fedor Ratnikov"
issued:
  date-parts:
    - [2026, 6, 16]
url: "https://arxiv.org/abs/2606.17659"

# Custom fields
paper_id: "2606.17659"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed-machine-learning"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-constrained-neural-networks-pcnns"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-19T09:24:42Z"
created_at: "2026-06-19T09:24:42Z"
---

# Physics-Constrained Neural Networks for Improved Short-Term Weather Forecasting: A Case Study over the South Pacific

**Authors**: Egor Bugaev, Fedor Buzaev, Dmitry Efremenko, Д. Деркач, Fedor Ratnikov
**Date**: 2026-06-16
**Paper ID**: [openalex:2606.17659](https://arxiv.org/abs/2606.17659)

## Summary

This paper enhances Physics-Constrained Neural Networks (PCNNs) for short-term weather forecasting by refining numerical integration and hybrid model design. The authors implement an upgraded solver using WENO-5 and subgrid-scale viscosity to increase the integration time step and stability. Furthermore, they introduce a unified autoregressive block to reduce overfitting across lead times, demonstrating superior performance on the WeatherBench South Pacific dataset compared to standard neural models.

## Key Contributions

- Introduces an upgraded numerical solver incorporating WENO-5, beta-plane approximation, and subgrid-scale viscosity, enabling a 1200s integration step.
- Replaces specialized modular chains with a unified autoregressive hybrid block to mitigate lead-time overfitting.
- Proposes two hybrid models, PI-PredFormer and PI-IAM4VP, achieving 8-22% lower RMSE on WeatherBench (South Pacific) compared to non-physical baselines.

## Open Questions & Future Work

- [[tighter-coupling-pcnn-weather-forecasting]]

## Key Concepts

- [[physics-constrained-neural-networks-pcnns]]: Hybrid models that integrate numerical weather prediction methods with neural network backbones to improve forecast accuracy and physical consistency.

## Archivist Review

The review focused on identifying core scientific ML concepts and fundamental research bottlenecks, excluding model-specific subcomponents and established datasets. I approved the PCNN framework as a central mechanism and identified a critical research question regarding the coupling of physics and neural components. Other candidates were rejected because they were either paper-local architectures or widely known benchmark datasets.

### Approved Concepts
- Physics-Constrained Neural Networks (PCNNs): The paper advances the architectural integration of numerical methods and neural backbones in scientific forecasting.

### Approved Open Questions
- Tighter coupling in PCNNs: Addressing the drift between neural predictions and physical constraints is essential for improving the reliability of mid-to-long-range hybrid forecasts.

### Rejected Candidates
- [concept] Unified Autoregressive Hybrid Block (`unified-autoregressive-hybrid-block`) - subcomponent_of_broader_mechanism: This is a specific architectural subcomponent of the proposed hybrid model and lacks the broader generalizability required for a permanent vault entry.
- [dataset] WeatherBench (`weatherbench`) - duplicate_existing: This is a well-established standard benchmark dataset that does not require a new standalone vault entry.
- [concept] PI-PredFormer (`pi-predformer`) - paper_local: This is a specific model architecture instance rather than a foundational concept or mechanism.
- [concept] PI-IAM4VP (`pi-iam4vp`) - paper_local: This is a specific model architecture instance rather than a foundational concept or mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.17659)
- [PDF](https://arxiv.org/pdf/2606.17659)

