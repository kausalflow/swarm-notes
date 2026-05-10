---
# CSL-compatible fields
title: "Socio-Conformal Calibration in Complex Survey Data: Marginal Validity Is Not Enough for Subgroup Reliability"
author:
  - literal: "Amir Rafe"
  - literal: "Subasish Das"
issued:
  date-parts:
    - [2026, 5, 7]
url: "https://arxiv.org/abs/2605.05562"

# Custom fields
paper_id: "2605.05562"
paper_source: "openalex"
domain: "nlp,social-science"
tags:
  - "conformal-prediction"
  - "fairness"
  - "survey-data"
  - "uncertainty-estimation"
  - "forecasting"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "socio-conformal-calibration"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-10T07:23:34Z"
created_at: "2026-05-10T07:23:34Z"
---

# Socio-Conformal Calibration in Complex Survey Data: Marginal Validity Is Not Enough for Subgroup Reliability

**Authors**: Amir Rafe, Subasish Das
**Date**: 2026-05-07
**Paper ID**: [openalex:2605.05562](https://arxiv.org/abs/2605.05562)

## Summary

This paper examines the limitations of standard conformal prediction in survey-based social forecasting, specifically concerning subgroup reliability. Using the Pew American Trends Panel, the authors demonstrate that while standard methods achieve aggregate marginal coverage, they fail to maintain parity across race-education subgroups. The study finds that naive group-specific calibration (Mondrian) often degrades fairness-efficiency trade-offs, and proposes a regularized approach to mitigate instability. The results suggest that nominal marginal validity is an insufficient metric for ensuring fairness in high-stakes social measurement applications.

## Key Contributions

- Demonstrates that nominal marginal conformal validity leads to significant subgroup coverage gaps in survey-based social measurement.
- Shows that naive Mondrian (group-specific) conformal calibration can exacerbate fairness-efficiency trade-offs by increasing both set size and subgroup coverage instability.
- Introduces a regularized Mondrian comparator to shrink group-specific thresholds toward global quantiles, providing a more stable, though not perfectly fair, alternative.

## Open Questions & Future Work

- [[survey-weighted-conformal-calibration-theory]]

## Key Concepts

- [[socio-conformal-calibration]]: A framework for evaluating and adjusting conformal prediction reliability across population subgroups in complex survey data.

## Archivist Review

The paper addresses a significant, underexplored tension between marginal coverage and subgroup reliability in conformal prediction. I approved the proposed 'Socio-Conformal Calibration' concept as it captures this fairness-aware calibration paradigm, and the open question regarding survey-weighted calibration theory as it identifies a concrete, substantial technical bottleneck. Datasets were rejected as they were either too specific to the paper's study or not widely reusable benchmarks.

### Approved Concepts
- Socio-Conformal Calibration: Addresses the limitation of standard conformal prediction in providing reliable subgroup-specific uncertainty quantification, a critical issue for social and survey data.

### Approved Open Questions
- Survey-weighted conformal calibration theory: It is essential for maintaining statistical validity and demographic equity in population-representative inferences derived from high-stakes survey datasets.

## Links

- [Abstract](https://arxiv.org/abs/2605.05562)
- [PDF](https://arxiv.org/pdf/2605.05562)

