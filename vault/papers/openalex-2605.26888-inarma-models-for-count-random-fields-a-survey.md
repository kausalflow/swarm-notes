---
# CSL-compatible fields
title: "INARMA Models for Count Random Fields -- a Survey"
author:
  - literal: "Angelika Silbernagel"
  - literal: "Christian H. Weiß"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26888"

# Custom fields
paper_id: "2605.26888"
paper_source: "openalex"
domain: "time-series"
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
processed_at: "2026-05-29T08:39:12Z"
created_at: "2026-05-29T08:39:12Z"
---

# INARMA Models for Count Random Fields -- a Survey

**Authors**: Angelika Silbernagel, Christian H. Weiß
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26888](https://arxiv.org/abs/2605.26888)

## Summary

This survey paper reviews the extension of integer-valued autoregressive moving-average (INARMA) models from classical count time series to count random fields on two-dimensional grids. It categorizes existing approaches by their specific thinning operators, the order of the models, and their structural representation as unilateral or multilateral fields. The work provides a formal synthesis of the field, highlighting methodological developments in handling spatial dependencies for discrete-valued data.

## Key Contributions

- Provides a comprehensive survey of INARMA models extended from count time series to count random fields.
- Systematizes the categorization of spatial INARMA models based on thinning operators, model order, and spatial dependency structures (unilateral vs. multilateral).
- Synthesizes existing methodology for modeling count data on two-dimensional grids, serving as a roadmap for future research in count random fields.

## Open Questions & Future Work

- [[bounded-count-inarma-models]]
- [[signed-integer-random-fields]]

## Archivist Review

The paper is a survey of established INARMA models for random fields. I rejected the concept of INARMA itself as it is a well-known statistical framework in the literature. I approved two open questions that describe significant limitations in the current applicability of INARMA models (bounded vs. unbounded and non-negative vs. signed), which align with the skill context of addressing representational challenges in time-series and spatial modeling. The third open question was rejected as it pertains to the evaluation of a specific model variant rather than a foundational research direction.

### Approved Open Questions
- Bounded count INARMA models: Many practical applications involve bounded counts that cannot be accurately represented by unbounded INARMA models.
- Signed integer random fields: Extension to signed integers is necessary for spatial data representing net differences or changes that allow negative values.

### Rejected Candidates
- [open_question] Multilateral CINAR model structure (`multilateral-cinar-investigation`) - low_impact: This is a specific model-validation task rather than a foundational research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2605.26888)
- [PDF](https://arxiv.org/pdf/2605.26888)

