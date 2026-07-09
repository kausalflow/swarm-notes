---
# CSL-compatible fields
title: "Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observation Sensitivity"
author:
  - literal: "C.G. Park"
  - literal: "Junsu Ha"
  - literal: "Fu J"
  - literal: "F. C. Park"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.04739"

# Custom fields
paper_id: "2607.04739"
paper_source: "openalex"
domain: "robotics"
tags:
  - "diffusion-model"
  - "robotics"
  - "autonomous-agent"
  - "planning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spatial-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:01Z"
created_at: "2026-07-09T08:19:01Z"
---

# Spatial Attention: Adapting Execution Horizons for Diffusion Policies via Observation Sensitivity

**Authors**: C.G. Park, Junsu Ha, Fu J, F. C. Park
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.04739](https://arxiv.org/abs/2607.04739)

## Summary

This paper addresses the trade-off between robot responsiveness and computational efficiency in action-chunking diffusion policies by introducing an adaptive execution horizon strategy. The authors define 'Spatial Attention' as the expected squared norm of the action log-likelihood gradient with respect to observations, serving as a dynamic measure of how sensitive the policy is to environmental perturbations. By jointly forecasting this attention metric and the action chunk, the model intelligently assigns shorter execution windows to high-sensitivity states and longer ones to low-sensitivity states, resulting in superior performance on robotic tasks.

## Key Contributions

- Introduces 'Spatial Attention', a novel sensitivity-based metric derived from action log-likelihood gradients to quantify policy-observation dependencies.
- Develops an adaptive execution horizon framework that dynamically shortens chunk execution times during high-sensitivity phases and extends them during low-sensitivity phases.
- Demonstrates through simulation and real-world robotics experiments that the proposed approach improves success rates over fixed-horizon baselines without increasing the average compute budget per action.

## Open Questions & Future Work

- [[adaptive-horizons-for-streaming-policies]]

## Key Concepts

- [[spatial-attention]]: A metric based on the gradient of action log-likelihood with respect to observations, used to gauge policy sensitivity and inform adaptive action chunk execution horizons.

## Archivist Review

The concept 'Spatial Attention' provides a valuable, mathematically grounded metric for managing the trade-off between responsiveness and compute in generative policies. The open question regarding 'Adaptive Horizons for Streaming Policies' correctly identifies a fundamental limitation of current chunked-action frameworks that must be addressed to transition toward fully continuous control architectures. Other candidates were deemed overly specific to the robot domain or redundant with existing concepts.

### Approved Concepts
- Spatial Attention: It provides a mathematically grounded metric for dynamic execution horizon adjustment, linking observation sensitivity to policy stability and sampling efficiency.

### Approved Open Questions
- Adaptive Horizons for Streaming Policies: As robotics moves toward more fluid, streaming control policies, the inability to apply discrete-based adaptive horizon techniques creates a functional gap in ensuring real-time responsiveness and robustness for these newer architectures.

## Links

- [Abstract](https://arxiv.org/abs/2607.04739)
- [PDF](https://arxiv.org/pdf/2607.04739)

