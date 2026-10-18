---
# CSL-compatible fields
title: "Learning and Forecasting Multiscale Spatiotemporal Epidemic Dynamics with Lagrangian-Eulerian Graph Neural ODEs"
author:
  - literal: "Jinyi Duan"
  - literal: "Qian Li"
  - literal: "Biao Tang"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21223"

# Custom fields
paper_id: "2610.21223"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
  - "gnn"
  - "differential-privacy"
  - "robustness"
  - "interpretability"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "lagrangian-eulerian-graph-neural-odes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:13:20Z"
created_at: "2026-10-18T09:13:20Z"
---

# Learning and Forecasting Multiscale Spatiotemporal Epidemic Dynamics with Lagrangian-Eulerian Graph Neural ODEs

**Authors**: Jinyi Duan, Qian Li, Biao Tang
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21223](https://arxiv.org/abs/2610.21223)

## Summary

The authors propose LE-EpiGNODE, a mechanism-guided neural ODE model that replaces generic message passing with Lagrangian infection generation (driven by age-contact info) and Eulerian population transport (driven by mobility). Evaluated across 14 synthetic mechanisms and 3 real-world COVID-19 settings against 21 baselines, LE-EpiGNODE achieves superior long-horizon accuracy (reducing WMAPE by 17.7-40.0% at the longest horizon) while preserving interpretable process-level dynamics.

## Key Contributions

- Introduced LE-EpiGNODE, a mechanism-guided neural ODE replacing generic message passing with Lagrangian infection generation and conservative Eulerian population transport.
- Evaluated across 14 controlled synthetic mechanisms, 3 complementary COVID-19 settings, 21 comparators, and 5 ablations, demonstrating robust long-horizon forecasting gains.
- Achieved the lowest WMAPE across all three real-world datasets at the longest forecasting horizon, reducing error by 17.7-40.0% relative to the best baseline.

## Limitations

Future work could extend the Lagrangian-Eulerian decomposition to larger-scale multi-pathogen interactions and unobserved transmission routes.

## Open Questions & Future Work

- [[identifiability-and-adaptation-in-epidemic-neural-odes]]

## Key Concepts

- [[lagrangian-eulerian-graph-neural-odes]]: A process-specific, mechanism-guided neural ODE framework that models epidemic dynamics via Lagrangian infection generation and conservative Eulerian population transport.

## Archivist Review

Approved the overarching framework concept of Lagrangian-Eulerian graph neural ODEs and the open question regarding identifiability and adaptation in continuous epidemic neural models. The specific model name LE-EpiGNODE was rejected as a paper-local duplicate of the main framework. No datasets met the strict long-term reusability or novelty threshold.

### Approved Concepts
- Lagrangian-Eulerian Graph Neural ODEs: It introduces a novel process-specific mechanism combining Lagrangian infection generation and Eulerian population transport via structured neural ODEs for epidemic forecasting.

### Approved Open Questions
- Identifiability and Adaptation in Epidemic Neural ODEs: Improving identifiability and adaptability under nonstationary interventions is critical for deploying continuous-time neural epidemic models in real-world public health crises where reporting noise and sudden policy shifts are ubiquitous.

### Rejected Candidates
- [concept] LE-EpiGNODE (`le-epignode`) - subcomponent_of_broader_mechanism: Synonymous with or subsumed by the broader framework concept 'lagrangian-eulerian-graph-neural-odes'.

## Links

- [Abstract](https://arxiv.org/abs/2610.21223)
- [PDF](https://arxiv.org/pdf/2610.21223)

