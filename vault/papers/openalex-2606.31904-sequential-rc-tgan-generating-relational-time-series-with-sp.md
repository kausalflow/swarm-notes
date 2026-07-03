---
# CSL-compatible fields
title: "Sequential RC-TGAN: Generating Relational Time Series with Spectral Envelope Loss"
author:
  - literal: "Mohamed Gueye"
  - literal: "Yazid Attabi"
  - literal: "Manuel Morales"
  - literal: "Maxime Dumas"
issued:
  date-parts:
    - [2026, 6, 30]
url: "https://arxiv.org/abs/2606.31904"

# Custom fields
paper_id: "2606.31904"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "generative-adversarial-network"
  - "gan"
  - "synthetic-data-augmentation"
  - "evaluation"
architectures:
  []
datasets:
  []
concept_slugs:
  - "spectral-envelope-loss"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-03T07:55:02Z"
created_at: "2026-07-03T07:55:02Z"
---

# Sequential RC-TGAN: Generating Relational Time Series with Spectral Envelope Loss

**Authors**: Mohamed Gueye, Yazid Attabi, Manuel Morales, Maxime Dumas
**Date**: 2026-06-30
**Paper ID**: [openalex:2606.31904](https://arxiv.org/abs/2606.31904)

## Summary

Sequential RC-TGAN addresses the difficulty of generating relational categorical and continuous time series by integrating Spectral Envelope Theory into the training pipeline. The proposed differentiable Spectral Envelope Loss allows the generator to directly optimize for frequency-domain patterns, such as seasonality and cyclicity, which are often poorly captured by traditional encoding methods. To validate performance, the authors introduce a simulation-based benchmark with known spectral properties and propose new divergence-based metrics to rigorously evaluate cyclic fidelity. Experiments show that this approach achieves superior performance in reproducing long-term periodic structures across both categorical and continuous modalities.

## Key Contributions

- Proposes Sequential RC-TGAN, a generative framework specifically designed to model categorical and continuous relational time series.
- Introduces a differentiable Spectral Envelope Loss that enables backpropagation-based optimization of frequency-domain features like seasonality and cyclicity.
- Defines two novel evaluation metrics, Spectral Density Divergence and Spectral Envelope Divergence, to rigorously assess frequency-domain fidelity in generative models.

## Open Questions & Future Work

- [[frequency-domain-relational-generative-modeling]]

## Key Concepts

- [[spectral-envelope-loss]]: A differentiable loss function that optimizes the preservation of spectral properties and latent periodic structures in time series generation.

## Archivist Review

I approved the spectral envelope loss as a novel and potentially reusable training objective for generative time series models. I also approved an open question regarding frequency-domain modeling for relational time series, as this is a significant and unresolved research direction. Metrics were rejected as subcomponents of the paper's broader framework.

### Approved Concepts
- Spectral Envelope Loss: It allows the generative model to explicitly preserve periodicity and seasonality in categorical and continuous time series via backpropagation, directly addressing a gap in synthetic time series generation.

### Approved Open Questions
- Frequency Domain Relational Modeling: Addressing these gaps is essential for scaling relational generative models to enterprise data, which often features complex, mixed-type, and non-stationary temporal relationships.

### Rejected Candidates
- [concept] Spectral Density Divergence (`spectral-density-divergence`) - subcomponent_of_broader_mechanism: Metric subcomponents are generally considered paper-local unless they become standard benchmarks.
- [concept] Spectral Envelope Divergence (`spectral-envelope-divergence`) - subcomponent_of_broader_mechanism: Metric subcomponents are generally considered paper-local unless they become standard benchmarks.

## Links

- [Abstract](https://arxiv.org/abs/2606.31904)
- [PDF](https://arxiv.org/pdf/2606.31904)

