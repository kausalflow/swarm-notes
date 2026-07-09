---
# CSL-compatible fields
title: "Physically-Relevant Information Learning in High-Dimensional Time-Derivatives Spaces"
author:
  - literal: "Domiziano Doria"
  - literal: "Matteo Becchi"
  - literal: "G. M. Pavan"
issued:
  date-parts:
    - [2026, 7, 6]
url: "https://arxiv.org/abs/2607.05127"

# Custom fields
paper_id: "2607.05127"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-derivatives-tide-space"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-09T08:19:39Z"
created_at: "2026-07-09T08:19:39Z"
---

# Physically-Relevant Information Learning in High-Dimensional Time-Derivatives Spaces

**Authors**: Domiziano Doria, Matteo Becchi, G. M. Pavan
**Date**: 2026-07-06
**Paper ID**: [openalex:2607.05127](https://arxiv.org/abs/2607.05127)

## Summary

This paper introduces the Time-Derivatives (TiDe) space, a novel analytical framework for studying complex many-body dynamical systems directly from time-series data. By mapping observations into a high-dimensional space where each dimension corresponds to a successive order of the time derivative, the approach captures the interplay between system structure and dynamics. The authors demonstrate that this method allows for unsupervised feature extraction and intuitive physical interpretation without the need for traditional dimensionality reduction techniques. The effectiveness of the approach is validated on datasets from molecular dynamics and experimental tracking.

## Key Contributions

- Introduces the Time-Derivatives (TiDe) space framework, which encodes information from growing-order time derivatives to capture both structural and dynamical properties of complex systems.
- Demonstrates that TiDe spaces enable direct analysis and unsupervised feature extraction without requiring prior dimensionality reduction.
- Validates the framework's interpretability and robustness using datasets derived from molecular dynamics simulations and experimental tracking of dynamical systems.

## Open Questions & Future Work

- [[effective-tide-dimensionality-determination]]

## Key Concepts

- [[time-derivatives-tide-space]]: A high-dimensional analysis space where each dimension represents a growing-order time derivative of observed system data to capture both structural and dynamical physical information.

## Archivist Review

I approved the TiDe space concept as it offers a distinct, physically-motivated approach to embedding time series that challenges standard deep-learning-based dimensionality reduction methods. I also approved the open question regarding effective dimensionality determination, as it addresses a key technical bottleneck regarding noise accumulation in derivative-based state representations.

### Approved Concepts
- Time-Derivatives (TiDe) Space: Provides a novel, interpretable framework for analyzing complex dynamical systems by mapping time-series data to spaces defined by growing-order time derivatives, bypassing traditional dimensionality reduction.

### Approved Open Questions
- Determining Effective TiDe Dimensionality: Establishing a robust, universal heuristic for determining the effective TiDe dimensionality is critical to preventing 'information frustration' and performance degradation caused by adding redundant or noise-dominated dimensions in large-scale applications.

## Links

- [Abstract](https://arxiv.org/abs/2607.05127)
- [PDF](https://arxiv.org/pdf/2607.05127)

