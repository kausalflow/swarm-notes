---
# CSL-compatible fields
title: "Covariance Filters and Neural Networks Over Hilbert Spaces"
author:
  - literal: "Claudio Battiloro"
  - literal: "Andrea Cavallo"
  - literal: "Elvin Isufi"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2509.13178"

# Custom fields
paper_id: "2509.13178"
paper_source: "openalex"
domain: "nlp"
tags:
  - "convolutional-neural-network"
  - "time-series"
  - "text-classification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "hilbert-covariance-networks-hvns"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T07:01:39Z"
created_at: "2026-04-24T07:01:39Z"
---

# Covariance Filters and Neural Networks Over Hilbert Spaces

**Authors**: Claudio Battiloro, Andrea Cavallo, Elvin Isufi
**Date**: 2026-04-21
**Paper ID**: [openalex:2509.13178](https://arxiv.org/abs/2509.13178)

## Summary

The paper introduces Hilbert coVariance Networks (HVNs), a novel convolutional framework designed for processing signals within infinite-dimensional Hilbert spaces using empirical covariance operators. It constructively defines Hilbert coVariance Filters (HVFs) and establishes a rigorous discretization procedure, proving that empirical HVFs can recover the Functional PCA of the filtered signals. The versatility of the framework is shown across functional data types, and empirical results confirm its robustness for time-series classification.

## Key Contributions

- Introduces Hilbert coVariance Networks (HVNs) as a novel convolutional framework for signals in infinite-dimensional Hilbert spaces.
- Provides a principled discretization procedure that guarantees empirical HVFs recover the Functional PCA (FPCA) of the filtered signals.
- Demonstrates superior robustness and performance of HVNs on time-series classification tasks compared to MLP and FPCA-based baselines.

## Open Questions & Future Work

- [[hvn-discretization-convergence]]

## Key Concepts

- [[hilbert-covariance-networks-hvns]]: A convolutional learning architecture for signals in infinite-dimensional Hilbert spaces using empirical covariance operators.

## Archivist Review

I approved the overarching framework (HVNs) as it represents a significant methodological shift for signal processing in infinite-dimensional Hilbert spaces. I rejected the filter component (HVFs) as it is a subcomponent of the main architecture and does not warrant a separate vault entry. The open question was approved for addressing a critical theoretical convergence gap necessary for the framework's adoption.

### Approved Concepts
- Hilbert coVariance Networks (HVNs): This is the core contribution of the paper, extending covariance-based learning frameworks from finite to infinite-dimensional spaces.

### Approved Open Questions
- Convergence of Discrete HVNs: This is essential to guarantee the theoretical consistency and reliability of the framework across different discretization densities.

### Rejected Candidates
- [concept] Hilbert coVariance Filters (HVF) (`hilbert-covariance-filters-hvf`) - subcomponent_of_broader_mechanism: This is a subcomponent of the broader Hilbert coVariance Networks framework and is not independently required to describe the overall contribution.

## Links

- [Abstract](https://arxiv.org/abs/2509.13178)
- [PDF](https://arxiv.org/pdf/2509.13178)

