---
# CSL-compatible fields
title: "An Interval-Score ROC Curve for Assessment, Calibration and Ensembling of Probabilistic Forecasts"
author:
  - literal: "Simone Milanesi"
  - literal: "Marco Capelletti"
  - literal: "Flavio Bobba"
  - literal: "Giuseppe De Nicolao"
issued:
  date-parts:
    - [2026, 7, 30]
url: "https://arxiv.org/abs/2607.28178"

# Custom fields
paper_id: "2607.28178"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
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
processed_at: "2026-08-02T07:26:56Z"
created_at: "2026-08-02T07:26:56Z"
---

# An Interval-Score ROC Curve for Assessment, Calibration and Ensembling of Probabilistic Forecasts

**Authors**: Simone Milanesi, Marco Capelletti, Flavio Bobba, Giuseppe De Nicolao
**Date**: 2026-07-30
**Paper ID**: [openalex:2607.28178](https://arxiv.org/abs/2607.28178)

## Summary

Probabilistic forecast evaluation is traditionally reduced to single scalar scores, which can obscure trade-offs between forecast concentration and accuracy. This paper introduces the Interval-Score Receiver Operating Characteristic (IS-ROC) Curve, a graphical framework capturing the complete family of interval forecasts across varying tightness levels. The authors prove that the IS-ROC Curve induced by the data-generating process is Pareto optimal and convex, providing a geometric characterization of the optimal forecasting frontier. Building upon these geometric foundations, they propose a novel calibration procedure based on tangent optimization and a convex hull-based ensembling strategy for competing forecasters.

## Key Contributions

- Introduces the Interval-Score Receiver Operating Characteristic (IS-ROC) Curve as a graphical framework for multi-objective probabilistic forecast evaluation
- Establishes the Pareto optimality and convexity properties of the IS-ROC Curve induced by the data-generating process to characterize the optimal forecasting frontier
- Proposes a geometry-based calibration procedure using tangent optimization and convexification alongside an ensemble strategy via convex hull construction

## Archivist Review

Applied strict review standards, rejecting the single candidate open question because it represents routine future work exploring conditional extensions of a graphical evaluation tool rather than a major foundational research bottleneck. No permanent vault notes were created.

### Rejected Candidates
- [open_question] Conditional IS-ROC Curves (`conditional-is-roc-curves`) - low_impact: Standard future work direction proposing to extend the graphical framework to conditional covariates without exposing a deep architectural or methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2607.28178)
- [PDF](https://arxiv.org/pdf/2607.28178)

