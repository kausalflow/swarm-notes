---
# CSL-compatible fields
title: "Sequential Inference for Gaussian Processes: A Signal Processing Perspective"
author:
  - literal: "Daniel Waxman"
  - literal: "Fernando Llorente"
  - literal: "Petar M. Djurić"
issued:
  date-parts:
    - [2026, 4, 30]
url: "https://arxiv.org/abs/2604.28163"

# Custom fields
paper_id: "2604.28163"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-03T07:14:20Z"
created_at: "2026-05-03T07:14:20Z"
---

# Sequential Inference for Gaussian Processes: A Signal Processing Perspective

**Authors**: Daniel Waxman, Fernando Llorente, Petar M. Djurić
**Date**: 2026-04-30
**Paper ID**: [openalex:2604.28163](https://arxiv.org/abs/2604.28163)

## Summary

This paper provides a tutorial-style overview of Gaussian processes (GPs) through the lens of signal processing, specifically addressing the challenges of sequential, incremental, and streaming inference. It contrasts the traditional IID assumption in machine learning with the sequential requirements of signal processing systems. By bridging these two fields, the authors offer a coherent roadmap for practitioners to implement GP-based models for tasks such as time-series forecasting, anomaly detection, and state-space modeling.

## Key Contributions

- Provides a comprehensive, self-contained, and tutorial-style overview of Gaussian Processes (GPs) tailored for signal processing applications.
- Systematizes recent methodological developments in sequential, incremental, and streaming inference for GPs.
- Bridges machine learning advancements in GP inference with classical signal processing frameworks for real-world system deployment.

## Open Questions & Future Work

- [[scalability-of-spatiotemporal-markovian-gps]]
- [[online-hyperparameter-adaptation-gps]]

## Archivist Review

The paper acts as a pedagogical review rather than a contribution of new methods or architectures, so no new concepts were approved. The open questions were approved as they identify foundational bottlenecks in the scalability and adaptability of Gaussian process models in sequential contexts.

### Approved Open Questions
- Scalability of Spatiotemporal Markovian GPs: This complexity bottleneck restricts the use of Markovian GPs in high-dimensional spatiotemporal monitoring and climate modeling tasks.
- Online Hyperparameter Adaptation for GPs: Online adaptation of hyperparameters is a fundamental requirement for deploying GP models in autonomous real-time signal processing systems.

## Links

- [Abstract](https://arxiv.org/abs/2604.28163)
- [PDF](https://arxiv.org/pdf/2604.28163)

