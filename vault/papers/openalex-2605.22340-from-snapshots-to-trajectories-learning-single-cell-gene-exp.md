---
# CSL-compatible fields
title: "From Snapshots to Trajectories: Learning Single-Cell Gene Expression Dynamics via Conditional Flow Matching"
author:
  - literal: "Siyu Pu"
  - literal: "Qingqing Long"
  - literal: "Xiaohan Huang"
  - literal: "Haotian Chen"
  - literal: "Jiajia Wang"
  - literal: "Meng Xiao"
  - literal: "Xiao Luo"
  - literal: "Hengshu Zhu"
  - literal: "Yuanchun Zhou"
  - literal: "Xuezhi Wang"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22340"

# Custom fields
paper_id: "2605.22340"
paper_source: "openalex"
domain: "biology,time-series"
tags:
  - "time-series"
  - "generative-latent-flow-matching"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "coupling-conditioned-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:47:01Z"
created_at: "2026-05-24T07:47:01Z"
---

# From Snapshots to Trajectories: Learning Single-Cell Gene Expression Dynamics via Conditional Flow Matching

**Authors**: Siyu Pu, Qingqing Long, Xiaohan Huang, Haotian Chen, Jiajia Wang, Meng Xiao, Xiao Luo, Hengshu Zhu, Yuanchun Zhou, Xuezhi Wang
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22340](https://arxiv.org/abs/2605.22340)

## Summary

Single-cell Flow Matching (scFM) is a generative framework designed to model continuous cellular gene expression dynamics from sparse, unpaired snapshots. By integrating entropically regularized optimal transport into a flow matching architecture, the model learns temporally coherent velocity fields that mitigate local transition ambiguities. The approach further enforces consistency through bidirectional learning and latent regularization, resulting in superior performance for both trajectory interpolation and long-horizon forecasting.

## Key Contributions

- Introduces scFM, a coupling-conditioned flow matching framework that effectively bridges gaps between unpaired scRNA-seq snapshots.
- Utilizes entropically regularized optimal transport to construct soft, weighted targets for learning robust time-dependent velocity fields.
- Improves temporal coherence and reduces distribution drift in long-horizon trajectory forecasting through bidirectional consistency and latent dynamic regularization.

## Open Questions & Future Work

- [[long-horizon-drift-compounding]]

## Key Concepts

- [[coupling-conditioned-flow-matching]]: A generative modeling approach that uses entropically regularized optimal transport couplings to guide the learning of time-dependent velocity fields.

## Archivist Review

I approved the overarching mechanism (Coupling-Conditioned Flow Matching) instead of the paper-specific framework name (scFM) to ensure higher reusability. I also approved the open question regarding long-horizon drift compounding, as it represents a fundamental challenge in continuous-time generative dynamics modeling rather than a specific paper-local hurdle. I rejected the scFM concept as it is a subcomponent of the broader flow-matching methodology.

### Approved Concepts
- Coupling-Conditioned Flow Matching: The framework addresses the problem of learning continuous dynamics from unpaired snapshots by using optimal transport couplings as soft supervision targets for velocity fields.

### Approved Open Questions
- Compounding Long-Horizon Drift Mitigation: Addressing drift is central to ensuring the reliability of generative dynamics models for temporal forecasting in scientific domains.

### Rejected Candidates
- [concept] Single-cell Flow Matching (scFM) (`single-cell-flow-matching-scfm`) - subcomponent_of_broader_mechanism: Redundant with the overarching method (coupling-conditioned flow matching) and overly domain-specific to single-cell data.

## Links

- [Abstract](https://arxiv.org/abs/2605.22340)
- [PDF](https://arxiv.org/pdf/2605.22340)

