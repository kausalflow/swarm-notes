---
# CSL-compatible fields
title: "A computationally-tractable measure of global sensitivity for sampling-based Bayesian inference"
author:
  - literal: "Arina Odnoblyudova"
  - literal: "Charita Dellaporta"
  - literal: "François‐Xavier Briol"
issued:
  date-parts:
    - [2026, 5, 27]
url: "https://arxiv.org/abs/2605.28099"

# Custom fields
paper_id: "2605.28099"
paper_source: "openalex"
domain: "nlp"
tags:
  - "bayesian-inference"
  - "sensitivity-analysis"
  - "time-series"
  - "simulation-based-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "fisher-divergence-based-global-sensitivity-analysis"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-30T07:37:17Z"
created_at: "2026-05-30T07:37:17Z"
---

# A computationally-tractable measure of global sensitivity for sampling-based Bayesian inference

**Authors**: Arina Odnoblyudova, Charita Dellaporta, François‐Xavier Briol
**Date**: 2026-05-27
**Paper ID**: [openalex:2605.28099](https://arxiv.org/abs/2605.28099)

## Summary

This paper introduces a novel global sensitivity analysis framework for Bayesian inference that leverages the Fisher divergence to overcome the computational limitations of existing methods. The proposed approach is specifically designed to be tractable in high-dimensional settings, requiring only a set of reference posterior samples and access to score functions. The authors establish theoretical bounds on the impact of perturbations on the posterior and its moments, validating the effectiveness of the method across diverse applications such as time series modeling and neural simulation-based inference.

## Key Contributions

- Introduces a global sensitivity analysis method based on Fisher divergence that is computationally tractable in moderate to high dimensions using only posterior samples.
- Provides theoretical guarantees for controlling posterior distribution changes and bounding perturbations in the first two moments.
- Demonstrates applicability to challenging scenarios, including generalized Bayesian inference, time series models, and neural simulation-based inference.

## Open Questions & Future Work

- [[fisher-divergence-multimodal-sensitivity]]

## Key Concepts

- [[fisher-divergence-based-global-sensitivity-analysis]]: A computationally tractable method for global sensitivity analysis in Bayesian inference using samples and score function evaluations based on the Fisher divergence.

## Archivist Review

The paper provides a significant advancement in Bayesian sensitivity analysis by leveraging Fisher divergence to enable tractability in high dimensions. The concept is highly reusable for Bayesian workflows, and the identified open question regarding multimodal posteriors addresses a fundamental limitation of score-based methods. Other candidates were rejected to maintain the required scarcity of the vault.

### Approved Concepts
- Fisher-divergence-based Global Sensitivity Analysis: Enables quantification of sensitivity in high-dimensional Bayesian workflows where traditional sensitivity metrics are computationally infeasible.

### Approved Open Questions
- Fisher divergence for multimodal posteriors: Multimodal posteriors are common in complex Bayesian models, and the failure of score-based methods to capture mode-specific sensitivity is a major practical limitation for global sensitivity analysis.

## Links

- [Abstract](https://arxiv.org/abs/2605.28099)
- [PDF](https://arxiv.org/pdf/2605.28099)

