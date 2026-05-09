---
# CSL-compatible fields
title: "FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning"
author:
  - literal: "Waleed Razzaq"
  - literal: "Yun-Bo Zhao"
issued:
  date-parts:
    - [2026, 5, 6]
url: "https://arxiv.org/abs/2605.04421"

# Custom fields
paper_id: "2605.04421"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "attention-mechanism"
  - "llm"
  - "time-series"
  - "long-context"
  - "autonomous-agent"
architectures:
  []
datasets:
  []
concept_slugs:
  - "liquid-attention-network-lan"
  - "liquid-hyper-connections"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-09T07:03:25Z"
created_at: "2026-05-09T07:03:25Z"
---

# FLUID: Continuous-Time Hyperconnected Sparse Transformer for Sink-Free Learning

**Authors**: Waleed Razzaq, Yun-Bo Zhao
**Date**: 2026-05-06
**Paper ID**: [openalex:2605.04421](https://arxiv.org/abs/2605.04421)

## Summary

FLUID is a continuous-time transformer architecture that replaces discrete scaled-dot-product-attention with the Liquid Attention Network (LAN). LAN models attention logits as a solution to a linear ODE, providing a stable, theoretically grounded bridge between discrete attention and continuous-time RNNs. Furthermore, the model uses Liquid Hyper-Connections to dynamically regulate interlayer information flow, demonstrating significant improvements in autonomous vehicle control, long-range modeling, and irregular time-series tasks.

## Key Contributions

- Introduces the Liquid Attention Network (LAN), a continuous-time attention mechanism derived from a linear ODE modulated by input-dependent nonlinear recurrent gates.
- Proposes Liquid Hyper-Connections to replace static residual connections with adaptive, input-dependent flow regulation.
- Achieves state-of-the-art results on irregular time-series, long-range modeling, and autonomous control tasks, with improvements of up to 47%.

## Open Questions & Future Work

- [[stochastic-lan-formulation]]
- [[manifold-constrained-hyper-connections]]

## Key Concepts

- [[liquid-attention-network-lan]]: A continuous-time attention mechanism that interprets attention logits as a dynamical system solved via a linear ODE.
- [[liquid-hyper-connections]]: An adaptive residual connection mechanism that modulates interlayer information flow based on input-dependent states.

## Archivist Review

I have approved the core methodological contributions (LAN and Liquid Hyper-Connections) as they represent a coherent architectural departure from standard transformers. I have also approved two open questions that directly address the theoretical limitations of these new components (stochasticity and manifold constraints). Other candidates were rejected for being overly generic or implementation-focused.

### Approved Concepts
- Liquid Attention Network (LAN): The mechanism introduces a formal continuous-time attention derivation using ODEs, providing a theoretical bridge between discrete transformer attention and continuous-time recurrent dynamics.
- Liquid Hyper-Connections: It provides an adaptive approach to regulating interlayer signal flow, which is a critical design challenge for deep transformer architectures.

### Approved Open Questions
- Stochastic LAN formulation: Uncertainty quantification is a critical requirement for continuous-time models in safety-critical applications like autonomous control.
- Manifold-constrained hyper-connections: This addresses the trade-off between expressive capacity and training stability, which is central to scaling transformer architectures.

### Rejected Candidates
- [open_question] Learnable Top-K selection (`learnable-topk-selection`) - generic: The suggestion for learnable selection strategies is a generic optimization goal common to many sparse attention works.

## Links

- [Abstract](https://arxiv.org/abs/2605.04421)
- [PDF](https://arxiv.org/pdf/2605.04421)

