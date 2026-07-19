---
# CSL-compatible fields
title: "Frequency Selection in Bayesian Spectral Modeling of Time Series Data with Applications to Wearable Device Measurements"
author:
  - literal: "Beniamino Hadj-Amar"
  - literal: "Vaishnav Krishnan"
  - literal: "Marina Vannucci"
issued:
  date-parts:
    - [2026, 7, 16]
url: "https://arxiv.org/abs/2607.15157"

# Custom fields
paper_id: "2607.15157"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "interpretability"
  - "bayesian-inference"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bayesian-spike-and-slab-spectral-modeling"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-19T07:24:27Z"
created_at: "2026-07-19T07:24:27Z"
---

# Frequency Selection in Bayesian Spectral Modeling of Time Series Data with Applications to Wearable Device Measurements

**Authors**: Beniamino Hadj-Amar, Vaishnav Krishnan, Marina Vannucci
**Date**: 2026-07-16
**Paper ID**: [openalex:2607.15157](https://arxiv.org/abs/2607.15157)

## Summary

This paper presents a Bayesian spike-and-slab framework designed for robust spectral analysis and frequency selection in time series. The method utilizes a structured prior and stochastic search algorithm to identify relevant oscillatory components, facilitating high-resolution spectral reconstruction and sparsity. The framework is further extended to the multivariate case via a hierarchical structure that captures shared and specific rhythms across multiple signals. Empirical results demonstrate the model's effectiveness in identifying clinically meaningful patterns in wearable device measurements, such as circadian rhythms and physiological coupling.

## Key Contributions

- Introduces a Bayesian spike-and-slab framework for high-resolution spectral analysis, enabling simultaneous frequency selection and dimensionality reduction.
- Develops a hierarchical prior for multivariate signals that identifies shared and component-specific rhythms across multiple time series.
- Demonstrates superior performance in frequency estimation and spectral power reconstruction on actigraphy and physiological sensor data compared to traditional methods.

## Open Questions & Future Work

- [[learnable-frequency-separation-constraint]]
- [[scalable-multivariate-spectral-modeling]]

## Key Concepts

- [[bayesian-spike-and-slab-spectral-modeling]]: A spectral analysis framework using spike-and-slab priors for frequency selection and dimensionality reduction in time series.

## Archivist Review

I have approved the core Bayesian spike-and-slab methodology for spectral modeling, as it represents a robust, interpretable framework likely to recur in clinical and chronobiological research. I also approved two high-level open questions regarding the scalability and adaptive constraints of this framework, as these represent fundamental research bottlenecks in Bayesian spectral analysis that transcend the specifics of this paper. All other candidates were rejected as they were either paper-local or subcomponents not deserving of independent status.

### Approved Concepts
- Bayesian Spike-and-Slab Spectral Modeling: It provides a principled way to perform frequency selection and dimensionality reduction in spectral analysis, addressing high-resolution oscillatory component recovery.

### Approved Open Questions
- Learnable Frequency Separation Constraint: Treating the separation constraint as a learnable parameter would eliminate the need for manual hyperparameter tuning while potentially improving the model's ability to discern distinct physiological rhythms.
- Scalable Multivariate Spectral Modeling: Improving the scalability of multivariate spectral models is essential for applying these techniques to modern, high-dimensional sensor datasets in clinical research.

## Links

- [Abstract](https://arxiv.org/abs/2607.15157)
- [PDF](https://arxiv.org/pdf/2607.15157)

