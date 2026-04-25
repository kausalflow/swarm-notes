---
# CSL-compatible fields
title: "Vertex misalignment and changepoint localization in network time series"
author:
  - literal: "Tianyi Chen"
  - literal: "Mohammad Sharifi Kiasari"
  - literal: "Sijing Yu"
  - literal: "Youngser Park"
  - literal: "Avanti Athreya"
  - literal: "Vince Lyzinski"
  - literal: "Carey E. Priebe"
  - literal: "Zachary Lubberts"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20072"

# Custom fields
paper_id: "2604.20072"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "euclidean-mirrors"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:14:55Z"
created_at: "2026-04-25T06:14:55Z"
---

# Vertex misalignment and changepoint localization in network time series

**Authors**: Tianyi Chen, Mohammad Sharifi Kiasari, Sijing Yu, Youngser Park, Avanti Athreya, Vince Lyzinski, Carey E. Priebe, Zachary Lubberts
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20072](https://arxiv.org/abs/2604.20072)

## Summary

This paper investigates the critical role of vertex correspondence in changepoint localization for network time series. The authors demonstrate that vertex misalignment can significantly impede detection, particularly when changepoint information is embedded in joint distributions of latent positions. Through analysis of two model classes, they show that standard approaches like graph matching and optimal transport are insufficient to recover performance in these cases, highlighting the need for methods that account for the interplay of marginal and joint information.

## Key Contributions

- Analyzes the impact of vertex misalignment on the ability to detect changepoints in dynamic network time series.
- Demonstrates that the detectability of changepoints depends on whether information resides in the marginal or joint distributions of latent vertex positions.
- Proves that for certain network models, performance degradation caused by vertex misalignment is irreducible via graph matching or optimal transport techniques.

## Open Questions & Future Work

- [[mixed-marginal-joint-changepoint-modeling]]
- [[principled-dissimilarity-selection]]

## Key Concepts

- [[euclidean-mirrors]]: A statistical procedure for changepoint localization in dynamic networks that maps latent position processes into finite-dimensional representations.

## Archivist Review

The paper offers a sophisticated framework for analyzing changepoints in dynamic graphs. I approved the 'Euclidean mirrors' concept as it represents a distinct, reusable methodology for network time-series analysis. The open questions were refined to target the fundamental unresolved problem of signal distribution (marginal vs. joint) and the theoretical selection of dissimilarity metrics, which are essential for future research in network inference.

### Approved Concepts
- Euclidean mirrors: It serves as a novel, modern statistical framework for changepoint localization in latent position processes, providing a formal alternative to standard degree-based statistics.

### Approved Open Questions
- Modeling mixed changepoint information: This is critical for bridging the gap between theoretical models and real-world empirical network data where vertex correspondence is rarely known perfectly.
- Principled dissimilarity selection framework: Establishing a principled selection criterion is necessary for the consistent and robust application of mirrors in dynamic network inference.

## Links

- [Abstract](https://arxiv.org/abs/2604.20072)
- [PDF](https://arxiv.org/pdf/2604.20072)

