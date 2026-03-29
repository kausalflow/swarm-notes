---
# CSL-compatible fields
title: "Adaptive Subspace Modeling With Functional Tucker Decomposition"
author:
  - literal: "Noah Steidle"
  - literal: "Joppe De Jonghe"
  - literal: "Mariya Ishteva"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25530"

# Custom fields
paper_id: "2603.25530"
paper_source: "openalex"
domain: "multimodal"
tags:
  - "tensor-decomposition"
  - "time-series"
  - "image-classification"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "functional-tucker-decomposition"
  - "rkhs-driven-factor-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:08:18Z"
created_at: "2026-03-29T06:08:18Z"
---

# Adaptive Subspace Modeling With Functional Tucker Decomposition

**Authors**: Noah Steidle, Joppe De Jonghe, Mariya Ishteva
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25530](https://arxiv.org/abs/2603.25530)

## Summary

This paper introduces the Functional Tucker Decomposition (FTD) to address the information loss incurred when discretizing continuous, multidimensional data. The FTD enhances the standard Tucker model by incorporating mode-wise continuity constraints directly into the decomposition structure using Reproducing Kernel Hilbert Spaces (RKHS). This RKHS-driven representation allows for adaptive and expressive factor modeling that preserves the multi-linear structure while accommodating continuous data variations. The method is validated on domain-variant tensor classification problems, showing effectiveness in hyperspectral imaging and multivariate time series analysis.

## Key Contributions

- Introduction of the Functional Tucker Decomposition (FTD), which embeds mode-wise continuity constraints directly into the standard Tucker decomposition.
- Utilizing Reproducing Kernel Hilbert Spaces (RKHS) to model continuous, adaptive factors without needing pre-defined bases.
- Demonstrating improved performance in domain-variant tensor classification tasks, specifically in hyperspectral imaging and multivariate time series analysis.

## Limitations

The abstract does not explicitly detail limitations, but challenges may arise in tuning the RKHS kernel parameters.

## Open Questions & Future Work

- [[ftd-multiple-continuous-modes]]
- [[apply-functional-constraints-to-cpd]]

## Key Concepts

- [[functional-tucker-decomposition]]: A tensor decomposition method extending the Tucker structure by embedding mode-wise continuity constraints using Reproducing Kernel Hilbert Spaces (RKHS).
- [[rkhs-driven-factor-modeling]]: Modeling latent factors in a tensor decomposition via Reproducing Kernel Hilbert Spaces (RKHS) to enforce continuity.

## Archivist Review

Two core concepts were approved: the main Functional Tucker Decomposition (FTD) and the enabling RKHS-driven factor modeling technique. The FTD is central as a novel method combining structural decomposition with continuous constraints. Four open questions were approved as they represent specific, reusable technical challenges related to generalizing the FTD (multiple continuous modes, transfer to TTD/CPD) or improving its practical robustness (design point selection, handling missing data). The approval standard focused on capturing the central mathematical contribution and specific, non-boilerplate future research directions.

### Approved Concepts
- Functional Tucker Decomposition (FTD): This is the core novel mathematical method proposed for handling continuous data represented as tensors.
- RKHS-driven Factor Modeling: The use of RKHS is the key mechanism enabling the "functional" adaptability and continuity in the decomposition factors.

### Approved Open Questions
- Expand FTD to multiple continuous modes: Expanding to multiple continuous modes is crucial for complex, multi-channel medical time-series analysis, significantly increasing the method's utility beyond its current single-mode limitation.
- Apply functional constraints to CPD: Exploring functional constraints within the CPD would extend the RKHS modeling to decompositions where individual factor interpretation is the primary objective, contrasting with the FTD's focus on subspace structure.

### Rejected Candidates
- [concept] RKHS-driven Factor Modeling (`rkhs-driven-factor-modeling`) - generic: This concept is approved as it is the key enabling mechanism for the core FTD concept.
- [open_question] Expand FTD to multiple continuous modes (`ftd-multiple-continuous-modes`) - generic: This is a substantial, mechanism-specific future work direction for the core FTD method, particularly for medical time series.
- [open_question] General design point selection strategies (`optimal-rkhs-design-point-selection`) - generic: This is a general, reusable technical question regarding the practical deployment and stability of RKHS models in this context.
- [open_question] Transfer continuity constraint to TTD (`transfer-continuity-constraint-to-ttd`) - generic: This proposes a clear extension of the core mathematical technique (continuity constraint) to another major decomposition structure (TTD).
- [open_question] Apply functional constraints to CPD (`apply-functional-constraint-to-cpd`) - generic: This is a clear comparative extension of the core mathematical technique to the CPD structure, contrasting with the Tucker focus.
- [open_question] Adaptations for missing unaligned data (`adaptations-for-missing-unaligned-data`) - generic: This addresses a critical practical limitation (missing/unaligned data) for the proposed functional decomposition framework.

## Links

- [Abstract](https://arxiv.org/abs/2603.25530)
- [PDF](https://arxiv.org/pdf/2603.25530)

