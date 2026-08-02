---
# CSL-compatible fields
title: "ExSEnt: Extrema-Segmented Entropy analysis of time series"
author:
  - literal: "Sara Kamali"
  - literal: "Fabiano Baroni"
  - literal: "Pablo Varona"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2509.07751"

# Custom fields
paper_id: "2509.07751"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "entropy"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "extrema-segmented-entropy"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-02T07:26:19Z"
created_at: "2026-08-02T07:26:19Z"
---

# ExSEnt: Extrema-Segmented Entropy analysis of time series

**Authors**: Sara Kamali, Fabiano Baroni, Pablo Varona
**Date**: 2026-07-30
**Paper ID**: [openalex:2509.07751](https://arxiv.org/abs/2509.07751)

## Summary

The authors introduce Extrema-Segmented Entropy (ExSEnt), a framework for time-series complexity analysis that partitions signals into monotonic segments to decouple temporal duration variability from amplitude variability. By computing sample entropy and joint entropy on these separate sequences, ExSEnt provides an interpretable measure of complexity drivers. The method is validated on nonlinear dynamical systems tracking chaotic transitions and on physiological datasets such as electromyography and Parkinson's disease accelerometer recordings.

## Key Contributions

- Introduces ExSEnt, a feature-decomposed complexity framework separating temporal and amplitude contributions in time series via monotonic segment partitioning.
- Applies sample entropy and joint entropy to duration and amplitude sequences to isolate whether variability is driven by timing, magnitude, or their coupling.
- Validates ExSEnt on canonical nonlinear dynamical systems (Logistic map, Rössler system, Rulkov map) tracking regular-to-chaotic regime transitions.
- Demonstrates empirical utility on physiological time series (electromyography and ankle acceleration in Parkinson's disease).

## Open Questions & Future Work

- [[multiscale-feature-decomposed-entropy]]

## Key Concepts

- [[extrema-segmented-entropy]]: A feature-decomposed framework for quantifying time-series complexity by separating temporal and amplitude contributions through monotonic segment partitioning.

## Archivist Review

Approved the core Extrema-Segmented Entropy framework concept and its corresponding open question on multiscale feature-decomposed entropy extensions. No datasets met the strict novelty and standalone archival standards.

### Approved Concepts
- Extrema-Segmented Entropy: It introduces a novel framework for complexity quantification by decomposing time series into monotonic segments and evaluating duration and amplitude entropy separately.

### Approved Open Questions
- Multiscale Feature-Decomposed Entropy Bounds: Extending feature-decomposed entropy to multiple scales is critical for robust analysis of complex physiological and geophysical signals where temporal dynamics operate across hierarchical frequency bands.

## Links

- [Abstract](https://arxiv.org/abs/2509.07751)
- [PDF](https://arxiv.org/pdf/2509.07751)

