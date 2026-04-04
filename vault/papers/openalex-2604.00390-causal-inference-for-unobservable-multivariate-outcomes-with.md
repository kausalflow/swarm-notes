---
# CSL-compatible fields
title: "Causal Inference for Unobservable Multivariate Outcomes, with Applications to Brain Effective Connectivity"
author:
  - literal: "Hao Song"
  - literal: "Ani Eloyan"
  - literal: "Youjin Lee"
issued:
  date-parts:
    - [2026, 4, 1]
url: "https://arxiv.org/abs/2604.00390"

# Custom fields
paper_id: "2604.00390"
paper_source: "openalex"
domain: "medicine"
tags:
  - "causal-inference"
architectures:
  []
datasets:
  - "alzheimers-disease-neuroimaging-initiative"
concept_slugs:
  - "sample-splitting-for-causal-inference"
dataset_slugs:
  - "alzheimers-disease-neuroimaging-initiative"
skill: "TimeSeriesSkill"
processed_at: "2026-04-04T05:50:56Z"
created_at: "2026-04-04T05:50:56Z"
---

# Causal Inference for Unobservable Multivariate Outcomes, with Applications to Brain Effective Connectivity

**Authors**: Hao Song, Ani Eloyan, Youjin Lee
**Date**: 2026-04-01
**Paper ID**: [openalex:2604.00390](https://arxiv.org/abs/2604.00390)

## Summary

This paper addresses the challenge of estimating causal effects on derived, interdependent multivariate outcomes, such as brain effective connectivity. The authors propose a two-layer inference framework that utilizes sample splitting to handle within-outcome dependencies and inverse probability weighting to account for confounding. Theoretical and simulation-based evaluations demonstrate asymptotic validity and robust error control. The method is successfully applied to investigate the causal influence of amyloid on neuroimaging-derived connectivity patterns.

## Key Contributions

- Develops a two-layer causal inference framework to estimate intervention effects on derived multivariate outcomes, specifically targeting directional effective connectivity.
- Introduces a sample-splitting methodology to mitigate biases from intra-outcome dependencies, ensuring more accurate causal identification.
- Integrates inverse probability weighting with familywise error control to maintain statistical validity when evaluating causal effects across multiple outcome components.

## Open Questions & Future Work

- [[sample-splitting-model-selection-bias]]
- [[non-linear-derived-outcome-causality]]

## Key Concepts

- [[sample-splitting-for-causal-inference]]: A causal inference framework that employs sample-splitting to decouple the estimation of derived relational outcomes from the subsequent estimation of intervention effects.

## Archivist Review

I approved the general concept of 'sample-splitting for causal inference' and two open questions regarding the theoretical limitations of this approach in non-linear and adaptive contexts. The Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset was approved as it is a widely recognized standard in clinical research. The original concept was renamed for better reusability.

### Approved Concepts
- Sample-splitting for causal inference: Provides a structured approach to disentangling dependency structures in derived outcomes from intervention effects, avoiding post-selection bias.

### Approved Open Questions
- Sample-splitting model selection bias: Addresses the fundamental challenge of ensuring valid inference when the outcome itself is derived via data-dependent processes.
- Non-linear causal inference models: Necessary for moving beyond linear autoregressive models in complex dynamical systems.

### Rejected Candidates
- [concept] Sample-splitting effective connectivity estimation (`sample-splitting-effective-connectivity-estimation`) - other: Renamed to a more general term to reflect its broader applicability beyond brain effective connectivity.

## Datasets

- [[alzheimers-disease-neuroimaging-initiative]]

## Links

- [Abstract](https://arxiv.org/abs/2604.00390)
- [PDF](https://arxiv.org/pdf/2604.00390)

