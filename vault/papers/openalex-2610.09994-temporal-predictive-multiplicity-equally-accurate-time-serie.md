---
# CSL-compatible fields
title: "Temporal Predictive Multiplicity: Equally Accurate Time Series Models Yield Different Forecast Trajectories"
author:
  - literal: "Emanuele Albini"
  - literal: "Francesca Toni"
  - literal: "Saumitra Mishra"
  - literal: "Francesco Leofante"
issued:
  date-parts:
    - [2026, 10, 7]
url: "https://arxiv.org/abs/2610.09994"

# Custom fields
paper_id: "2610.09994"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "temporal-predictive-multiplicity"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:33:58Z"
created_at: "2026-10-09T11:33:58Z"
---

# Temporal Predictive Multiplicity: Equally Accurate Time Series Models Yield Different Forecast Trajectories

**Authors**: Emanuele Albini, Francesca Toni, Saumitra Mishra, Francesco Leofante
**Date**: 2026-10-07
**Paper ID**: [openalex:2610.09994](https://arxiv.org/abs/2610.09994)

## Summary

This paper investigates temporal predictive multiplicity in time-series forecasting, demonstrating that models with nearly identical predictive performance can produce substantially different forecast trajectories across horizons. The authors introduce a dedicated framework to characterize trajectory-level disagreement and evaluate 19 neural forecasting architectures across 11 datasets, revealing that horizon-wise comparisons fail to capture this broader variability.

## Key Contributions

- Introduces temporal predictive multiplicity, a framework characterizing disagreement over complete forecast trajectories among models with near-identical predictive performance.
- Demonstrates that constraining predictive performance or horizon-wise multiplicity alone still admits a broad range of different forecast trajectories.
- Evaluates 19 neural forecasting architectures across 11 datasets, showing that near-optimal models exhibit substantial variability in trajectories and that trajectory-level disagreement is largely independent of horizon-wise disagreement.

## Open Questions & Future Work

- [[probabilistic-temporal-multiplicity]]

## Key Concepts

- [[temporal-predictive-multiplicity]]: A framework characterizing disagreement over complete forecast trajectories among time-series models with near-identical predictive performance.

## Archivist Review

Approved the overarching concept of temporal predictive multiplicity and its natural extension to probabilistic forecasting. All other candidates were omitted to maintain strict selectivity.

### Approved Concepts
- Temporal Predictive Multiplicity: It establishes a foundational framework and definition for studying trajectory-level model disagreement across multiple forecasting horizons among near-optimal models.

### Approved Open Questions
- Probabilistic Temporal Predictive Multiplicity: Crucial for reliable decision-making under uncertainty, as models with identical aggregate point performance may assign radically different probabilities to tail events.

### Rejected Candidates
- [concept] Temporal Predictive Multiplicity (`temporal-predictive-multiplicity`) - other: approved
- [open_question] Probabilistic Temporal Predictive Multiplicity (`probabilistic-temporal-multiplicity`) - other: approved

## Links

- [Abstract](https://arxiv.org/abs/2610.09994)
- [PDF](https://arxiv.org/pdf/2610.09994)

