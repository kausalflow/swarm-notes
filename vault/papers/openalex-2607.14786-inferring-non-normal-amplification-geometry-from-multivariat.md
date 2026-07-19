---
# CSL-compatible fields
title: "Inferring Non-Normal Amplification Geometry from Multivariate Time Series"
author:
  - literal: "V. R. Saiprasad"
  - literal: "V. Troude"
  - literal: "D. Sornette"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.14786"

# Custom fields
paper_id: "2607.14786"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "non-normal-directional-response-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:14Z"
created_at: "2026-07-19T07:24:14Z"
---

# Inferring Non-Normal Amplification Geometry from Multivariate Time Series

**Authors**: V. R. Saiprasad, V. Troude, D. Sornette
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.14786](https://arxiv.org/abs/2607.14786)

## Summary

The paper addresses the challenge of transient growth in stable dynamical systems caused by non-normal geometry, which eigenvalue analysis often misses. The authors propose a data-driven method called non-normal directional response inference that uses sliding window linear operators to extract response geometry in a dominant two-dimensional subspace. The resulting diagnostic, a scale-free ratio R, provides an interpretable measure of transient amplification potential that is robust to finite data limitations and noise. This approach successfully detects shifts in dynamical regimes across various physiological datasets without requiring supervised event labels.

## Key Contributions

- Introduces non-normal directional response inference to detect transient amplification geometry without requiring the full high-dimensional governing operator.
- Defines a scale-free ratio R as a robust diagnostic for transient amplification that remains recoverable even with limited sample sizes or noisy data.
- Demonstrates the method's ability to identify transitions in physiological and behavioral time series across diverse domains like EEG, EHG, and inertial motion data.

## Open Questions & Future Work

- [[uncertainty-quantification-for-non-normal-inference]]

## Key Concepts

- [[non-normal-directional-response-inference]]: A data-driven method for inferring the geometric response properties of non-normal dynamical systems from multivariate time series.

## Archivist Review

I have approved the non-normal directional response inference concept as it provides a distinct, geometry-based approach to time series diagnostics that addresses the limitations of standard eigenvalue analysis. I also approved the open question regarding its uncertainty quantification, as this is a fundamental bottleneck for deploying the method reliably across diverse non-stationary systems. All other candidates were rejected as they were either too specific to the paper's implementation or effectively covered by the core mechanism itself.

### Approved Concepts
- Non-normal directional response inference: It addresses the limitation of traditional eigenvalue-based stability analysis by uncovering transient amplification mechanisms in non-normal systems from data, which are often invisible to spectral methods.

### Approved Open Questions
- Non-normal inference uncertainty quantification: Rigorous uncertainty quantification is essential for transitioning this diagnostic tool from an illustrative mechanism for exploratory analysis to a robust inferential framework capable of supporting scientific decision-making.

## Links

- [Abstract](https://arxiv.org/abs/2607.14786)
- [PDF](https://arxiv.org/pdf/2607.14786)

