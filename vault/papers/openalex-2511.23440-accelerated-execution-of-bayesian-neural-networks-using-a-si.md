---
# CSL-compatible fields
title: "Accelerated Execution of Bayesian Neural Networks using a Single Probabilistic Forward Pass and Code Generation"
author:
  - literal: "Bernhard Klein"
  - literal: "Falk Selker"
  - literal: "Hendrik Borras"
  - literal: "Sophie Steger"
  - literal: "Franz Pernkopf"
  - literal: "Holger Fröning"
issued:
  date-parts:
    - [2026, 10, 22]
url: "https://arxiv.org/abs/2511.23440"

# Custom fields
paper_id: "2511.23440"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "uncertainty"
  - "out-of-domain-detection"
  - "bayesian-neural-network"
  - "model-compression"
  - "quantization"
  - "efficient-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-10-23T09:41:30Z"
created_at: "2026-10-23T09:41:30Z"
---

# Accelerated Execution of Bayesian Neural Networks using a Single Probabilistic Forward Pass and Code Generation

**Authors**: Bernhard Klein, Falk Selker, Hendrik Borras, Sophie Steger, Franz Pernkopf, Holger Fröning
**Date**: 2026-10-22
**Paper ID**: [openalex:2511.23440](https://arxiv.org/abs/2511.23440)

## Summary

This paper addresses the high computational cost of Bayesian neural networks (BNNs) during inference by combining the Probabilistic Forward Pass (PFP) analytical uncertainty propagation method with deep learning code generation via TVM. By propagating Gaussian distributions through custom operators rather than executing multiple sampling forward passes, the proposed end-to-end deployment pipeline achieves dramatic speedups up to 3,900× on embedded ARM CPUs for small batch sizes. Evaluations on Dirty-MNIST and CIFAR-10 show that PFP-based BNNs maintain competitive uncertainty estimation and out-of-domain detection performance compared to traditional Stochastic Variational Inference while eliminating heavy computational overhead.

## Key Contributions

- Proposes an end-to-end pipeline for training, compilation, optimization, and deployment of Probabilistic Forward Pass (PFP)-based Bayesian Neural Networks on embedded ARM CPUs using TVM code generation.
- Implements custom Gaussian-propagating operators for MLPs and CNNs, achieving up to 3900x speedups for small mini-batch sizes compared to traditional Stochastic Variational Inference (SVI).
- Demonstrates that PFP-based BNNs match SVI-BNNs in uncertainty disentanglement on Dirty-MNIST and complex out-of-domain detection on CIFAR-10 against SVHN while drastically reducing computational overhead.

## Archivist Review

Reviewed the candidate open question against vault guidelines and rejected it as low impact and too general. No new concepts or datasets met the strict novelty and reusability standards.

### Rejected Candidates
- [open_question] Optimal Probabilistic Parameter Selection (`optimal-probabilistic-parameter-selection`) - low_impact: The question of optimal proportion of probabilistic parameters is broad and general rather than specific to a unique unresolved mechanism in this paper.

## Links

- [Abstract](https://arxiv.org/abs/2511.23440)
- [PDF](https://arxiv.org/pdf/2511.23440)

