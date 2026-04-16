---
# CSL-compatible fields
title: "Detection and Mode-Identification of Multiple Change Points in Tensor Factor Models"
author:
  - literal: "Yuqi Zhang"
  - literal: "Zetai Cen"
  - literal: "Haeran Cho"
issued:
  date-parts:
    - [2026, 4, 13]
url: "https://arxiv.org/abs/2604.11300"

# Custom fields
paper_id: "2604.11300"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mode-identifiability-of-tensor-change-points"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-16T06:29:21Z"
created_at: "2026-04-16T06:29:21Z"
---

# Detection and Mode-Identification of Multiple Change Points in Tensor Factor Models

**Authors**: Yuqi Zhang, Zetai Cen, Haeran Cho
**Date**: 2026-04-13
**Paper ID**: [openalex:2604.11300](https://arxiv.org/abs/2604.11300)

## Summary

This paper addresses the challenge of identifying and localizing multiple structural change points in high-dimensional tensor-valued time series modeled via Tucker decomposition. The authors introduce a two-stage framework: first, an efficient algorithm detects the timing of multiple structural breaks; second, a mode-identification procedure determines which specific tensor modes are affected by each shift. Theoretical consistency is established under weak moment conditions, and the method is validated on simulated data as well as New York City taxi usage and Fama-French portfolio return datasets. The results show that mode-identifiable shift detection significantly enhances the accuracy of subsequent mode-wise loading space estimation.

## Key Contributions

- Proposes a computationally efficient algorithm for detecting multiple structural change points in high-dimensional tensor-valued time series based on Tucker decomposition.
- Formalizes the concept of mode-identifiability to pinpoint specific tensor modes undergoing structural shifts.
- Establishes theoretical consistency for both change point detection and mode-identification under weak moment conditions.
- Demonstrates improved post-segmentation estimation of mode-wise loading spaces through the proposed mode-identification method on both simulated and real-world data.

## Key Concepts

- [[mode-identifiability-of-tensor-change-points]]: A formal framework for identifying which specific modes of a Tucker decomposition-based tensor factor model are affected by a detected structural change.

## Archivist Review

The paper contributes a novel formalization of mode-specific structural shifts in tensor data, which addresses a gap in high-dimensional time-series analysis. I approved the mode-identifiability concept as it offers a generalizable mechanism for interpreting change points in multi-way data. Other potential concepts were rejected for being overly descriptive of the task domain rather than representing a distinct reusable methodology.

### Approved Concepts
- Mode-Identifiability of Tensor Change Points: Provides a rigorous framework for localizing structural breaks in multi-dimensional tensor time series, which is essential for high-dimensional model interpretability.

### Rejected Candidates
- [concept] Tensor Factor Model Change Point Detection (`tensor-factor-model-change-point-detection`) - subcomponent_of_broader_mechanism: This is a problem domain description rather than a distinct reusable method, and it is largely subsumed by the specific mode-identifiability concept approved.

## Links

- [Abstract](https://arxiv.org/abs/2604.11300)
- [PDF](https://arxiv.org/pdf/2604.11300)

