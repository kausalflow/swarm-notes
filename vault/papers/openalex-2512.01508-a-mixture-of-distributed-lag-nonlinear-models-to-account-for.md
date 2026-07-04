---
# CSL-compatible fields
title: "A Mixture of Distributed Lag Non‐Linear Models to Account for Spatially Heterogeneous Exposure‐Lag‐Response Associations"
author:
  - literal: "Álvaro Briz‐Redón"
  - literal: "Ana Corberán‐Vallet"
  - literal: "Adina Iftimi"
  - literal: "Carmen Íñiguez"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2512.01508"

# Custom fields
paper_id: "2512.01508"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dlnm-clust"
dataset_slugs:
  []
skill: "GeneralMLSkill"
processed_at: "2026-07-04T07:37:46Z"
created_at: "2026-07-04T07:37:46Z"
---

# A Mixture of Distributed Lag Non‐Linear Models to Account for Spatially Heterogeneous Exposure‐Lag‐Response Associations

**Authors**: Álvaro Briz‐Redón, Ana Corberán‐Vallet, Adina Iftimi, Carmen Íñiguez
**Date**: 2026-07-01
**Paper ID**: [openalex:2512.01508](https://arxiv.org/abs/2512.01508)

## Summary

This paper addresses the common assumption of spatial homogeneity in environmental epidemiology by proposing DLNM-Clust, a Bayesian mixture model extending the traditional Distributed Lag Non-Linear Model (DLNM). By probabilistically assigning geographic units to latent clusters, the model captures complex, non-linear exposure-lag-response surfaces that vary spatially. The approach is validated on municipality-level data, demonstrating improved accuracy in capturing health risks compared to standard homogeneous methods.

## Key Contributions

- Introduces DLNM-Clust, a Bayesian mixture model that enables geographic units to follow distinct exposure-lag-response associations based on latent spatial clusters.
- Addresses spatial bias inherent in traditional homogeneous Distributed Lag Non-Linear Model (DLNM) applications in environmental epidemiology.
- Demonstrates the method's effectiveness in capturing region-specific air pollution health risks using municipality-level COVID-19 data in Belgium.

## Open Questions & Future Work

- [[computational-efficiency-bayesian-mixture-models]]
- [[automated-cluster-number-selection]]

## Key Concepts

- [[dlnm-clust]]: A mixture model for environmental epidemiology that assigns geographic units to latent clusters, each with a distinct distributed lag non-linear model specification.

## Archivist Review

The approved concepts and questions focus on the methodological novelty of the mixture-based DLNM and the specific computational/selection bottlenecks encountered when applying Bayesian mixture models to spatiotemporal epidemiology. I have refined the open question titles for greater precision and alignment with the existing vault.

### Approved Concepts
- DLNM-Clust: It addresses the limitation of homogeneous exposure-lag-response associations in traditional DLNMs by allowing spatial heterogeneity through latent cluster assignment.

### Approved Open Questions
- Efficiency of Bayesian Mixture Inference: Computational efficiency is a major bottleneck for the practical, large-scale deployment of high-dimensional Bayesian mixture models in environmental health surveillance.
- Automated Cluster Count Selection: Automating cluster count selection is critical for reducing researcher bias and improving the robustness of model selection in complex environmental epidemiology.

## Links

- [Abstract](https://arxiv.org/abs/2512.01508)
- [PDF](https://arxiv.org/pdf/2512.01508)

