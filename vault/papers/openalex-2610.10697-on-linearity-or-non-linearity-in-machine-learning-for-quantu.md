---
# CSL-compatible fields
title: "On linearity or non-linearity in machine learning for quantum chaotic dynamics"
author:
  - literal: "Francesco Perciavalle"
  - literal: "Gallo, Agostino, 1499-1570"
  - literal: "Francesco Plastina"
  - literal: "Gianluigi Greco"
  - literal: "Nicola Lo Gullo"
  - literal: "Carlo Adornetto"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.10697"

# Custom fields
paper_id: "2610.10697"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-10T10:53:01Z"
created_at: "2026-10-10T10:53:01Z"
---

# On linearity or non-linearity in machine learning for quantum chaotic dynamics

**Authors**: Francesco Perciavalle, Gallo, Agostino, 1499-1570, Francesco Plastina, Gianluigi Greco, Nicola Lo Gullo, Carlo Adornetto
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.10697](https://arxiv.org/abs/2610.10697)

## Summary

This paper investigates the effectiveness of machine learning for predicting quantum chaotic dynamics by formulating the problem as time-series forecasting on a Rydberg-atom PXP chain. The authors compare a nonlinear Transformer against a simple linear model, DLinear, across dynamical regimes ranging from ergodic behavior to quantum many-body scarring. Surprisingly, while the Transformer degrades near the scarred limit, DLinear maintains high accuracy across all initial states, demonstrating that complex quantum many-body evolution can be effectively predicted using simple linear mappings.

## Key Contributions

- Formulates quantum chaotic dynamics as a time-series forecasting problem across ergodic and scarred dynamical regimes using a PXP chain benchmark.
- Compares a nonlinear Transformer and a linear forecasting model (DLinear) in predicting quantum many-body observables.
- Demonstrates that the simple linear model (DLinear) outperforms the Transformer as dynamics approach the quantum many-body scarred limit, proving that underlying quantum complexity does not necessitate complex nonlinear forecasting models.

## Limitations

The evaluation is focused on few-qubit PXP chains and specific observables, leaving scaling to larger qubit counts open for future study.

## Open Questions & Future Work

- [[generalizing-linear-forecasting-quantum-chaos]]

## Archivist Review

Applied strict scarcity and novelty filters. Approved the substantive open question regarding generalizing linear forecasting to broader quantum chaos settings, but rejected paper-local benchmarks as concepts.

### Approved Open Questions
- Generalizing Linear Forecasting in Quantum Chaos: It is theoretically critical to understand whether the surprising efficacy of linear models over complex nonlinear transformers in quantum chaotic forecasting is a universal feature of many-body dynamics or specific to particular conserved sectors or entanglement structures.

### Rejected Candidates
- [concept] PXP Chain Quantum Forecasting (`pxp-chain-quantum-forecasting`) - paper_local: Paper-local benchmark and application rather than a reusable time-series forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2610.10697)
- [PDF](https://arxiv.org/pdf/2610.10697)

