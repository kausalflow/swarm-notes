---
# CSL-compatible fields
title: "Variational Augmented Invertible Koopman Autoencoder for probabilistic time series forecasting"
author:
  - literal: "Anthony Frion"
  - literal: "Lucas Drumetz"
  - literal: "Guillaume Tochon"
  - literal: "M. Dalla Mura"
  - literal: "Ali Can Bekar"
  - literal: "Abdeldjalil Aïssa El Bey"
issued:
  date-parts:
    - [2026, 9, 29]
url: "https://arxiv.org/abs/2609.37435"

# Custom fields
paper_id: "2609.37435"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "uncertainty-quantification"
  - "normalizing-flow"
  - "latent-variable-model"
architectures:
  - "encoder-only"
datasets:
  []
concept_slugs:
  - "variational-augmented-invertible-koopman-autoencoder"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-01T11:14:29Z"
created_at: "2026-10-01T11:14:29Z"
---

# Variational Augmented Invertible Koopman Autoencoder for probabilistic time series forecasting

**Authors**: Anthony Frion, Lucas Drumetz, Guillaume Tochon, M. Dalla Mura, Ali Can Bekar, Abdeldjalil Aïssa El Bey
**Date**: 2026-09-29
**Paper ID**: [openalex:2609.37435](https://arxiv.org/abs/2609.37435)

## Summary

This paper introduces the Variational Augmented Invertible Koopman AutoEncoder (VAIKAE), a novel probabilistic framework for long-term time series forecasting that models latent embeddings as Gaussian distributions. By incorporating normalizing flow models, VAIKAE enables likelihood computations directly in the state space of dynamical systems for robust training and uncertainty quantification. Additionally, the authors propose uncertainty-aware latent data assimilation strategies, demonstrating strong performance on benchmark evaluations.

## Key Contributions

- Proposed the Variational Augmented Invertible Koopman AutoEncoder (VAIKAE) to extend deterministic neural Koopman models to a probabilistic setting with Gaussian latent distributions.
- Leveraged normalizing flow models within VAIKAE to enable likelihood computations in the state space of dynamical systems during training.
- Developed new strategies for uncertainty-aware latent data assimilation using trained VAIKAE models, validated on long-term time series forecasting benchmarks.

## Open Questions & Future Work

- [[crps-based-training-koopman-autoencoders]]

## Key Concepts

- [[variational-augmented-invertible-koopman-autoencoder]]: A probabilistic neural Koopman autoencoder that uses normalizing flows to enable likelihood-based training and uncertainty quantification in time series forecasting.

## Archivist Review

Approved the VAIKAE concept for combining Koopman operators with variational normalizing flows for probabilistic forecasting, and retained the CRPS training open question as an actionable scaling bottleneck. Rejected the second open question as a vague operational extension.

### Approved Concepts
- Variational Augmented Invertible Koopman AutoEncoder: Introduces a probabilistic Koopman autoencoder leveraging normalizing flows and Gaussian latent distributions for uncertainty quantification in time series forecasting.

### Approved Open Questions
- CRPS-Based Koopman Autoencoder Training: Directly addresses the computational scaling bottleneck of likelihood-based training for high-dimensional states, which is critical for scaling Koopman autoencoders to massive spatio-temporal Earth science and fluid dynamics applications.

### Rejected Candidates
- [open_question] Generalizing CRPS Variational Data Assimilation (`crps-variational-data-assimilation-generalization`) - low_impact: Vague future work extension duplicating broader variational data assimilation goals.

## Links

- [Abstract](https://arxiv.org/abs/2609.37435)
- [PDF](https://arxiv.org/pdf/2609.37435)

