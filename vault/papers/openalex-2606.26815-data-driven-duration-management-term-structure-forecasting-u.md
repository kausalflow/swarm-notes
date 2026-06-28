---
# CSL-compatible fields
title: "Data-Driven Duration Management -- Term Structure Forecasting Using Machine Learning"
author:
  - literal: "Tobias Lausser"
  - literal: "Joao Eduardo Vuolo"
  - literal: "Rudi Zagst"
issued:
  date-parts:
    - [2026, 6, 25]
url: "https://arxiv.org/abs/2606.26815"

# Custom fields
paper_id: "2606.26815"
paper_source: "openalex"
domain: "finance"
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
processed_at: "2026-06-28T08:16:22Z"
created_at: "2026-06-28T08:16:22Z"
---

# Data-Driven Duration Management -- Term Structure Forecasting Using Machine Learning

**Authors**: Tobias Lausser, Joao Eduardo Vuolo, Rudi Zagst
**Date**: 2026-06-25
**Paper ID**: [openalex:2606.26815](https://arxiv.org/abs/2606.26815)

## Summary

This paper evaluates machine learning and traditional econometric approaches for forecasting the term structure of interest rates in U.S. and European government bond markets. By integrating macroeconomic variables and dimensionality reduction techniques, the authors construct several neural network models inspired by classical finance structures like Dynamic Nelson-Siegel and PCA. The research finds that neural networks improve predictive performance and portfolio outcomes, while proposing a robust evaluation framework that bridges statistical accuracy with economic utility.

## Key Contributions

- Demonstrates that neural network architectures consistently outperform traditional econometric benchmarks (DNS, PCA) in both statistical forecast accuracy and quantitative bond trading strategy performance.
- Develops a dual-evaluation framework that combines traditional statistical error metrics (RMSE, MAE) with the economic relevance of real-world portfolio construction strategies.
- Identifies market-specific optimal forecasting architectures, showing that direct-forecasting NNs integrating DNS/AE features are superior for U.S. treasuries, whereas factor-based NNs using PCA features suffice for European sovereign bonds.

## Open Questions & Future Work

- [[non-linear-dimensionality-reduction-for-term-structures]]

## Archivist Review

The paper provides a comparative study of ML and classical econometric methods in finance, but does not introduce distinct, reusable ML architectures or methodologies beyond existing practice. The proposed evaluation framework is standard for the domain, and the identified datasets are generic market descriptors. The open question regarding the utility of non-linear dimensionality reduction in term structure forecasting is approved as it addresses a fundamental trade-off between interpretability and capacity in quantitative finance.

### Approved Open Questions
- Non-linear dimensionality for yield curves: Clarifying the specific domains where non-linear dimensionality reduction outperforms linear counterparts is critical for moving beyond empirical benchmarking and establishing a theoretical basis for the adoption of machine learning in fixed-income risk management.

### Rejected Candidates
- [concept] Dual-evaluation framework (statistical + economic) (`bond-market-evaluation-framework`) - not_novel: The integration of economic trading metrics with statistical error is a standard practice in financial forecasting papers; this does not constitute a unique, reusable methodological concept.

## Links

- [Abstract](https://arxiv.org/abs/2606.26815)
- [PDF](https://arxiv.org/pdf/2606.26815)

