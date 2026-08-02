---
# CSL-compatible fields
title: "Selfnormalization for relevant inference with supremum-type statistics"
author:
  - literal: "P. Bastian"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.27818"

# Custom fields
paper_id: "2607.27818"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "hypothesis-testing"
  - "statistical-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:27:31Z"
created_at: "2026-08-02T07:27:31Z"
---

# Selfnormalization for relevant inference with supremum-type statistics

**Authors**: P. Bastian
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.27818](https://arxiv.org/abs/2607.27818)

## Summary

The paper introduces a self-normalized inference approach for detecting relevant changes in functional time series using supremum-type statistics. Because the supremum norm lacks Hadamard differentiability, standard projection-based self-normalization fails; the author overcomes this by employing a smooth log-sum-exp approximation and a derivative-derived self-normalizer. Furthermore, by combining multiple smoothing levels to cancel leading bias terms, the method avoids the difficult direct estimation of extremal geometry, yielding an asymptotically exact test free of long-run covariance nuisance parameters.

## Key Contributions

- Developed a self-normalized inference framework for relevant changes in functional time series using the supremum norm.
- Addressed the lack of Hadamard differentiability of the supremum norm via a smooth log-sum-exp approximation and derivative-based projected selfnormalizer.
- Derived explicit smoothing-bias expansions and combined multiple smoothing levels to eliminate leading bias terms without geometric estimation.
- Constructed an asymptotically exact test for relevant changes with an asymptotically pivotal distribution free of long-run covariance nuisance parameters.

## Archivist Review

The submitted concept is an advanced theoretical statistical method for supremum-type statistics under non-Hadamard differentiability. Following rigorous sparsity and impact criteria, it is too specialized to warrant a permanent standalone vault note. No datasets were present.

### Rejected Candidates
- [concept] Selfnormalization for Supremum-Type Statistics (`selfnormalization-for-supremum-type-statistics`) - low_impact: While technically thorough, this is an advanced econometric/statistical change-point method rather than a widely reusable machine learning concept or architecture.

## Links

- [Abstract](https://arxiv.org/abs/2607.27818)
- [PDF](https://arxiv.org/pdf/2607.27818)

