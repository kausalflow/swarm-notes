---
# CSL-compatible fields
title: "Partial Multistep Prediction of Chaotic Time Series: What Remains Predictable beyond the Horizon of Predictability?"
author:
  - literal: "Vasilii A. Gromov"
  - literal: "Maksim Lomakin"
  - literal: "Aleksei Kudryashov"
  - literal: "Korney K. Tomashchuk"
issued:
  date-parts:
    - [2026, 10, 14]
url: "https://arxiv.org/abs/2610.20093"

# Custom fields
paper_id: "2610.20093"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-17T08:55:02Z"
created_at: "2026-10-17T08:55:02Z"
---

# Partial Multistep Prediction of Chaotic Time Series: What Remains Predictable beyond the Horizon of Predictability?

**Authors**: Vasilii A. Gromov, Maksim Lomakin, Aleksei Kudryashov, Korney K. Tomashchuk
**Date**: 2026-10-14
**Paper ID**: [openalex:2610.20093](https://arxiv.org/abs/2610.20093)

## Summary

This paper investigates partial multistep prediction for chaotic time series by omitting unreliable intermediate positions to prevent error propagation beyond the horizon of predictability. Using a lightweight pattern-based local predictor combined with an agreement-based ensemble, the method recovers long-horizon predictive information such as topological scroll identification in the Lorenz system even when precise geometric localization fails. Experiments across a heterogeneous collection of chaotic systems demonstrate that this ensemble strictly extends the positive-$R^2$ horizon relative to standard recursive baselines.

## Key Contributions

- Investigates partial multistep prediction by omitting intermediate steps in chaotic time series forecasting to bypass error propagation beyond the horizon of predictability.
- Demonstrates through experiments on the Lorenz system that an agreement-based ensemble recovers predictive topological information (identifying the occupied scroll) even when precise geometric accuracy is lost.
- Shows across a heterogeneous collection of chaotic systems that the agreement-based ensemble strictly extends the positive-$R^2$ horizon compared to the recursive baseline for every tested system.

## Archivist Review

Evaluated the submitted concepts and open questions against the rigorous vault standards. The proposed open questions relate too specifically to the paper's pattern-based masking implementation and heuristic weighting techniques rather than broader foundational challenges in time series forecasting. No concepts or datasets met the strict reusability criteria, so all candidates were archived as rejected.

### Rejected Candidates
- [open_question] Observable Trajectory Weighting Schemes (`observable-trajectory-weighting`) - low_impact: The question describes a paper-specific optimization gap rather than a broad, foundational bottleneck in time series forecasting.
- [open_question] Mask-Aware Predictors (`mask-aware-predictors`) - paper_local: The question focuses on implementation details of pattern enumeration for partial multistep predictors rather than a universal open research problem.

## Links

- [Abstract](https://arxiv.org/abs/2610.20093)
- [PDF](https://arxiv.org/pdf/2610.20093)

