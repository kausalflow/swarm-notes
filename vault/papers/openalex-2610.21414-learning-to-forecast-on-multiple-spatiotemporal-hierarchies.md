---
# CSL-compatible fields
title: "Learning to Forecast on Multiple Spatiotemporal Hierarchies"
author:
  - literal: "Valentina Moretti"
  - literal: "Cesare Alippi"
  - literal: "Andrea Cini"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21414"

# Custom fields
paper_id: "2610.21414"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "graph-neural-network"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-18T09:12:43Z"
created_at: "2026-10-18T09:12:43Z"
---

# Learning to Forecast on Multiple Spatiotemporal Hierarchies

**Authors**: Valentina Moretti, Cesare Alippi, Andrea Cini
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21414](https://arxiv.org/abs/2610.21414)

## Summary

Hierarchical forecasting typically relies on a single fixed aggregation structure, limiting generalization across different spatiotemporal scales. This work proposes a graph deep learning framework that trains models jointly across multiple hierarchies as multi-task regularization to learn robust, generalizable representations. To address the computational burden of ensuring forecast coherence, the authors introduce a novel top-down operator achieving linear time and space complexity with respect to hierarchy size. Experiments demonstrate that this multi-hierarchy approach improves forecasting accuracy compared to training on a single structure.

## Key Contributions

- Proposes a graph deep learning framework that leverages variations across multiple spatiotemporal hierarchies as multi-task regularization to prevent over-specialization and improve generalization.
- Introduces a novel top-down operator that produces coherent forecasts across aggregation constraints with linear time and space complexity with respect to the hierarchy size.
- Demonstrates through experiments that multi-hierarchy training improves forecasting accuracy over single-structure baselines and competes effectively with state-of-the-art methods.

## Archivist Review

No novel reusable concepts or datasets meet the rigorous threshold for inclusion.

## Links

- [Abstract](https://arxiv.org/abs/2610.21414)
- [PDF](https://arxiv.org/pdf/2610.21414)

