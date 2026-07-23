---
# CSL-compatible fields
title: "Feature Attribution-Based Explainability Analysis of Deep Learning Models in Predictive Process Monitoring"
author:
  - literal: "Kseniya Sahatova"
  - literal: "Rafael S. Oyamada"
  - literal: "Xuefei Lu"
  - literal: "Johannes De Smedt"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.17783"

# Custom fields
paper_id: "2607.17783"
paper_source: "openalex"
domain: "nlp"
tags:
  - "explainability"
  - "interpretability"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:52Z"
created_at: "2026-07-23T07:27:52Z"
---

# Feature Attribution-Based Explainability Analysis of Deep Learning Models in Predictive Process Monitoring

**Authors**: Kseniya Sahatova, Rafael S. Oyamada, Xuefei Lu, Johannes De Smedt
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.17783](https://arxiv.org/abs/2607.17783)

## Summary

Deep learning models in predictive process monitoring achieve high predictive performance but lack interpretability due to their black-box nature, while existing event-level and aggregated attribution methods face trade-offs between computational cost and fidelity to control-flow dynamics. To resolve this dilemma, the authors propose a control-flow-aware segmentation method that partitions traces into meaningful segments and computes segment-level SHAP explanations. Evaluation on synthetic event logs and real-world municipal and loan application processes demonstrates that the approach accurately identifies influential trace segments and steering change points.

## Key Contributions

- Proposes a local post-hoc explainability method using control-flow-aware segmentation for deep learning models in predictive process monitoring.
- Enables segment-level SHAP explanations that balance computational complexity and the representation of underlying control-flow dynamics in long event logs.
- Demonstrates the effectiveness of the proposed segmentation method on synthetic event logs with verifiable change points as well as real-world loan application and municipal administrative processes.

## Archivist Review

Applied strict selection rules. The proposed concept of control-flow-aware segmentation for process monitoring explainability is too narrow and domain-specific to process logs to recur widely across general time-series forecasting or ML literature. The sole open question is standard boilerplate future work proposing an extension to multi-class outcomes without offering a technical mechanism or bottleneck analysis.

### Rejected Candidates
- [open_question] Extending Explainability Beyond Binary Outcomes (`extending-explainability-beyond-binary-outcome-prediction`) - weak_evidence: Boilerplate future work suggesting extension to non-binary tasks without a specific methodological mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2607.17783)
- [PDF](https://arxiv.org/pdf/2607.17783)

