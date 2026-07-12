---
# CSL-compatible fields
title: "CAAD: Causality-Aware Multivariate Time Series Anomaly Detection via Multi-Scale Alignment and Structural Causal Consistency"
author:
  - literal: "Xin Wang"
  - literal: "Yunshi Wen"
  - literal: "Y He"
  - literal: "Haotian Xu"
  - literal: "Youlan Zhao"
  - literal: "M J Haddad"
  - literal: "Ma Tc"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08555"

# Custom fields
paper_id: "2607.08555"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "caad-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:24:22Z"
created_at: "2026-07-12T07:24:22Z"
---

# CAAD: Causality-Aware Multivariate Time Series Anomaly Detection via Multi-Scale Alignment and Structural Causal Consistency

**Authors**: Xin Wang, Yunshi Wen, Y He, Haotian Xu, Youlan Zhao, M J Haddad, Ma Tc
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08555](https://arxiv.org/abs/2607.08555)

## Summary

CAAD is a multivariate time-series anomaly detection framework that shifts focus from temporal pattern similarity to the preservation of internal causal relationships. By modeling exogenous variables as residuals and utilizing multi-scale alignment, the framework detects anomalies as significant disruptions in Granger causality consistency. A gradient-based matrix further enables the precise monitoring of structural topological changes, leading to high-precision detection of subtle, intervention-based system failures.

## Key Contributions

- Introduces CAAD, a novel anomaly detection framework that reframes the task as the continuous verification of Granger causality consistency.
- Utilizes multi-scale alignment for internalizing system dynamics combined with a gradient-based matrix to detect causal relationship breakdowns.
- Demonstrates superior performance over state-of-the-art baselines on complex industrial system anomaly detection tasks.

## Open Questions & Future Work

- [[causality-aware-root-cause-diagnosis]]

## Key Concepts

- [[caad-framework]]: A causal-aware anomaly detection framework that monitors deviations in Granger causality consistency and relational topology to identify industrial system failures.

## Archivist Review

The CAAD framework is approved for its novel approach to anomaly detection through continuous Granger causality consistency verification, providing a distinct methodology compared to existing temporal similarity models. The open question regarding the integration of root cause diagnosis was approved as it targets a significant, non-trivial functional gap in current causality-aware anomaly detection research. A second proposed open question on generalization was rejected as it represents a generic, aspirational research objective.

### Approved Concepts
- CAAD Framework: The framework shifts the anomaly detection paradigm from purely temporal similarity to Granger causality consistency verification.

### Approved Open Questions
- Root Cause Diagnosis Integration: Bridging the gap between anomaly detection and root cause analysis is critical for minimizing system downtime in industrial practice.

### Rejected Candidates
- [open_question] Generalization Across Causal Density (`causality-aware-model-generalization`) - generic: The question describes a generic research goal of improving generalization across diverse datasets rather than a specific, technical research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.08555)
- [PDF](https://arxiv.org/pdf/2607.08555)

