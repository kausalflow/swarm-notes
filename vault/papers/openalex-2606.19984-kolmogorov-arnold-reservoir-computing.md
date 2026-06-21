---
# CSL-compatible fields
title: "Kolmogorov-Arnold Reservoir Computing"
author:
  - literal: "Juntian Huang"
  - literal: "Jürgen Kurths"
  - literal: "Ying Tang"
issued:
  date-parts:
    - [2026, 6, 18]
url: "https://arxiv.org/abs/2606.19984"

# Custom fields
paper_id: "2606.19984"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir-computing"
  - "kolmogorov-arnold-network"
  - "kan"
architectures:
  []
datasets:
  []
concept_slugs:
  - "kolmogorov-arnold-reservoir-computing-karc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-21T08:54:16Z"
created_at: "2026-06-21T08:54:16Z"
---

# Kolmogorov-Arnold Reservoir Computing

**Authors**: Juntian Huang, Jürgen Kurths, Ying Tang
**Date**: 2026-06-18
**Paper ID**: [openalex:2606.19984](https://arxiv.org/abs/2606.19984)

## Summary

Kolmogorov-Arnold Reservoir Computing (KARC) is a novel framework that bridges reservoir computing with Kolmogorov-Arnold Networks (KANs) to address limitations in representational capacity. By replacing traditional recurrent reservoirs with explicit basis-function expansions, KARC achieves higher fidelity in dynamical system forecasting while maintaining efficient, closed-form training. The method significantly outperforms existing reservoir computing approaches on partial differential equation benchmarks and offers extensibility to generative tasks like diffusion-based text-to-image generation.

## Key Contributions

- Introduces Kolmogorov-Arnold Reservoir Computing (KARC), a method replacing conventional reservoirs with basis-function expansions inspired by the Kolmogorov-Arnold theorem.
- Proves KARC as a lightweight alternative to Kolmogorov-Arnold Networks (KANs) that supports efficient closed-form training.
- Demonstrates superior forecasting performance over state-of-the-art reservoir computing methods on complex benchmarks, including partial differential equations.

## Open Questions & Future Work

- [[developing-expressive-karc-variants]]
- [[extending-karc-to-stochastic-systems]]

## Key Concepts

- [[kolmogorov-arnold-reservoir-computing-karc]]: A reservoir computing framework that replaces traditional reservoirs with basis-function expansions inspired by Kolmogorov-Arnold networks to enhance representational capacity.

## Archivist Review

I have approved the KARC concept as it represents a novel and reusable architectural paradigm for reservoir computing. The open questions regarding expressive variants and stochastic extensions address fundamental trade-offs and domain applicability challenges relevant to time-series modeling. No datasets were approved as none were presented as core, standalone benchmarks.

### Approved Concepts
- Kolmogorov-Arnold Reservoir Computing (KARC): Introduces a new paradigm by merging KAN-inspired basis expansions with the efficiency of reservoir computing, providing a principled approach to dynamical system forecasting.

### Approved Open Questions
- Developing expressive KARC variants: This addresses the fundamental trade-off between model expressivity and computational efficiency, which is critical for scaling these methods to more complex dynamical systems.
- Extending KARC to stochastic systems: Expanding the scope to stochastic dynamics is essential for its applicability in non-idealized environments, which is a recurring bottleneck for dynamical system modeling.

## Links

- [Abstract](https://arxiv.org/abs/2606.19984)
- [PDF](https://arxiv.org/pdf/2606.19984)

