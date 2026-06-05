---
# CSL-compatible fields
title: "AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE"
author:
  - literal: "Tao Xie"
  - literal: "Zexi Tan"
  - literal: "Haoyi Xiao"
  - literal: "Mengke Li"
  - literal: "Yiqun Zhang"
  - literal: "Yang Lu"
  - literal: "Cuie Yang"
  - literal: "Yiu-ming Cheung"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03631"

# Custom fields
paper_id: "2606.03631"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "mixture-of-experts"
  - "moe"
  - "interpretability"
  - "explainability"
  - "classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "anchor-routed-mixture-of-experts"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:38:19Z"
created_at: "2026-06-05T08:38:19Z"
---

# AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE

**Authors**: Tao Xie, Zexi Tan, Haoyi Xiao, Mengke Li, Yiqun Zhang, Yang Lu, Cuie Yang, Yiu-ming Cheung
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03631](https://arxiv.org/abs/2606.03631)

## Summary

AnchorMoE is an interpretable-by-construction framework for multivariate time series classification based on a Mixture-of-Experts (MoE) architecture. By routing multi-view representations of local input patches to specialized experts, the model generates predictions as an exact additive decomposition over those segments. To ensure robust performance despite sparse and noisy signal distributions, the framework incorporates a geometric orthogonality constraint and an uncertainty-aware reliability gate. Experimental results confirm that AnchorMoE delivers competitive classification accuracy while providing inherent, ante-hoc transparency into decision-driving temporal patterns.

## Key Contributions

- Proposes AnchorMoE, an interpretable-by-construction MTSC framework that achieves competitive classification performance.
- Enables ante-hoc transparency through an additive decomposition of input segments into expert-based contributions.
- Introduces a geometric orthogonality constraint and an uncertainty-aware reliability gate to effectively isolate discriminative temporal signals from background noise.

## Open Questions & Future Work

- [[modeling-higher-order-segment-interactions-in-interpretable-moe]]
- [[balancing-reliability-gating-with-context-retention]]

## Key Concepts

- [[anchor-routed-mixture-of-experts]]: A Mixture-of-Experts architecture for time series classification that uses anchor-based routing to create an interpretable, additive decomposition of predictions.

## Archivist Review

I approved the Anchor-Routed Mixture-of-Experts as a reusable architectural pattern for ante-hoc interpretability in time series classification. I also approved two open questions that highlight the fundamental limitations in currently popular additive decomposition and reliability gating mechanisms, which are likely to remain relevant as this research area matures.

### Approved Concepts
- Anchor-Routed Mixture-of-Experts: Introduces a novel MoE routing mechanism for time series that enforces an additive decision decomposition, providing inherent interpretability.

### Approved Open Questions
- Modeling Higher-Order Segment Interactions: This is a fundamental tradeoff in self-explaining models: balancing the simplicity required for interpretability with the expressive capacity needed to model complex, interdependent time-series dynamics.
- Balancing Reliability Gating and Context Retention: Reliability gating is a double-edged sword; while it improves the faithfulness of attribution by removing noise, it risks reducing the classification performance and interpretability if it eliminates marginal but contextually relevant features.

## Links

- [Abstract](https://arxiv.org/abs/2606.03631)
- [PDF](https://arxiv.org/pdf/2606.03631)

