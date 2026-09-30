---
# CSL-compatible fields
title: "Supervision Recovery for Time Series Anomaly Detection via Context-Anchored Pairing"
author:
  - literal: "Yifei Gao"
  - literal: "Tian Lan"
  - literal: "Yimeng Lu"
  - literal: "Xuming An"
  - literal: "Meng Wang"
  - literal: "Wenjun He"
  - literal: "Yijie Li"
  - literal: "Chen Zhang"
issued:
  date-parts:
    - [2026, 9, 27]
url: "https://arxiv.org/abs/2609.33610"

# Custom fields
paper_id: "2609.33610"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "semi-supervised-learning"
  - "representation-learning"
  - "unsupervised"
  - "benchmark"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "context-anchored-pair-supervision"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-30T10:50:12Z"
created_at: "2026-09-30T10:50:12Z"
---

# Supervision Recovery for Time Series Anomaly Detection via Context-Anchored Pairing

**Authors**: Yifei Gao, Tian Lan, Yimeng Lu, Xuming An, Meng Wang, Wenjun He, Yijie Li, Chen Zhang
**Date**: 2026-09-27
**Paper ID**: [openalex:2609.33610](https://arxiv.org/abs/2609.33610)

## Summary

Time series anomaly detection (TSAD) suffers from label scarcity and the context-dependent nature of anomalies. This paper introduces Context-Anchored Pair Supervision (CAPS), a supervision-recovery framework that constructs matched normal-anomalous pairs under identical temporal contexts. By simulating normal-anomalous pairs and applying reconstruction, background consistency, and counterfactual recombination, CAPS learns anomaly representations that form a sampleable multimodal prior. These realized semantics provide robust temporal supervision for discriminative anomaly detectors, outperforming existing unsupervised or surrogate methods across nine datasets.

## Key Contributions

- Proposes Context-Anchored Pair Supervision (CAPS), a supervision-recovery framework that matches normal and anomalous outcomes under identical temporal contexts without target-domain anomaly labels.
- Leverages simulated normal-anomalous pairs to learn structure and anomaly-semantic representations via reconstruction, background consistency, and counterfactual recombination.
- Realizes sampled semantics conditionally as residual-form effects on target reference trajectories to provide temporal supervision for discriminative detectors.
- Achieves top aggregate performance across four evaluation metrics on nine datasets compared against baseline methods.

## Open Questions & Future Work

- [[multivariate-cross-variable-dependency-modeling]]

## Key Concepts

- [[context-anchored-pair-supervision]]: A supervision-recovery framework for time series anomaly detection that matches normal and anomalous outcomes under identical temporal contexts using simulated pairs.

## Archivist Review

Approved the central framework concept 'Context-Anchored Pair Supervision' and the open question on multivariate cross-variable dependency modeling. Rejected the unnamed dataset grouping in accordance with scarcity and naming rules.

### Approved Concepts
- Context-Anchored Pair Supervision: Introduces a novel supervision-recovery paradigm for time series anomaly detection using simulated normal-anomalous pairs under identical temporal contexts.

### Approved Open Questions
- Multivariate Cross-Variable Dependency Modeling: Crucial for scaling anomaly detection frameworks to complex multi-sensor industrial systems where anomalies frequently manifest as abnormal correlations or interactions across multiple dimensions rather than isolated univariate changes.

### Rejected Candidates
- [dataset] Nine Datasets (`nine-datasets`) - not_reusable: Generic collection of unnamed datasets without specific benchmark names.

## Links

- [Abstract](https://arxiv.org/abs/2609.33610)
- [PDF](https://arxiv.org/pdf/2609.33610)

