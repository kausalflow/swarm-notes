---
# CSL-compatible fields
title: "TopTimeNet: Topologically-assisted time-series classification model"
author:
  - literal: "Sharareh Sayyad"
  - literal: "Sophia Bazzi"
issued:
  date-parts:
    - [2026, 9, 30]
url: "https://arxiv.org/abs/2609.39792"

# Custom fields
paper_id: "2609.39792"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "topological-data-analysis"
  - "classification"
  - "model-compression"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "toptimenet"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-03T10:08:06Z"
created_at: "2026-10-03T10:08:06Z"
---

# TopTimeNet: Topologically-assisted time-series classification model

**Authors**: Sharareh Sayyad, Sophia Bazzi
**Date**: 2026-09-30
**Paper ID**: [openalex:2609.39792](https://arxiv.org/abs/2609.39792)

## Summary

Distinguishing periodic from chaotic dynamics is addressed by TopTimeNet, an architecture that decouples feature extraction from classification by using a fixed, non-learned stage to derive a 42-dimensional geometric and topological descriptor from Takens delay embeddings and persistent homology. A lightweight learnable stage then performs classification on these descriptors. Evaluated on 49 nonlinear dynamical systems, TopTimeNet achieves competitive accuracy compared to CNNs and Transformers while requiring orders of magnitude fewer parameters. Furthermore, the study analyzes noise robustness, demonstrating that robustness to precomputed feature perturbations contrasts with vulnerability under raw signal noise recomputation.

## Key Contributions

- Introduces TopTimeNet, a topologically-assisted time-series classification model that decouples fixed geometric/topological feature extraction from a lightweight learnable classifier.
- Demonstrates that a 1,638-parameter TopTimeNet configuration matches the mean accuracy of models with 33x more trainable parameters across 49 nonlinear dynamical systems.
- Shows that TopTimeNet matches CNN accuracy and surpasses converged Transformer models while using three to four orders of magnitude fewer trainable parameters.
- Reveals that TopTimeNet degrades gracefully under feature perturbations but sharply when noise is injected into raw signals prior to feature recomputation.

## Limitations

Robustness to precomputed feature perturbations does not imply robustness of the complete raw-signal-to-prediction pipeline when feature extraction is recomputed.

## Open Questions & Future Work

- [[multiclass-dynamical-regimes]]

## Key Concepts

- [[toptimenet]]: A topologically-assisted time-series classification model that decouples fixed geometric and topological feature extraction from a lightweight learnable classifier.

## Archivist Review

Approved the TopTimeNet concept as a prominent architecture exemplifying topological feature extraction decoupled from classification. Approved one open question on multi-class dynamical regime classification, while rejecting the quantum dynamics extension as too speculative. No datasets met the strict novelty and standalone archival criteria.

### Approved Concepts
- TopTimeNet: Central to the paper's novel approach of decoupling fixed geometric/topological feature construction from a lightweight learnable classifier for time-series classification.

### Approved Open Questions
- Multi-class dynamical regime classification: Expanding beyond binary classification is crucial for real-world time-series analysis where multiple nuanced dynamical regimes coexist.

### Rejected Candidates
- [open_question] Topological classification of quantum dynamics (`quantum-dynamics-classification`) - low_impact: Speculative and peripheral open question about extending the method to quantum domains without concrete grounding.

## Links

- [Abstract](https://arxiv.org/abs/2609.39792)
- [PDF](https://arxiv.org/pdf/2609.39792)

