---
# CSL-compatible fields
title: "MercerFlow: Flow Matching in a Kernel-Induced Latent Space for Probabilistic Forecasting"
author:
  - literal: "Ilya Kuleshov"
  - literal: "Egor Serov"
  - literal: "Alexey Zaytsev"
issued:
  date-parts:
    - [2026, 10, 5]
url: "https://arxiv.org/abs/2610.06039"

# Custom fields
paper_id: "2610.06039"
paper_source: "openalex"
domain: "time-series"
tags:
  - "forecasting"
  - "probabilistic-forecasting"
  - "generative-model"
  - "flow-matching"
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "mercerflow"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-08T11:40:57Z"
created_at: "2026-10-08T11:40:57Z"
---

# MercerFlow: Flow Matching in a Kernel-Induced Latent Space for Probabilistic Forecasting

**Authors**: Ilya Kuleshov, Egor Serov, Alexey Zaytsev
**Date**: 2026-10-05
**Paper ID**: [openalex:2610.06039](https://arxiv.org/abs/2610.06039)

## Summary

This paper investigates latent-space flow matching for probabilistic time series forecasting and introduces MercerFlow, a framework that leverages the Mercer eigenbasis of the prior kernel as an invertible latent map. By diagonalizing the covariance and adapting to non-stationary and periodic priors without data-dependent fitting, MercerFlow enables an efficient MLP-based flow matching model to match or outperform sequential baselines like TSFlow while significantly reducing training memory and time.

## Key Contributions

- Proposes MercerFlow, a flow matching model operating in a kernel-induced latent space using the Mercer eigenbasis of the prior kernel.
- Demonstrates that the Mercer eigenbasis diagonalizes the covariance, decouples from training data, and handles non-stationary and periodic priors effectively.
- Achieves competitive or superior CRPS performance compared to TSFlow on five GluonTS benchmarks while reducing training memory by ~4.7x and time per epoch by 3.5x--4.4x.

## Open Questions & Future Work

- [[kernel-induced-latent-flow-matching-scaling]]

## Key Concepts

- [[mercerflow]]: A probabilistic time series forecasting framework using flow matching in a kernel-induced latent space defined by the Mercer eigenbasis of the prior kernel.

## Archivist Review

Approved MercerFlow as the central methodological contribution and the open question regarding scaling kernel-induced latent flow matching, ensuring all vault guidelines and scarcity constraints were strictly met.

### Approved Concepts
- MercerFlow: Central framework introduced in the paper combining kernel-induced latent spaces and flow matching for time series forecasting.

### Approved Open Questions
- Scaling Latent Flow Matching: Understanding how prior-codec alignment and latent-space preconditioning scale to multivariate, high-dimensional, and transformer- or state-space-based generative architectures is crucial for advancing efficient probabilistic forecasting.

## Links

- [Abstract](https://arxiv.org/abs/2610.06039)
- [PDF](https://arxiv.org/pdf/2610.06039)

