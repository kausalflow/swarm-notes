---
# CSL-compatible fields
title: "Reduced-order modeling of a viscoelastic turbulent jet with hybrid machine learning models"
author:
  - literal: "Christian Amor"
  - literal: "Adrián Corrochano"
  - literal: "Marco Edoardo Rosti"
  - literal: "Soledad Le Clainche"
issued:
  date-parts:
    - [2026, 4, 29]
url: "https://arxiv.org/abs/2604.26240"

# Custom fields
paper_id: "2604.26240"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-02T06:57:10Z"
created_at: "2026-05-02T06:57:10Z"
---

# Reduced-order modeling of a viscoelastic turbulent jet with hybrid machine learning models

**Authors**: Christian Amor, Adrián Corrochano, Marco Edoardo Rosti, Soledad Le Clainche
**Date**: 2026-04-29
**Paper ID**: [openalex:2604.26240](https://arxiv.org/abs/2604.26240)

## Summary

This paper introduces a hybrid reduced-order modeling approach to address the high computational costs associated with simulating viscoelastic turbulent jets. By combining proper orthogonal decomposition for spatial compression and neural networks for the temporal evolution of mode coefficients, the method effectively predicts the system's long-term dynamics. The study highlights the architectural requirements for robust forecasting, specifically emphasizing the role of skip connections in capturing smaller-scale features.

## Key Contributions

- Proposes a hybrid reduced-order model (ROM) for viscoelastic turbulent jets, combining Proper Orthogonal Decomposition (POD) for dimensionality reduction with neural networks for temporal coefficient prediction.
- Demonstrates that hybrid models can accurately capture long-term statistical behavior of viscoelastic jets while providing significant acceleration over full-scale numerical simulations.
- Identifies that skip connections are essential for enabling deeper, generalizable neural networks capable of predicting complex, small-scale dynamics in viscoelastic turbulent flows.

## Open Questions & Future Work

- [[nonlinear-orthogonal-mode-decomposition]]

## Archivist Review

The paper focuses on a specific application of established hybrid reduced-order modeling techniques. While the findings regarding skip connections are useful for practitioners, they are implementation details rather than fundamental, reusable conceptual contributions. The open question regarding nonlinear orthogonal mode decomposition is approved as it addresses a longstanding, non-trivial tension in scientific machine learning between linear interpretability and nonlinear compression.

### Approved Open Questions
- Nonlinear orthogonal mode decomposition: Bridging this gap is crucial for building ROMs that are both computationally efficient (requiring fewer modes) and physically interpretable, which is essential for scaling ROMs to highly complex, high-Reynolds or high-Weissenberg number turbulence.

### Rejected Candidates
- [concept] Hybrid reduced-order model (`hybrid-reduced-order-model`) - not_novel: This is a broad class of existing methods already well-represented in the field of scientific machine learning.

## Links

- [Abstract](https://arxiv.org/abs/2604.26240)
- [PDF](https://arxiv.org/pdf/2604.26240)

