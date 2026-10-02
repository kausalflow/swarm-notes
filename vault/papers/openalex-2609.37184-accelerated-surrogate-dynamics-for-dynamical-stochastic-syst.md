---
# CSL-compatible fields
title: "Accelerated surrogate dynamics for dynamical, stochastic system evolution"
author:
  - literal: "Marco Jochum"
  - literal: "Ioannis Kouroudis"
  - literal: "Gohar Ali Siddiqui"
  - literal: "Taher Amine Hamzaoui"
  - literal: "Manuel Gößwein"
  - literal: "Alessio Gagliardi"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37184"

# Custom fields
paper_id: "2609.37184"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "transformer"
  - "variational-autoencoder"
  - "vae"
  - "graph-neural-network"
  - "gnn"
  - "convolutional-neural-network"
  - "cnn"
  - "uncertainty"
architectures:
  - "encoder-decoder"
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-02T10:48:01Z"
created_at: "2026-10-02T10:48:01Z"
---

# Accelerated surrogate dynamics for dynamical, stochastic system evolution

**Authors**: Marco Jochum, Ioannis Kouroudis, Gohar Ali Siddiqui, Taher Amine Hamzaoui, Manuel Gößwein, Alessio Gagliardi
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37184](https://arxiv.org/abs/2609.37184)

## Summary

This paper introduces an accelerated surrogate dynamics framework for simulating complex, stochastic systems by combining a Variational Autoencoder with a convolutional or graph-based dimensionality reduction module and a Temporal Fusion Transformer for time-series propagation. The approach handles high-dimensional feature spaces while simultaneously capturing both short- and long-range temporal effects to prevent simulation drift. Evaluated across three distinct test cases, the framework achieves high-fidelity results comparable to full dynamic simulations at a fraction of the computational cost, while supporting inbuilt uncertainty quantification.

## Key Contributions

- Proposes a surrogate dynamics framework combining dimensionality reduction (VAE with convolutional or graph basis) and temporal propagation via a Temporal Fusion Transformer.
- Addresses high-dimensional feature spaces and prevents local/global drift by encoding both long- and short-range effects alongside static covariate support.
- Achieves practically identical results to full dynamic simulations at a fraction of the computational cost across three distinct stochastic system test cases while providing inbuilt uncertainty quantification.

## Archivist Review

No concepts proposed as the framework combines existing architectures (VAE + CNN/GNN + TFT) without introducing a distinct, novel standalone mechanism or methodology that warrants its own vault entry.

## Links

- [Abstract](https://arxiv.org/abs/2609.37184)
- [PDF](https://arxiv.org/pdf/2609.37184)

