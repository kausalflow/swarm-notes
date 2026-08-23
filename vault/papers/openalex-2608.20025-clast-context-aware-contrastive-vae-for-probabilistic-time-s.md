---
# CSL-compatible fields
title: "CLaST: Context-aware Contrastive VAE for Probabilistic Time Series Forecasting"
author:
  - literal: "Alexander Marusov"
  - literal: "Dmitry Anikin"
  - literal: "Petr Sokerin"
  - literal: "Vitaliy Pozdnyakov"
  - literal: "Ilya Kuleshov"
  - literal: "Alexey Zaytsev"
issued:
  date-parts:
    - [2026, 8, 20]
url: "https://arxiv.org/abs/2608.20025"

# Custom fields
paper_id: "2608.20025"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "probabilistic-forecasting"
  - "variational-autoencoder"
  - "vae"
  - "contrastive-learning"
  - "multivariate-time-series"
  - "benchmark"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  - "clast"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-23T05:18:55Z"
created_at: "2026-08-23T05:18:55Z"
---

# CLaST: Context-aware Contrastive VAE for Probabilistic Time Series Forecasting

**Authors**: Alexander Marusov, Dmitry Anikin, Petr Sokerin, Vitaliy Pozdnyakov, Ilya Kuleshov, Alexey Zaytsev
**Date**: 2026-08-20
**Paper ID**: [openalex:2608.20025](https://arxiv.org/abs/2608.20025)

## Summary

CLaST is a context-aware contrastive variational autoencoder (VAE) designed for probabilistic multivariate time series forecasting. By leveraging a novel contrastive loss function to preserve contextual similarity between temporal observations, CLaST addresses the limited expressiveness of latent representations found in conventional generative models. Extensive evaluations across nine benchmarks show significant performance gains in both short-term and long-term forecasting tasks compared to existing strong baselines.

## Key Contributions

- Proposes CLaST, a VAE framework for probabilistic multivariate time series forecasting that incorporates a contrastive loss to preserve contextual similarity between observations.
- Demonstrates consistent improvements across nine widely adopted benchmarks, outperforming baseline methods by up to 16.4% in CRPS and 14.4% in NMAE on short-term tasks.
- Achieves superior long-term prediction performance, exceeding second-best methods by up to 48.6% in CRPS and 25.1% in NMAE.

## Open Questions & Future Work

- [[scalable-similarity-matrix-computation]]

## Key Concepts

- [[clast]]: A context-aware contrastive VAE framework for probabilistic multivariate time series forecasting that preserves contextual similarity across latent representations.

## Archivist Review

We approve the overarching concept CLaST and the open question regarding scalable similarity matrix computation, maintaining strict adherence to our scarcity caps and novelty standards. No named datasets are approved since none were explicitly highlighted in the abstract or analysis text.

### Approved Concepts
- CLaST: CLaST introduces a contrastive VAE framework specifically designed to preserve contextual similarity in latent representations for probabilistic time series forecasting.

### Approved Open Questions
- Scalable Similarity Matrix Computation: Quadratic complexity limits applicability to extremely long input sequences or very high-dimensional time series, making scalable similarity estimation an important direction for future research.

## Links

- [Abstract](https://arxiv.org/abs/2608.20025)
- [PDF](https://arxiv.org/pdf/2608.20025)

