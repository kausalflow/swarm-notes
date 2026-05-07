---
# CSL-compatible fields
title: "EstemPMM: Polynomial Maximization Method for Non-Gaussian Regression and Time Series in R"
author:
  - literal: "Serhii Zabolotnii"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02673"

# Custom fields
paper_id: "2605.02673"
paper_source: "openalex"
domain: "time-series,nlp"
tags:
  - "time-series"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "polynomial-maximization-method"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:37:02Z"
created_at: "2026-05-07T07:37:02Z"
---

# EstemPMM: Polynomial Maximization Method for Non-Gaussian Regression and Time Series in R

**Authors**: Serhii Zabolotnii
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02673](https://arxiv.org/abs/2605.02673)

## Summary

EstemPMM is an R package implementing the Polynomial Maximization Method (PMM) for parameter estimation in regression and time-series models with non-Gaussian errors. By utilizing higher-order error cumulants like skewness and excess kurtosis, PMM estimators achieve superior asymptotic efficiency compared to ordinary least squares (OLS) in asymmetric or leptokurtic settings. The package offers an automated dispatcher to select optimal estimation strategies and provides a comprehensive suite of tools for model fitting, forecasting, and uncertainty quantification.

## Key Contributions

- Presents the EstemPMM R package, providing a unified interface for regression and ARMA-type time series models under non-Gaussian conditions.
- Introduces estimators that leverage third and fourth standardized moments (skewness and excess kurtosis) to outperform OLS in asymmetric or leptokurtic error environments.
- Demonstrates parameter-precision gains on heavy-tailed financial data (WTI crude oil) and provides asymptotic efficiency metrics for estimator validation.

## Key Concepts

- [[polynomial-maximization-method]]: An estimation method using third and fourth standardized moments to achieve higher asymptotic efficiency than ordinary least squares in the presence of non-Gaussian error distributions.

## Archivist Review

I approved the 'Polynomial Maximization Method' as it provides a distinct, theoretically grounded approach for parameter estimation that outperforms standard OLS under common non-Gaussian conditions. I rejected the R package itself as a candidate, adhering to the policy of focusing on reusable mechanisms rather than specific implementations.

### Approved Concepts
- Polynomial Maximization Method (PMM): PMM provides a robust alternative to OLS for non-Gaussian, asymmetric, or leptokurtic errors by leveraging higher-order cumulants.

## Links

- [Abstract](https://arxiv.org/abs/2605.02673)
- [PDF](https://arxiv.org/pdf/2605.02673)

