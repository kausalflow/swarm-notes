---
# CSL-compatible fields
title: "When a High Score Is an Illusion: Certifying Genuine versus Repackaged Forecasting Skill"
author:
  - literal: "Pin Ni"
  - literal: "Francesca Medda"
  - literal: "Ramin Okhrati"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.19223"

# Custom fields
paper_id: "2609.19223"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "evaluation"
  - "benchmark"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-19T09:04:17Z"
created_at: "2026-09-19T09:04:17Z"
---

# When a High Score Is an Illusion: Certifying Genuine versus Repackaged Forecasting Skill

**Authors**: Pin Ni, Francesca Medda, Ramin Okhrati
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.19223](https://arxiv.org/abs/2609.19223)

## Summary

Ranks in time-series forecasting evaluations often depend on shared observations, creating an illusion of high skill through observation reuse rather than genuine predictive performance. This paper characterizes assignments that preserve association between population-rank contrasts and separates the expected score into its target and an interaction term between map pairs. The authors introduce unbiased kernel and U-statistic estimators along with sharp shared-baseline ranges, demonstrating empirically that interaction can account for over 90% of expected shared scores in air-quality forecasting archives.

## Key Contributions

- Characterizes rank-preserving assignments that maintain association between specified population-rank contrasts under shared baseline evaluation.
- Proposes an unbiased three-trajectory kernel and complete U-statistics to estimate the interaction term separating expected scores.
- Demonstrates on a Beijing air-quality archive that interaction accounts for 91.4% to 94.5% of learned forecasts' expected shared scores.
- Shows in a matched category-control null experiment that distinct references reduce false rejections from 402 to 41 out of 1,000 panels.

## Archivist Review

Applied strict review standards: no concepts or datasets met the rigorous standards for permanent standalone vault notes, and the candidate open question lacked sufficient specificity and technical depth.

### Rejected Candidates
- [open_question] Joint Calibration in Forecast Ranks (`joint-calibration-rank-forecasts`) - low_impact: The proposed open question is vague and does not target a specific unresolved technical bottleneck or concrete mechanism discussed in the paper.

## Links

- [Abstract](https://arxiv.org/abs/2609.19223)
- [PDF](https://arxiv.org/pdf/2609.19223)

