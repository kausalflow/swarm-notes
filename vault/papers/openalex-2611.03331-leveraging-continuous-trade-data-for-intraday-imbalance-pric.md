---
# CSL-compatible fields
title: "Leveraging Continuous Trade Data for Intraday Imbalance Price Forecasting"
author:
  - literal: "Klimis Stylpnopoulos"
  - literal: "Jethro Browell"
  - literal: "Janine Illian"
  - literal: "Ciaran Gilbert"
  - literal: "Wayne Jones"
issued:
  date-parts:
    - [2026, 11, 2]
url: "https://arxiv.org/abs/2611.03331"

# Custom fields
paper_id: "2611.03331"
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
processed_at: "2026-11-04T12:40:33Z"
created_at: "2026-11-04T12:40:33Z"
---

# Leveraging Continuous Trade Data for Intraday Imbalance Price Forecasting

**Authors**: Klimis Stylpnopoulos, Jethro Browell, Janine Illian, Ciaran Gilbert, Wayne Jones
**Date**: 2026-11-02
**Paper ID**: [openalex:2611.03331](https://arxiv.org/abs/2611.03331)

## Summary

This paper presents an approach to integrate continuous intraday market trade data into short-term electricity imbalance price forecasting, producing both parametric and non-parametric density forecasts. Using extensive feature engineering to transform irregular trade data into a tabular format, the proposed methods combined with quantile regression and LASSO significantly improve forecast accuracy. Furthermore, a Natural Gradient Boosting model predicting bimodal Gaussian mixture parameters is introduced, achieving up to a 20% reduction in Pinball Loss on Great Britain market data near gate closure.

## Key Contributions

- Proposes a feature engineering approach to integrate irregular continuous intraday trade data into tabular forecasting models for electricity imbalance prices.
- Demonstrates that integrating continuous trade data reduces Pinball Loss of state-of-the-art models by 20% at 30 seconds before gate closure and 7.5% at one hour before delivery on Great Britain market data.
- Introduces a Natural Gradient Boosting based model predicting means and variances of a bimodal Gaussian mixture, balancing predictive accuracy and computational efficiency.

## Links

- [Abstract](https://arxiv.org/abs/2611.03331)
- [PDF](https://arxiv.org/pdf/2611.03331)

