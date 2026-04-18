---
# CSL-compatible fields
title: "Unsupervised Anomaly Detection in Process-Complex Industrial Time Series: A Real-World Case Study"
author:
  - literal: "Sergej Krasnikov"
  - literal: "Lukas Meitz"
  - literal: "Samineh Bagheri"
  - literal: "Michael Heider"
  - literal: "Thorsten Schöler"
  - literal: "Jörg Hähner"
issued:
  date-parts:
    - [2026, 4, 15]
url: "https://arxiv.org/abs/2604.13928"

# Custom fields
paper_id: "2604.13928"
paper_source: "openalex"
domain: "time-series"
tags:
  - "anomaly-detection"
  - "time-series"
  - "autoencoder"
  - "convolutional-neural-network"
  - "variational-autoencoder"
  - "recurrent-neural-network"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-18T06:06:36Z"
created_at: "2026-04-18T06:06:36Z"
---

# Unsupervised Anomaly Detection in Process-Complex Industrial Time Series: A Real-World Case Study

**Authors**: Sergej Krasnikov, Lukas Meitz, Samineh Bagheri, Michael Heider, Thorsten Schöler, Jörg Hähner
**Date**: 2026-04-15
**Paper ID**: [openalex:2604.13928](https://arxiv.org/abs/2604.13928)

## Summary

This paper addresses the performance gap of traditional anomaly detection methods when applied to complex, multi-stage industrial time-series data. Through an empirical case study, the authors compare various model classes, including Isolation Forests and several autoencoder configurations. The study demonstrates that while Isolation Forests struggle with the non-periodic, multi-scale dynamics inherent in industrial processes, temporal convolutional autoencoders provide a significantly more robust solution.

## Key Contributions

- Empirical validation that classical Isolation Forest methods fail to capture non-periodic, multi-scale dynamics in complex industrial production data.
- Systematic comparison of multiple autoencoder architectures, identifying temporal convolutional autoencoders as the most robust choice for process-complex industrial time series.
- Introduction of a unique, real-world industrial dataset demonstrating high variability and heterogeneous multi-stage processes.

## Open Questions & Future Work

- [[generalizability-of-industrial-anomaly-detection-architectures]]

## Archivist Review

The paper provides a valuable empirical case study on the architectural performance gap in complex industrial time series, but it does not introduce new methods or frameworks that qualify as independent, reusable concepts. I have approved the open question regarding architectural generalizability as it highlights a persistent, unresolved challenge in this domain. I rejected the proposed concept candidates as they describe the problem setting rather than offering specific, novel technical methodologies.

### Approved Open Questions
- Generalizability of industrial anomaly detection architectures: Establishing generalized architectural guidelines is critical for shifting industrial anomaly detection from bespoke implementations to reliable, robust deployment frameworks for diverse manufacturing environments.

### Rejected Candidates
- [concept] Process-complex industrial time series (`process-complex-industrial-time-series`) - generic: This is a descriptive problem domain rather than a specific technical methodology or reusable concept.
- [concept] Isolation Forests for complex dynamics benchmarking (`isolation-forests-for-complex-dynamics`) - not_novel: Comparing baseline models on a case study is a standard evaluation practice, not a novel methodology warranting a permanent vault note.

## Links

- [Abstract](https://arxiv.org/abs/2604.13928)
- [PDF](https://arxiv.org/pdf/2604.13928)

