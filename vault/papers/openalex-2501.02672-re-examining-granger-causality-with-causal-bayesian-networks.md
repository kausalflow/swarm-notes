---
# CSL-compatible fields
title: "Re-examining Granger Causality with Causal Bayesian Networks and Reichenbach's Principles"
author:
  - literal: "Samuel Adedayo"
issued:
  date-parts:
    - [2026, 7, 24]
url: "https://arxiv.org/abs/2501.02672"

# Custom fields
paper_id: "2501.02672"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "causal-discovery"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "causalised-granger-causality"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-26T07:29:59Z"
created_at: "2026-07-26T07:29:59Z"
---

# Re-examining Granger Causality with Causal Bayesian Networks and Reichenbach's Principles

**Authors**: Samuel Adedayo
**Date**: 2026-07-24
**Paper ID**: [openalex:2501.02672](https://arxiv.org/abs/2501.02672)

## Summary

This paper re-examines Granger causality by interpreting bivariate and multivariate formulations through causal Bayesian networks and Reichenbach's common cause principles, leading to causalised Granger causality (c-GC) and c-GC* to better distinguish direct causal effects from confounding or indirect dependencies.

## Key Contributions

- Re-interprets bivariate and multivariate Granger causality through causal Bayesian networks and Reichenbach's common cause principles to clarify structural limitations.
- Proposes causalised Granger causality (c-GC) and a conservative variant c-GC* that combine marginal dependence checks and conditioned association tests.
- Validates the proposed criteria on synthetic dynamical systems, Sachs protein-signalling data, and Lorenz-96 simulations, demonstrating robust recovery of causal structure under cycles and noise.

## Open Questions & Future Work

- [[scaling-cgc-high-dimensional-datasets]]

## Key Concepts

- [[causalised-granger-causality]]: A causalised formulation of Granger causality that combines bivariate and multivariate checks under causal graphical principles to recover true directed causal structures.

## Archivist Review

Approved the core methodological concept of causalised Granger causality and the associated open question on scaling to high-dimensional time-series systems. Rejection of Reichenbach's principles was upheld as it is a classical philosophical concept.

### Approved Concepts
- Causalised Granger Causality: Introduces a novel extension of Granger causality grounded in causal Bayesian networks and Reichenbach's principles to distinguish direct causal effects from indirect paths and common causes.

### Approved Open Questions
- Scaling Causalized Granger Causality: Scalability to high dimensions is a persistent bottleneck in time-series causal structure learning and vector autoregressive methods.

### Rejected Candidates
- [concept] Reichenbach's Principles for Granger Causality (`reichens-principles`) - not_novel: Reichenbach's principle is a well-established philosophical and statistical concept rather than a new ML method or object.

## Links

- [Abstract](https://arxiv.org/abs/2501.02672)
- [PDF](https://arxiv.org/pdf/2501.02672)

