---
# CSL-compatible fields
title: "Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates"
author:
  - literal: "K. C. Peng"
  - literal: "J Jiang"
  - literal: "C Y Lin"
  - literal: "Y Peng"
  - literal: "Junghoon Park"
  - literal: "Hua-an Tseng"
  - literal: "Hsin-Yi Lin"
  - literal: "Kuan-Cheng Chen"
  - literal: "Chen-Yu Liu"
  - literal: "Shinjae Yoo"
  - literal: "Samuel Yen-Chi Chen"
issued:
  date-parts:
    - [2026, 7, 2]
url: "https://arxiv.org/abs/2607.02363"

# Custom fields
paper_id: "2607.02363"
paper_source: "openalex"
domain: "nlp, time-series"
tags:
  - "language-model"
  - "time-series"
  - "forecasting"
  - "quantum-machine-learning"
  - "memory-mechanism"
architectures:
  []
datasets:
  - "milan-sms-dataset"
concept_slugs:
  - "bounded-old-state-modulation-rule"
dataset_slugs:
  - "milan-sms-dataset"
skill: "TimeSeriesSkill"
processed_at: "2026-07-05T07:53:04Z"
created_at: "2026-07-05T07:53:04Z"
---

# Stable Self-Modulating Quantum Fast-Weight Programmers with Bounded Memory Gates

**Authors**: K. C. Peng, J Jiang, C Y Lin, Y Peng, Junghoon Park, Hua-an Tseng, Hsin-Yi Lin, Kuan-Cheng Chen, Chen-Yu Liu, Shinjae Yoo, Samuel Yen-Chi Chen
**Date**: 2026-07-02
**Paper ID**: [openalex:2607.02363](https://arxiv.org/abs/2607.02363)

## Summary

This paper addresses numerical instability in self-modulating quantum fast-weight programmers (QFWPs) by introducing a bounded old-state modulation rule. By applying a sign-preserving tanh gate specifically to the recurrent memory branch, the proposed method successfully prevents divergence in long-sequence modeling regimes. Empirical evaluation on quantum-dynamics forecasting and the Milan SMS telecommunication dataset reveals that old-state modulation is essential for performance, with the bounded gating approach enhancing both convergence and robustness.

## Key Contributions

- Identifies accumulated-memory modulation as the primary driver of performance gains in self-modulating quantum fast-weight programmers.
- Proposes a bounded old-state modulation rule that eliminates long-sequence numerical divergence while improving aggregate robustness.
- Demonstrates consistent improvements over standard quantum sequence modeling on quantum-dynamics forecasting and real-world telecommunication activity datasets.

## Open Questions & Future Work

- [[universality-of-bounded-gating-stability]]

## Key Concepts

- [[bounded-old-state-modulation-rule]]: A stability-focused gating mechanism for quantum fast-weight programmers that applies a sign-preserving tanh constraint to the recurrent memory branch.

## Archivist Review

The paper is approved for the concept of bounded memory modulation in quantum sequence modeling and the associated open question regarding the universality of such stability constraints. A specific dataset (Milan SMS) is added as a canonical reference for communication activity forecasting, ensuring consistency with vault naming conventions. The rejection of the original dataset label is purely for standardization purposes.

### Approved Concepts
- Bounded Old-State Modulation Rule: It provides a specific stabilization mechanism for quantum fast-weight programmers, preventing the numerical divergence found in unbounded variants during long-sequence modeling.

### Approved Open Questions
- Universality of Bounded Gating: Understanding the universality of the stabilization requirement is critical for architectural design of quantum-classical hybrid models, as unnecessarily aggressive bounding might restrict the expressive capacity of the model in stable regimes.

### Rejected Candidates
- [dataset] Milan SMS (`milan-sms`) - other: Replaced with standardized slug 'milan-sms-dataset' for consistency with vault standards.

## Datasets

- [[milan-sms-dataset]]

## Links

- [Abstract](https://arxiv.org/abs/2607.02363)
- [PDF](https://arxiv.org/pdf/2607.02363)

