---
# CSL-compatible fields
title: "Information bottleneck for learning the phase space of dynamics from high-dimensional experimental data"
author:
  - literal: "K. Michael Martini"
  - literal: "Eslam Abdelaleem"
  - literal: "Paarth Gulati"
  - literal: "Ilya Nemenman"
issued:
  date-parts:
    - [2026, 4, 27]
url: "https://arxiv.org/abs/2604.24662"

# Custom fields
paper_id: "2604.24662"
paper_source: "openalex"
domain: "nlp"
tags:
  - "time-series"
  - "interpretability"
architectures:
  []
datasets:
  []
concept_slugs:
  - "dynamical-symmetric-information-bottleneck"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-30T07:24:48Z"
created_at: "2026-04-30T07:24:48Z"
---

# Information bottleneck for learning the phase space of dynamics from high-dimensional experimental data

**Authors**: K. Michael Martini, Eslam Abdelaleem, Paarth Gulati, Ilya Nemenman
**Date**: 2026-04-27
**Paper ID**: [openalex:2604.24662](https://arxiv.org/abs/2604.24662)

## Summary

This paper introduces the Dynamical Symmetric Information Bottleneck (DySIB), a framework for learning low-dimensional latent representations of dynamical systems from high-dimensional observations. By maximizing predictive mutual information between past and future windows while minimizing complexity, the method avoids the need for explicit data reconstruction. Validation on a physical pendulum system demonstrates that DySIB effectively recovers the underlying phase space topology, geometry, and canonical coordinates in an unsupervised manner.

## Key Contributions

- Introduced DySIB, an information-theoretic method for unsupervised discovery of low-dimensional state variables from high-dimensional time series.
- Demonstrated that maximizing predictive mutual information in latent space successfully recovers the topology and geometry of the phase space of a physical pendulum.
- Showed that the learned representations align smoothly with canonical coordinates without requiring direct observation or reconstruction of raw data.

## Open Questions & Future Work

- [[canonical-latent-representation-form]]

## Key Concepts

- [[dynamical-symmetric-information-bottleneck]]: A method that learns low-dimensional dynamical representations by maximizing predictive mutual information between temporal windows while penalizing representation complexity.

## Archivist Review

I have approved the DySIB framework as it offers a clean, reconstruction-free approach to latent dynamics that is highly reusable for time-series representation learning. I also approved the open question regarding canonical latent forms because it addresses a fundamental, recurring limitation in the interpretability and cross-model alignment of learned latent manifolds. Standard boilerplate items were avoided in accordance with the selective review policy.

### Approved Concepts
- Dynamical Symmetric Information Bottleneck: It provides a novel, reconstruction-free objective function for learning interpretable latent representations of dynamical systems.

### Approved Open Questions
- Canonical latent representation form: Establishing such a canonical form is essential for moving beyond problem-specific validation and ensuring the reproducibility and generalizability of latent space learning across diverse dynamical systems.

## Links

- [Abstract](https://arxiv.org/abs/2604.24662)
- [PDF](https://arxiv.org/pdf/2604.24662)

