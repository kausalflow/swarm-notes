---
# CSL-compatible fields
title: "Stable Fine-Time-Step Long-Horizon Turbulence Prediction with a Multi-Stepsize Mixture-of-Experts Neural Operator"
author:
  - literal: "Guanyu Pan"
  - literal: "Huiyu Yang"
  - literal: "Yunpeng Wang"
  - literal: "Zikun Xu"
  - literal: "Jianchun Wang"
  - literal: "Nianyu Yi"
issued:
  date-parts:
    - [2026, 4, 14]
url: "https://arxiv.org/abs/2604.12794"

# Custom fields
paper_id: "2604.12794"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "mixture-of-experts"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multi-stepsize-mixture-of-experts-neural-operator"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-17T06:30:21Z"
created_at: "2026-04-17T06:30:21Z"
---

# Stable Fine-Time-Step Long-Horizon Turbulence Prediction with a Multi-Stepsize Mixture-of-Experts Neural Operator

**Authors**: Guanyu Pan, Huiyu Yang, Yunpeng Wang, Zikun Xu, Jianchun Wang, Nianyu Yi
**Date**: 2026-04-14
**Paper ID**: [openalex:2604.12794](https://arxiv.org/abs/2604.12794)

## Summary

This paper addresses the instability and error accumulation in long-horizon autoregressive forecasting of 3D turbulent flows at fine temporal resolutions. The authors introduce the Ms-MoE neural operator, which leverages a novel IFactFormer backbone to perform stride-parameterized time advancement through scale-specific expert routing. By training on significantly finer resolution DNS data, the model achieves more robust long-horizon rollouts and superior preservation of long-time-averaged statistics compared to existing neural operator benchmarks.

## Key Contributions

- Proposed a multi-stepsize mixture-of-experts (Ms-MoE) neural operator that enables stable long-horizon autoregressive predictions at significantly finer temporal resolutions than existing surrogates.
- Developed the IFactFormer backbone, a stride-parameterized architecture that represents a family of time-advancement operators for turbulent flows.
- Demonstrated superior stability and statistical agreement on forced homogeneous isotropic turbulence (HIT) and turbulent channel flow, supporting up to 20x finer resolution than standard baselines.

## Open Questions & Future Work

- [[long-horizon-stability-compositional-consistency]]

## Key Concepts

- [[multi-stepsize-mixture-of-experts-neural-operator]]: A neural operator that routes inputs to scale-specific experts based on a requested temporal stride to stabilize autoregressive forecasting.

## Archivist Review

The paper introduces a novel approach to stabilizing autoregressive forecasting in turbulence by parameterizing the time-step, which is a significant contribution to the field. I approved the Ms-MoE concept as a generalizable forecasting mechanism and the open question regarding compositional consistency, as these are highly relevant for the long-term reliability of neural surrogates in chaotic time-series domains. The IFactFormer backbone was rejected as it serves as a supporting component for the primary Ms-MoE mechanism.

### Approved Concepts
- Multi-stepsize Mixture-of-Experts (Ms-MoE) Neural Operator: Provides a stride-parameterized forecasting mechanism to mitigate error accumulation and instability in high-frequency autoregressive rollouts.

### Approved Open Questions
- Long-horizon stability and consistency: This is a fundamental challenge for the deployment of learned surrogates in high-fidelity physics simulations.

### Rejected Candidates
- [concept] Implicit Factorized Transformer (IFactFormer) (`ifactformer`) - subcomponent_of_broader_mechanism: The backbone is described as a subcomponent of the Ms-MoE framework and lacks sufficient independent utility evidence outside of this specific implementation.

## Links

- [Abstract](https://arxiv.org/abs/2604.12794)
- [PDF](https://arxiv.org/pdf/2604.12794)

