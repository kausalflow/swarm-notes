---
# CSL-compatible fields
title: "Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification"
author:
  - literal: "Veerendhra Kumar Dangeti"
  - literal: "Xiao Gu"
  - literal: "Ying Weng"
  - literal: "Shreyank N Gowda"
issued:
  date-parts:
    - [2026, 6, 10]
url: "https://arxiv.org/abs/2606.12252"

# Custom fields
paper_id: "2606.12252"
paper_source: "openalex"
domain: "medicine"
tags:
  - "time-series"
  - "interpretability"
  - "explainability"
  - "efficient-transformer"
  - "clinical-time-series-analysis"
architectures:
  []
datasets:
  []
concept_slugs:
  - "erts-explainability-based-reliability-training-signal"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-13T08:16:50Z"
created_at: "2026-06-13T08:16:50Z"
---

# Using Explainability as a Training-Time Reliability Signal for Efficient ECG Classification

**Authors**: Veerendhra Kumar Dangeti, Xiao Gu, Ying Weng, Shreyank N Gowda
**Date**: 2026-06-10
**Paper ID**: [openalex:2606.12252](https://arxiv.org/abs/2606.12252)

## Summary

The paper introduces ERTS, a training framework for clinical time-series analysis that uses explainability as a reliability signal to improve model training efficiency. By utilizing Grad-CAM attention maps, ERTS computes focus scores that allow the model to prioritize samples with coherent and localized patterns while filtering out those driven by noise or ambiguity. The method demonstrates significant improvements in classification performance and training efficiency across three ECG datasets compared to standard confidence-based data dropout strategies.

## Key Contributions

- Introduced ERTS, an explainability-based reliability training signal that uses Grad-CAM focus scores to selectively perform gradient updates.
- Demonstrated that using explanation quality as a sample filtering mechanism improves macro-F1 scores in ECG classification compared to confidence-based approaches.
- Reduced effective training costs across multiple backbone architectures by prioritizing informative, high-focus samples.

## Open Questions & Future Work

- [[explainability-as-training-signal-refinement]]

## Key Concepts

- [[erts-explainability-based-reliability-training-signal]]: A training strategy that leverages explanation focus scores to filter noisy or unreliable samples, improving classification efficiency and reliability in clinical time-series.

## Archivist Review

The paper introduces a compelling framework that operationalizes explainability (Grad-CAM focus) as a dynamic training-time supervisory signal for sample prioritization. The concept is approved for its novelty in integrating interpretability with active learning/data filtering. The open question reflects the identified need for more rigorous, clinically-informed attribution metrics as this paradigm evolves.

### Approved Concepts
- ERTS (Explainability-based Reliability Training Signal): It introduces a novel mechanism to use post-hoc explainability methods as an online training-time supervisory signal for sample selection.

### Approved Open Questions
- Refining Explainability-Guided Training Signals: Establishing a formal and reliable way to use explainability as a training-time signal is critical for bridging the gap between purely post hoc interpretability and active, data-efficient model optimization.

## Links

- [Abstract](https://arxiv.org/abs/2606.12252)
- [PDF](https://arxiv.org/pdf/2606.12252)

