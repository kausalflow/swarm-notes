---
# CSL-compatible fields
title: "Mutual information-entropy plane: a new quantifier space for time series analysis"
author:
  - literal: "Gonzalez Acosta Gaspar"
  - literal: "Kowalski Andrés M"
issued:
  date-parts:
    - [2026, 8, 24]
url: "https://arxiv.org/abs/2608.23456"

# Custom fields
paper_id: "2608.23456"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "information-theory"
  - "entropy"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-27T15:58:17Z"
created_at: "2026-08-27T15:58:17Z"
---

# Mutual information-entropy plane: a new quantifier space for time series analysis

**Authors**: Gonzalez Acosta Gaspar, Kowalski Andrés M
**Date**: 2026-08-24
**Paper ID**: [openalex:2608.23456](https://arxiv.org/abs/2608.23456)

## Summary

This paper introduces a novel two-dimensional quantifier plane, the mutual information-entropy plane, which combines normalized permutation entropy and normalized permutation mutual information to characterize time series. By integrating these Shannon information theory metrics through the Bandt and Pompe embedding method, the proposed plane simultaneously captures intrinsic uncertainty and shared information. Furthermore, the framework incorporates conditional entropy to reveal informational independence and determine directional dependencies, demonstrating its effectiveness across regular, chaotic, and stochastic dynamical regimes.

## Key Contributions

- Introduces a two-dimensional quantifier plane combining normalized permutation entropy and normalized permutation mutual information derived from Shannon's information theory and the Bandt and Pompe method.
- Demonstrates that conditional entropy within this informational plane captures informational independence and directional relationships between variable pairs.
- Illustrates the utility of the mutual information-entropy plane by analyzing regular, chaotic, and stochastic dynamics across varying coupling factors.

## Open Questions & Future Work

- [[robust-parameter-selection-for-information-planes]]

## Archivist Review

The paper presents an information-theoretic quantifier plane combining permutation entropy and mutual information. The concept itself is a specialized analytical tool rather than a widely recurring architecture or training paradigm. However, the open question on parameter selection addresses a fundamental hyperparameter sensitivity in information planes that merits tracking.

### Approved Open Questions
- Robust Parameter Selection for Information Planes: Sensitivity to hyperparameters hinders automated or cross-study comparison without strict manual homogeneity.

### Rejected Candidates
- [open_question] Information Plane Resolution for Short or Noisy Series (`information-plane-resolution-short-noisy-series`) - low_impact: Standard limitation regarding data length and noise sensitivity in information-theoretic estimation rather than a distinct algorithmic bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.23456)
- [PDF](https://arxiv.org/pdf/2608.23456)

