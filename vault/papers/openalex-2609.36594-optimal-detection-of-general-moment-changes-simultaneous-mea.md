---
# CSL-compatible fields
title: "Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond"
author:
  - literal: "Xiaokai Luo"
  - literal: "ChenghaoXu"
  - literal: "Haotian Xu"
  - literal: "Carlos Misael Madrid Padilla"
  - literal: "Daren Wang"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.36594"

# Custom fields
paper_id: "2609.36594"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:47:58Z"
created_at: "2026-10-02T10:47:58Z"
---

# Optimal detection of general moment changes: Simultaneous mean and covariance change detection and beyond

**Authors**: Xiaokai Luo, ChenghaoXu, Haotian Xu, Carlos Misael Madrid Padilla, Daren Wang
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.36594](https://arxiv.org/abs/2609.36594)

## Summary

The paper investigates multiple change-point detection in multivariate time series undergoing piecewise constant distributional shifts across arbitrary moment orders, extending beyond traditional mean and covariance changes. By introducing a unified tensor representation for moments up to order p, the authors develop a detection procedure that accommodates temporal dependence and high-dimensional growth. Theoretical analysis proves the procedure achieves a localization error rate matching a newly established minimax lower bound. Furthermore, limiting distributions and asymptotically valid confidence intervals are derived for both vanishing and nonvanishing moment jumps, with empirical validation on numerical and real-world data.

## Key Contributions

- Proposes a tensor representation framework that unifies multivariate time series moments of various orders up to a prescribed order p for change-point detection.
- Establishes a minimax lower bound for moment change localization and proves the proposed procedure achieves the optimal localization error rate under temporal dependence and high-dimensional settings.
- Derives limiting distributions under both nonvanishing and vanishing moment jumps and constructs asymptotically valid confidence intervals for the vanishing-jump regime.

## Archivist Review

Applied strict selectivity: no permanent standalone notes are warranted as the single proposed open question is essentially a restatement of the paper's core contribution rather than an independent, recurring research bottleneck.

### Rejected Candidates
- [open_question] Optimal Detection of General Moment Changes (`optimal-detection-of-general-moment-changes`) - paper_local: Too broad and essentially mirrors the paper's overarching title and core theme without posing a specific, actionable future research bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.36594)
- [PDF](https://arxiv.org/pdf/2609.36594)

