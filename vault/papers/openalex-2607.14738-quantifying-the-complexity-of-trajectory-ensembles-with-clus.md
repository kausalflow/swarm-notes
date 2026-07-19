---
# CSL-compatible fields
title: "Quantifying the complexity of trajectory ensembles with clustering-weighted multivariate multiscale sample entropy"
author:
  - literal: "Chenxiao Tian"
  - literal: "Jürgen Hackl"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14738"

# Custom fields
paper_id: "2607.14738"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "complexity"
architectures:
  []
datasets:
  []
concept_slugs:
  - "clustering-weighted-multivariate-multiscale-sample-entropy-cwmmse"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:49Z"
created_at: "2026-07-19T07:24:49Z"
---

# Quantifying the complexity of trajectory ensembles with clustering-weighted multivariate multiscale sample entropy

**Authors**: Chenxiao Tian, Jürgen Hackl
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14738](https://arxiv.org/abs/2607.14738)

## Summary

The paper addresses the limitation of existing entropy measures that, when applied to ensembles of trajectories, rely on averaging and fail to distinguish between system redundancy and population diversity. To solve this, the authors introduce clustering-weighted multivariate multiscale sample entropy (CWMMSE), a measure that groups trajectories into behavior-based clusters weighted by their specific dynamical complexity. Unlike standard approaches, CWMMSE explicitly separates individual complexity from population diversity, offering a more nuanced view of ensemble behavior. Empirical results across eleven scientific domains demonstrate that CWMMSE provides more accurate assessments than simple averaging, as validated by its ability to detect structural changes in complex systems like seismic activity and cardiac cohorts.

## Key Contributions

- Introduces CWMMSE to quantify population complexity by integrating individual dynamical complexity and population diversity.
- Proves the strong consistency of the empirical plug-in estimator for CWMMSE under a fixed finite partition.
- Demonstrates the efficacy of CWMMSE across eleven distinct physical, environmental, and biomedical systems, highlighting its ability to surpass simple averaging methods.

## Open Questions & Future Work

- [[data-driven-resolution-selection-cwmmse]]
- [[noise-robust-complexity-weighting-cwmmse]]

## Key Concepts

- [[clustering-weighted-multivariate-multiscale-sample-entropy-cwmmse]]: A method for measuring ensemble trajectory complexity by weighting behavioral pattern clusters by their dynamical complexity.

## Archivist Review

I approved the CWMMSE framework as a novel and reusable approach for ensemble trajectory analysis that distinctively addresses the deficiency of population-averaging. I also approved two high-value open questions regarding the parameterization (clustering resolution) and the underlying noise sensitivity of the measure, as these represent clear, non-boilerplate bottlenecks for future refinement of this specific methodology.

### Approved Concepts
- Clustering-Weighted Multivariate Multiscale Sample Entropy (CWMMSE): It introduces a novel framework for quantifying the complexity of trajectory ensembles by balancing individual dynamical complexity with population diversity, moving beyond simplistic averaging.

### Approved Open Questions
- Automated Resolution Selection CWMMSE: The resolution is a primary free parameter that dictates the estimation of ensemble diversity; standardizing its selection is critical for the measure's scientific rigour.
- Noise-Robust Complexity Weighting CWMMSE: Reducing sensitivity to unstructured noise would significantly enhance the measure's specificity and prevent misinterpretation of simple noisy systems as dynamically complex.

## Links

- [Abstract](https://arxiv.org/abs/2607.14738)
- [PDF](https://arxiv.org/pdf/2607.14738)

