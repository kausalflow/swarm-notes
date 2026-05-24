---
# CSL-compatible fields
title: "Causal Discovery in Structural VAR Models Under Equal Noise Variance"
author:
  - literal: "SeyedSina Seyedi HasanAbadi"
  - literal: "Fahimeh Arab"
  - literal: "Erfan Nozari"
  - literal: "AmirEmad Ghassami"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.21846"

# Custom fields
paper_id: "2605.21846"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "observational-alignment-discrepancy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:47:17Z"
created_at: "2026-05-24T07:47:17Z"
---

# Causal Discovery in Structural VAR Models Under Equal Noise Variance

**Authors**: SeyedSina Seyedi HasanAbadi, Fahimeh Arab, Erfan Nozari, AmirEmad Ghassami
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.21846](https://arxiv.org/abs/2605.21846)

## Summary

This paper addresses the challenge of causal discovery in multivariate time series where causal effects can be contemporaneous, focusing on linear Gaussian structural VAR models with equal noise variance. It proves that such models are not point-identifiable, as multiple parameterizations can induce the same observed law. To resolve this, the authors characterize the observational equivalence class using orthogonal transformations and propose the observational alignment discrepancy to compare models. Finally, they introduce ENVAR, an algorithm that leverages this characterization to recover sparse causal structures, with empirical validation on synthetic data and fMRI recordings.

## Key Contributions

- Proves that in linear Gaussian structural VAR models with equal noise variance, the underlying causal graph is not point-identifiable and defines the resulting observational equivalence class via orthogonal transformations.
- Introduces the observational alignment discrepancy, a metric for comparing structural models that accounts for the non-unique identification of parameters while preserving the observed law.
- Develops ENVAR, a sparsity-based algorithm for recovering sparse causal structures within the identified equivalence class, demonstrating its effectiveness on synthetic and fMRI data.

## Open Questions & Future Work

- [[structural-representative-selection-in-svar]]

## Key Concepts

- [[observational-alignment-discrepancy]]: A model discrepancy metric designed to compare structural VAR models modulo the orthogonal transformations that preserve the observed process law.

## Archivist Review

The approved concept defines a formal way to measure differences between observationally equivalent structural VAR models, which is a significant theoretical contribution. The approved open question addresses the fundamental identifiability limitation in SVAR systems, moving beyond the specific algorithm proposed. ENVAR was rejected as it is a specific procedural implementation of these theoretical principles.

### Approved Concepts
- Observational Alignment Discrepancy: It provides a mathematically principled way to compare structural VAR models that are observationally equivalent under the equal noise variance assumption, addressing the lack of point identifiability.

### Approved Open Questions
- Selecting Representatives in SVARs: This is a central limitation of the proposed framework, as it highlights that the identified equivalence class may still contain many valid models, and the current selection criterion (sparsity) might be insufficient or suboptimal for real-world applications where ground truth is complex.

### Rejected Candidates
- [concept] ENVAR (`envar`) - subcomponent_of_broader_mechanism: ENVAR is a specific algorithm instantiation rather than a foundational concept; the core theoretical contribution is the equivalence class characterization and the discrepancy metric.

## Links

- [Abstract](https://arxiv.org/abs/2605.21846)
- [PDF](https://arxiv.org/pdf/2605.21846)

