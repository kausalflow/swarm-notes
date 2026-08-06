---
# CSL-compatible fields
title: "Statistical comparisons of time-series feature sets on classification tasks"
author:
  - literal: "Trent Henderson"
  - literal: "Ben Fulcher"
issued:
  date-parts:
    - [2026, 8, 3]
url: "https://arxiv.org/abs/2608.01586"

# Custom fields
paper_id: "2608.01586"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "text-classification"
  - "benchmark"
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
processed_at: "2026-08-06T07:31:24Z"
created_at: "2026-08-06T07:31:24Z"
---

# Statistical comparisons of time-series feature sets on classification tasks

**Authors**: Trent Henderson, Ben Fulcher
**Date**: 2026-08-03
**Paper ID**: [openalex:2608.01586](https://arxiv.org/abs/2608.01586)

## Summary

This paper presents a comprehensive empirical comparison of six open-source time-series feature sets and three baseline sets across 124 univariate time-series classification problems, utilizing a normalization-based benchmarking approach. The authors find that while feature sets perform similarly overall (with 85.3% pairwise ties), the largest set, tsfresh, achieves the highest overall win rate of 29.03%. Furthermore, the study identifies specific domains and problems where simpler baseline features, such as Fourier coefficients and quantiles, are sufficient for strong classification performance.

## Key Contributions

- Evaluated the relative classification performance of six open-source time-series feature sets and three baseline sets across 124 univariate time-series classification problems
- Introduced a normalization-based approach for problem-level benchmarking to better index relative algorithmic strengths and weaknesses compared to rank-based methods
- Demonstrated that despite dramatic differences in size and composition, feature sets performed similarly overall (85.3% pairwise ties), with tsfresh achieving the strongest overall performance (29.03% wins)
- Highlighted specific problem categories where simple baseline features like Fourier coefficients and quantiles matched complex feature sets

## Open Questions & Future Work

- [[feature-sets-regression-forecasting]]

## Archivist Review

The paper provides an empirical comparison of existing time-series feature sets across classification tasks using normalization-based benchmarking. No standalone vault concepts were approved because the work evaluates existing libraries rather than proposing a reusable algorithmic primitive, architecture, or representation. One open question regarding extending feature set benchmarking to regression and forecasting was approved as it directly connects classification feature evaluations to forecasting tasks.

### Approved Open Questions
- Feature Sets for Regression and Forecasting: Extends the benchmarking methodology to other foundational time-series tasks, testing whether feature set performance trends translate beyond classification.

### Rejected Candidates
- [open_question] Constructing Bespoke Reduced Feature Sets (`bespoke-reduced-feature-sets`) - low_impact: Standard incremental future work proposing a combined feature set.
- [open_question] Domain-Tailored Baseline Feature Sets (`domain-tailored-baseline-features`) - low_impact: Standard future work suggestion about tailoring baselines to additional domains without a distinct algorithmic mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2608.01586)
- [PDF](https://arxiv.org/pdf/2608.01586)

