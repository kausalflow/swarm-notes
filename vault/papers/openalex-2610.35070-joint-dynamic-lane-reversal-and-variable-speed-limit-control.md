---
# CSL-compatible fields
title: "Joint Dynamic Lane Reversal and Variable Speed Limit Control: A Graphormer-Based Approach"
author:
  - literal: "Hamed Araab"
  - literal: "Abbas Ahmadi"
  - literal: "Mohammad Hossein Basiri"
issued:
  date-parts:
    - [2026, 10, 26]
url: "https://arxiv.org/abs/2610.35070"

# Custom fields
paper_id: "2610.35070"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "transformer"
  - "attention-mechanism"
  - "self-attention"
  - "reinforcement-learning"
  - "graph-neural-network"
  - "pre-training"
  - "fine-tuning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "global-endpoint-relation-aware-spatio-temporal-self-attention"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-29T11:12:15Z"
created_at: "2026-10-29T11:12:15Z"
---

# Joint Dynamic Lane Reversal and Variable Speed Limit Control: A Graphormer-Based Approach

**Authors**: Hamed Araab, Abbas Ahmadi, Mohammad Hossein Basiri
**Date**: 2026-10-26
**Paper ID**: [openalex:2610.35070](https://arxiv.org/abs/2610.35070)

## Summary

This paper proposes a graphormer-based approach for joint network-wide dynamic lane allocation and directional speed limit control, leveraging connected and automated vehicles. The method uses an action-resolution algorithm based on graph orientation theory to maintain network strong connectivity during lane reversals, paired with a novel attention mechanism called GERASTSA. Pretrained on action-conditioned traffic forecasting and fine-tuned using proximal policy optimization, the learned policy achieves substantial daily traffic delay reductions on a grid benchmark compared to static configurations and baseline balancers.

## Key Contributions

- Formulates network-wide dynamic lane allocation and directional speed limit control with one-way roads and strong connectivity guarantees using graph orientation theory.
- Introduces Global Endpoint Relation-Aware Spatio-Temporal Self-Attention (GERASTSA) to share representations across all road controllers in a transformer architecture.
- Demonstrates that pretraining on action-conditioned traffic forecasting followed by per-road PPO fine-tuning cuts daily delay by 90% against a fixed configuration on a 6 x 6 grid benchmark.

## Limitations

Variable speed limits added delay in the evaluated scenario, and restricting operation to two-way roads substantially limits performance gains.

## Key Concepts

- [[global-endpoint-relation-aware-spatio-temporal-self-attention]]: A spatio-temporal self-attention mechanism biased by road endpoint relations for joint traffic control in graphormers.

## Archivist Review

Approved the specialized attention mechanism (GERASTSA) as it constitutes a distinct methodological contribution to graph-based spatio-temporal transformers. Rejected the open question as it represents a routine generalization objective without a specific methodological formulation.

### Approved Concepts
- Global Endpoint Relation-Aware Spatio-Temporal Self-Attention: It is the core attention mechanism enabling the graphormer approach to jointly model dynamic lane reversal and variable speed limit control across road-time tokens.

### Rejected Candidates
- [open_question] Cross-Network Transferability in Traffic Control (`cross-network-transferability-traffic-control`) - low_impact: While cross-network transfer is mentioned, it is standard future work for reinforcement learning traffic policies rather than a well-scoped mechanistic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2610.35070)
- [PDF](https://arxiv.org/pdf/2610.35070)

