---
# CSL-compatible fields
title: "Context-dependent time-series prediction via HyperReservoirs"
author:
  - literal: "Kohei Tsuchiyama"
  - literal: "Takatomo Mihana"
  - literal: "Ryoichi Horisaki"
  - literal: "André Röhm"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34847"

# Custom fields
paper_id: "2609.34847"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hyperreservoir"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:19Z"
created_at: "2026-09-30T10:49:19Z"
---

# Context-dependent time-series prediction via HyperReservoirs

**Authors**: Kohei Tsuchiyama, Takatomo Mihana, Ryoichi Horisaki, André Röhm
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34847](https://arxiv.org/abs/2609.34847)

## Summary

The paper introduces HyperReservoirs, an extension of reservoir computing designed to handle time-series data featuring multiple dynamical regimes or varying time-sampling scales. The architecture couples a main reservoir with a smaller context reservoir that modulates the main reservoir's output weights, combining hypernetwork-like modulation with standard linear regression training. Evaluations on Lorenz and Rössler systems show that HyperReservoirs outperform conventional Echo State Networks and full-matrix Conceptors in terms of prediction error across varying bifurcation parameters and sampling rates.

## Key Contributions

- Proposes HyperReservoirs, an extended reservoir computing model combining a main reservoir with a context reservoir that modulates output weights.
- Retains simple training via linear regression of standard reservoir computing while handling multi-regime and varying time-scale time series.
- Demonstrates lower mean test error than conventional Echo State Networks (ESNs) and full-matrix Conceptors across Lorenz and Rössler systems with changing bifurcation parameters and time sampling scales.

## Limitations

Evaluation is limited to synthetic dynamical systems (Lorenz and Rössler systems).

## Open Questions & Future Work

- [[generalization-to-unseen-contexts-in-hyperreservoirs]]

## Key Concepts

- [[hyperreservoir]]: An extended reservoir computing model that uses a smaller context reservoir to modulate the output weights of a main reservoir for multi-regime time series prediction.

## Archivist Review

Approved the core concept 'HyperReservoir' as a central, reusable contribution bridging reservoir computing and hypernetworks for multi-regime time series forecasting. Approved the open question regarding generalization to unseen contexts as an important limitation of current context-dependent reservoir frameworks. No specific standardized vault datasets were named.

### Approved Concepts
- HyperReservoir: Introduces a novel reservoir computing extension that modulates output weights using a smaller context reservoir, analogous to hypernetworks while preserving linear regression training.

### Approved Open Questions
- Generalization to Unseen Contexts: Extending contextual decoding to handle unobserved or streaming/inferred contexts is critical for real-world deployments where environmental changes or regime shifts are continuous and non-stationary.

## Links

- [Abstract](https://arxiv.org/abs/2609.34847)
- [PDF](https://arxiv.org/pdf/2609.34847)

