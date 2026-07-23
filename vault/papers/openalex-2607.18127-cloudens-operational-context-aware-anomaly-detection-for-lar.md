---
# CSL-compatible fields
title: "ClouDens: Operational Context-Aware Anomaly Detection for Large-scale Cloud System Monitoring"
author:
  - literal: "Thu T. H. Doan"
  - literal: "Mohammad Saiful Islam"
  - literal: "Andriy Miranskyy"
  - literal: "Ngoc-Thanh Nguyen"
  - literal: "Rogardt Heldal"
  - literal: "Patrizio Pelliccione"
issued:
  date-parts:
    - [2026, 7, 20]
url: "https://arxiv.org/abs/2607.18127"

# Custom fields
paper_id: "2607.18127"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "graph-neural-network"
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-23T07:27:11Z"
created_at: "2026-07-23T07:27:11Z"
---

# ClouDens: Operational Context-Aware Anomaly Detection for Large-scale Cloud System Monitoring

**Authors**: Thu T. H. Doan, Mohammad Saiful Islam, Andriy Miranskyy, Ngoc-Thanh Nguyen, Rogardt Heldal, Patrizio Pelliccione
**Date**: 2026-07-20
**Paper ID**: [openalex:2607.18127](https://arxiv.org/abs/2607.18127)

## Summary

This paper presents ClouDens, an operational context-aware anomaly detection framework designed for large-scale cloud systems that handles high-dimensional, sparse multivariate time series from telemetry logs. ClouDens partitions telemetry logs into domain-guided subsets, builds a context-aware graph of service dependencies, and applies Spatio-Temporal Graph Neural Networks for forecasting-based anomaly detection. Evaluated on the IBM Cloud Telemetry Dataset, ClouDens outperforms a GRU-based baseline by achieving higher NAB scores and earlier anomaly identification.

## Key Contributions

- Proposed ClouDens, an operational context-aware anomaly detection framework for large-scale cloud systems that partitions high-dimensional telemetry logs into domain-guided subsets and constructs context-aware graphs.
- Demonstrated through an empirical study on the IBM Cloud Console platform that operational-context attributes encoded in log schemas improve early anomaly detection.
- Achieved higher NAB scores in count-based telemetry features compared to a baseline GRU-based model on the IBM Cloud Telemetry Dataset.

## Archivist Review

Applied strict scarcity and reusability standards. No concepts met the criteria for standalone vault notes, and the proposed open questions were either too application-specific or too generic to qualify as fundamental research bottlenecks.

### Rejected Candidates
- [open_question] Dynamic Graph Topologies for Cloud Anomaly Detection (`dynamic-graph-topologies-cloud-anomaly-detection`) - low_impact: Too specific to cloud microservice monitoring systems rather than a fundamental time-series or machine learning limitation.
- [open_question] Adaptive Scoring and Ensemble Configuration (`adaptive-scoring-and-ensemble-configuration`) - generic: Standard hyperparameter and ensemble tuning problem common across many anomaly detection and machine learning domains.

## Links

- [Abstract](https://arxiv.org/abs/2607.18127)
- [PDF](https://arxiv.org/pdf/2607.18127)

