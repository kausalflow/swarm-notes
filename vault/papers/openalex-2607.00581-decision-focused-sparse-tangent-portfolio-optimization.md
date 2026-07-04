---
# CSL-compatible fields
title: "Decision-focused Sparse Tangent Portfolio Optimization"
author:
  - literal: "Haeun Jeon"
  - literal: "Seunghoon Choi"
  - literal: "Hyunglip Bae"
  - literal: "Yongjae Lee"
  - literal: "Woo Chang Kim"
issued:
  date-parts:
    - [2026, 7, 1]
url: "https://arxiv.org/abs/2607.00581"

# Custom fields
paper_id: "2607.00581"
paper_source: "openalex"
domain: "finance,time-series"
tags:
  - "finance"
  - "time-series"
  - "forecasting"
  - "optimization"
  - "decision-focused-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "decision-focused-learning-for-portfolio-optimization"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-04T07:37:39Z"
created_at: "2026-07-04T07:37:39Z"
---

# Decision-focused Sparse Tangent Portfolio Optimization

**Authors**: Haeun Jeon, Seunghoon Choi, Hyunglip Bae, Yongjae Lee, Woo Chang Kim
**Date**: 2026-07-01
**Paper ID**: [openalex:2607.00581](https://arxiv.org/abs/2607.00581)

## Summary

This paper introduces a decision-focused learning framework for sparse tangent portfolio optimization, overcoming the limitations of standard predict-then-optimize approaches. The authors reformulate Sharpe ratio maximization as a DPP-compliant convex programming layer and utilize a smooth top-k operator to enforce exact portfolio cardinality. This integration allows for end-to-end gradient-based training, directly aligning predictive models with downstream portfolio performance. Experiments across four equity markets demonstrate robust improvements in Sharpe ratios over traditional statistical and prediction-centric baselines.

## Key Contributions

- Proposes an end-to-end decision-focused learning framework that integrates portfolio optimization as a differentiable convex layer.
- Replaces discrete cardinality selection with a smooth top-k operator to enable gradient-based training of portfolio selection models.
- Demonstrates superior out-of-sample Sharpe ratios across four major equity market datasets compared to historical and predict-then-optimize baselines.

## Open Questions & Future Work

- [[practical-constraints-in-dfl-portfolio-optimization]]
- [[scalability-of-differentiable-selection-mechanisms]]

## Key Concepts

- [[decision-focused-learning-for-portfolio-optimization]]: An end-to-end learning paradigm that embeds Sharpe ratio maximization as a DPP-compliant convex programming layer, enabling gradient-based alignment between forecasting and portfolio selection.

## Archivist Review

The paper provides a well-defined decision-focused learning framework for finance. I approved the core DFL concept and two substantial open questions regarding the scalability and practical constraint integration of this approach, both of which are central bottlenecks for future research in decision-aware forecasting. No datasets were approved as they were not uniquely defined or central to the paper's novel architectural contribution.

### Approved Concepts
- Decision-focused Learning for Portfolio Optimization: It bridges the gap between predictive accuracy and decision quality by embedding constrained portfolio optimization directly into the model training process via differentiable convex programming.

### Approved Open Questions
- Practical Constraints in DFL: These constraints fundamentally alter the optimal frontier; without them, the utility of DFL-based optimization models in real-world finance is limited.
- Scalability of Differentiable Selection: Computational efficiency is a primary bottleneck for scaling end-to-end learning frameworks to high-dimensional financial datasets.

## Links

- [Abstract](https://arxiv.org/abs/2607.00581)
- [PDF](https://arxiv.org/pdf/2607.00581)

