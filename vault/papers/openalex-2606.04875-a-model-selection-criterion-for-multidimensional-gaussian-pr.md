---
# CSL-compatible fields
title: "A Model Selection Criterion for Multidimensional Gaussian Processes: Application to Radial Velocities"
author:
  - literal: "Barragán Oscar"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.04875"

# Custom fields
paper_id: "2606.04875"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mgic-rv"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:40:40Z"
created_at: "2026-06-06T07:40:40Z"
---

# A Model Selection Criterion for Multidimensional Gaussian Processes: Application to Radial Velocities

**Authors**: Barragán Oscar
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.04875](https://arxiv.org/abs/2606.04875)

## Summary

This paper addresses the difficulty of selecting optimal ancillary indicators in multidimensional Gaussian process (multi-GP) regression for radial velocity signal analysis. The author introduces a new model comparison metric, MGIC_rv, which evaluates how well different combinations of indicators constrain the target radial velocity signal. By incorporating a specifically derived effective parameter count to handle multi-GP regularization, the criterion allows for robust model selection in scenarios where classical information criteria fail. While applied to stellar activity, the approach is generalized to any multi-variate regression task focused on inferring a specific observable.

## Key Contributions

- Introduces MGIC_rv, a model selection criterion for multidimensional Gaussian process regression that quantifies the effectiveness of ancillary indicators in explaining a target observable.
- Formulates an effective parameter count that properly accounts for the regularization effects inherent in multi-GP models.
- Demonstrates the robustness of MGIC_rv for selecting stellar activity indicators in radial velocity measurements.

## Open Questions & Future Work

- [[mgic-threshold-crossvalidation-relation]]

## Key Concepts

- [[mgic-rv]]: An information criterion designed to evaluate multidimensional Gaussian process models by quantifying their capacity to explain a specific target variable within a multi-variate system.

## Archivist Review

The paper proposes a specialized information criterion for multi-GP model selection which addresses a clear limitation in existing model comparison methods when targeting specific observables. I have approved the MGIC_rv concept and a corresponding open question regarding the theoretical formalization of its thresholding mechanisms, as these represent a valuable contribution to the time-series forecasting and GP literature. No datasets were approved as none were central to the theoretical contributions or unique enough for the vault.

### Approved Concepts
- MGIC_rv: It provides a novel, quantitative framework for comparing multidimensional Gaussian process models specifically when inference focuses on a single observable within a multi-variate system.

### Approved Open Questions
- MGIC threshold and validation: Establishing formal thresholds and clarifying the relationship with cross-validation is necessary to validate the robustness and statistical consistency of the model selection framework across diverse scientific applications.

## Links

- [Abstract](https://arxiv.org/abs/2606.04875)
- [PDF](https://arxiv.org/pdf/2606.04875)

