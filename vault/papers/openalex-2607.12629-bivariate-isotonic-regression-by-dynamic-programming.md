---
# CSL-compatible fields
title: "Bivariate Isotonic Regression by Dynamic Programming"
author:
  - literal: "Pedro Afonso Fernandes"
issued:
  date-parts:
    - [2026, 7, 14]
url: "https://arxiv.org/abs/2607.12629"

# Custom fields
paper_id: "2607.12629"
paper_source: "openalex"
domain: "finance"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-17T07:10:20Z"
created_at: "2026-07-17T07:10:20Z"
---

# Bivariate Isotonic Regression by Dynamic Programming

**Authors**: Pedro Afonso Fernandes
**Date**: 2026-07-14
**Paper ID**: [openalex:2607.12629](https://arxiv.org/abs/2607.12629)

## Summary

This paper proposes a dynamic programming approach to solve the bivariate isotonic regression problem by utilizing an anti-diagonal traversal procedure. This generalizes existing univariate dynamic programming techniques, providing a more versatile method for finding monotonic relationships in multi-dimensional data. The author demonstrates the algorithm's practical utility by analyzing the association between baseball player salaries and performance metrics, highlighting its potential relevance for economic and forecasting applications.

## Key Contributions

- Extends the dynamic programming framework for isotonic regression from univariate to bivariate problems.
- Implements an anti-diagonal traversal procedure to efficiently solve bivariate isotonic regression.
- Demonstrates the algorithm's applicability to multi-variate economic data analysis using the baseball dataset.

## Open Questions & Future Work

- [[multivariate-isotonic-regression-algorithms]]

## Archivist Review

The submission was reviewed for its contribution to forecasting methodology. The proposed bivariate dynamic programming approach was rejected as an incremental implementation detail of a well-known statistical method. The open question regarding multivariate isotonic regression was approved as it reflects a legitimate, high-level bottleneck in statistical estimation and non-parametric modeling.

### Approved Open Questions
- General multivariate isotonic regression algorithms: This is a foundational problem in statistics and machine learning as it impacts the reliability of non-parametric estimators in high-dimensional economic and physical modeling where theoretical monotonic constraints must be satisfied.

### Rejected Candidates
- [concept] Bivariate Isotonic Regression via Dynamic Programming (`bivariate-isotonic-regression-by-dp`) - not_novel: Isotonic regression is a well-established statistical concept, and this specific implementation technique for the bivariate case is incremental rather than a transformative, reusable architectural concept.

## Links

- [Abstract](https://arxiv.org/abs/2607.12629)
- [PDF](https://arxiv.org/pdf/2607.12629)

