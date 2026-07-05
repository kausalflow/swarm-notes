---
# CSL-compatible fields
title: "UniWind: Toward Unified Day-Ahead Wind Power Forecasting via Physics-Informed State Routing"
author:
  - literal: "Ronghui Xu"
  - literal: "Tongxin Wu"
  - literal: "Guozhen Zhang"
  - literal: "Yihan Li"
  - literal: "Chenjuan Guo"
  - literal: "B Yang"
  - literal: "Yong Li"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.01670"

# Custom fields
paper_id: "2607.01670"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physics-informed-state-routing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:52:53Z"
created_at: "2026-07-05T07:52:53Z"
---

# UniWind: Toward Unified Day-Ahead Wind Power Forecasting via Physics-Informed State Routing

**Authors**: Ronghui Xu, Tongxin Wu, Guozhen Zhang, Yihan Li, Chenjuan Guo, B Yang, Yong Li
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.01670](https://arxiv.org/abs/2607.01670)

## Summary

UniWind addresses the challenge of wind power forecasting by disentangling meteorological drivers from latent operational states such as maintenance or curtailment. The model utilizes a Physical Prior Estimator to establish a physically grounded power envelope, which is then refined by a State-aware Power Corrector. This corrector leverages a Latent State Encoder to apply state-specific adjustments through a knowledge-guided routing mechanism. Experimental results indicate that UniWind effectively enhances forecast accuracy and facilitates robust zero-shot adaptation across diverse wind farm sites.

## Key Contributions

- Proposes UniWind, a novel forecasting model that integrates physics-informed constraints with learned latent operational state embeddings.
- Introduces a Physical Prior Estimator that combines site-calibrated monotonic warping with a shared power curve to bound wind power predictions.
- Achieves superior performance and robust cross-farm zero-shot generalization compared to baseline data-driven and physics-based models on diverse wind farm datasets.

## Open Questions & Future Work

- [[disentangling-operational-states-from-meteorological-dynamics]]

## Key Concepts

- [[physics-informed-state-routing]]: A forecasting framework that partitions predictions into a physically grounded prior and state-specific corrections using latent embeddings.

## Archivist Review

The approved concept 'Physics-Informed State Routing' offers a clean, reusable architecture for time-series forecasting in industrial settings. I refined the open question to focus more precisely on the disentanglement problem rather than generic meteorological integration, as the latter is a common limitation in most climate/energy forecasting papers. I rejected the initial open question as a near-duplicate that lacks the clarity of the refined version.

### Approved Concepts
- Physics-Informed State Routing: It provides a modular, interpretable framework for disentangling physical potential from latent operational dynamics in industrial time-series.

### Approved Open Questions
- Disentangling Operational States: This highlights a fundamental bottleneck in the effective separation of exogenous environmental signals from endogenous operational state changes in industrial time-series.

### Rejected Candidates
- [open_question] Integrating Local Meteorological Dynamics (`improving-meteorological-integration-for-wind-forecasting`) - duplicate_existing: The proposed question is generic and conflates a specific wind-forecasting improvement with the broader challenge of disentangling operational states, which is better covered by the approved open question.

## Links

- [Abstract](https://arxiv.org/abs/2607.01670)
- [PDF](https://arxiv.org/pdf/2607.01670)

