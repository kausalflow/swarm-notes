---
# CSL-compatible fields
title: "Machine Learning for Exact Time Series Aggregation in Generation Expansion Planning with Energy Storage"
author:
  - literal: "Jakub Rybka"
  - literal: "Luca Santosuosso"
  - literal: "Thomas Klatzer"
  - literal: "Sonja Wogrin"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28356"

# Custom fields
paper_id: "2605.28356"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
  - "machine-learning"
  - "optimization"
architectures:
  []
datasets:
  []
concept_slugs:
  - "iterative-time-series-aggregation-gep"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:35:32Z"
created_at: "2026-05-30T07:35:32Z"
---

# Machine Learning for Exact Time Series Aggregation in Generation Expansion Planning with Energy Storage

**Authors**: Jakub Rybka, Luca Santosuosso, Thomas Klatzer, Sonja Wogrin
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28356](https://arxiv.org/abs/2605.28356)

## Summary

This paper introduces an iterative time series aggregation (TSA) method to reduce the computational complexity of generation expansion planning (GEP) models involving renewable, thermal, and storage technologies. By incorporating machine learning-based marginal cost estimates into the clustering process, the proposed approach identifies and preserves the active constraints of the full-scale model. Unlike conventional heuristic TSA techniques, this method enables the assessment of the optimality gap, providing a rigorous framework for model reduction in energy systems planning.

## Key Contributions

- Proposes an iterative TSA method for generation expansion planning that allows for the explicit calculation of the optimality gap between aggregated and full-scale models.
- Develops a machine learning-augmented clustering strategy that uses marginal cost estimates to preserve active constraints during time series aggregation.
- Demonstrates that utilizing learned marginal cost features for temporal clustering significantly enhances the accuracy of GEP model reductions compared to traditional heuristic methods.

## Key Concepts

- [[iterative-time-series-aggregation-gep]]: A time series aggregation technique for generation expansion planning that enables optimality gap assessment and leverages marginal cost estimates to preserve active constraints.

## Archivist Review

The concept was approved as it introduces a novel framework for rigorous model reduction in energy systems, offering a clear methodological shift from heuristic approaches. The original slug was modified to include the domain context for clarity and specificity. No datasets or open questions met the high bar for permanent archival in this instance.

### Approved Concepts
- Iterative Time Series Aggregation (GEP): The method provides a formal mechanism for assessing the optimality gap between aggregated and full-scale GEP models, addressing a major limitation of traditional heuristic TSA approaches.

### Rejected Candidates
- [concept] Iterative Time Series Aggregation (`iterative-time-series-aggregation`) - duplicate_existing: This slug was renamed to include context to ensure precision within the knowledge vault.

## Links

- [Abstract](https://arxiv.org/abs/2605.28356)
- [PDF](https://arxiv.org/pdf/2605.28356)

