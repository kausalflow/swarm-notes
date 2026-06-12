---
# CSL-compatible fields
title: "PhysMetrics.Weather: An Evaluation Framework for Physical Consistency in ML Weather Models"
author:
  - literal: "Emma Kasteleyn"
  - literal: "Timo Maier"
  - literal: "Axel Lauer"
  - literal: "Veronika Eyring"
  - literal: "Pierre Gentine"
  - literal: "Ana Lučić"
issued:
  date-parts:
    - [2026, 6, 9]
url: "https://arxiv.org/abs/2606.10642"

# Custom fields
paper_id: "2606.10642"
paper_source: "openalex"
domain: "nlp"
tags:
  - "benchmark"
  - "evaluation"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "physmetrics-weather"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-12T08:54:13Z"
created_at: "2026-06-12T08:54:13Z"
---

# PhysMetrics.Weather: An Evaluation Framework for Physical Consistency in ML Weather Models

**Authors**: Emma Kasteleyn, Timo Maier, Axel Lauer, Veronika Eyring, Pierre Gentine, Ana Lučić
**Date**: 2026-06-09
**Paper ID**: [openalex:2606.10642](https://arxiv.org/abs/2606.10642)

## Summary

PhysMetrics.Weather addresses the reliance of machine learning weather prediction (MLWP) models on pure data-driven training and pixel-wise error metrics, which often result in physically inconsistent forecasts. The proposed framework provides a systematic evaluation suite covering conservation, spectral, and dynamical properties to quantify physical realism. This tool assists in developing physics-informed architectures and validates the reliability of models for operational meteorological applications.

## Key Contributions

- Introduces PhysMetrics.Weather, a comprehensive evaluation framework for quantifying physical consistency in machine learning weather prediction (MLWP) models.
- Defines a taxonomy of three metric categories—conservation, spectral, and dynamical—to move beyond standard pixel-wise error metrics like RMSE.
- Provides an open-source tool for guiding the development of physics-informed model architectures and assessing operational reliability.

## Open Questions & Future Work

- [[probabilistic-physical-consistency-evaluation]]

## Key Concepts

- [[physmetrics-weather]]: An evaluation framework that assesses the physical realism of machine learning weather prediction models using conservation, spectral, and dynamical metrics.

## Archivist Review

I approved the main framework as a central contribution and one open question regarding probabilistic consistency, as this represents a significant shift in ML weather modeling requirements. I rejected the variable scope extension question because it primarily reflects data infrastructure limitations rather than a foundational research gap in physical consistency evaluation.

### Approved Concepts
- PhysMetrics.Weather: Addresses the critical lack of physical consistency guarantees in data-driven machine learning weather prediction models.

### Approved Open Questions
- Evaluating Probabilistic Physical Consistency: As forecasting models shift toward generative architectures, evaluating only the mean state is insufficient, making probabilistic physical consistency essential for interpreting atmospheric variance.

### Rejected Candidates
- [open_question] Extending PhysMetrics.Weather Variable Scope (`extending-physmetrics-variable-scope`) - low_impact: This describes a limitation in data availability rather than a fundamental research bottleneck or unresolved methodological mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2606.10642)
- [PDF](https://arxiv.org/pdf/2606.10642)

