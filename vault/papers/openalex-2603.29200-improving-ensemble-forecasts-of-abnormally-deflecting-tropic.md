---
# CSL-compatible fields
title: "Improving Ensemble Forecasts of Abnormally Deflecting Tropical Cyclones with Fused Atmosphere-Ocean-Terrain Data"
author:
  - literal: "Qixiang Li"
  - literal: "Shuwei Huo"
  - literal: "Chong Wang"
  - literal: "Xiaofeng Li"
  - literal: "Yuan Zhou"
issued:
  date-parts:
    - [2026, 3, 31]
url: "https://arxiv.org/abs/2603.29200"

# Custom fields
paper_id: "2603.29200"
paper_source: "openalex"
domain: "time-series"
tags:
  - "multimodal"
  - "time-series"
  - "forecasting"
  - "dataset"
architectures:
  []
datasets:
  - "aot-tcs"
concept_slugs:
  - "atmosphere-ocean-terrain-coupling-architecture"
dataset_slugs:
  - "aot-tcs"
skill: "TimeSeriesSkill"
processed_at: "2026-04-03T06:07:11Z"
created_at: "2026-04-03T06:07:11Z"
---

# Improving Ensemble Forecasts of Abnormally Deflecting Tropical Cyclones with Fused Atmosphere-Ocean-Terrain Data

**Authors**: Qixiang Li, Shuwei Huo, Chong Wang, Xiaofeng Li, Yuan Zhou
**Date**: 2026-03-31
**Paper ID**: [openalex:2603.29200](https://arxiv.org/abs/2603.29200)

## Summary

This paper addresses the limitations of current deep learning-based tropical cyclone (TC) forecasting models, which typically struggle with abnormally deflected storm trajectories due to their reliance on homogeneous data sources. The authors introduce the AOT-TCs dataset, a comprehensive multi-source collection integrating atmospheric, oceanic, and terrain variables. Furthermore, they propose an explicit atmosphere-ocean-terrain coupling architecture that captures complex physical interactions to improve prediction accuracy. Experimental results demonstrate that this approach sets a new state-of-the-art for both normal and abnormally deflected TCs in the Northwest Pacific.

## Key Contributions

- Introduces AOT-TCs, a novel multimodal, multi-source dataset for Northwest Pacific tropical cyclone forecasting that integrates atmospheric, oceanic, and land variables.
- Proposes an atmosphere-ocean-terrain coupling architecture that explicitly models cross-domain physical interactions.
- Achieves state-of-the-art performance on Northwest Pacific tropical cyclone cases (2017-2024), significantly improving accuracy for abnormally deflected cyclones.

## Open Questions & Future Work

- [[tc-forecasting-model-generalization-under-climate-change]]

## Key Concepts

- [[atmosphere-ocean-terrain-coupling-architecture]]: A neural architecture designed for tropical cyclone forecasting that explicitly integrates atmospheric, oceanic, and terrain variables.

## Archivist Review

I approved the core architecture concept as it provides a reusable paradigm for multi-source geophysical forecasting. The AOT-TCs dataset is approved as a foundational, domain-specific resource for this area. The open question on model generalization to extremes is approved for its significance to both climate-driven forecasting and the broader challenge of machine learning bias toward mean behaviors.

### Approved Concepts
- Atmosphere-Ocean-Terrain Coupling Architecture: Enables the model to capture complex interactions across heterogeneous physical domains, which is crucial for forecasting abnormally deflected tropical cyclones.

### Approved Open Questions
- Model Generalization to Extremes: This is technically important because it addresses the inherent 'mode collapse' or bias toward mean behaviors in machine learning models, which is critical for disaster prevention and mitigation under accelerating climate change. Tracking how models evolve to capture rare events is vital for reliable forecasting.

## Datasets

- [[aot-tcs]]

## Links

- [Abstract](https://arxiv.org/abs/2603.29200)
- [PDF](https://arxiv.org/pdf/2603.29200)

