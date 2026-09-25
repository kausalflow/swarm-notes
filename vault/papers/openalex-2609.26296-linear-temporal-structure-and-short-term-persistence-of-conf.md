---
# CSL-compatible fields
title: "Linear Temporal Structure and Short-Term Persistence of Conflict Activity in Middle Eastern Countries"
author:
  - literal: "Hyuntae Ahn"
  - literal: "Mi Jin Lee"
issued:
  date-parts:
    - [2026, 9, 22]
url: "https://arxiv.org/abs/2609.26296"

# Custom fields
paper_id: "2609.26296"
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
processed_at: "2026-09-25T09:55:30Z"
created_at: "2026-09-25T09:55:30Z"
---

# Linear Temporal Structure and Short-Term Persistence of Conflict Activity in Middle Eastern Countries

**Authors**: Hyuntae Ahn, Mi Jin Lee
**Date**: 2026-09-22
**Paper ID**: [openalex:2609.26296](https://arxiv.org/abs/2609.26296)

## Summary

This paper examines the linear temporal structure and short-term persistence of conflict-frequency time series across Middle Eastern countries using the ARIMA framework and correlation metrics. The authors find that linear temporal dependence is largely captured by ARIMA models, though abrupt changes remain hard to predict. Furthermore, short-term persistence metrics—such as the first zero-crossing point and integrated correlation time—show a significant negative association with mean GDP per capita, linking conflict dynamics to socioeconomic factors.

## Key Contributions

- Demonstrates that conflict-frequency time series in Middle Eastern countries exhibit measurable linear temporal structure largely captured by the ARIMA framework.
- Quantifies short-term persistence of conflict activity using the first zero-crossing point and integrated correlation time, revealing persistence ranges of 2--6 days and 0.6--1.7 days respectively.
- Identifies a significant negative association between integrated correlation time and mean GDP per capita, linking short-term conflict persistence to socioeconomic conditions.

## Limitations

Abrupt changes in conflict activity remain difficult to predict under simple linear autoregressive models.

## Open Questions & Future Work

- [[magnitude-weighted-conflict-networks]]

## Archivist Review

Applied strict selection criteria, rejecting the application-specific conflict network open question as too narrow and domain-local for a general ML knowledge vault.

### Approved Open Questions
- Magnitude-Weighted Conflict Networks: Addressing event magnitude weighting and cross-country conflict networks is critical for moving beyond simple frequency baselines to capture the true intensity and propagation dynamics of regional conflicts.

### Rejected Candidates
- [open_question] Magnitude-Weighted Conflict Networks (`magnitude-weighted-conflict-networks`) - low_impact: The paper evaluates standard linear temporal structures using ARIMA, making this open question domain-specific to conflict modeling rather than a broad forecasting or time-series bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2609.26296)
- [PDF](https://arxiv.org/pdf/2609.26296)

