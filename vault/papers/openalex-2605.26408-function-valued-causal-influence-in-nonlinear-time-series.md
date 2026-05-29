---
# CSL-compatible fields
title: "Function-Valued Causal Influence in Nonlinear Time Series"
author:
  - literal: "Valentina Kuskova"
  - literal: "Dmitry Zaytsev"
  - literal: "Michael Coppedge"
issued:
  date-parts:
    - [2026, 5, 26]
url: "https://arxiv.org/abs/2605.26408"

# Custom fields
paper_id: "2605.26408"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "causal-inference"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "function-valued-causal-influence"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-29T08:37:35Z"
created_at: "2026-05-29T08:37:35Z"
---

# Function-Valued Causal Influence in Nonlinear Time Series

**Authors**: Valentina Kuskova, Dmitry Zaytsev, Michael Coppedge
**Date**: 2026-05-26
**Paper ID**: [openalex:2605.26408](https://arxiv.org/abs/2605.26408)

## Summary

This paper addresses the limitations of summarizing nonlinear causal relationships in time series through static scalar edge scores. The authors argue that such scores obscure the state-dependent nature of causal influences and formalize a function-valued approach for additive architectures. By leveraging Individual Conditional Expectation, the framework recovers causal response functions that capture diverse behaviors like thresholding and sign-changing effects, offering deeper insight into complex time series dynamics.

## Key Contributions

- Formalizes function-valued causal influence to address the information loss occurring in scalar-based nonlinear causal discovery.
- Introduces a practical estimation framework using Individual Conditional Expectation for additive, contribution-decomposable architectures.
- Demonstrates that function-valued analysis reveals regime-specific, asymmetric causal structures systematically missed by standard scalar edge score methods.

## Open Questions & Future Work

- [[function-valued-causal-analysis-non-additive]]

## Key Concepts

- [[function-valued-causal-influence]]: A causal discovery framework that represents influence as state-dependent functions rather than scalar scores.

## Archivist Review

The paper makes a compelling argument for moving beyond scalar causal edge scores by framing causal influence as a state-dependent function. I have approved the framework itself as a foundational concept for nonlinear causal interpretability and identified the extension to non-additive models as a significant open research question for the field.

### Approved Concepts
- Function-Valued Causal Influence: It shifts causal discovery from scalar edge scores to regime-dependent functions, overcoming information bottlenecks inherent in current nonlinear time series models.

### Approved Open Questions
- Extending function-valued analysis frameworks: This is technically important because many high-performance machine learning models for time series do not satisfy the additivity constraint, making the current function-valued framework inapplicable to a wide class of modern architectures.

## Links

- [Abstract](https://arxiv.org/abs/2605.26408)
- [PDF](https://arxiv.org/pdf/2605.26408)

