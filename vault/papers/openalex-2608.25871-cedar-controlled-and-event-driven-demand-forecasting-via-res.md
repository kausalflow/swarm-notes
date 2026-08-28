---
# CSL-compatible fields
title: "CEDAR: Controlled and Event-Driven Demand Forecasting via Residual Decomposition"
author:
  - literal: "Junjie Meng"
  - literal: "Ranxu Zhang"
  - literal: "Zi-an Zhang"
  - literal: "Shujun Liu"
  - literal: "Xiaoning Qi"
  - literal: "Xiaozhou Xu"
  - literal: "Yanyong Zhang"
  - literal: "Hui Xiong"
  - literal: "Chao Wang"
issued:
  date-parts:
    - [2026, 8, 26]
url: "https://arxiv.org/abs/2608.25871"

# Custom fields
paper_id: "2608.25871"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "llm"
  - "multimodal"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "cedar"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-28T16:59:33Z"
created_at: "2026-08-28T16:59:33Z"
---

# CEDAR: Controlled and Event-Driven Demand Forecasting via Residual Decomposition

**Authors**: Junjie Meng, Ranxu Zhang, Zi-an Zhang, Shujun Liu, Xiaoning Qi, Xiaozhou Xu, Yanyong Zhang, Hui Xiong, Chao Wang
**Date**: 2026-08-26
**Paper ID**: [openalex:2608.25871](https://arxiv.org/abs/2608.25871)

## Summary

This paper introduces CEDAR, a two-stage framework for controlled and event-driven demand forecasting in large-scale e-commerce marketplaces to support active planning rather than passive prediction. In Stage I, an Action-Interleaved Transformer models controllable action-conditioned state transitions to support counterfactual rollouts under planned interventions. In Stage II, a Residual Correction Module aligns external event signals and LLM-assisted text representations to correct event-driven deviations. Experiments on a large-scale industrial dataset from Alibaba 1688 demonstrate superior simulation accuracy and practical utility for budget planning.

## Key Contributions

- Proposes CEDAR, a two-stage controlled and event-driven demand forecasting framework that decouples endogenous market evolution from decision-induced transitions.
- Introduces an Action-Interleaved Transformer in Stage I to learn controllable action-conditioned state transitions for rollout under planned interventions.
- Implements a Residual Correction Module in Stage II leveraging external event signals and LLM-assisted text representations to correct event-driven deviations.
- Demonstrates consistent improvements in simulation accuracy over strong TSF baselines and delivers practical gains for real-world budget planning on Alibaba 1688.

## Limitations

Future work could explore expanding the residual correction module to handle broader, unstructured multi-modal event streams across different industry domains.

## Open Questions & Future Work

- [[causal-disentanglement-counterfactual-rollouts]]

## Key Concepts

- [[cedar]]: A two-stage decision-conditioned forecasting framework featuring an Action-Interleaved Transformer and a Residual Correction Module for e-commerce demand simulation under planned interventions.

## Archivist Review

Approved the core conceptual framework CEDAR for decision-conditioned demand forecasting and the open question on causal disentanglement in counterfactual rollouts. Industrial proprietary datasets were correctly excluded from vault entry as per policy.

### Approved Concepts
- CEDAR: It introduces a novel two-stage framework combining action-interleaved transformers and residual correction for decision-conditioned demand forecasting.

### Approved Open Questions
- Causal Disentanglement in Counterfactual Rollouts: Important for bridging offline sequence modeling with rigorous causal inference in dynamic, intervention-driven environments.

## Links

- [Abstract](https://arxiv.org/abs/2608.25871)
- [PDF](https://arxiv.org/pdf/2608.25871)

