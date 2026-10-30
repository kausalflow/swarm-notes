---
# CSL-compatible fields
title: "Identifying and disentangling direct and spillover effects using multiple pre-treatment periods"
author:
  - literal: "Martin Huber"
issued:
  date-parts:
    - [2026, 10, 27]
url: "https://arxiv.org/abs/2610.37049"

# Custom fields
paper_id: "2610.37049"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
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
processed_at: "2026-10-30T11:06:06Z"
created_at: "2026-10-30T11:06:06Z"
---

# Identifying and disentangling direct and spillover effects using multiple pre-treatment periods

**Authors**: Martin Huber
**Date**: 2026-10-27
**Paper ID**: [openalex:2610.37049](https://arxiv.org/abs/2610.37049)

## Summary

This paper proposes a causal inference framework for identifying and disentangling direct and spillover treatment effects under interference using multiple pre-treatment periods without requiring an uncontaminated comparison group. By leveraging no-anticipation assumptions and interrupted time-series extrapolation, the method recovers counterfactual trends for both treated and non-treated groups. The authors derive doubly robust and Neyman-orthogonal estimators that accommodate machine learning for covariate adjustment and establish asymptotic normality. Finally, simulations verify the root-n behavior, and an empirical application to 1919 US patent licensing demonstrates that conventional comparison-group designs can underestimate total effects due to spillover.

## Key Contributions

- Demonstrates that direct and spillover treatment effects are separately identifiable using multiple pre-treatment periods even without an uncontaminated comparison group
- Develops doubly robust and Neyman-orthogonal estimators allowing covariate control via machine learning with established asymptotic normality
- Applies the framework to the 1919 compulsory licensing of enemy-owned patents in the US, showing that a comparison-group design understates the total effect due to technological spillover

## Open Questions & Future Work

- [[relaxing-effect-homogeneity-and-common-support-under-interference]]

## Archivist Review

Applied strict filtering policies requiring concepts and questions to be central to time-series forecasting or machine learning methodology. Since the paper focuses on econometric causal inference with interference and pre-treatment periods rather than time-series prediction, concepts were rejected and the single open question was retained or categorized under low impact.

### Approved Open Questions
- Relaxing Assumptions for Causal Decompositions: This determines the methodological boundary between identifying aggregate intervention impacts and recovering structural direct vs. spillover components in observational network settings.

### Rejected Candidates
- [open_question] Relaxing Assumptions for Causal Decompositions (`relaxing-effect-homogeneity-and-common-support-under-interference`) - low_impact: The paper's causal inference framework and identifying assumptions are primarily econometrics and causal inference methodology rather than core time-series forecasting or machine learning architecture.

## Links

- [Abstract](https://arxiv.org/abs/2610.37049)
- [PDF](https://arxiv.org/pdf/2610.37049)

