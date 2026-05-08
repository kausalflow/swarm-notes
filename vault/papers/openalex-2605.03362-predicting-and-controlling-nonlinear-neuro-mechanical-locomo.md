---
# CSL-compatible fields
title: "Predicting and controlling nonlinear neuro-mechanical locomotion dynamics"
author:
  - literal: "Alexander E. Cohen"
  - literal: "Jörn Dunkel"
issued:
  date-parts:
    - [2026, 5, 5]
url: "https://arxiv.org/abs/2605.03362"

# Custom fields
paper_id: "2605.03362"
paper_source: "openalex"
domain: "biology"
tags:
  - "time-series"
  - "bayesian-inference"
  - "stochastic-modeling"
architectures:
  []
datasets:
  []
concept_slugs:
  - "multiscale-neuromechanical-modeling-framework"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-08T06:28:15Z"
created_at: "2026-05-08T06:28:15Z"
---

# Predicting and controlling nonlinear neuro-mechanical locomotion dynamics

**Authors**: Alexander E. Cohen, Jörn Dunkel
**Date**: 2026-05-05
**Paper ID**: [openalex:2605.03362](https://arxiv.org/abs/2605.03362)

## Summary

This paper introduces a computational framework for inferring multiscale neuromechanical models that map neural activity time series to behavioral locomotion. By utilizing spectral mode representations, Helmholtz-Nambu decompositions, and Bayesian inference, the approach identifies predictive stochastic models from experimental data efficiently. The model is validated using recordings from C. elegans, where it accurately captures behavioral transitions and enables real-time control predictions. The methodology is designed to be highly generic, providing a scalable solution for studying neuromechanical links across various biological organisms.

## Key Contributions

- Introduced a multiscale neuromechanical modeling framework combining spectral mode representations, Helmholtz-Nambu decomposition, and Bayesian inference.
- Demonstrated the framework's ability to accurately describe neural-to-locomotion dynamics in Caenorhabditis elegans.
- Showed the utility of the inferred stochastic model in predicting neural activation for real-time locomotion control, facilitating future optogenetic experimental designs.

## Open Questions & Future Work

- [[predictive-neuromechanical-modeling-limitations]]

## Key Concepts

- [[multiscale-neuromechanical-modeling-framework]]: A computational framework that combines spectral mode representations and Helmholtz-Nambu decompositions to link neural activity with animal locomotion dynamics.

## Archivist Review

I have approved the multiscale neuromechanical modeling framework as it offers a novel approach to linking time-series data with latent dynamical systems. The open question was refined to capture the fundamental challenge of neuro-mechanical inference rather than just the specific application to worms. The provided dataset was rejected for being a local experimental corpus rather than a general-purpose ML benchmark.

### Approved Concepts
- Multiscale Neuromechanical Modeling Framework: It provides a novel, data-efficient method for bridging the gap between neural time series and behavioral locomotion patterns using spectral and decomposition techniques.

### Approved Open Questions
- Predicting Locomotion from Neurons: Developing such a framework is critical for transitioning from descriptive to predictive neuroscience, as it provides a necessary basis for designing optogenetic experiments and understanding the neural control of behavior in real time.

### Rejected Candidates
- [dataset] Caenorhabditis elegans locomotion dataset (`caenorhabditis-elegans-locomotion-dataset`) - low_impact: This is a specific domain-specific experimental dataset, not a standardized community-wide benchmark useful for general ML research.

## Links

- [Abstract](https://arxiv.org/abs/2605.03362)
- [PDF](https://arxiv.org/pdf/2605.03362)

