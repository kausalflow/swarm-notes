---
# CSL-compatible fields
title: "NeuroDDAF: Neural Dynamic Diffusion-Advection Fields with Evidential Fusion for Air Quality Forecasting"
author:
  - literal: "Prasanjit Dey"
  - literal: "Soumyabrata Dev"
  - literal: "Angela Meyer"
  - literal: "Bianca Schoen-Phelan"
  - literal: "],concepts:[{display_name:"
  - literal: "evidence_excerpt:"
  - literal: "importance_reason:"
  - literal: "one_liner:"
  - literal: "reusability_reason:"
  - literal: "slug:"
  - literal: "}
],datasets:["
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.01175"

# Custom fields
paper_id: "2604.01175"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "attention-mechanism"
  - "neural-ode"
architectures:
  []
datasets:
  []
concept_slugs:
  - "evidential-fusion-mechanism"
  - "wind-modulated-latent-neural-ode"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:49:38Z"
created_at: "2026-04-04T05:49:38Z"
---

# NeuroDDAF: Neural Dynamic Diffusion-Advection Fields with Evidential Fusion for Air Quality Forecasting

**Authors**: Prasanjit Dey, Soumyabrata Dev, Angela Meyer, Bianca Schoen-Phelan, ],concepts:[{display_name:, evidence_excerpt:, importance_reason:, one_liner:, reusability_reason:, slug:, }
],datasets:[
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.01175](https://arxiv.org/abs/2604.01175)

## Summary

NeuroDDAF is a physics-informed framework designed for robust air quality forecasting by unifying neural representation learning with open-system transport modeling. The model integrates a GRU-Graph Attention encoder with Fourier-domain diffusion-advection components and wind-modulated latent Neural ODEs to account for spatiotemporal dynamics. By utilizing an evidential fusion mechanism, the approach improves forecast accuracy while ensuring well-calibrated uncertainty estimates across various urban environments.

## Key Contributions

- Introduces NeuroDDAF, a physics-informed forecasting framework combining GRU-Graph Attention with Fourier-domain diffusion-advection modeling.
- Utilizes wind-modulated latent Neural ODEs to model continuous-time evolution under dynamic spatiotemporal connectivity.
- Employs an evidential fusion mechanism that adaptively combines physics-guided and neural forecasts while providing well-calibrated uncertainty quantification.
- Achieves superior performance on urban air quality forecasting, including a 9.7% RMSE reduction over AirPhyNet across 1-3 day horizons in benchmark cities.

## Open Questions & Future Work

- [[incorporating-chemical-transformations-in-forecasting]]

## Key Concepts

- [[evidential-fusion-mechanism]]: A fusion approach that adaptively combines disparate model sources while simultaneously quantifying prediction uncertainty through evidential learning.
- [[wind-modulated-latent-neural-ode]]: A latent Neural ODE architecture where the transition dynamics are governed by time-varying exogenous environmental factors.

## Archivist Review

Approved two core architectural mechanisms—the evidential fusion strategy and the wind-modulated latent ODE—as they offer reusable solutions for hybridizing physics and deep learning in transport-based time series forecasting. Added one open question specifically targeting the integration of chemical kinetics into hybrid forecasting, as this represents a clear technical hurdle for the field. Rejected the generic open question on data integration as it lacks the necessary technical specificity to advance foundational research.

### Approved Concepts
- Evidential Fusion Mechanism: Provides a principled way to weigh hybrid (physics-based and data-driven) forecasts while generating calibrated uncertainty in spatiotemporal settings.
- Wind-Modulated Latent Neural ODE: Addresses the challenge of continuous-time dynamics in transport problems where underlying physical connectivity is governed by exogenous time-varying conditions (e.g., wind).

### Approved Open Questions
- Incorporating Chemical Transformations: Capturing chemical transformations is critical for moving beyond simple transport modeling to accurate prediction of secondary pollutants in urban environments.

### Rejected Candidates
- [open_question] Real-time Adaptive Data Integration (`real-time-adaptive-data-integration-for-forecasting`) - generic: This is a generic future work suggestion regarding data integration that does not target a specific technical bottleneck in current ML forecasting architectures.

## Links

- [Abstract](https://arxiv.org/abs/2604.01175)
- [PDF](https://arxiv.org/pdf/2604.01175)

