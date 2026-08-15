---
# CSL-compatible fields
title: "JAPE: Joint Anomaly Prediction and Intrinsic Explanation in Multivariate Time Series"
author:
  - literal: "Yian Wei"
  - literal: "Yuanyuan Yao"
  - literal: "Lu Chen"
  - literal: "Xiangmin Zhou"
  - literal: "Tianyi Li"
issued:
  date-parts:
    - [2026, 8, 12]
url: "https://arxiv.org/abs/2608.11801"

# Custom fields
paper_id: "2608.11801"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
  - "spatio-temporal"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-15T05:14:54Z"
created_at: "2026-08-15T05:14:54Z"
---

# JAPE: Joint Anomaly Prediction and Intrinsic Explanation in Multivariate Time Series

**Authors**: Yian Wei, Yuanyuan Yao, Lu Chen, Xiangmin Zhou, Tianyi Li
**Date**: 2026-08-12
**Paper ID**: [openalex:2608.11801](https://arxiv.org/abs/2608.11801)

## Summary

Multivariate time-series anomaly prediction often struggles with weak precursors when modeled purely as numerical deviations and lacks native interpretability. To address this, the authors introduce JAPE, a joint framework that shifts anomaly prediction to dependency-structure modeling. JAPE features a Decoupled Spatio-Temporal Representation (DSTR) backbone for lag-aware dependency capture, a dual-view alerting mechanism combining numerical and structural views, and Native Predictive Explanation (NPE) for variable ranking. Extensive experiments on five real-world benchmarks show significant performance gains in prediction accuracy and explainability.

## Key Contributions

- Proposes JAPE, a joint anomaly prediction and intrinsic explanation framework that shifts multivariate time-series anomaly prediction from numerical deviation modeling to dependency structure modeling.
- Introduces a Decoupled Spatio-Temporal Representation (DSTR) backbone with learnable lag aggregation to capture structural precursors before numerical deviations emerge.
- Designs a dual-view alerting mechanism fusing numerical forecasts and evolving dependency graphs, alongside Native Predictive Explanation (NPE) for variable-level ranking without additional training.
- Demonstrates improvements of 19.7% in average F1 and 41.3% in AUC-PR across five real-world benchmarks, with a 26.6% gain in MRR for explainability.

## Archivist Review

Reviewed candidates against vault standards. The proposed concepts and open questions represent paper-internal components or boilerplate future work rather than standalone, highly reusable primitives or profound conceptual bottlenecks. Therefore, no items were approved.

### Rejected Candidates
- [concept] Decoupled Spatio-Temporal Representation DSTR (`decoupled-spatio-temporal-representation-dstr`) - subcomponent_of_broader_mechanism: Paper-internal backbone architecture combining standard decoupled temporal-spatial modeling and lag aggregation, lacking broad standalone reusability outside this framework.
- [concept] Native Predictive Explanation NPE (`native-predictive-explanation-npe`) - not_reusable: A task-specific explanation heuristic for reusing predicted graphs in this particular model rather than a general methodological primitive.
- [open_question] Scaling and Adapting Dependency Graph Forecasting (`scaling-and-adapting-dependency-graphs-for-time-series`) - weak_evidence: Generic future work regarding scaling graph-based models to larger systems and continual learning.

## Links

- [Abstract](https://arxiv.org/abs/2608.11801)
- [PDF](https://arxiv.org/pdf/2608.11801)

