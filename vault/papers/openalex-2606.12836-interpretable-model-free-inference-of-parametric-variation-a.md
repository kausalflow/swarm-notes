---
# CSL-compatible fields
title: "Interpretable model-free inference of parametric variation across time-series data through large-scale feature extraction"
author:
  - literal: "Ben Fulcher"
  - literal: "Carl H. Lubba"
  - literal: "Giorgio F. Gilestro"
  - literal: "Simon R. Schultz"
  - literal: "Nick S. Jones"
issued:
  date-parts:
    - [2026, 6, 11]
url: "https://arxiv.org/abs/2606.12836"

# Custom fields
paper_id: "2606.12836"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "feature-extraction"
  - "unsupervised-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "time-series-feature-based-parameter-inference"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-14T08:37:54Z"
created_at: "2026-06-14T08:37:54Z"
---

# Interpretable model-free inference of parametric variation across time-series data through large-scale feature extraction

**Authors**: Ben Fulcher, Carl H. Lubba, Giorgio F. Gilestro, Simon R. Schultz, Nick S. Jones
**Date**: 2026-06-11
**Paper ID**: [openalex:2606.12836](https://arxiv.org/abs/2606.12836)

## Summary

This paper presents an unsupervised, model-free methodology for identifying latent parametric variation in time-series data. By projecting series into a high-dimensional space defined by over 7000 interpretable statistics, the approach reveals low-dimensional structures that correspond to the underlying generative degrees of freedom. The method is validated across a range of simulated dynamical systems and successfully applied to extract biologically relevant features from large-scale fruit fly movement datasets.

## Key Contributions

- Introduces a model-free, unsupervised framework that reconstructs latent parametric variation from time-series by analyzing low-dimensional structure in a high-dimensional feature space.
- Validates the approach on 13 diverse dynamical systems, including linear stochastic, nonlinear oscillatory, and chaotic processes.
- Demonstrates utility in biological research by extracting interpretable components related to sex and circadian rhythmicity from large-scale fruit fly movement data.

## Open Questions & Future Work

- [[feature-library-bias-mitigation-in-dynamical-inference]]

## Key Concepts

- [[time-series-feature-based-parameter-inference]]: A model-free, unsupervised framework that projects time series into a high-dimensional feature space to identify low-dimensional structure representing generative parametric variation.

## Archivist Review

The paper provides a significant methodological contribution for model-free inference of dynamical parameters. I approved the overarching framework as a concept and defined a focused open question on library-induced bias. Other candidates were rejected as subcomponents or renamed to fit vault standards.

### Approved Concepts
- Time-Series Feature-Based Parameter Inference: Provides a generalizable, unsupervised framework for identifying latent generative parameters from complex dynamics without requiring explicit physical modeling.

### Approved Open Questions
- Feature Library Bias Mitigation: Fundamental for ensuring the reliability and generalizability of model-free inference techniques across different scientific domains and varying data regimes.

### Rejected Candidates
- [concept] Time-Series Feature Extraction Library (`time-series-feature-extraction-library`) - subcomponent_of_broader_mechanism: This is better represented by the methodological framework of feature-based inference rather than the library of statistics itself.
- [open_question] Automated Feature Selection for Inference (`automated-feature-selection-for-parameter-inference`) - subcomponent_of_broader_mechanism: This is a specific optimization problem that can be subsumed into the broader challenge of library bias and reliable inference.
- [open_question] Mitigating Feature Library Bias (`mitigating-feature-library-bias`) - duplicate_existing: Renamed for better alignment with existing open question standards and to improve clarity.

## Links

- [Abstract](https://arxiv.org/abs/2606.12836)
- [PDF](https://arxiv.org/pdf/2606.12836)

