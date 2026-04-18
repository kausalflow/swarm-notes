---
# CSL-compatible fields
title: "Deepbullwhip: An Open-Source Simulation and Benchmarking for Multi-Echelon Bullwhip Analyses"
author:
  - literal: "Mansur M. Arief"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13478"

# Custom fields
paper_id: "2604.13478"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "dataset"
  - "time-series"
architectures:
  []
datasets:
  - "WSTS semiconductor billings"
concept_slugs:
  - "deepbullwhip"
dataset_slugs:
  - "wsts-semiconductor-billings"
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:07:27Z"
created_at: "2026-04-18T06:07:27Z"
---

# Deepbullwhip: An Open-Source Simulation and Benchmarking for Multi-Echelon Bullwhip Analyses

**Authors**: Mansur M. Arief
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13478](https://arxiv.org/abs/2604.13478)

## Summary

Deepbullwhip is an open-source framework designed to address computational barriers in multi-echelon inventory research by providing modular simulation and standardized benchmarking for bullwhip effects. The system features a highly efficient, vectorized Monte Carlo engine that enables rapid exploration of complex supply chain dynamics and policy tradeoffs. By integrating a registry of ordering policies and datasets, the framework facilitates rigorous, reproducible comparisons of mitigation strategies that were previously hindered by fragmented methodologies. Experiments demonstrate that real-world demand patterns, such as those from WSTS, yield significantly different bullwhip severities compared to synthetic benchmarks, highlighting the importance of the proposed standardized evaluation approach.

## Key Contributions

- Introduces deepbullwhip, an open-source Python package for multi-echelon supply chain simulation with a vectorized Monte Carlo engine achieving 50-90x speedup.
- Establishes a registry-based benchmarking framework including six standardized bullwhip metrics and a library of demand datasets and ordering policies.
- Demonstrates scalability and bullwhip severity disparities through experiments on semiconductor supply chains, revealing a 155x bullwhip difference between synthetic and real-world demand data.

## Open Questions & Future Work

- [[benchmarking-non-serial-topologies]]
- [[multivariate-demand-generation]]

## Key Concepts

- [[deepbullwhip]]: An open-source simulation and benchmarking framework for multi-echelon supply chain bullwhip analyses.

## Archivist Review

The framework 'Deepbullwhip' and its primary dataset are approved as they address a core bottleneck in supply chain inventory research by providing modularized, high-speed simulation and standardized benchmarking. The open questions regarding non-serial topology and multivariate demand represent substantive research frontiers beyond the current scope of the software. I maintained high selectivity by ensuring no subcomponents or minor features were included.

### Approved Concepts
- Deepbullwhip: It provides a standardized, modular infrastructure for simulating and benchmarking bullwhip effects across multi-echelon supply chains.

### Approved Open Questions
- Benchmarking Non-Serial Supply Chains: Multi-echelon supply chains in industry are rarely perfectly serial; therefore, validating the framework's robustness across arbitrary DAG topologies is crucial for practical applicability.
- Multi-Product Demand Modeling: Real-world demand is often correlated across products; ignoring this correlation limits the accuracy of bullwhip analyses in realistic multi-SKU inventory environments.

## Datasets

- [[wsts-semiconductor-billings]]

## Links

- [Abstract](https://arxiv.org/abs/2604.13478)
- [PDF](https://arxiv.org/pdf/2604.13478)

