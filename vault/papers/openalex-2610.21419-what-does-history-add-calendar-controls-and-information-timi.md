---
# CSL-compatible fields
title: "What Does History Add? Calendar Controls and Information-Timing Audits for University Trajectory Forecasting"
author:
  - literal: "Zepei Cao"
issued:
  date-parts:
    - [2026, 10, 15]
url: "https://arxiv.org/abs/2610.21419"

# Custom fields
paper_id: "2610.21419"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "evaluation"
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
processed_at: "2026-10-18T09:13:25Z"
created_at: "2026-10-18T09:13:25Z"
---

# What Does History Add? Calendar Controls and Information-Timing Audits for University Trajectory Forecasting

**Authors**: Zepei Cao
**Date**: 2026-10-15
**Paper ID**: [openalex:2610.21419](https://arxiv.org/abs/2610.21419)

## Summary

This paper presents an evaluation audit of historical summaries in a rule-based university trajectory simulator across seventeen ridge specifications and persistence models. Using 16,750 routes and 804,000 monthly records, the author finds that while six-month history improves raw prediction error over current-state baselines, its advantage largely vanishes when compared against calendar-length-only controls. Exploratory decomposition further exposes component-specific performance variations, such as preparation-index gains versus high support violation rates in fatigue predictions.

## Key Contributions

- Evaluates predictive value of historical summaries using seventeen ridge specifications and persistence in a university trajectory simulator across 16,750 routes and 804,000 monthly records.
- Demonstrates that six-month history reduces six-step normalized RMSE from 0.159234 to 0.151522, but performs similarly to a length-only control with a difference of -0.000895.
- Finds that exploratory decomposition reveals clear preparation-index and funds benefits, whereas fatigue dominates loss and shows uncertain length-controlled benefit with 28.20% support violations.

## Limitations

Evaluates a rule-based university trajectory simulator conditioning on recorded future plans rather than real-student forecasts, causal action effects, autonomous planning, or language-model memory.

## Open Questions & Future Work

- [[real-world-educational-validation]]

## Archivist Review

Reviewed the paper analysis and confirmed that no novel, reusable forecasting concepts or datasets qualify for standalone vault notes. The single proposed open question regarding real-world educational validation is approved as it addresses the generalizability of simulation-based trajectory auditing.

### Approved Open Questions
- Real-World Educational Validation: Crucial for ensuring that findings from controlled simulation environments translate to actual empirical student performance and robust educational decision-making.

### Rejected Candidates
- [open_question] Real-World Educational Validation (`real-world-educational-validation`) - other: The candidate was approved instead of rejected.

## Links

- [Abstract](https://arxiv.org/abs/2610.21419)
- [PDF](https://arxiv.org/pdf/2610.21419)

