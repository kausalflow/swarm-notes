---
# CSL-compatible fields
title: "Prior elicitation for Bayesian estimation of single-subject connectivity networks"
author:
  - literal: "Yiye Jiang"
  - literal: "Alice Chevaux"
  - literal: "Wendy Meiring"
  - literal: "Alex Petersen"
  - literal: "Guillaume Kon Kam King"
  - literal: "Julyan Arbel"
  - literal: "Sophie Achard"
issued:
  date-parts:
    - [2026, 5, 4]
url: "https://arxiv.org/abs/2605.02587"

# Custom fields
paper_id: "2605.02587"
paper_source: "openalex"
domain: "biology"
tags:
  - "bayesian-estimation"
  - "neuroimaging"
architectures:
  []
datasets:
  []
concept_slugs:
  - "prior-elicitation-framework-for-connectivity-networks"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-07T07:38:01Z"
created_at: "2026-05-07T07:38:01Z"
---

# Prior elicitation for Bayesian estimation of single-subject connectivity networks

**Authors**: Yiye Jiang, Alice Chevaux, Wendy Meiring, Alex Petersen, Guillaume Kon Kam King, Julyan Arbel, Sophie Achard
**Date**: 2026-05-04
**Paper ID**: [openalex:2605.02587](https://arxiv.org/abs/2605.02587)

## Summary

This paper proposes a Bayesian framework for inferring single-subject functional connectivity graphs from resting-state fMRI data. The core innovation is a prior elicitation procedure that maps qualitative expert knowledge regarding correlation levels and variability into rigorous hyperparameter settings for Bayesian estimation. Unlike traditional methods that produce static weight estimates, this approach yields full posterior distributions, facilitating robust uncertainty quantification and significant connectivity detection. Experimental results confirm the effectiveness of these expert-informed priors in enhancing connectivity estimation accuracy compared to current state-of-the-art single-subject methods.

## Key Contributions

- Introduces a Bayesian approach for inferring single-subject functional connectivity networks from multivariate resting-state fMRI time series.
- Develops a dedicated prior elicitation framework that transforms expert beliefs into interpretable hyperparameters for correlation matrices.
- Demonstrates superior performance over existing single-subject Bayesian functional connectivity methods by providing posterior distributions for connectivity weights, enabling uncertainty quantification and significant connection identification.

## Open Questions & Future Work

- [[fixed-weight-mixture-posterior-robustness]]

## Key Concepts

- [[prior-elicitation-framework-for-connectivity-networks]]: A systematic methodology for mapping expert beliefs about correlation characteristics into interpretable hyperparameters for Bayesian estimation of connectivity graphs.

## Archivist Review

The submission presents a methodology for expert-informed prior elicitation in Bayesian network estimation, which is conceptually sound and generalizes well beyond the specific fMRI domain. The open question regarding mixture weight collapse in Bayesian priors addresses a non-trivial issue in maintaining the robustness of shrinkage priors. Other domain-specific details were excluded to maintain the vault's focus on foundational forecasting and estimation mechanisms.

### Approved Concepts
- Prior Elicitation Framework for Connectivity Networks: Provides a formal, interpretable methodology for converting expert knowledge into Bayesian hyperparameter configurations for covariance estimation, which is broadly applicable to high-dimensional time series.

### Approved Open Questions
- Fixed-Weight Mixture Posterior Robustness: This is a fundamental stability issue in Bayesian estimation where the loss of the regularization component compromises the robustness of the resulting network weights.

## Links

- [Abstract](https://arxiv.org/abs/2605.02587)
- [PDF](https://arxiv.org/pdf/2605.02587)

