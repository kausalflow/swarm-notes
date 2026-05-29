---
# CSL-compatible fields
title: "Topological Signatures of Imperial Stress: Persistent Homology of the Eastern Mediterranean Trade Network, 0--400 CE"
author:
  - literal: "José de Jesús Bernal Alvarado"
  - literal: "David Delepine"
  - literal: "Carlos Pinedo Guadarrama"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.27200"

# Custom fields
paper_id: "2605.27200"
paper_source: "openalex"
domain: "graph-learning, history"
tags:
  - "graph-neural-network"
  - "time-series"
  - "dataset"
  - "evaluation"
architectures:
  []
datasets:
  - "ORBIS Geospatial Network Model of the Roman World"
concept_slugs:
  - "persistent-homology-for-network-resilience-analysis"
dataset_slugs:
  - "orbis-geospatial-network-model-of-the-roman-world"
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:39:55Z"
created_at: "2026-05-29T08:39:55Z"
---

# Topological Signatures of Imperial Stress: Persistent Homology of the Eastern Mediterranean Trade Network, 0--400 CE

**Authors**: José de Jesús Bernal Alvarado, David Delepine, Carlos Pinedo Guadarrama
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.27200](https://arxiv.org/abs/2605.27200)

## Summary

This paper uses persistent homology to quantify the structural resilience of the Eastern Mediterranean trade network within the ORBIS Geospatial Network Model between 0 and 400 CE. By constructing a differential friction model that incorporates historical events like epidemics and military conflict, the authors generate a decadal time series of network topologies. Their findings reveal three distinct historical phases characterized by Betti number ($β_1$) persistent entropy, showing that topology detects stress patterns not visible in traditional economic indices.

## Key Contributions

- Demonstrates that persistent homology of the ORBIS network identifies three structurally distinct phases in Roman Mediterranean trade resilience.
- Introduces a differential friction model that maps historical perturbations (epidemics, civil wars) onto static infrastructure to generate dynamic network snapshots.
- Provides empirical evidence that the Eastern Mediterranean network experienced irreversible structural decline starting in the 290-400 CE period, distinct from earlier recoverable crisis phases.

## Open Questions & Future Work

- [[geospatial-data-density-bias-in-historical-networks]]

## Key Concepts

- [[persistent-homology-for-network-resilience-analysis]]: A methodology for quantifying network structural resilience by applying persistent homology to time-varying snapshots of geospatial trade networks under historical perturbation.

## Archivist Review

I have approved the core methodological contribution of using persistent homology for network resilience analysis and the critical dataset used in the study. I also identified the data-density disparity as a significant research bottleneck, generalizing the authors' observation about Western network coverage into a broader question about geospatial data-density bias in network-based history. I rejected the local candidates in favor of these more general formulations.

### Approved Concepts
- Persistent Homology for Network Resilience Analysis: It bridges topological data analysis with network infrastructure modeling to identify latent resilience phases that traditional aggregate indicators often miss.

### Approved Open Questions
- Geospatial Density Bias Analysis: This is a fundamental data-fidelity bottleneck that prevents comparative cross-regional validation of resilience-based historical findings.

### Rejected Candidates
- [concept] Persistent Homology for Trade Network Resilience (`persistent-homology-for-trade-network-resilience`) - other: Renamed to be more general and abstract for better vault utility.
- [open_question] Western Network Topological Coverage (`western-network-topological-coverage`) - other: Renamed to describe the broader methodological bottleneck rather than a specific region.

## Datasets

- [[orbis-geospatial-network-model-of-the-roman-world]]

## Links

- [Abstract](https://arxiv.org/abs/2605.27200)
- [PDF](https://arxiv.org/pdf/2605.27200)

