---
# CSL-compatible fields
title: "Graph Neural ODE Digital Twins for Control-Oriented Reactor Thermal-Hydraulic Forecasting Under Partial Observability"
author:
  - literal: "Akzhol Almukhametov"
  - literal: "Doyeong Lim"
  - literal: "Rui Hu"
  - literal: "Yang Liu"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.07292"

# Custom fields
paper_id: "2604.07292"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "graph-neural-network"
  - "forecasting"
  - "physics-informed-machine-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "gnn-ode-digital-twin"
  - "topology-guided-missing-node-initialization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:05Z"
created_at: "2026-04-11T05:55:05Z"
---

# Graph Neural ODE Digital Twins for Control-Oriented Reactor Thermal-Hydraulic Forecasting Under Partial Observability

**Authors**: Akzhol Almukhametov, Doyeong Lim, Rui Hu, Yang Liu
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.07292](https://arxiv.org/abs/2604.07292)

## Summary

This paper presents a GNN-ODE surrogate model designed for real-time thermal-hydraulic forecasting in advanced reactors. The model represents the reactor as a directed sensor graph, using message passing to encode hydraulic connectivity and Neural ODEs to evolve latent dynamics in continuous time. It addresses partial observability through a topology-guided missing-node initializer and demonstrates high accuracy in predicting uninstrumented states. The surrogate is validated on simulated transients and experimental facility data, exhibiting efficient inference speed and consistency with physical correlations.

## Key Contributions

- Proposes a GNN-ODE hybrid architecture for real-time thermal-hydraulic state forecasting in nuclear reactor systems.
- Demonstrates state reconstruction of uninstrumented locations with R^2 up to 0.995 using a topology-guided initializer.
- Achieves 105x real-time inference speed, enabling efficient ensemble uncertainty quantification.
- Validates sim-to-real transfer via discriminative fine-tuning, successfully recovering physical heat-transfer correlations.

## Open Questions & Future Work

- [[noise-mitigation-in-online-ode-surrogates]]
- [[topology-transfer-of-graph-surrogates]]

## Key Concepts

- [[gnn-ode-digital-twin]]: A hybrid architecture that integrates graph-structured spatial message passing with continuous-time latent dynamics governed by Neural ODEs.
- [[topology-guided-missing-node-initialization]]: A technique that uses system graph topology to learn and infer the states of unobserved or missing nodes.

## Archivist Review

I have approved the core architectural concept (GNN-ODE Digital Twin) and its specific mechanism for handling partial observability (Topology-guided Missing-node Initialization), as both are highly reusable for spatiotemporal modeling. The approved open questions focus on the two most significant deployment challenges for this class of models: numerical stability under sensor noise and the transferability of learned spatial priors across different system topologies. Standard ML terms were rejected in favor of domain-specific mechanisms.

### Approved Concepts
- GNN-ODE Digital Twin: This architecture provides a scalable way to model complex spatiotemporal dynamics in systems with graph-structured connectivity, facilitating continuous-time forecasting for digital twins.
- Topology-guided Missing-node Initialization: Addresses the fundamental challenge of inferring latent/unobserved states in graph-structured systems, which is critical for real-world deployment where sensor coverage is partial.

### Approved Open Questions
- Noise Mitigation for ODE Surrogates: This is a critical bottleneck for the practical deployment of Neural ODE-based surrogates in noisy, real-world operational environments.
- Topology Transfer of Graph Surrogates: Establishing topology transfer capability is essential for scaling digital twins across different industrial designs and reducing the dependency on expensive, facility-specific experimental campaigns.

## Links

- [Abstract](https://arxiv.org/abs/2604.07292)
- [PDF](https://arxiv.org/pdf/2604.07292)

