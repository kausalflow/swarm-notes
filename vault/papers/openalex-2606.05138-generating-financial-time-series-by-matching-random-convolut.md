---
# CSL-compatible fields
title: "Generating Financial Time Series by Matching Random Convolutional Features"
author:
  - literal: "Konrad J. Mueller"
  - literal: "Nikita Zozoulenko"
  - literal: "Ben Wood"
  - literal: "Thomas Cass"
  - literal: "Lukas Gonon"
issued:
  date-parts:
    - [2026, 6, 3]
url: "https://arxiv.org/abs/2606.05138"

# Custom fields
paper_id: "2606.05138"
paper_source: "openalex"
domain: "finance"
tags:
  - "generative-model"
  - "time-series"
  - "feature-extraction"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "sock-soft-competing-kernels"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-06T07:39:44Z"
created_at: "2026-06-06T07:39:44Z"
---

# Generating Financial Time Series by Matching Random Convolutional Features

**Authors**: Konrad J. Mueller, Nikita Zozoulenko, Ben Wood, Thomas Cass, Lukas Gonon
**Date**: 2026-06-03
**Paper ID**: [openalex:2606.05138](https://arxiv.org/abs/2606.05138)

## Summary

Generating realistic financial time series from limited historical data is prone to overfitting with adversarial training. This paper proposes SOCK (SOft Competing Kernels), a fully differentiable random convolutional feature map that allows for supervising generative models by matching features rather than relying on discriminator memorization or limited-depth path signatures. Empirical results demonstrate that SOCK-based generative training outperforms standard diffusion and signature-based baselines across multiple small-sample financial datasets. Furthermore, SOCK shows strong utility as an unsupervised feature extractor for downstream classification and hypothesis testing tasks.

## Key Contributions

- Introduces SOCK (SOft Competing Kernels), a fully differentiable random convolutional feature map that enables the training of generative time series models without the limitations of signature-based methods.
- Demonstrates that generators trained using SOCK feature matching significantly outperform path signature and diffusion baselines on small-sample financial data.
- Validates the expressiveness of SOCK by showing competitive or superior performance in two-sample hypothesis testing and time-series classification compared to existing unsupervised feature maps.

## Open Questions & Future Work

- [[scalability-of-random-feature-matching-for-time-series-generation]]

## Key Concepts

- [[sock-soft-competing-kernels]]: A fully differentiable random convolutional feature map designed for supervising generative time series models.

## Archivist Review

I approved SOCK as a reusable differentiable feature extraction mechanism for generative time series training. I also approved an open question regarding the scalability of random feature matching in contrast to learned discriminators, as this is a fundamental limitation in the current study of non-adversarial generative training. I rejected no candidates because only one concept and one question were proposed, both of which were high-quality.

### Approved Concepts
- SOCK (SOft Competing Kernels): It provides a differentiable alternative to standard random convolutional feature maps (e.g., Rocket, Hydra), enabling their use as supervision signals for training generative models on time series.

### Approved Open Questions
- Scalability of Random Feature Matching: Understanding the performance limits of non-adversarial feature matching compared to learned discriminators is crucial for the adoption of these methods in broader financial time series generation tasks.

## Links

- [Abstract](https://arxiv.org/abs/2606.05138)
- [PDF](https://arxiv.org/pdf/2606.05138)

