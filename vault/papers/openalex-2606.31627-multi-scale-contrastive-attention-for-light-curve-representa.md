---
# CSL-compatible fields
title: "Multi-Scale Contrastive Attention for Light-Curve Representation Learning"
author:
  - literal: "Torsha Majumder"
  - literal: "Konstantin Malanchev"
  - literal: "Émille E. O. Ishida"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31627"

# Custom fields
paper_id: "2606.31627"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "self-supervised-learning"
  - "contrastive-learning"
  - "time-series"
  - "multimodal"
  - "attention-mechanism"
  - "fine-tuning"
architectures:
  - "encoder-only"
datasets:
  - "zwicky-transient-facility"
concept_slugs:
  - "astra-clr"
dataset_slugs:
  - "zwicky-transient-facility"
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:56:14Z"
created_at: "2026-07-03T07:56:14Z"
---

# Multi-Scale Contrastive Attention for Light-Curve Representation Learning

**Authors**: Torsha Majumder, Konstantin Malanchev, Émille E. O. Ishida
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31627](https://arxiv.org/abs/2606.31627)

## Summary

Astra-CLR is an attention-based, self-supervised contrastive learning framework designed to extract discriminative representations from inhomogeneous, multi-filter astronomical light curves. The model employs a local-to-global temporal mapping strategy by contrasting multi-scale sequence views and integrates a multi-view late fusion architecture to accommodate varying observation cadences. Pre-trained on a large-scale unlabeled dataset from the Zwicky Transient Facility, it achieves strong classification performance on variability classes, particularly when refined through label-efficient fine-tuning.

## Key Contributions

- Introduced Astra-CLR, a self-supervised contrastive learning framework for light curve representation learning trained on 2.1 million ZTF samples.
- Developed a multi-view late fusion architecture to handle multi-filter inhomogeneous astronomical time-series data.
- Achieved 0.77 accuracy on 12 variability classes via label-efficient partial top-layer fine-tuning.

## Open Questions & Future Work

- [[variable-cadence-time-series-modeling]]
- [[cross-survey-generalization]]

## Key Concepts

- [[astra-clr]]: An attention-based, self-supervised contrastive learning framework for mapping raw, inhomogeneous light curves into a discriminative latent space using multi-scale temporal views.

## Archivist Review

The framework Astra-CLR is approved as a representative for contrastive light-curve modeling. The ZTF dataset is approved as a critical, large-scale source for astronomical time-series training. The two open questions are approved because they address fundamental bottlenecks in astronomical time-series representation learning: irregular temporal sampling and the limitations of cross-survey generalization, which are highly relevant beyond the specific paper.

### Approved Concepts
- Astra-CLR: Central framework proposed for self-supervised light curve representation learning.

### Approved Open Questions
- Native variable-cadence representation learning: This is a central bottleneck in time-domain astronomy, as it limits the ability to process raw data efficiently without loss of information.
- Cross-survey representation generalization: Generalization across surveys is vital for creating universal foundational models in astronomy, reducing the overhead of bespoke model development.

## Datasets

- [[zwicky-transient-facility]]

## Links

- [Abstract](https://arxiv.org/abs/2606.31627)
- [PDF](https://arxiv.org/pdf/2606.31627)

