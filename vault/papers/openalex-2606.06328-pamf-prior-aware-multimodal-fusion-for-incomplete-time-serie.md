---
# CSL-compatible fields
title: "PAMF: Prior-Aware Multimodal Fusion for Incomplete Time Series Data"
author:
  - literal: "Ziwen Kan"
  - literal: "Wugeng Zheng"
  - literal: "Tianlong Chen"
  - literal: "Song Wang"
issued:
  date-parts:
    - [2026, 6, 4]
url: "https://arxiv.org/abs/2606.06328"

# Custom fields
paper_id: "2606.06328"
paper_source: "openalex"
domain: "nlp"
tags:
  - "multimodal"
  - "time-series"
  - "imputation"
  - "flow-matching"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prior-aware-flow-matching"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-07T08:18:52Z"
created_at: "2026-06-07T08:18:52Z"
---

# PAMF: Prior-Aware Multimodal Fusion for Incomplete Time Series Data

**Authors**: Ziwen Kan, Wugeng Zheng, Tianlong Chen, Song Wang
**Date**: 2026-06-04
**Paper ID**: [openalex:2606.06328](https://arxiv.org/abs/2606.06328)

## Summary

PAMF is a multimodal time-series framework designed to handle incomplete observations by explicitly addressing within-modality and modality-level missingness. Unlike methods that treat all missingness uniformly, PAMF employs prior-aware flow matching to initialize imputation with type-specific priors. Furthermore, it tightly couples the imputation and downstream classification tasks through weight-sharing encoders, allowing downstream requirements to guide the imputation process for more informative feature representation.

## Key Contributions

- Introduces PAMF, a novel framework for multimodal time-series that explicitly models two distinct missingness patterns: within-modality and modality-level missing.
- Implements prior-aware flow matching to distinguish missingness types, coupled with architecturally matched encoders and weight sharing to align imputation with downstream prediction.
- Achieves state-of-the-art performance on multiple multimodal healthcare benchmarks compared to existing imputation and classification baselines.

## Open Questions & Future Work

- [[unified-missingness-multimodal-imputation]]

## Key Concepts

- [[prior-aware-flow-matching]]: A flow-matching approach that initializes source states with type-specific priors to address distinct missingness structures in multimodal time series.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 1 concept(s), 1 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Prior-aware flow matching: It provides a novel framework for integrating task-specific priors into generative imputation, addressing structural missingness in multimodal time series.

### Approved Open Questions
- Unified Missingness Multimodal Imputation: This represents a fundamental bottleneck in the utility of multimodal healthcare systems where sensor failure is common and downstream decision-making is sensitive to data gaps.

### Rejected Candidates
- [concept] Weight-sharing encoders (`weight-sharing-encoders`) - generic: Weight sharing is a standard, generic architectural design choice rather than a novel or complex concept deserving of a permanent note.

## Links

- [Abstract](https://arxiv.org/abs/2606.06328)
- [PDF](https://arxiv.org/pdf/2606.06328)

