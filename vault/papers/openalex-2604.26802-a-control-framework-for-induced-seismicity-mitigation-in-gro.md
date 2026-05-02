---
# CSL-compatible fields
title: "A Control Framework for Induced Seismicity Mitigation in Groningen Gas Reservoir"
author:
  - literal: "Diego Gutiérrez‐Oribio"
  - literal: "Ioannis Stefanou"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26802"

# Custom fields
paper_id: "2604.26802"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "control-oriented-induced-seismicity-mitigation-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:57:16Z"
created_at: "2026-05-02T06:57:16Z"
---

# A Control Framework for Induced Seismicity Mitigation in Groningen Gas Reservoir

**Authors**: Diego Gutiérrez‐Oribio, Ioannis Stefanou
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26802](https://arxiv.org/abs/2604.26802)

## Summary

This paper proposes a feedback control framework to mitigate induced seismicity in gas reservoirs, specifically targeting the Groningen field. By coupling pore-pressure diffusion with seismicity rate dynamics, the authors design a robust controller that manages extraction and injection flux to maximize production while keeping seismic activity below prescribed safety thresholds. The framework incorporates stochastic event generation to bridge the gap between continuous physical models and discrete event catalogs, allowing for effective digital control of production operations under actuator constraints.

## Key Contributions

- Develops a control-oriented methodology that integrates pore-pressure diffusion with seismicity rate dynamics to optimize gas production under seismic constraints.
- Implements a stochastic event-generation procedure to synthesize realistic earthquake catalogs from continuous seismicity rate fields for controller validation.
- Designs a robust feedback controller that handles actuator saturation (flux limits) to regulate seismicity toward reference levels in the Groningen gas field.

## Open Questions & Future Work

- [[seismicity-rate-estimation-challenges]]

## Key Concepts

- [[control-oriented-induced-seismicity-mitigation-framework]]: A feedback control framework that regulates gas production rates to minimize induced seismicity while meeting operational objectives.

## Archivist Review

I approved the control-oriented framework as it represents a significant methodological shift from standard predictive modeling to active control in geotechnical time-series. I also approved the open question regarding SR estimation, as it highlights a fundamental limitation in using statistical rates as state variables for real-time control. Other candidates were not submitted, keeping the vault focused on this domain-specific contribution.

### Approved Concepts
- Control-Oriented Induced Seismicity Mitigation Framework: It provides a novel, closed-loop approach to solve the inverse problem of optimizing production subject to safety constraints, moving beyond descriptive/forecasting-only models in geophysics.

### Approved Open Questions
- Real-time Seismicity Rate Estimation: This is a fundamental bottleneck for implementing feedback control in seismicity mitigation, as the controller performance is strictly limited by the fidelity and responsiveness of the input state estimation.

## Links

- [Abstract](https://arxiv.org/abs/2604.26802)
- [PDF](https://arxiv.org/pdf/2604.26802)

