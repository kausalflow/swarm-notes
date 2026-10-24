---
# CSL-compatible fields
title: "RadioDreamer: A World Model for Radio Map Forecasting and Imagination-Based Optimization"
author:
  - literal: "Haoye Chai"
  - literal: "Mugen Peng"
issued:
  date-parts:
    - [2026, 10, 21]
url: "https://arxiv.org/abs/2610.29382"

# Custom fields
paper_id: "2610.29382"
paper_source: "openalex"
domain: "reinforcement-learning"
tags:
  - "transformer"
  - "reinforcement-learning"
  - "autonomous-agent"
  - "planning"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "radiodreamer"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-24T09:12:10Z"
created_at: "2026-10-24T09:12:10Z"
---

# RadioDreamer: A World Model for Radio Map Forecasting and Imagination-Based Optimization

**Authors**: Haoye Chai, Mugen Peng
**Date**: 2026-10-21
**Paper ID**: [openalex:2610.29382](https://arxiv.org/abs/2610.29382)

## Summary

RadioDreamer is a two-stage world model that unifies action-conditioned radio-map forecasting and imagination-based network optimization within a latent space. Using a structured spatio-temporal transformer backbone with dynamic-region supervision, the model learns causal environmental transitions from sequential interactions to predict radio map evolution. Through counterfactual latent trajectory planning, RadioDreamer reduces full-map forecasting error by 25.2% and outperforms model-free policies by 8.8% in accumulated return for long-horizon network optimization.

## Key Contributions

- Introduces RadioDreamer, a two-stage world model unifying action-conditioned radio-map forecasting and imagination-based network optimization within a latent space.
- Employs a structured spatio-temporal transformer backbone with dynamic-region supervision to model action-sensitive areas and causal environmental transitions.
- Reduces full-map forecasting error by 25.2% on average and achieves ~80% accuracy in predicting radio signal evolution direction.
- Surpasses model-free policies by 8.8% in accumulated return for long-horizon network configuration via imagination-based planning.

## Open Questions & Future Work

- [[real-world-multiscene-world-models]]

## Key Concepts

- [[radiodreamer]]: A two-stage world model for action-conditioned radio map forecasting and imagination-based network optimization.

## Archivist Review

Approved RadioDreamer as a central world-model framework for radio map forecasting and imagination-based optimization, along with the corresponding open question on real-world multi-scene scaling. Rejected the internal supervision submodule as a subcomponent of the broader mechanism.

### Approved Concepts
- RadioDreamer: It introduces a novel world model architecture unifying action-conditioned forecasting and imagination-based optimization for radio maps.

### Approved Open Questions
- Real-World Multi-Scene World Models: Extending world models from simulation to real-world deployment with multi-scene generalization is crucial for practical wireless network automation and management.

### Rejected Candidates
- [concept] Dynamic-Region Supervision (`dynamic-region-supervision`) - subcomponent_of_broader_mechanism: Paper-internal subcomponent used within RadioDreamer.

## Links

- [Abstract](https://arxiv.org/abs/2610.29382)
- [PDF](https://arxiv.org/pdf/2610.29382)

