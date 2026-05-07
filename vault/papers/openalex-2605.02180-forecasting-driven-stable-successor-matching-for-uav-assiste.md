---
# CSL-compatible fields
title: "Forecasting-Driven Stable Successor Matching for UAV-Assisted Continuous Edge Services"
author:
  - literal: "Houyi Qi"
  - literal: "Minghui Liwang"
  - literal: "Yuhan Su"
  - literal: "Xianbin Wang"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02180"

# Custom fields
paper_id: "2605.02180"
paper_source: "openalex"
domain: "nlp"
tags:
  - "lstm"
  - "forecasting"
  - "edge-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fresco-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:27Z"
created_at: "2026-05-07T07:37:27Z"
---

# Forecasting-Driven Stable Successor Matching for UAV-Assisted Continuous Edge Services

**Authors**: Houyi Qi, Minghui Liwang, Yuhan Su, Xianbin Wang
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02180](https://arxiv.org/abs/2605.02180)

## Summary

This paper proposes Fresco, a forecasting-driven framework for continuous service provisioning in UAV-assisted edge networks. By leveraging an LSTM-based module to predict mission disruption risks, Fresco identifies optimal standby UAVs and initiates resource reservation and context synchronization in advance. This proactive approach ensures seamless handover and mission continuity despite UAV mobility and energy constraints, outperforming reactive handover mechanisms with minimal overhead.

## Key Contributions

- Introduces the Fresco framework, which utilizes LSTM-based disruption risk prediction to orchestrate proactive resource reservation for mission-critical UAV edge services.
- Implements an online risk-aware successor matching algorithm that satisfies constraints on delay, energy, and computational load while minimizing reservation overhead.
- Demonstrates through experimental validation that the proposed proactive approach significantly improves mission continuity in dynamic edge networks compared to reactive baseline strategies.

## Open Questions & Future Work

- [[adaptive-prediction-horizon-for-dynamic-service-scheduling]]

## Key Concepts

- [[fresco-framework]]: A forecasting-driven scheduling framework that proactively reserves standby resources and synchronizes service context in UAV edge networks to ensure mission continuity.

## Archivist Review

I approved the Fresco framework as it establishes a distinct, proactive paradigm for edge service continuity. I generalized the open question to be applicable to broader dynamic networking domains beyond just UAVs, as this is a fundamental trade-off in predictive resource orchestration. Other candidates were rejected as implementation-specific details.

### Approved Concepts
- Fresco Framework: Core contribution defining a proactive service handover mechanism for UAV edge networks.

### Approved Open Questions
- Adaptive Prediction Horizon Design: The current limitation of fixed-horizon prediction in proactive handover schemes presents a bottleneck for robustness in highly variable mobile edge environments.

### Rejected Candidates
- [concept] LSTM-based Disruption Risk Prediction (`lstm-disruption-risk-prediction`) - subcomponent_of_broader_mechanism: The use of LSTM for risk prediction is an implementation detail rather than a distinct, reusable methodology.

## Links

- [Abstract](https://arxiv.org/abs/2605.02180)
- [PDF](https://arxiv.org/pdf/2605.02180)

