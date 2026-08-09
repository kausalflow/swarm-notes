---
# CSL-compatible fields
title: "Variable-Horizon Workforce Demand Forecasting with an Aggregate Demand Constraint for Construction Workforce Planning"
author:
  - literal: "Hanbyeol Park"
  - literal: "Jaehyeon Heo"
  - literal: "Taekhyun Park"
  - literal: "Minseong Kim"
  - literal: "Hyerim Bae"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05551"

# Custom fields
paper_id: "2608.05551"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "constraint-preserving-residual-allocation-forecasting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:17Z"
created_at: "2026-08-09T05:40:17Z"
---

# Variable-Horizon Workforce Demand Forecasting with an Aggregate Demand Constraint for Construction Workforce Planning

**Authors**: Hanbyeol Park, Jaehyeon Heo, Taekhyun Park, Minseong Kim, Hyerim Bae
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05551](https://arxiv.org/abs/2608.05551)

## Summary

This paper introduces constraint-preserving residual allocation forecasting (CP-RAF), a method designed for construction workforce planning that handles variable forecast horizons and satisfies a pre-specified aggregate demand constraint. CP-RAF retrieves similar completed tasks using temporal shape representations, estimates remaining allocation profiles through similarity-weight averaging, and distributes predetermined demand accordingly. Evaluations on construction field data show that CP-RAF outperforms traditional machine learning baselines across both fixed and variable forecasting horizons.

## Key Contributions

- Proposes constraint-preserving residual allocation forecasting (CP-RAF) to handle variable forecast horizons and aggregate demand constraints in construction workforce planning.
- Utilizes similarity-weight averaging of completed tasks with similar temporal shapes to estimate allocation profiles over remaining durations.
- Demonstrates superior performance over eight baseline models in medium- and long-horizon fixed-length forecasting while maintaining low error under variable-length forecasting.

## Limitations

Evaluated specifically on construction workforce field data; generalizability to other resource-constrained scheduling domains remains to be explored.

## Open Questions & Future Work

- [[multivariate-extension-cp-raf]]

## Key Concepts

- [[constraint-preserving-residual-allocation-forecasting]]: A forecasting method for workforce planning that accommodates variable forecast horizons while preserving aggregate demand constraints via similarity-weight averaging and residual allocation.

## Archivist Review

Approved the overarching constraint-preserving residual allocation forecasting framework as a novel concept and retained its natural multivariate extension open question. Rejected subcomponents and generic anomaly filtering suggestions in accordance with vault scarcity and specificity principles.

### Approved Concepts
- Constraint-Preserving Residual Allocation Forecasting: Introduces a novel framework to handle variable forecast horizons and aggregate demand constraints in construction workforce planning.

### Approved Open Questions
- Multivariate Extension of CP-RAF: Extending similarity-based residual allocation to multivariate settings is crucial for accounting for multi-resource dependencies and project context in complex operational planning.

### Rejected Candidates
- [concept] Aggregate Demand Constraint (`aggregate-demand-constraint`) - subcomponent_of_broader_mechanism: Standard operational constraint formulation rather than a reusable algorithmic mechanism.
- [open_question] Anomaly Detection for Workforce Forecasting (`anomaly-detection-workforce-forecasting`) - weak_evidence: Generic future work direction regarding anomaly filtering rather than a specific unresolved methodological bottleneck.

## Links

- [Abstract](https://arxiv.org/abs/2608.05551)
- [PDF](https://arxiv.org/pdf/2608.05551)

