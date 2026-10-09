---
# CSL-compatible fields
title: "High-dimensional online calibration from harmonic weights"
author:
  - literal: "Maxwell Fishelson"
  - literal: "Mehryar Mohri"
issued:
  date-parts:
    - [2026, 10, 6]
url: "https://arxiv.org/abs/2610.07740"

# Custom fields
paper_id: "2610.07740"
paper_source: "openalex"
domain: "nlp"
tags:
  - "calibration"
  - "online-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-09T11:36:13Z"
created_at: "2026-10-09T11:36:13Z"
---

# High-dimensional online calibration from harmonic weights

**Authors**: Maxwell Fishelson, Mehryar Mohri
**Date**: 2026-10-06
**Paper ID**: [openalex:2610.07740](https://arxiv.org/abs/2610.07740)

## Summary

This paper studies the online calibration of multidimensional forecasts over arbitrary convex sets and error norms. The authors introduce a simple algorithm using harmonically weighted distributions over smoothed past outcomes that achieves $\varepsilon$-calibration in a number of rounds polynomial in dimension $d$ for fixed accuracy, specifically $d^{O(1/\varepsilon)}$ for binary outcomes and multi-class forecasting. This significantly improves upon the exponential dimension dependence of previous bounds. The theoretical analysis relies on a matrix discrepancy problem where the discrete Hilbert transform matrix is shown to achieve optimal discrepancy simultaneously for all norms.

## Key Contributions

- Proposes the first algorithm for online calibration of $d$ binary outcomes achieving $\varepsilon$-calibration in $d^{O(1/\varepsilon)}$ rounds, exponentially improving prior bounds.
- Obtains a $d^{O(1/\varepsilon)}$ rate for multi-class forecasting ($Y=\Delta_d$), improving previous $d^{\widetilde{O}(1/\varepsilon^2)}$ bounds.
- Establishes a general convergence rate of $\exp(O(\gamma(Y,L)/\varepsilon))$ rounds for arbitrary convex sets $Y$ and error norms $L$, governed by a matrix discrepancy parameter.
- Proves that the discrete Hilbert transform matrix achieves optimal discrepancy up to a universal constant simultaneously for every norm $L$.

## Archivist Review

Applied strict selection criteria, keeping the vault focused on genuinely novel time-series and forecasting paradigms while rejecting paper-local theoretical open questions.

### Rejected Candidates
- [open_question] Norm Ball Geometric Coefficient Limits (`norm-ball-geometric-coefficient-limits-calibration`) - not_novel: not_novel

## Links

- [Abstract](https://arxiv.org/abs/2610.07740)
- [PDF](https://arxiv.org/pdf/2610.07740)

