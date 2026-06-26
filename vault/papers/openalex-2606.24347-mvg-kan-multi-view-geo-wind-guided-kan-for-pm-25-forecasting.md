---
# CSL-compatible fields
title: "MVG-KAN: Multi-View Geo-Wind Guided KAN for PM$_{2.5}$ Forecasting"
author:
  - literal: "Cheng Huang"
  - literal: "Muyao Guan"
  - literal: "Jairus Yougui Railey"
  - literal: "Ning Xu"
  - literal: "Honghui Xu"
  - literal: "Changjiang Zhang"
  - literal: "Zhen Zhang"
  - literal: "Shiqing Zhang"
  - literal: "Cong Bai"
issued:
  date-parts:
    - [2026, 6, 23]
url: "https://arxiv.org/abs/2606.24347"

# Custom fields
paper_id: "2606.24347"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "forecasting"
  - "spatial-temporal-modeling"
  - "physics-informed-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "geo-wind-graph"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-26T08:25:29Z"
created_at: "2026-06-26T08:25:29Z"
---

# MVG-KAN: Multi-View Geo-Wind Guided KAN for PM$_{2.5}$ Forecasting

**Authors**: Cheng Huang, Muyao Guan, Jairus Yougui Railey, Ning Xu, Honghui Xu, Changjiang Zhang, Zhen Zhang, Shiqing Zhang, Cong Bai
**Date**: 2026-06-23
**Paper ID**: [openalex:2606.24347](https://arxiv.org/abs/2606.24347)

## Summary

MVG-KAN is a spatiotemporal forecasting framework designed for PM2.5 air quality prediction by decomposing signals into local periodic and station-specific residual components. It employs a physically-motivated Geo-Wind Graph to capture wind-driven pollutant dispersion and a Temporal Kolmogorov-Arnold Network (TKAN) to model complex nonlinear autoregressive dynamics. By explicitly separating stable patterns from non-periodic residuals, the model achieves improved forecasting accuracy in heterogeneous urban environments.

## Key Contributions

- Introduces MVG-KAN, a multi-view framework separating periodic patterns from residual dynamics for PM2.5 forecasting.
- Proposes the Geo-Wind Graph, which incorporates physical wind-direction and wind-speed transport priors into spatial residual propagation.
- Integrates a Temporal Kolmogorov-Arnold Network (TKAN) to perform station-wise nonlinear autoregressive correction on de-periodized PM2.5 residuals.

## Open Questions & Future Work

- [[integrating-physical-dynamics-pm2.5-forecasting]]

## Key Concepts

- [[geo-wind-graph]]: A directed spatial graph prior that models residual pollutant propagation by combining geographic distance decay with wind-direction and wind-speed transport.

## Archivist Review

The review focused on isolating the reusable architectural patterns (Geo-Wind Graph) from the specific model instance (MVG-KAN). The open question regarding the integration of physical processes was approved for its relevance to bridging data-driven and mechanistic forecasting. No datasets were approved as none were specifically named as unique, novel contributions of the paper.

### Approved Concepts
- Geo-Wind Graph: It provides a physically motivated directed spatial prior for residual propagation in spatiotemporal time series, which is a reusable architectural pattern for modeling transport phenomena.

### Approved Open Questions
- Integrating Physical Dynamics in Forecasting: Bridging the gap between empirical spatiotemporal modeling and formal chemical-transport simulations is necessary to improve predictive reliability during extreme pollution events.

### Rejected Candidates
- [concept] Multi-View Geo-Wind Guided KAN (MVG-KAN) (`mvg-kan`) - subcomponent_of_broader_mechanism: The framework is a specific application instance; the subcomponents (Geo-Wind Graph and KAN-based residual head) are the reusable contributions.

## Links

- [Abstract](https://arxiv.org/abs/2606.24347)
- [PDF](https://arxiv.org/pdf/2606.24347)

