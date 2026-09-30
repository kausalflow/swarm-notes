---
# CSL-compatible fields
title: "GT-PSSM: Unified Probabilistic Framework for Stochastic Dynamics Modeling and Dependency Learning in Multivariate Time Series Anomaly Detection"
author:
  - literal: "Wonmo Koo"
  - literal: "Jaeyeong Lee"
  - literal: "Taeseong Yoon"
  - literal: "Heeyoung Kim"
issued:
  date-parts:
    - [2026, 9, 28]
url: "https://arxiv.org/abs/2609.34161"

# Custom fields
paper_id: "2609.34161"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "graph-neural-network"
  - "transformer"
  - "attention-mechanism"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "graph-transformer-enhanced-probabilistic-state-space-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:49:56Z"
created_at: "2026-09-30T10:49:56Z"
---

# GT-PSSM: Unified Probabilistic Framework for Stochastic Dynamics Modeling and Dependency Learning in Multivariate Time Series Anomaly Detection

**Authors**: Wonmo Koo, Jaeyeong Lee, Taeseong Yoon, Heeyoung Kim
**Date**: 2026-09-28
**Paper ID**: [openalex:2609.34161](https://arxiv.org/abs/2609.34161)

## Summary

Multivariate time series anomaly detection is often hindered by deterministic models that rely on unreliable point-wise error scores under stochastic system conditions. To address this, the authors propose the Graph-Transformer-Enhanced Probabilistic State-Space Model (GT-PSSM), which couples probabilistic state-space modeling with Graph Transformers to capture long-range temporal dependencies and inter-variable interactions. This unified framework robustly accounts for measurement noise and intrinsic randomness, enabling more accurate and reliable anomaly scoring.

## Key Contributions

- Proposes GT-PSSM, a unified probabilistic framework combining probabilistic state-space models (PSSMs) and Graph Transformers for multivariate time series anomaly detection.
- Integrates explicit cross-variable structure modeling and long-range temporal dependency learning to overcome the noise sensitivity of recurrent PSSM architectures.
- Provides robust probabilistic anomaly scoring that accounts for intrinsic system randomness and measurement noise rather than relying solely on deterministic point-wise errors.

## Open Questions & Future Work

- [[causal-graph-learning-root-cause-analysis]]

## Key Concepts

- [[graph-transformer-enhanced-probabilistic-state-space-model]]: A probabilistic state-space model enhanced with graph transformers for multivariate time series anomaly detection.

## Archivist Review

Approved the primary methodological contribution (GT-PSSM) and its explicit open question concerning causal graph learning for anomaly localization, maintaining high standards of scarcity and vault relevance.

### Approved Concepts
- Graph-Transformer-Enhanced Probabilistic State-Space Model: Introduces a unified probabilistic framework combining PSSMs and Graph Transformers for multivariate time series anomaly detection.

### Approved Open Questions
- Causal Graph Learning for Anomaly Localization: Transitioning from associative to causal graph learning is crucial for advancing from mere anomaly detection to actionable root-cause localization in complex cyber-physical and industrial systems.

## Links

- [Abstract](https://arxiv.org/abs/2609.34161)
- [PDF](https://arxiv.org/pdf/2609.34161)

