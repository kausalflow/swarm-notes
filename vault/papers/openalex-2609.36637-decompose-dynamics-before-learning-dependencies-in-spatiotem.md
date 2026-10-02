---
# CSL-compatible fields
title: "Decompose Dynamics Before Learning Dependencies in Spatiotemporal Systems"
author:
  - literal: "Ziqi Wang"
  - literal: "Deqing Hu"
  - literal: "Cheng Bao"
  - literal: "Zhiwei Ling"
  - literal: "Wenzhuo Qian"
  - literal: "Jiahui Zhai"
  - literal: "Hailiang Zhao"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36637"

# Custom fields
paper_id: "2609.36637"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "spatiotemporal"
  - "graph-neural-network"
  - "representation-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "component-aware-network-dynamics-with-ordered-relations-candor"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:48:19Z"
created_at: "2026-10-02T10:48:19Z"
---

# Decompose Dynamics Before Learning Dependencies in Spatiotemporal Systems

**Authors**: Ziqi Wang, Deqing Hu, Cheng Bao, Zhiwei Ling, Wenzhuo Qian, Jiahui Zhai, Hailiang Zhao
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36637](https://arxiv.org/abs/2609.36637)

## Summary

The paper introduces Component-Aware Network Dynamics with Ordered Relations (CANDOR), a spatiotemporal forecasting framework that decouples local dynamics into distinct components—persistent background, gradual accumulation and release, and sparse shocks—before modeling node dependencies. By conditioning specialized physical and functional branches on these decomposed components, CANDOR effectively captures both directed propagation and latent dependencies. Experiments across urban traffic and river water-quality datasets demonstrate significant improvements over existing state-of-the-art baselines.

## Key Contributions

- Introduces Component-Aware Network Dynamics with Ordered Relations (CANDOR), a spatiotemporal representation learning framework that decomposes local dynamics before learning dependencies.
- Implements a delay-aware physical branch and a topology-unconstrained functional branch conditioned on decomposed components (persistent background, accumulation/release, sparse shocks).
- Achieves up to 4.31% MAE reduction on traffic benchmarks and up to 5.47% MSE reduction on water-quality forecasting datasets.

## Open Questions & Future Work

- [[dynamics-decomposition-dependency-learning]]

## Key Concepts

- [[component-aware-network-dynamics-with-ordered-relations-candor]]: A spatiotemporal forecasting framework that decomposes local dynamics before learning structural and functional dependencies.

## Archivist Review

Approved the overarching CANDOR framework concept and the primary open question regarding dynamics decomposition for dependency learning, following strict scarcity and novelty guidelines. No named datasets were present in the abstract text.

### Approved Concepts
- Component-Aware Network Dynamics with Ordered Relations (CANDOR): CANDOR introduces the novel core principle of decomposing local dynamics into persistent background, accumulation/release, and sparse shocks before learning dependencies.

### Approved Open Questions
- Dynamics Decomposition for Dependency Learning: Understanding how local dynamics decomposition guides relation learning is central to advancing principled spatiotemporal modeling and representation learning.

## Links

- [Abstract](https://arxiv.org/abs/2609.36637)
- [PDF](https://arxiv.org/pdf/2609.36637)

