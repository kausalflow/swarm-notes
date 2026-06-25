---
# CSL-compatible fields
title: "Online forecast reconciliation using linear models"
author:
  - literal: "Tobias Rønlev-Knudsen"
  - literal: "Henrik Madsen"
  - literal: "Jan Kloppenborg Møller"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23326"

# Custom fields
paper_id: "2606.23326"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "forecast-reconciliation"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:19:39Z"
created_at: "2026-06-25T08:19:39Z"
---

# Online forecast reconciliation using linear models

**Authors**: Tobias Rønlev-Knudsen, Henrik Madsen, Jan Kloppenborg Møller
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23326](https://arxiv.org/abs/2606.23326)

## Summary

This paper introduces an adaptive framework for online hierarchical forecast reconciliation using multivariate linear models and ridge regression. By framing hierarchical constraints within a graph-theoretic structure and employing the matrix normal distribution, the approach enables systematic residual characterization and parameter estimation. The authors further derive a recursive inference algorithm that allows for real-time model updates and apply this methodology to district heating load forecasting to demonstrate its practical efficacy.

## Key Contributions

- Formulates a multivariate linear reconciliation model using the matrix normal distribution to characterize hierarchical residuals.
- Demonstrates that hierarchical forecast reconciliation can be mathematically posed as a ridge regression problem.
- Develops a recursive inference scheme for online hierarchical forecasting based on recursive least squares.
- Provides a robust implementation via the PyOnlineForecast package, validated on a district heating load forecasting case study.

## Open Questions & Future Work

- [[recursive-estimation-scalability-bottleneck]]

## Archivist Review

The paper presents a routine application of recursive least squares to forecast reconciliation, which lacks sufficient novelty to justify new concepts. The identified open question regarding the scalability of recursive matrix updates in online linear models is a fundamental and trackable bottleneck for time-series forecasting infrastructure.

### Approved Open Questions
- Recursive estimation scalability bottleneck: This is a fundamental bottleneck for deploying adaptive, online linear forecasting models in real-world streaming data applications where the model must operate continuously.

### Rejected Candidates
- [concept] Matrix Normal Hierarchical Reconciliation (`matrix-normal-hierarchical-reconciliation`) - not_novel: This is a specialized application of standard multivariate statistics rather than a reusable core mechanism.
- [concept] PyOnlineForecast package (`pyonlineforecast-package`) - paper_local: This is a library/tool rather than a theoretical concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.23326)
- [PDF](https://arxiv.org/pdf/2606.23326)

