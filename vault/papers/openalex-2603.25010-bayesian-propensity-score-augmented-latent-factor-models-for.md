---
# CSL-compatible fields
title: "Bayesian Propensity Score-Augmented Latent Factor Models for Causal Inference with Time-Series Cross-Sectional Data"
author:
  - literal: "Licheng Liu"
issued:
  date-parts:
    - [2026, 3, 26]
url: "https://arxiv.org/abs/2603.25010"

# Custom fields
paper_id: "2603.25010"
paper_source: "openalex"
domain: "time-series"
tags:
  - "latent-factor-model"
  - "causal-inference"
  - "time-series"
  - "bayesian"
  - "propensity-score"
  - "cross-sectional-data"
architectures:
  []
datasets:
  []
concept_slugs:
  - "bayesian-propensity-score-augmented-latent-factor-model"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-29T06:06:47Z"
created_at: "2026-03-29T06:06:47Z"
---

# Bayesian Propensity Score-Augmented Latent Factor Models for Causal Inference with Time-Series Cross-Sectional Data

**Authors**: Licheng Liu
**Date**: 2026-03-26
**Paper ID**: [openalex:2603.25010](https://arxiv.org/abs/2603.25010)

## Summary

This paper introduces a novel Bayesian framework for causal inference when analyzing data structured as a time-series cross-section, which typically suffers from complex treatment assignment mechanisms. The proposed model explicitly combines latent factor models for treatment assignment with a flexible outcome model that incorporates the propensity score, often via stratification, to allow for more granular and credible comparisons. To enable practical estimation, the authors employ an approximate Bayesian procedure specifically designed to overcome the model feedback issue often encountered when integrating propensity scores into Bayesian models. The method is shown via simulation and application to political connections and firm value to effectively capture heterogeneity and provide more robust causal estimates.

## Key Contributions

- Proposed a Bayesian propensity score-augmented latent factor model specifically designed for causal inference in time-series cross-sectional data.
- The framework models treatment assignment via latent factor loadings and flexibly incorporates the propensity score (e.g., via stratification) into the outcome model.
- Developed an approximate Bayesian procedure to address the model feedback problem inherent in standard Bayesian propensity score analysis for estimation and inference.
- Demonstrated improved performance and the ability to capture greater heterogeneity across propensity-score strata compared to existing approaches.

## Limitations

The paper focuses on the Bayesian approximate procedure, and further theoretical guarantees on its convergence or accuracy relative to exact methods could be explored.

## Open Questions & Future Work

- [[relaxing-parametric-ps-outcome-model]]
- [[achieving-double-robustness-with-latent-factors]]

## Key Concepts

- [[bayesian-propensity-score-augmented-latent-factor-model]]: A Bayesian framework that combines latent factor models to account for unobserved time-series cross-sectional confounding with propensity score incorporation (via stratification) in the outcome model to facilitate credible causal comparisons.

## Archivist Review

Archivist review kept only candidates judged central to the paper and reusable across future work. Approved 1 concept(s), 2 open question(s), and 0 dataset(s), with 1 rejected candidate note(s).

### Approved Concepts
- Bayesian Propensity Score-Augmented Latent Factor Model (PS-LFM): This is the core methodological contribution, explicitly merging latent factor modeling for unobserved confounding with propensity score augmentation for causal inference in a Bayesian time-series context.

### Approved Open Questions
- Relaxing parametric PS-outcome model: The parametric specification limits the flexibility of the propensity score augmentation, and developing semiparametric or non-parametric ways to incorporate the PS into the outcome model without losing identification is a key extension.
- Achieving double-robustness extension: Achieving double robustness in the presence of unobserved confounding modeled via latent factors remains a significant, unresolved challenge in causal inference methodology.

### Rejected Candidates
- [open_question] Latent factor identification necessity (`latent-factor-identification-in-pslfm`) - paper_local: While important, the candidate focuses on a specific identification constraint (rotational equivalence) within the proposed Bayesian method rather than a broader methodological bottleneck, making it slightly too paper-local compared to the other two approved open questions.

## Links

- [Abstract](https://arxiv.org/abs/2603.25010)
- [PDF](https://arxiv.org/pdf/2603.25010)

