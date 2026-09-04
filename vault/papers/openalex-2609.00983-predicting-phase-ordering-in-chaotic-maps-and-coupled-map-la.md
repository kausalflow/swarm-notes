---
# CSL-compatible fields
title: "Predicting Phase Ordering in Chaotic Maps and Coupled Map Lattices"
author:
  - literal: "Shiva Dixit"
  - literal: "Swati Chauhan"
  - literal: "Manish Dev Shrimali"
issued:
  date-parts:
    - [2026, 9, 1]
url: "https://arxiv.org/abs/2609.00983"

# Custom fields
paper_id: "2609.00983"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reservoir-computing"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-04T09:11:38Z"
created_at: "2026-09-04T09:11:38Z"
---

# Predicting Phase Ordering in Chaotic Maps and Coupled Map Lattices

**Authors**: Shiva Dixit, Swati Chauhan, Manish Dev Shrimali
**Date**: 2026-09-01
**Paper ID**: [openalex:2609.00983](https://arxiv.org/abs/2609.00983)

## Summary

This paper introduces a data-driven machine learning framework based on parameter-aware reservoir computing (PARC) to predict order-parameter dynamics and phase transitions in chaotic systems, specifically logistic maps and coupled map lattices (CML). By training the reservoir exclusively on pre-crisis data, the model successfully reconstructs the full bifurcation diagram and anticipates critical transitions such as the shift from ordered to disordered states. Furthermore, by exploiting spatial homogeneity, a single-site trained reservoir successfully scales to a 50x50 CML to capture the transition from in-phase synchronization to anti-phase clustered states.

## Key Contributions

- Proposes a parameter-aware reservoir computing (PARC) framework to predict order-parameter dynamics and phase transitions in chaotic logistic maps and coupled map lattices (CML).
- Demonstrates that a reservoir trained only on pre-crisis time series data below the attractor-merging crisis can successfully reconstruct the full bifurcation diagram and predict the directional order parameter transition.
- Exploits spatial homogeneity in a 2D coupled map lattice (L=50) by training a single reservoir on one site and replicating it across all sites to predict phase coherence transitions from in-phase synchronization to anti-phase clustered states.

## Open Questions & Future Work

- [[multi-parametric-phase-diagram-prediction]]

## Archivist Review

The paper presents an interesting application of reservoir computing to chaotic phase ordering, but the core concepts (parameter-aware reservoir computing, spatial replication) are minor variations of standard reservoir computing techniques. Therefore, no concepts met the strict novelty and reusability bar for the vault. One open question on multi-parametric phase diagram prediction was considered but ultimately rejected to maintain strict scarcity.

### Approved Open Questions
- Multi-Parametric Phase Diagram Prediction: Crucial for modeling complex physical systems where multiple control parameters govern stability and phase transitions simultaneously.

### Rejected Candidates
- [open_question] Multi-Parametric Phase Diagram Prediction (`multi-parametric-phase-diagram-prediction`) - low_impact: The open question is important, but we are keeping approvals strictly minimal and scarce.
- [open_question] Reservoir Computing on Disordered Lattices (`reservoir-computing-on-disordered-lattices`) - low_impact: This represents a standard future work extension regarding spatial heterogeneity.

## Links

- [Abstract](https://arxiv.org/abs/2609.00983)
- [PDF](https://arxiv.org/pdf/2609.00983)

