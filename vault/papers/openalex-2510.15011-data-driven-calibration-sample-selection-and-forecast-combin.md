---
# CSL-compatible fields
title: "Data-driven calibration sample selection and forecast combination in electricity price forecasting: An application of the ARHNN method"
author:
  - literal: "Tomasz Serafin"
  - literal: "Weronika Nitka"
issued:
  date-parts:
    - [2026, 9, 17]
url: "https://arxiv.org/abs/2510.15011"

# Custom fields
paper_id: "2510.15011"
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
  - "autoregressive-hybrid-nearest-neighbors-arhnn"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:02Z"
created_at: "2026-09-18T09:17:02Z"
---

# Data-driven calibration sample selection and forecast combination in electricity price forecasting: An application of the ARHNN method

**Authors**: Tomasz Serafin, Weronika Nitka
**Date**: 2026-09-17
**Paper ID**: [openalex:2510.15011](https://arxiv.org/abs/2510.15011)

## Summary

This paper explores calibration sample selection and forecast combination for electricity price forecasting by applying the Autoregressive Hybrid Nearest Neighbors (ARHNN) method to long-term time series from the German, Spanish, and New England markets. The authors demonstrate that ARHNN outperforms standard literature benchmarks by up to 10% in accuracy, introduce two computationally efficient simplified variants, and validate the practical business utility of their approach via an automated battery storage trading strategy.

## Key Contributions

- Applied the Autoregressive Hybrid Nearest Neighbors (ARHNN) method to electricity price forecasting across German, Spanish, and New England electricity markets, outperforming literature benchmarks by up to 10% in forecast accuracy.
- Proposed two simplified variants of the ARHNN method that drastically decrease computation time with only minor losses in prediction accuracy.
- Demonstrated the practical business value of the forecast-driven approach through a battery storage system trading case study with a new automated trading strategy.

## Open Questions & Future Work

- [[statistical-vs-economic-forecasting-value]]

## Key Concepts

- [[autoregressive-hybrid-nearest-neighbors-arhnn]]: An autoregressive hybrid nearest neighbors forecasting method that integrates calibration sample selection and forecast combination.

## Archivist Review

Approved the ARHNN concept as a distinct time series forecasting methodology and the open question regarding statistical versus economic forecasting performance. No specific named datasets were provided in the abstract that qualify under vault criteria.

### Approved Concepts
- Autoregressive Hybrid Nearest Neighbors (ARHNN): Central methodology proposed and evaluated for electricity price forecasting via calibration sample selection and forecast combination.

### Approved Open Questions
- Statistical vs. Economic Forecasting Value: Understanding the mapping between statistical loss functions and real-world economic utility is critical for deploying profitable decision-making models in energy markets.

## Links

- [Abstract](https://arxiv.org/abs/2510.15011)
- [PDF](https://arxiv.org/pdf/2510.15011)

