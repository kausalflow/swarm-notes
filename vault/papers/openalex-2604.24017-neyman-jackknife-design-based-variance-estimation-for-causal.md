---
# CSL-compatible fields
title: "Neyman Jackknife: Design-Based Variance Estimation for Causal Inference under Interference"
author:
  - literal: "Bryan Park"
  - literal: "Stefan Wager"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24017"

# Custom fields
paper_id: "2604.24017"
paper_source: "openalex"
domain: "nlp"
tags:
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neyman-jackknife"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:24:41Z"
created_at: "2026-04-30T07:24:41Z"
---

# Neyman Jackknife: Design-Based Variance Estimation for Causal Inference under Interference

**Authors**: Bryan Park, Stefan Wager
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24017](https://arxiv.org/abs/2604.24017)

## Summary

The authors introduce the Neyman Jackknife, a flexible framework for conservative variance estimation designed for finite-population causal inference in the presence of interference. By recomputing target estimators with subsets of treatment assignments omitted, the method offers a unified approach to uncertainty quantification. The framework recovers classical estimators such as the Neyman variance estimator and Newey-West HAC estimator, demonstrating both theoretical consistency and superior empirical performance compared to specialized baselines.

## Key Contributions

- Introduces the Neyman Jackknife, a general framework for conservative variance estimation in finite-population causal inference under interference.
- Demonstrates the framework's versatility by recovering standard variance estimators in classical SUTVA settings and HAC settings for time series.
- Provides numerical evidence that this general-purpose approach matches or outperforms specialized variance estimators across multiple applications.

## Open Questions & Future Work

- [[variance-estimation-under-misspecified-exposure-mappings]]

## Key Concepts

- [[neyman-jackknife]]: A flexible design-based variance estimation framework for causal inference that uses recomputation on omitted treatment assignments to maintain conservatism.

## Archivist Review

I have approved the 'Neyman Jackknife' as a significant, reusable methodological concept for variance estimation. I also approved the open question regarding misspecified exposure mappings, as it represents a core, non-trivial limitation in robust causal and time-series inference. I rejected the spectral gap approximation candidate because it is primarily an implementation-level hurdle specific to this framework rather than a general, high-impact research challenge.

### Approved Concepts
- Neyman Jackknife: It provides a unified, design-based blueprint for conservative variance estimation that recovers classical estimators while generalizing to settings with interference.

### Approved Open Questions
- Variance estimation under misspecified exposure mappings: Misspecification of exposure mappings is common in applied settings, and existing design-based variance estimators can become anti-conservative if the exposure mapping is incorrectly specified.

### Rejected Candidates
- [open_question] Computational spectral gap approximation (`computational-spectral-gap-approximation`) - subcomponent_of_broader_mechanism: This is a task-specific implementation bottleneck for a specific estimator rather than a foundational open question in time series or causal inference.

## Links

- [Abstract](https://arxiv.org/abs/2604.24017)
- [PDF](https://arxiv.org/pdf/2604.24017)

