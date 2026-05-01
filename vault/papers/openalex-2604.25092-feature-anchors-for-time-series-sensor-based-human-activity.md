---
# CSL-compatible fields
title: "Feature Anchors for Time-Series Sensor-Based Human Activity Recognition"
author:
  - literal: "Ruijie Yao"
  - literal: "Chenhang Li"
  - literal: "Danyang Zhuo"
  - literal: "Tingjun Chen"
  - literal: "Xiaoyue Ni"
issued:
  date-parts:
    - [2026, 4, 28]
url: "https://arxiv.org/abs/2604.25092"

# Custom fields
paper_id: "2604.25092"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "benchmark"
  - "dataset"
architectures:
  []
datasets:
  - "daphnet"
  - "pamap2"
concept_slugs:
  - "feature-anchors"
dataset_slugs:
  - "daphnet"
  - "pamap2"
skill: "TimeSeriesSkill"
processed_at: "2026-05-01T07:22:16Z"
created_at: "2026-05-01T07:22:16Z"
---

# Feature Anchors for Time-Series Sensor-Based Human Activity Recognition

**Authors**: Ruijie Yao, Chenhang Li, Danyang Zhuo, Tingjun Chen, Xiaoyue Ni
**Date**: 2026-04-28
**Paper ID**: [openalex:2604.25092](https://arxiv.org/abs/2604.25092)

## Summary

This paper introduces Temporal Conditioning Network for Feature Anchors (TCNet) to address the lack of explicit, adaptable representations in sensor-based Human Activity Recognition (HAR). By treating handcrafted time-series features as feature anchors, the model modulates these explicit components using context from raw IMU signals, balancing domain-expert interpretability with deep learning flexibility. Empirical results across five HAR benchmarks, including USC-HAD and PAMAP2, demonstrate that TCNet outperforms existing approaches by maintaining interpretable anchor semantics while adapting to specific classification objectives.

## Key Contributions

- Introduces the Temporal Conditioning Network for Feature Anchors (TCNet), a model that integrates handcrafted TSFs as dynamic anchors modulated by raw IMU context.
- Demonstrates that TCNet significantly outperforms standard latent representation models on five HAR benchmarks, including a 14.6 mF1 improvement on the Daphnet dataset.
- Establishes that keeping handcrafted features explicit and adaptable within the model improves both classification performance and representation interpretability for human activity recognition.

## Open Questions & Future Work

- [[extending-feature-anchors-to-diverse-modalities]]
- [[learning-sparse-task-specific-anchors]]

## Key Concepts

- [[feature-anchors]]: A mechanism for using handcrafted time-series features as explicit, neural-context-modulated intermediate representations.

## Archivist Review

The concept 'Feature Anchors' is approved as it provides a clear, reusable architectural principle for combining symbolic features with neural context. Daphnet and PAMAP2 are approved as representative HAR benchmarks central to the paper's empirical claims. The open questions regarding modality expansion and sparse learning target substantial, non-trivial research bottlenecks inherent to the proposed framework.

### Approved Concepts
- Feature Anchors: Introduces a paradigm for integrating interpretable handcrafted features as dynamic, model-internal components in HAR tasks, preserving their semantics while allowing neural adaptation.

### Approved Open Questions
- Extending feature anchors to diverse modalities: Establishing the universality of the feature-anchor design principle beyond specific sensor types is a key research bottleneck.
- Learning sparse, task-specific anchors: Addresses the scalability and efficiency of the feature-anchor approach in resource-constrained environments.

## Datasets

- [[daphnet]]
- [[pamap2]]

## Links

- [Abstract](https://arxiv.org/abs/2604.25092)
- [PDF](https://arxiv.org/pdf/2604.25092)

