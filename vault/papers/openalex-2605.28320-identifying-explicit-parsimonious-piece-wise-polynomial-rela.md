---
# CSL-compatible fields
title: "Identifying Explicit Parsimonious Piece-wise Polynomial Relationships in Industrial time-series: Application to manipulator robots"
author:
  - literal: "Mazen Alamir"
  - literal: "Sacha Clavel"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28320"

# Custom fields
paper_id: "2605.28320"
paper_source: "openalex"
domain: "robotics"
tags:
  - "time-series"
  - "anomaly-detection"
  - "interpretability"
  - "robotics"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:36:18Z"
created_at: "2026-05-30T07:36:18Z"
---

# Identifying Explicit Parsimonious Piece-wise Polynomial Relationships in Industrial time-series: Application to manipulator robots

**Authors**: Mazen Alamir, Sacha Clavel
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28320](https://arxiv.org/abs/2605.28320)

## Summary

This paper introduces a methodology for identifying parsimonious, explicit piece-wise polynomial relationships from complex, high-dimensional industrial time-series data. Building upon previous work in implicit relationship identification for anomaly detection, the approach provides interpretable explicit models by leveraging the polynomial components of implicit representations. The framework is evaluated on inverse modeling for 6-axis and 4-axis manipulator robots, showing that these parsimonious models generalize more effectively to unseen operational contexts than standard deep neural network architectures.

## Key Contributions

- Introduces an algorithm to extract parsimonious explicit piece-wise polynomial relationships from high-dimensional raw feature sets.
- Extends existing implicit identification frameworks to derive interpretable explicit models suitable for inverse kinematics modeling.
- Demonstrates superior generalization capabilities of the proposed parsimonious modeling approach over deep neural network structures in unseen robotic operating contexts.

## Open Questions & Future Work

- [[generalization-of-parsimonious-industrial-models]]

## Archivist Review

I applied a high bar for novelty and reusability, rejecting the proposed algorithmic approach as it appears to be a specific procedural extension of a previously existing, unnamed identification framework. The open question was approved after being refined to a more descriptive, canonical slug, as it identifies a substantive, non-trivial limitation in model generalization for industrial time-series.

### Approved Open Questions
- Generalization of Parsimonious Models: Generalization to unseen operational contexts remains a primary bottleneck for deploying data-driven industrial models, and understanding why specific model architectures fail on certain axes is essential for reliability.

### Rejected Candidates
- [open_question] Generalization of Parsimonious Models (`improving-generalization-industrial-piecewise-polynomials`) - duplicate_existing: Renamed to a more canonical slug and tightened for consistency.

## Links

- [Abstract](https://arxiv.org/abs/2605.28320)
- [PDF](https://arxiv.org/pdf/2605.28320)

