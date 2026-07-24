---
# CSL-compatible fields
title: "ConceptCF: Concept-based Counterfactuals for the Explainability of Time Series"
author:
  - literal: "Annemarie Jutte"
  - literal: "Faizan Ahmed"
  - literal: "Jeroen Linssen"
  - literal: "Maurice van Keulen"
issued:
  date-parts:
    - [2026, 7, 21]
url: "https://arxiv.org/abs/2607.18748"

# Custom fields
paper_id: "2607.18748"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "explainability"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "conceptcf"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-24T07:24:47Z"
created_at: "2026-07-24T07:24:47Z"
---

# ConceptCF: Concept-based Counterfactuals for the Explainability of Time Series

**Authors**: Annemarie Jutte, Faizan Ahmed, Jeroen Linssen, Maurice van Keulen
**Date**: 2026-07-21
**Paper ID**: [openalex:2607.18748](https://arxiv.org/abs/2607.18748)

## Summary

This paper introduces ConceptCF, a counterfactual generation method designed to enhance the explainability of time series models using human-interpretable concepts. By leveraging time series decomposition to construct concepts like scale and frequency bands, and employing a genetic algorithm for mutation optimization, ConceptCF produces actionable explanations. Evaluations show that ConceptCF outperforms five existing state-of-the-art baselines across multiple evaluation metrics including validity, proximity, sparsity, and plausibility.

## Key Contributions

- Proposes ConceptCF, a counterfactual generation method that operates on human-interpretable concepts such as scale and frequency bands constructed through time series decomposition.
- Utilizes a genetic algorithm to optimize concept mutations for generating meaningful counterfactual explanations.
- Demonstrates top-tier performance against five state-of-the-art approaches across validity, confidence, proximity, sparsity, and plausibility metrics.

## Open Questions & Future Work

- [[alternative-unsupervised-concept-construction-time-series]]

## Key Concepts

- [[conceptcf]]: A method for generating counterfactual explanations for time series models that operates on human-interpretable concepts constructed via time series decomposition.

## Archivist Review

Approved the core method ConceptCF for concept-based counterfactual explainability in time series, along with its explicitly formulated open question on alternative unsupervised concept construction. No named datasets met the strict inclusion threshold.

### Approved Concepts
- ConceptCF: It is the primary methodological contribution of the paper, providing concept-based counterfactual explanations for time series.

### Approved Open Questions
- Alternative and Unsupervised Concept Construction: Expanding the definition and construction of concepts beyond rigid global transformations can significantly broaden the applicability and expressiveness of concept-based explainability methods in complex temporal domains.

## Links

- [Abstract](https://arxiv.org/abs/2607.18748)
- [PDF](https://arxiv.org/pdf/2607.18748)

