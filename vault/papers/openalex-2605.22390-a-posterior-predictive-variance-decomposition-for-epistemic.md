---
# CSL-compatible fields
title: "A Posterior-Predictive Variance Decomposition for Epistemic and Aleatoric Uncertainty in Wind Power Forecasting"
author:
  - literal: "Yinsong Chen"
  - literal: "Samson S. Yu"
  - literal: "Kashem M. Muttaqi"
issued:
  date-parts:
    - [2026, 5, 21]
url: "https://arxiv.org/abs/2605.22390"

# Custom fields
paper_id: "2605.22390"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
architectures:
  []
datasets:
  []
concept_slugs:
  - "posterior-predictive-variance-decomposition"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-24T07:46:55Z"
created_at: "2026-05-24T07:46:55Z"
---

# A Posterior-Predictive Variance Decomposition for Epistemic and Aleatoric Uncertainty in Wind Power Forecasting

**Authors**: Yinsong Chen, Samson S. Yu, Kashem M. Muttaqi
**Date**: 2026-05-21
**Paper ID**: [openalex:2605.22390](https://arxiv.org/abs/2605.22390)

## Summary

This paper addresses the limitation of current wind power forecasting models that conflate different sources of uncertainty. By applying the law of total variance, the authors derive a method to decompose total predictive uncertainty into epistemic (model-driven) and aleatoric (data-driven) components. The framework includes a novel evaluation protocol that validates disentanglement through synthetic experiments, data-property analysis, and scaling laws. Results demonstrate that the decomposed uncertainties provide actionable insights into model performance under noise and distribution shifts.

## Key Contributions

- Derives an explicit mathematical decomposition of total predictive uncertainty into epistemic and aleatoric components using the law of total variance for heteroscedastic Bayesian neural networks.
- Introduces a three-module evaluation protocol to validate uncertainty disentanglement in the absence of ground-truth uncertainty labels, covering synthetic noise, data-property sensitivity, and scaling behavior.
- Demonstrates the effectiveness of the decomposition in wind power forecasting, showing theoretically consistent responses to distributional shifts and training dataset sizes.

## Open Questions & Future Work

- [[model-misspecification-uncertainty-disentanglement]]

## Key Concepts

- [[posterior-predictive-variance-decomposition]]: A method that uses the law of total variance to decompose neural network predictive uncertainty into distinct epistemic and aleatoric components.

## Archivist Review

I approved the proposed uncertainty decomposition concept as it provides a principled framework for a recurring challenge in time-series forecasting. The open question regarding model misspecification and bias in this decomposition is also valuable, as it addresses a fundamental, persistent issue in uncertainty quantification for neural models. No datasets were approved, as none were identified as uniquely novel or standardized benchmarks in this context.

### Approved Concepts
- Posterior-predictive variance decomposition: Provides a mathematically grounded method to isolate epistemic and aleatoric uncertainty in neural regression without requiring ground-truth uncertainty labels.

### Approved Open Questions
- Model Misspecification in Uncertainty Disentanglement: Understanding the contribution of model bias is essential for validating the operational reliability of uncertainty disentanglement in real-world forecasting tasks, where perfect model specification is rarely guaranteed.

## Links

- [Abstract](https://arxiv.org/abs/2605.22390)
- [PDF](https://arxiv.org/pdf/2605.22390)

