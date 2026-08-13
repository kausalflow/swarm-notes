---
# CSL-compatible fields
title: "A Comparison of High-Dimensional Variable Selection Procedures for Electricity Spot Price Forecasting"
author:
  - literal: "Charisios Grivas"
  - literal: "Mikkel Mandrup"
  - literal: "Orimar Sauri"
issued:
  date-parts:
    - [2026, 8, 10]
url: "https://arxiv.org/abs/2608.09213"

# Custom fields
paper_id: "2608.09213"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-13T06:09:22Z"
created_at: "2026-08-13T06:09:22Z"
---

# A Comparison of High-Dimensional Variable Selection Procedures for Electricity Spot Price Forecasting

**Authors**: Charisios Grivas, Mikkel Mandrup, Orimar Sauri
**Date**: 2026-08-10
**Paper ID**: [openalex:2608.09213](https://arxiv.org/abs/2608.09213)

## Summary

This paper evaluates six high-dimensional variable selection procedures for electricity spot price forecasting across six regional markets, focusing on the trade-off between out-of-sample predictive accuracy and model parsimony. The authors find that the Boosting Multiple Testing (BMT) method matches the strong forecasting accuracy of traditional shrinkage methods like LASSO and Elastic Net while employing less than one-tenth of the variables. These findings indicate that over-parameterization is not a necessary prerequisite for high predictive performance in energy price forecasting.

## Key Contributions

- Evaluated six variable selection procedures across an extensive dataset from six regional electricity markets for electricity spot price forecasting.
- Demonstrated that Boosting Multiple Testing (BMT) matches the out-of-sample forecasting accuracy of LASSO and Elastic Net while utilizing less than one-tenth of the variables.
- Established that high model parsimony and strong predictive performance are not mutually exclusive in electricity price forecasting.

## Open Questions & Future Work

- [[high-dimensional-variable-selection-forecasting]]

## Archivist Review

Strictly applied the sparsity policy: no new concepts or datasets were approved because the paper is an empirical evaluation comparing existing methods (LASSO, Elastic Net, Boosting Multiple Testing) rather than introducing a novel architectural primitive or unique reusable resource. One open question addressing high-dimensional variable selection and parsimony in forecasting was approved.

### Approved Open Questions
- High-Dimensional Variable Selection for Forecasting: Addressing high multicollinearity and pseudo-signal selection in high-dimensional forecasting without incurring severe over-parameterization is a central challenge across econometric and machine learning applications.

## Links

- [Abstract](https://arxiv.org/abs/2608.09213)
- [PDF](https://arxiv.org/pdf/2608.09213)

