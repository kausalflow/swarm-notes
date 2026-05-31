---
# CSL-compatible fields
title: "Stochastic network epidemic model and particle filter: General framework and application to influenza in Japan"
author:
  - literal: "Ihtisham Ul Haq"
  - literal: "Serge Richard"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29907"

# Custom fields
paper_id: "2605.29907"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:10:50Z"
created_at: "2026-05-31T08:10:50Z"
---

# Stochastic network epidemic model and particle filter: General framework and application to influenza in Japan

**Authors**: Ihtisham Ul Haq, Serge Richard
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29907](https://arxiv.org/abs/2605.29907)

## Summary

This paper introduces a two-dimensional lattice graph model to simulate the stochastic spread of infectious diseases under partial observability. The authors propose a particle filter-based data assimilation framework that enables sequential estimation of hidden system states and unknown parameters. The model is validated on synthetic datasets and applied to real-world influenza surveillance data from Japan, demonstrating its utility for real-time epidemic monitoring and short-term forecasting.

## Key Contributions

- Introduces a two-dimensional lattice graph stochastic epidemic model for infectious disease spread.
- Develops a particle filter (PF) based data assimilation framework for simultaneous state and parameter estimation in partially observed network models.
- Demonstrates the efficacy of the framework for one-week-ahead influenza forecasting in Japan, validated against prefectural data.

## Open Questions & Future Work

- [[dynamic-agent-mobility-epidemic-models]]
- [[flexible-node-connectivity-networks]]

## Archivist Review

The paper presents a specific application of established particle filter methods to a 2D lattice epidemic model. While the empirical results are useful, the core modeling approach is domain-specific and does not introduce a generalized forecasting paradigm or representation that would recur across diverse time-series tasks. Consequently, no new concepts were approved, while the proposed open questions regarding agent mobility and network connectivity limitations were retained as they address fundamental challenges in epidemic modeling.

### Approved Open Questions
- Incorporating Agent Mobility Models: Static models often fail to capture the speed of propagation and the spatial spread of epidemics, especially during sudden surges, which limits the predictive accuracy of the particle filter for real-world scenarios.
- Expanding Lattice Connectivity Dynamics: Lattice-based models are computationally efficient but potentially underestimate the reproduction rate due to restricted neighborhood connectivity, making it vital to find a balance between model complexity and realism.

### Rejected Candidates
- [concept] Two-Dimensional Lattice Graph Stochastic Epidemic Model (`lattice-graph-stochastic-epidemic-model`) - paper_local: This is a specific application-level modeling choice rather than a general-purpose forecasting or representation mechanism.
- [concept] Particle Filter Based Data Assimilation Framework for Epidemic Systems (`pf-data-assimilation-epidemic-framework`) - not_novel: Particle filters are well-established, and this specific implementation is a straightforward application to epidemic modeling without defining a new reusable paradigm.

## Links

- [Abstract](https://arxiv.org/abs/2605.29907)
- [PDF](https://arxiv.org/pdf/2605.29907)

