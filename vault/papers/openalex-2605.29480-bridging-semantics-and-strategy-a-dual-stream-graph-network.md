---
# CSL-compatible fields
title: "Bridging Semantics and Strategy: A Dual-Stream Graph Network for Equitable Negotiation Forecasting"
author:
  - literal: "Moirangthem Tiken Singh"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29480"

# Custom fields
paper_id: "2605.29480"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "graph-neural-network"
  - "multimodal"
  - "negotiation-forecasting"
architectures:
  []
datasets:
  - "DealOrNoDeal"
  - "CaSiNo"
concept_slugs:
  - "semantic-temporal-graph-fusion-network-st-gfn"
dataset_slugs:
  - "dealornodeal"
  - "casino"
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:09:46Z"
created_at: "2026-05-31T08:09:46Z"
---

# Bridging Semantics and Strategy: A Dual-Stream Graph Network for Equitable Negotiation Forecasting

**Authors**: Moirangthem Tiken Singh
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29480](https://arxiv.org/abs/2605.29480)

## Summary

This paper introduces the Semantic-Temporal Graph Fusion Network (ST-GFN), a dual-stream architecture designed for negotiation outcome forecasting by fusing linguistic cues from dialogue and latent strategic constraints from economic state graphs. By utilizing a dynamic gated fusion mechanism, the model adaptively weights these modalities according to the negotiation task structure. Furthermore, the inclusion of a fairness-regularized composite loss function significantly improves the equitable representation of negotiation outcomes without sacrificing predictive accuracy.

## Key Contributions

- Introduced the ST-GFN dual-stream architecture to integrate transformer-based textual features with GAT-based strategic economic state modeling.
- Developed a fairness-regularized composite loss function that reduces Inequality Discrepancy by 43.8% in high-disparity negotiation environments.
- Demonstrated adaptive modality weighting that shifts between linguistic cues and strategic constraints based on task structure (e.g., free-form vs. structured).

## Open Questions & Future Work

- [[dynamic-graph-negotiation-modeling]]

## Key Concepts

- [[semantic-temporal-graph-fusion-network-st-gfn]]: A dual-stream architecture that fuses textual dialogue features with graph-based economic state representations using a dynamic gating mechanism for negotiation forecasting.

## Archivist Review

The Semantic-Temporal Graph Fusion Network is a clear, reusable architectural contribution for multimodal negotiation forecasting. The dataset benchmarks are standard in this domain and provide essential evaluation context. The open question on dynamic relational graph modeling captures a critical research bottleneck in negotiation modeling, while the fairness concept was omitted in favor of focusing on the primary architectural mechanism.

### Approved Concepts
- Semantic-Temporal Graph Fusion Network (ST-GFN): Central dual-stream architecture designed for negotiation forecasting by fusing heterogeneous linguistic and strategic data.

### Approved Open Questions
- Dynamic Relational Graph Modeling: Negotiation is inherently a temporal, multi-turn process where power dynamics and trust evolve; static graphs fail to capture these crucial transitions, limiting the predictive robustness of current systems.

## Datasets

- [[dealornodeal]]
- [[casino]]

## Links

- [Abstract](https://arxiv.org/abs/2605.29480)
- [PDF](https://arxiv.org/pdf/2605.29480)

