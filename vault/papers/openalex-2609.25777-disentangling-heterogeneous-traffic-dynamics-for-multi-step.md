---
# CSL-compatible fields
title: "Disentangling Heterogeneous Traffic Dynamics for Multi-Step Traffic Forecasting via Adaptive Spectral Decomposition"
author:
  - literal: "Zijun Huang"
  - literal: "Chenrui Fu"
  - literal: "Wenhao Wang"
  - literal: "Xiaochuan Gou"
  - literal: "Chih‐Chieh Hung"
  - literal: "Guanyao Li"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.25777"

# Custom fields
paper_id: "2609.25777"
paper_source: "openalex"
domain: "time-series"
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
processed_at: "2026-09-25T09:54:50Z"
created_at: "2026-09-25T09:54:50Z"
---

# Disentangling Heterogeneous Traffic Dynamics for Multi-Step Traffic Forecasting via Adaptive Spectral Decomposition

**Authors**: Zijun Huang, Chenrui Fu, Wenhao Wang, Xiaochuan Gou, Chih‐Chieh Hung, Guanyao Li
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.25777](https://arxiv.org/abs/2609.25777)

## Summary

This paper proposes the Adaptive Decomposition Network (ADNet) for multi-step traffic forecasting, which overcomes the limitations of rigid frequency partitioning by introducing a learnable complementary spectral decomposition mechanism. ADNet adaptively disentangles heterogeneous traffic signals into dominant and residual components—allowing each frequency bin to contribute to both via learned proportions—and models them through dedicated spatiotemporal forecasting branches. Experiments on the TraffiDent dataset demonstrate that ADNet outperforms existing approaches, particularly across longer forecasting horizons.

## Key Contributions

- Proposes the Adaptive Decomposition Network (ADNet), a component-specific framework that adaptively disentangles traffic dynamics into dominant and residual components using a learnable complementary spectral decomposition mechanism.
- Replaces hard frequency partitioning with a flexible allocation where every frequency bin contributes to both components with learned proportions optimized jointly with the forecasting objective.
- Demonstrates superior empirical performance on the Alameda and Orange regions of the TraffiDent dataset, achieving top results in 20 out of 24 reported comparisons, especially at longer forecasting horizons.

## Limitations

The evaluation focuses primarily on regional traffic datasets (Alameda and Orange regions of TraffiDent), leaving broader multi-domain time-series applicability as an open area.

## Archivist Review

Applied strict scarcity and novelty filters. The proposed Adaptive Decomposition Network (ADNet) is a paper-specific architecture rather than a broadly reusable foundational concept, so it was rejected to protect knowledge vault quality. No open questions or datasets met the strict standalone criteria.

### Rejected Candidates
- [concept] Adaptive Decomposition Network (ADNet) (`adaptive-decomposition-network-adnet`) - paper_local: This is a paper-specific architecture and model name rather than a reusable standalone mechanism or fundamental conceptual abstraction.

## Links

- [Abstract](https://arxiv.org/abs/2609.25777)
- [PDF](https://arxiv.org/pdf/2609.25777)

