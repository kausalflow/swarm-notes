---
# CSL-compatible fields
title: "Simultaneous Inference for Partially Observed Functional Time Series"
author:
  - literal: "P. Bastian"
  - literal: "Tim Kutta"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31269"

# Custom fields
paper_id: "2606.31269"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "supremum-norm-functional-time-series-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:54:55Z"
created_at: "2026-07-03T07:54:55Z"
---

# Simultaneous Inference for Partially Observed Functional Time Series

**Authors**: P. Bastian, Tim Kutta
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31269](https://arxiv.org/abs/2606.31269)

## Summary

This paper introduces a novel statistical inference framework for functional time series characterized by dependent, partially observed data. By modeling data on the space of bounded functions with the supremum norm, the authors enable simultaneous inference across functional domains, addressing limitations of conventional Hilbert-space methods. The approach incorporates extended multiscale inference for non-stationary trends and demonstrates improved results for both fully and partially observed functional data by avoiding functional Central Limit Theorems.

## Key Contributions

- Proposes the first inference method for dependent, partially observed functional time series using supremum-norm-based modeling.
- Extends multiscale inference methods to account for non-stationary trends in partially observed functions.
- Outperforms existing methods by providing simultaneous confidence bands and removing reliance on functional Central Limit Theorems for fully observed functions.

## Open Questions & Future Work

- [[relaxing-uniform-positivity-assumption-long-run-variance]]

## Key Concepts

- [[supremum-norm-functional-time-series-inference]]: A statistical inference framework for functional time series that supports irregular missingness and simultaneous confidence bands via the supremum norm.

## Archivist Review

I approved the core statistical methodology of using supremum-norm inference for functional time series as a reusable advancement over Hilbert-space methods. I also approved the identified open question regarding the relaxation of the long-run variance positivity assumption, as it highlights a technical bottleneck in the scalability and applicability of the Gaussian approximation approach. No datasets were approved as none were cited as central, reusable contributions to the field.

### Approved Concepts
- Supremum-norm functional time series inference: It enables simultaneous inference on functional data with missing observations by shifting from Hilbert-space methods to supremum-norm-based modeling.

### Approved Open Questions
- Relaxing long-run variance positivity: Relaxing this assumption would generalize the inference framework to regimes where the long-run variance might vanish at some points, increasing the practical robustness of the method.

### Rejected Candidates
- [concept] Simultaneous confidence bands for partially observed functional time series (`simultaneous-confidence-bands-for-partially-observed-functional-time-series`) - other: The proposed concept was overly specific and renamed to reflect the underlying mathematical mechanism (supremum-norm inference).

## Links

- [Abstract](https://arxiv.org/abs/2606.31269)
- [PDF](https://arxiv.org/pdf/2606.31269)

