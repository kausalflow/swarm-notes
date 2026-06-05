---
# CSL-compatible fields
title: "Beyond Point Estimates: Reliable Evaluation of Prediction Performance Metrics under Clustered Data"
author:
  - literal: "Taekwon Hong"
  - literal: "Daeyoung Lim"
  - literal: "Woojung Bae"
issued:
  date-parts:
    - [2026, 6, 2]
url: "https://arxiv.org/abs/2606.03656"

# Custom fields
paper_id: "2606.03656"
paper_source: "openalex"
domain: "nlp"
tags:
  - "evaluation"
  - "robustness"
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cluster-robust-sandwich-variance-estimator-for-metrics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-05T08:40:10Z"
created_at: "2026-06-05T08:40:10Z"
---

# Beyond Point Estimates: Reliable Evaluation of Prediction Performance Metrics under Clustered Data

**Authors**: Taekwon Hong, Daeyoung Lim, Woojung Bae
**Date**: 2026-06-02
**Paper ID**: [openalex:2606.03656](https://arxiv.org/abs/2606.03656)

## Summary

This paper addresses the critical need for uncertainty quantification in machine learning model evaluation, particularly when data exhibits dependencies such as in time series or clustered subjects. The authors propose a unified framework that represents common performance metrics as smooth functionals of confusion-matrix probabilities, facilitating the use of cluster-robust sandwich variance estimators. This methodology enables the generation of asymptotically valid confidence intervals and hypothesis tests, effectively preventing the underestimation of variability common in naive evaluation methods. Furthermore, the work provides principled tools for study design, including power and sample size approximations.

## Key Contributions

- Develops a unified mathematical framework representing performance metrics as smooth functionals of confusion-matrix probabilities, enabling rigorous uncertainty estimation.
- Utilizes the cluster-robust sandwich variance estimator to generate valid confidence intervals, hypothesis tests, and paired comparisons in clustered or dependent data settings.
- Provides analytical power and sample size approximations for study design that account for data clustering, addressing a significant oversight in current model evaluation practices.

## Open Questions & Future Work

- [[small-sample-cluster-robust-inference]]
- [[multi-way-dependence-evaluation]]

## Key Concepts

- [[cluster-robust-sandwich-variance-estimator-for-metrics]]: A statistical method for calculating valid confidence intervals for performance metrics by representing them as smooth functionals of confusion-matrix probabilities under clustered data.

## Archivist Review

I approved the cluster-robust variance estimation framework as a central, reusable method for metric uncertainty quantification. The two open questions address fundamental statistical limitations in the validity of performance evaluation under small-sample and non-nested data regimes, both of which are critical for reliable ML deployment. No datasets were approved as none were central, named benchmarks for this specific methodology.

### Approved Concepts
- cluster-robust sandwich variance estimator for metrics: It provides a statistically rigorous framework to compute uncertainty for performance metrics by framing them as smooth functionals, filling a critical gap in ML model evaluation practices.

### Approved Open Questions
- Robust inference for small clusters: In critical domains like clinical trials, small sample sizes are common, and incorrect uncertainty quantification leads to invalid statistical conclusions.
- Evaluation under multi-way dependence: As machine learning models are deployed in complex, multi-dimensional environments, ignoring non-nested dependencies results in biased variance estimates.

## Links

- [Abstract](https://arxiv.org/abs/2606.03656)
- [PDF](https://arxiv.org/pdf/2606.03656)

