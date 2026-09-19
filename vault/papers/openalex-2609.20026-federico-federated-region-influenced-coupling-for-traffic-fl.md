---
# CSL-compatible fields
title: "FedeRICo: Federated Region-Influenced Coupling for Traffic Flow Prediction"
author:
  - literal: "Fermin Orozco"
  - literal: "Man Luo"
  - literal: "Johan Wahlström"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2609.20026"

# Custom fields
paper_id: "2609.20026"
paper_source: "openalex"
domain: "time-series"
tags:
  - "federated-learning"
  - "time-series"
  - "forecasting"
  - "spatial-temporal"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  - "federated-region-influenced-coupling-federico"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:04:50Z"
created_at: "2026-09-19T09:04:50Z"
---

# FedeRICo: Federated Region-Influenced Coupling for Traffic Flow Prediction

**Authors**: Fermin Orozco, Man Luo, Johan Wahlström
**Date**: 2026-09-17
**Paper ID**: [openalex:2609.20026](https://arxiv.org/abs/2609.20026)

## Summary

Urban traffic forecasting across privacy-constrained stakeholders often suffers from client heterogeneity and broken spatial dependencies across partitioned road networks. To address this, the authors propose FedeRICo, a federated framework that combines gradient-level collaboration with boundary-aware residual communication. FedeRICo uses a dual-branch architecture with a globally guided branch coordinated via gradient alignment and a private residual branch that exchanges trend-decomposed boundary messages between adjacent clients. Experiments on four real-world traffic benchmarks show that FedeRICo outperforms existing federated spatial-temporal baselines while keeping training runtimes competitive.

## Key Contributions

- Proposes FedeRICo, a federated traffic forecasting framework combining gradient-level collaboration and boundary-aware residual communication to address cross-client heterogeneity and broken boundary dynamics.
- Employs a dual-branch forecasting architecture featuring a globally guided branch coordinated via gradient alignment and a private residual branch incorporating boundary residual signals.
- Utilizes a trend-residual decomposition to extract and communicate transient spatial-temporal residual signals between adjacent clients while suppressing periodic structure.
- Demonstrates consistent outperformance over state-of-the-art federated spatial-temporal baselines across four real-world traffic benchmarks while maintaining competitive runtime.

## Limitations

Limited to federated traffic forecasting scenarios where clients share physical boundaries or adjacency relationships.

## Open Questions & Future Work

- [[asynchronous-federated-spatial-temporal-forecasting]]

## Key Concepts

- [[federated-region-influenced-coupling-federico]]: A federated traffic forecasting framework combining gradient-level collaboration with boundary-aware residual communication to handle cross-client heterogeneity and spatial dependencies.

## Archivist Review

Approved the core federated traffic forecasting framework 'FedeRICo' as a reusable concept, along with the open question on asynchronous federated spatial-temporal forecasting. Rejected standard trend-residual decomposition, unnamed datasets, and the secondary privacy question.

### Approved Concepts
- Federated Region-Influenced Coupling (FedeRICo): Core methodological contribution providing a federated traffic forecasting framework with gradient-level collaboration and boundary-aware residual communication.

### Approved Open Questions
- Asynchronous Federated Traffic Forecasting: Asynchronous federated learning is critical for real-world deployment where clients join and drop out dynamically, yet standard spatial-temporal architectures currently assume synchronized communication rounds.

### Rejected Candidates
- [concept] Trend-Residual Decomposition (`trend-residual-decomposition`) - not_novel: Trend-residual decomposition is a standard time-series preprocessing and modeling technique rather than a novel conceptual contribution unique to this paper.
- [dataset] Four Real-World Traffic Forecasting Benchmarks (`four-real-world-traffic-forecasting-benchmarks`) - generic: The abstract refers to four unnamed real-world traffic forecasting benchmarks rather than specific named benchmark datasets.
- [open_question] Formal Privacy for Boundary Messages (`formal-privacy-boundary-messages`) - low_impact: While important, this is a routine application of differential privacy to a specific messaging component rather than a standalone vault-level open question.

## Links

- [Abstract](https://arxiv.org/abs/2609.20026)
- [PDF](https://arxiv.org/pdf/2609.20026)

