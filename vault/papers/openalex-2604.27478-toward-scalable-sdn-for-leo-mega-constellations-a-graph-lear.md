---
# CSL-compatible fields
title: "Toward Scalable SDN for LEO Mega-Constellations: A Graph Learning Approach"
author:
  - literal: "Sivaram Krishnan"
  - literal: "Bassel Al Homssi"
  - literal: "Zhouyou Gu"
  - literal: "Jihong Park"
  - literal: "Sung-Min Oh"
  - literal: "Jinho Choi"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.27478"

# Custom fields
paper_id: "2604.27478"
paper_source: "openalex"
domain: "nlp"
tags:
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "graph-koopman-autoencoder-gkae"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:27Z"
created_at: "2026-05-03T07:14:27Z"
---

# Toward Scalable SDN for LEO Mega-Constellations: A Graph Learning Approach

**Authors**: Sivaram Krishnan, Bassel Al Homssi, Zhouyou Gu, Jihong Park, Sung-Min Oh, Jinho Choi
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.27478](https://arxiv.org/abs/2604.27478)

## Summary

This paper addresses the scalability challenges of software-defined networking in LEO mega-constellations by proposing a hierarchical framework that manages network dynamics through orbital shells. The core method, a Graph Koopman Autoencoder (GKAE), uses graph neural networks to capture topological information and Koopman theory to linearize complex, nonlinear system dynamics. By forecasting spatio-temporal behavior in a compact linear subspace, the framework enables efficient, globally coordinated control with a reduced computational footprint. Experimental results on Starlink constellation models confirm significant improvements in both compression ratios and forecasting accuracy.

## Key Contributions

- Introduces a hierarchical SDN framework for LEO mega-constellations to manage network control at scale.
- Proposes the Graph Koopman Autoencoder (GKAE) for efficient linearization and spatio-temporal forecasting of constellation dynamics.
- Demonstrates at least 42.8% spatial compression and 10.81% improvement in temporal forecasting accuracy on the Starlink constellation compared to baseline methods.

## Open Questions & Future Work

- [[sdn-controller-placement-optimization]]
- [[heterogeneous-graph-learning-6g-ntn]]

## Key Concepts

- [[graph-koopman-autoencoder-gkae]]: A neural architecture that leverages graph neural networks and Koopman theory to perform linearized spatio-temporal forecasting for large-scale dynamic networks.

## Archivist Review

Approved the Graph Koopman Autoencoder (GKAE) for its novel combination of graph learning and Koopman theory for complex dynamic systems. The two open questions were approved as they address fundamental architectural bottlenecks in scaling SDN for next-generation satellite constellations. The Starlink dataset was rejected as it is a standard domain-specific simulation target rather than a foundational research dataset.

### Approved Concepts
- Graph Koopman Autoencoder (GKAE): The GKAE is the core contribution of the paper, combining graph neural networks and Koopman theory to linearize and compress the spatio-temporal dynamics of satellite mega-constellations.

### Approved Open Questions
- SDN Controller Placement Optimization: This is a critical architectural decision for scalability; choosing the wrong placement can render centralized SDN control infeasible due to extreme control-loop latency or excessive satellite payload requirements.
- Heterogeneous Graph Learning for 6G: As satellite networks become core components of 6G, the inability to model heterogeneous network components as a unified graph will hinder seamless cross-tier resource management and end-to-end performance optimization.

## Links

- [Abstract](https://arxiv.org/abs/2604.27478)
- [PDF](https://arxiv.org/pdf/2604.27478)

