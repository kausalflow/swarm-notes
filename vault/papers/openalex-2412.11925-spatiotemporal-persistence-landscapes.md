---
# CSL-compatible fields
title: "Spatiotemporal persistence landscapes"
author:
  - literal: "Martina Flammer"
  - literal: "Knut Hüper"
issued:
  date-parts:
    - [2026, 9, 8]
url: "https://arxiv.org/abs/2412.11925"

# Custom fields
paper_id: "2412.11925"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "topological-data-analysis"
  - "persistent-homology"
  - "representation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spatiotemporal-persistence-landscapes"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-10T09:17:22Z"
created_at: "2026-09-10T09:17:22Z"
---

# Spatiotemporal persistence landscapes

**Authors**: Martina Flammer, Knut Hüper
**Date**: 2026-09-08
**Paper ID**: [openalex:2412.11925](https://arxiv.org/abs/2412.11925)

## Summary

The paper introduces spatiotemporal persistence landscapes, a novel topological data analysis invariant for time series and time-varying point clouds that simultaneously captures features persistent across both space and time. By defining an extended zigzag module that merges zigzag and multiparameter persistent homology, the authors construct a stable family of functions taking values in Lebesgue spaces. This enables direct application to statistical analysis and machine learning pipelines for spatiotemporal data.

## Key Contributions

- Proposes a method to apply and visualize persistent homology of time series capturing features persistent with respect to both space and time simultaneously.
- Defines an extended zigzag module combining ideas from zigzag persistent homology and multiparameter persistent homology.
- Introduces spatiotemporal persistence landscapes using a recent generalization of the rank invariant and proves their stability under an adapted interleaving distance.

## Open Questions & Future Work

- [[scalable-computation-extended-zigzag-landscapes]]

## Key Concepts

- [[spatiotemporal-persistence-landscapes]]: An extension of persistence landscapes for extended zigzag modules that captures features persistent across both space and time.

## Archivist Review

Approved the central topological invariant concept 'Spatiotemporal Persistence Landscapes' and its associated computational scalability question while strictly adhering to scarcity and quality rules. No datasets met the strict criteria for standalone archival notes.

### Approved Concepts
- Spatiotemporal Persistence Landscapes: Central novelty of the paper, combining zigzag persistent homology and multiparameter persistent homology to capture features persistent with respect to both space and time.

### Approved Open Questions
- Scalable Computation of Extended Zigzag Landscapes: Computational efficiency is critical for applying topological summaries like persistence landscapes to high-dimensional or long time series in practical machine learning pipelines.

## Links

- [Abstract](https://arxiv.org/abs/2412.11925)
- [PDF](https://arxiv.org/pdf/2412.11925)

