---
# CSL-compatible fields
title: "The Topological Stability Index: A Variance-Based Measure for Persistence Barcodes"
author:
  - literal: "Joris Kirchner"
  - literal: "Ioannis Diamantis"
issued:
  date-parts:
    - [2026, 5, 28]
url: "https://arxiv.org/abs/2605.29839"

# Custom fields
paper_id: "2605.29839"
paper_source: "openalex"
domain: "nlp"
tags:
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "topological-stability-index-tsi"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-31T08:11:30Z"
created_at: "2026-05-31T08:11:30Z"
---

# The Topological Stability Index: A Variance-Based Measure for Persistence Barcodes

**Authors**: Joris Kirchner, Ioannis Diamantis
**Date**: 2026-05-28
**Paper ID**: [openalex:2605.29839](https://arxiv.org/abs/2605.29839)

## Summary

The paper introduces the Topological Stability Index (TSI), a variance-based scalar measure designed to quantify the dispersion of persistence lifetimes in topological data analysis. Unlike existing methods such as persistent entropy, the TSI captures absolute variability and maintains sensitivity to heterogeneous feature scales. The authors also derive a normalized, scale-invariant version (cvTSI) and demonstrate its direct relationship to the Rényi entropy of order two. Empirical evaluations on synthetic data and stochastic time series indicate that the TSI effectively complements entropy by isolating structural variability from deterministic trends.

## Key Contributions

- Introduces the Topological Stability Index (TSI), a variance-based summary statistic for persistence barcodes sensitive to absolute feature scale.
- Derives update formulas for TSI under insertion and deletion of bars, facilitating efficient computation in dynamic settings.
- Establishes a formal algebraic link between the scale-invariant version (cvTSI) and the Rényi entropy of order two, providing a bridge between variance-based and information-theoretic summaries.

## Open Questions & Future Work

- [[tsi-stability-functional-analogues]]

## Key Concepts

- [[topological-stability-index-tsi]]: A variance-based scalar measure for persistence barcodes that quantifies the dispersion of persistence lifetimes.

## Archivist Review

I approved the Topological Stability Index (TSI) as it introduces a novel, variance-based summary statistic for TDA that addresses specific limitations of persistent entropy. The open question regarding stability and functional analogues was also approved because it highlights a fundamental limitation (lack of continuity under insertion) that is central to the reliable application of these new topological descriptors. Other potential quantities mentioned in the paper were deemed subcomponents or less central to the primary contribution.

### Approved Concepts
- Topological Stability Index (TSI): It provides a novel, variance-based alternative to persistent entropy for summarizing persistence barcodes, offering sensitivity to feature scales.

### Approved Open Questions
- Stability and Functional Analogues: Establishing stability properties is fundamental for the reliability of summary statistics in topological data analysis, as it dictates the sensitivity to noise and sampling variability.

## Links

- [Abstract](https://arxiv.org/abs/2605.29839)
- [PDF](https://arxiv.org/pdf/2605.29839)

