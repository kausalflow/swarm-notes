---
# CSL-compatible fields
title: "Multimodal Spatiotemporal-Frequency Fusion with Peak Enhancement for Cellular Traffic Forecasting"
author:
  - literal: "Qingzhong Li"
  - literal: "Yue Hu"
  - literal: "Hui Ma"
  - literal: "Yajun Zhang"
  - literal: "Xinjun Pei"
  - literal: "Ming Yan"
  - literal: "Fei Xing"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07016"

# Custom fields
paper_id: "2607.07016"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "multimodal"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mspf-net"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:33Z"
created_at: "2026-07-11T07:05:33Z"
---

# Multimodal Spatiotemporal-Frequency Fusion with Peak Enhancement for Cellular Traffic Forecasting

**Authors**: Qingzhong Li, Yue Hu, Hui Ma, Yajun Zhang, Xinjun Pei, Ming Yan, Fei Xing
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07016](https://arxiv.org/abs/2607.07016)

## Summary

This paper introduces MSPF-Net, a multimodal framework designed for cellular traffic forecasting that captures complex dynamics by integrating spatiotemporal and spectral traffic patterns with exogenous urban contextual signals. To address the challenge of bursty traffic, the authors propose a Peak Enhancement Module that extracts burst-aware representations for sudden activity spikes. The framework uses a Dynamic Fusion Prediction Module to adaptively aggregate these heterogeneous features, significantly improving forecasting accuracy. Experimental results on benchmark datasets, including Milano and Trento, demonstrate the effectiveness of this approach in handling both intrinsic dynamics and external event-driven traffic disturbances.

## Key Contributions

- Introduces MSPF-Net, a novel multimodal framework for cellular traffic forecasting that integrates spatiotemporal-frequency patterns with exogenous urban news signals.
- Develops a Peak Enhancement Module specifically to capture and forecast burst-like cellular traffic spikes that are often overlooked by traditional methods.
- Demonstrates consistent performance improvements over baselines on the Milano, Trento, and LTE cellular traffic datasets by jointly modeling endogenous dynamics and external context.

## Open Questions & Future Work

- [[multimodal-alignment-traffic-forecasting]]

## Key Concepts

- [[mspf-net]]: A multimodal cellular traffic forecasting framework that fuses spatiotemporal-frequency features, burst-aware representations, and external urban news context.

## Archivist Review

The paper provides a modular framework for multimodal traffic forecasting. I approved the overarching MSPF-Net architecture and the open question regarding multimodal alignment. I rejected the Milano and Trento datasets as they are regional subsets rather than foundational, reusable benchmarks.

### Approved Concepts
- MSPF-Net: Central framework introduced by the paper to address the limitation of current methods in handling both bursty traffic dynamics and exogenous contextual signals.

### Approved Open Questions
- Improving Multimodal Data Alignment: Effective multimodal fusion relies on accurate data alignment; without it, models cannot fully exploit the contextual information necessary for predicting event-driven traffic anomalies.

### Rejected Candidates
- [dataset] Milano (`milano`) - not_novel: Standard regional cellular datasets are routine and do not require standalone vault entries.
- [dataset] Trento (`trento`) - not_novel: Standard regional cellular datasets are routine and do not require standalone vault entries.

## Links

- [Abstract](https://arxiv.org/abs/2607.07016)
- [PDF](https://arxiv.org/pdf/2607.07016)

