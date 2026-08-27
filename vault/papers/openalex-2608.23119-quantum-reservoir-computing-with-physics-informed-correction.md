---
# CSL-compatible fields
title: "Quantum Reservoir Computing with Physics-Informed Correction for Reduced-Order PDE Forecasting"
author:
  - literal: "Krishna Bhatia"
  - literal: "Harsh"
  - literal: "Shalini Devendrababu"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23119"

# Custom fields
paper_id: "2608.23119"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed-neural-networks"
  - "reservoir-computing"
  - "dynamical-systems"
architectures:
  - "rwkv"
datasets:
  []
concept_slugs:
  - "quantum-reservoir-computing-with-physics-informed-correction"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:38Z"
created_at: "2026-08-27T15:58:38Z"
---

# Quantum Reservoir Computing with Physics-Informed Correction for Reduced-Order PDE Forecasting

**Authors**: Krishna Bhatia, Harsh, Shalini Devendrababu
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23119](https://arxiv.org/abs/2608.23119)

## Summary

This paper introduces a hybrid proposal-correction architecture for reduced-order partial differential equation (PDE) forecasting, coupling a pure-state quantum reservoir computer (QRC) for latent coefficient dynamics with a physics-informed corrector (PIC) for local rollout refinement. Evaluated on the Burgers and chaotic Kuramoto-Sivashinsky (KS) equations, the proposed QRC+PIC approach consistently outperforms standalone QRC across RMSE, NRMSE, and PDE residual metrics. The findings establish quantum reservoir computing with physics-informed correction as a promising, benchmark-dependent strategy for chaotic time-series forecasting.

## Key Contributions

- Proposes a hybrid proposal-correction architecture combining pure-state quantum reservoir computing (QRC) for latent dynamics prediction and a PINN-based physics-informed corrector (PIC) for local rollout refinement.
- Evaluates the framework on the Burgers equation and the chaotic Kuramoto-Sivashinsky (KS) equation.
- Demonstrates that QRC+PIC consistently improves over standalone QRC in RMSE, NRMSE, and PDE residuals on the Kuramoto-Sivashinsky benchmark.

## Limitations

Evaluated primarily on Burgers and Kuramoto-Sivashinsky equations, and highlights that simple baselines remain strong under certain regimes such as Burgers.

## Open Questions & Future Work

- [[hardware-qrc-noisy-deployment]]

## Key Concepts

- [[quantum-reservoir-computing-with-physics-informed-correction]]: A hybrid proposal-correction architecture that combines a quantum reservoir computer with a physics-informed corrector for reduced-order PDE forecasting.

## Archivist Review

Applied strict scarcity and novelty filters, approving the primary hybrid architecture concept and the open question regarding physical NISQ hardware deployment while rejecting redundant or paper-local variants.

### Approved Concepts
- Quantum Reservoir Computing with Physics-Informed Correction: Central methodological novelty combining pure-state quantum reservoir computing with physics-informed correction for PDE forecasting.

### Approved Open Questions
- Hardware Quantum Reservoir Forecasting: Understanding how quantum noise and hardware constraints impact chaotic reduced-order forecasting is critical for transitioning quantum machine learning models from simulation to real-world deployment.

## Links

- [Abstract](https://arxiv.org/abs/2608.23119)
- [PDF](https://arxiv.org/pdf/2608.23119)

