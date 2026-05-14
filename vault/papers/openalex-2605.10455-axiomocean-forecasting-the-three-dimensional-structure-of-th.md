---
# CSL-compatible fields
title: "AxiomOcean: Forecasting the Three-Dimensional Structure of the Upper Ocean"
author:
  - literal: "Sensen Wu"
  - literal: "Yifan Chen"
  - literal: "Guantao Pu"
  - literal: "Xiaoyao Sun"
  - literal: "Yijun Chen"
  - literal: "Jin Qi"
  - literal: "Ming Kong"
  - literal: "Keyi Yang"
  - literal: "Lichen Xu"
  - literal: "Wenguan Wang"
  - literal: "Xiaofeng Li"
  - literal: "Zhenhong Du"
issued:
  date-parts:
    - [2026, 5, 11]
url: "https://arxiv.org/abs/2605.10455"

# Custom fields
paper_id: "2605.10455"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "physics-informed-long-short-term-memory-pi-lstm"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hierarchical-3d-column-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-14T07:37:55Z"
created_at: "2026-05-14T07:37:55Z"
---

# AxiomOcean: Forecasting the Three-Dimensional Structure of the Upper Ocean

**Authors**: Sensen Wu, Yifan Chen, Guantao Pu, Xiaoyao Sun, Yijun Chen, Jin Qi, Ming Kong, Keyi Yang, Lichen Xu, Wenguan Wang, Xiaofeng Li, Zhenhong Du
**Date**: 2026-05-11
**Paper ID**: [openalex:2605.10455](https://arxiv.org/abs/2605.10455)

## Summary

AxiomOcean is an AI-based forecasting model designed to address the limitations of existing methods in representing the three-dimensional structure of the upper ocean. By employing a hierarchical 3D encoder-backbone-decoder architecture, the model explicitly accounts for cross-layer dependencies and subsurface stratification. It achieves superior forecast accuracy and physical fidelity for global temperature, salinity, and current fields at 1/12° resolution compared to conventional AI approaches. Significant improvements in predicting upper-ocean heat content and eddy kinetic energy underscore the value of vertical structure preservation in geophysical forecasting.

## Key Contributions

- Introduces AxiomOcean, a global 3D AI ocean forecasting model that explicitly models vertical hierarchy and cross-layer dependence.
- Predicts 3D temperature, salinity, and current fields at 1/12° resolution down to 643m depth.
- Demonstrates 20-35% reduction in day-1 RMSE compared to previous AI models while preserving eddy kinetic energy and subsurface variance.

## Open Questions & Future Work

- [[physical-consistency-in-subsurface-fluid-forecasting]]

## Key Concepts

- [[hierarchical-3d-column-forecasting]]: A forecasting framework that explicitly preserves vertical hierarchy and cross-layer dependencies for 3D state prediction in fluid columns.

## Archivist Review

I have approved a generalized concept for hierarchical 3D column forecasting, as the specific model name 'AxiomOcean' is better framed as an instantiation of this broader methodological contribution. The open question reflects a critical, persistent bottleneck in climate and fluid modeling: balancing AI forecasting performance with the preservation of physical structural integrity in subsurface layers.

### Approved Concepts
- Hierarchical 3D Column Forecasting: Addresses the critical issue of vertical structure degradation in deep learning-based geophysical forecasting, moving beyond 2D surface models.

### Approved Open Questions
- Physical Consistency in Subsurface Forecasting: This is a fundamental challenge in bridging the performance gap between AI surrogates and traditional physical numerical models in climate science.

### Rejected Candidates
- [concept] AxiomOcean (`axiomocean`) - subcomponent_of_broader_mechanism: The model itself is an implementation of the more general concept of hierarchical 3D column forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2605.10455)
- [PDF](https://arxiv.org/pdf/2605.10455)

