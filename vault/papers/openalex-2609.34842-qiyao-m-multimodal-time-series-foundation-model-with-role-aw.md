---
# CSL-compatible fields
title: "QiYao-M: Multimodal Time Series Foundation Model with Role-Aware Modeling of Endogenous and Exogenous Modalities"
author:
  - literal: "Hanyin Cheng"
  - literal: "Linfeng Wang"
  - literal: "Zhengbo Qu"
  - literal: "Yang Shu"
  - literal: "Zhongwen Rao"
  - literal: "Meng Wang"
  - literal: "Yijie Li"
  - literal: "Xin Jiang"
  - literal: "Bin Yang"
  - literal: "Chenjuan Guo"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34842"

# Custom fields
paper_id: "2609.34842"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "foundation-model"
  - "pre-training"
architectures:
  []
datasets:
  []
concept_slugs:
  - "qiyao-m"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:08Z"
created_at: "2026-09-30T10:49:08Z"
---

# QiYao-M: Multimodal Time Series Foundation Model with Role-Aware Modeling of Endogenous and Exogenous Modalities

**Authors**: Hanyin Cheng, Linfeng Wang, Zhengbo Qu, Yang Shu, Zhongwen Rao, Meng Wang, Yijie Li, Xin Jiang, Bin Yang, Chenjuan Guo
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34842](https://arxiv.org/abs/2609.34842)

## Summary

Existing multimodal time series foundation models often treat heterogeneous modalities with shared mechanisms, ignoring the distinct predictive roles of endogenous versus exogenous variables. To address this, the authors propose QiYao-M, which models endogenous and exogenous modalities separately via specialized predictors and retrieval enhancers. Extensive experiments demonstrate superior forecasting performance across various unimodal and multimodal scenarios.

## Key Contributions

- Proposes QiYao-M, a role-aware multimodal time series foundation model that models endogenous and exogenous modalities separately.
- Introduces an Endo-Multimodal Predictor and Endo-Multimodal Supervision to capture temporal dynamics and evolution for endogenous modalities.
- Proposes an Exo-Multimodal Retrieval Enhancer and Endo-Modality Proxy Training to enable cross-domain downstream adaptation under exo-multimodal data scarcity.

## Open Questions & Future Work

- [[role-aware-multimodal-fusion-asymmetry]]

## Key Concepts

- [[qiyao-m]]: A role-aware multimodal time series foundation model that models endogenous and exogenous modalities separately.

## Archivist Review

Approved the central multimodal time series foundation model architecture concept (QiYao-M) and its corresponding open question regarding asymmetric multimodal fusion. Subcomponents and paper-local training proxy routines were rejected to maintain high vault selectivity.

### Approved Concepts
- QiYao-M: QiYao-M introduces a role-aware multimodal time series foundation model that separates endogenous and exogenous modality modeling.

### Approved Open Questions
- Asymmetric Modeling of Multimodal Time Series: Crucial for building truly generalized multimodal foundation models that do not require specialized, decoupled pathways for internal versus external signals.

### Rejected Candidates
- [concept] Endo-Modality Proxy Training (`endo-modality-proxy-training`) - subcomponent_of_broader_mechanism: Subcomponent of the broader QiYao-M model framework.

## Links

- [Abstract](https://arxiv.org/abs/2609.34842)
- [PDF](https://arxiv.org/pdf/2609.34842)

