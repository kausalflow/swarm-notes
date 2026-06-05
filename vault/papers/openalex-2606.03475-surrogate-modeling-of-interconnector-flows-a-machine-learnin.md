---
# CSL-compatible fields
title: "Surrogate Modeling of Interconnector Flows: A Machine Learning Alternative to Full-Scale Power System Simulations with Application to Cross-Border Electricity Exchange"
author:
  - literal: "Robert Gaugl"
  - literal: "Eloy Insunza"
  - literal: "José Portela"
  - literal: "Sonja Wogrin"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03475"

# Custom fields
paper_id: "2606.03475"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "physics-informed"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:39:19Z"
created_at: "2026-06-05T08:39:19Z"
---

# Surrogate Modeling of Interconnector Flows: A Machine Learning Alternative to Full-Scale Power System Simulations with Application to Cross-Border Electricity Exchange

**Authors**: Robert Gaugl, Eloy Insunza, José Portela, Sonja Wogrin
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03475](https://arxiv.org/abs/2606.03475)

## Summary

This paper addresses the computational intractability of planning high-renewable power systems by proposing a machine-learning surrogate model that predicts cross-border electricity flows. The surrogate maps nodal demand and renewable generation data to interconnector flow profiles, which are then used as fixed boundary conditions in reduced power system optimization models. By incorporating a physics-informed loss function, the neural network surrogate ensures flow consistency, achieving up to 500x speedups while maintaining high fidelity to full-scale DC optimal power flow simulations.

## Key Contributions

- Proposes a machine-learning surrogate framework mapping nodal power system data to interconnector-level electricity flows to facilitate tractable power system optimization.
- Introduces a physics-informed loss function for neural network surrogate models to penalize physically impossible cross-border flow patterns.
- Demonstrates ~500x runtime reduction in power system simulations by using ML-generated boundary conditions compared to full-scale DC optimal power flow simulations.

## Open Questions & Future Work

- [[surrogate-modeling-power-system-feasibility]]

## Archivist Review

The paper presents a specific application of surrogate modeling for power systems. I have rejected the surrogate framework and its loss function as they are highly domain-specific applications of existing concepts. The open question regarding feasibility-aware surrogate modeling for complex infrastructure systems was approved as it captures a non-trivial research challenge in power system planning and temporal surrogate modeling.

### Approved Open Questions
- Surrogate Modeling Power System Feasibility: As power systems integrate higher shares of renewables, the structural patterns of interconnector flows become increasingly volatile and difficult to capture with simple scaling, making robust surrogates critical for computationally tractable long-term planning.

### Rejected Candidates
- [concept] Surrogate-based flow modeling framework (`surrogate-modeling-framework-for-interconnector-flows`) - paper_local: This is a domain-specific application of surrogate modeling rather than a reusable core mechanism for the vault.
- [concept] Physics-informed flow loss function (`physics-informed-flow-loss-function`) - subcomponent_of_broader_mechanism: This is a standard implementation of a constrained loss function tailored specifically to power flow, not a general-purpose mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.03475)
- [PDF](https://arxiv.org/pdf/2606.03475)

