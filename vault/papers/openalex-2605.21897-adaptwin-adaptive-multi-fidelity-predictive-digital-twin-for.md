---
# CSL-compatible fields
title: "AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin for Proactive Radio Resource Management in Vehicular Networks"
author:
  - literal: "Armin Makvandi"
  - literal: "Md. Zahid Hassan"
  - literal: "Md. Jahangir Hossain"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21897"

# Custom fields
paper_id: "2605.21897"
paper_source: "openalex"
domain: "nlp"
tags:
  - "llm"
  - "transformer"
  - "continual-learning"
  - "long-context"
  - "multi-agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-multi-fidelity-digital-twin"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:48:29Z"
created_at: "2026-05-24T07:48:29Z"
---

# AdaPTwin: Adaptive Multi-Fidelity Predictive Digital Twin for Proactive Radio Resource Management in Vehicular Networks

**Authors**: Armin Makvandi, Md. Zahid Hassan, Md. Jahangir Hossain
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21897](https://arxiv.org/abs/2605.21897)

## Summary

AdaPTwin is an adaptive multi-fidelity digital twin framework designed for proactive radio resource management in vehicular networks. It employs a hierarchical cloud-edge architecture to perform periodic fidelity selection in the cloud while maintaining real-time edge-based radio resource management through trajectory forecasting and look-ahead ray tracing. By dynamically adjusting simulation fidelity, the system effectively balances computational overhead and accuracy, outperforming traditional non-adaptive predictive digital twins.

## Key Contributions

- Proposed AdaPTwin, an adaptive multi-fidelity digital twin framework that dynamically adjusts simulation fidelity based on vehicular network conditions.
- Implemented a hierarchical cloud-edge architecture allowing for computationally expensive fidelity selection in the cloud and real-time RRM at the edge.
- Achieved up to 90% sum-rate gain and 80% outage reduction compared to non-adaptive digital twin baselines in vehicular scenarios.

## Open Questions & Future Work

- [[uncertainty-safety-aware-dt-rrm]]

## Key Concepts

- [[adaptive-multi-fidelity-digital-twin]]: A digital twin architectural pattern that dynamically modulates simulation resolution and fidelity in response to real-time environmental volatility and computational constraints.

## Archivist Review

I approved the overarching architectural pattern of adaptive multi-fidelity digital twins as it represents a robust, reusable strategy for real-time control. I rejected the paper-specific name AdaPTwin in favor of this broader concept. The open question regarding uncertainty and safety is a critical, domain-universal requirement for deploying predictive twins in physical environments.

### Approved Concepts
- Adaptive Multi-Fidelity Digital Twin: The framework introduces a dynamic switching mechanism between simulation fidelities to balance computational load and accuracy in real-time control, a fundamental problem in digital twin architectures.

### Approved Open Questions
- Safety and Uncertainty-Aware RRM: Reliability in safety-critical vehicular RRM cannot rely on point-estimates alone, making the integration of uncertainty into the twin's loop essential.

### Rejected Candidates
- [concept] AdaPTwin (`adaptwin`) - subcomponent_of_broader_mechanism: The paper-specific title 'AdaPTwin' is less reusable than the underlying architectural mechanism, which I have promoted as 'adaptive-multi-fidelity-digital-twin'.
- [dataset] NVIDIA Sionna (`nvidia-sionna`) - other: Sionna is a simulation library/tool, not a dataset in the context of academic benchmarking.

## Links

- [Abstract](https://arxiv.org/abs/2605.21897)
- [PDF](https://arxiv.org/pdf/2605.21897)

