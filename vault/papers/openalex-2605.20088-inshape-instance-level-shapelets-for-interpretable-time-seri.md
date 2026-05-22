---
# CSL-compatible fields
title: "INSHAPE: Instance-Level Shapelets for Interpretable Time-Series Classification"
author:
  - literal: "Seongjun Lee"
  - literal: "Seokhyun Lee"
  - literal: "Changhee Lee"
issued:
  date-parts:
    - [2026, 5, 19]
url: "https://arxiv.org/abs/2605.20088"

# Custom fields
paper_id: "2605.20088"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "explainability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "instance-level-shapelets"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-22T08:17:03Z"
created_at: "2026-05-22T08:17:03Z"
---

# INSHAPE: Instance-Level Shapelets for Interpretable Time-Series Classification

**Authors**: Seongjun Lee, Seokhyun Lee, Changhee Lee
**Date**: 2026-05-19
**Paper ID**: [openalex:2605.20088](https://arxiv.org/abs/2605.20088)

## Summary

INSHAPE is an interpretable time-series classification framework that focuses on discovering instance-specific discriminative temporal patterns, or shapelets, rather than population-wide averages. By modeling the dependencies between these non-overlapping segments, the model provides clearer local explanations while maintaining strong predictive power. Additionally, it offers a bottom-up approach to global interpretability by aggregating these instance-specific patterns into population-level prototypes. Extensive benchmarks on UCR and UEA datasets demonstrate its superior performance over existing state-of-the-art shapelet-based methods.

## Key Contributions

- Introduces INSHAPE, which models instance-specific discriminative temporal patterns rather than relying on population-level averages.
- Implements a dependency-aware modeling approach for shapelets to capture interactions between temporal patterns within a single time series.
- Achieves state-of-the-art predictive performance on 128 UCR and 30 UEA datasets while providing a hierarchical interpretation framework that aggregates instance-level features into global prototypes.

## Open Questions & Future Work

- [[shapelet-length-interpretability-tradeoff]]

## Key Concepts

- [[instance-level-shapelets]]: A framework for time-series classification that models discriminative, instance-specific temporal patterns and their inter-pattern dependencies.

## Archivist Review

I approved the 'Instance-Level Shapelets' concept as a distinct methodological shift away from population-level patterns in time-series classification. I also included a refined version of the open question regarding the trade-off between pattern complexity and interpretability, which is a significant bottleneck in this field. Generic or aggregate dataset mentions (UCR/UEA) were rejected as they are standard, broad benchmarks.

### Approved Concepts
- Instance-Level Shapelets: Shifts the paradigm from population-level to instance-specific pattern discovery for better accuracy and interpretability in time-series classification.

### Approved Open Questions
- Shapelet Length Interpretability Tradeoff: This addresses a fundamental limitation in current interpretable time-series classification regarding the trade-off between model expressivity and explanation clarity.

### Rejected Candidates
- [open_question] Balancing Shapelet Length and Interpretability (`shapelet-length-dependency-tradeoff`) - other: Renamed for consistency and conciseness.

## Links

- [Abstract](https://arxiv.org/abs/2605.20088)
- [PDF](https://arxiv.org/pdf/2605.20088)

