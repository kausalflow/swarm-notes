---
# CSL-compatible fields
title: "QCNN with Rough Path Signature Kernels"
author:
  - literal: "Leonardo Nogueira Falabella"
  - literal: "Vasily Sazonov"
issued:
  date-parts:
    - [2026, 7, 8]
url: "https://arxiv.org/abs/2607.07634"

# Custom fields
paper_id: "2607.07634"
paper_source: "openalex"
domain: "nlp,time-series"
tags:
  - "time-series"
  - "text-classification"
  - "quantum-neural-networks"
  - "kernel-methods"
architectures:
  []
datasets:
  []
concept_slugs:
  - "rough-path-signature-kernels"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-11T07:05:40Z"
created_at: "2026-07-11T07:05:40Z"
---

# QCNN with Rough Path Signature Kernels

**Authors**: Leonardo Nogueira Falabella, Vasily Sazonov
**Date**: 2026-07-08
**Paper ID**: [openalex:2607.07634](https://arxiv.org/abs/2607.07634)

## Summary

This paper introduces a hybrid quantum-classical architecture for time series classification that leverages rough path signature kernels to maintain invariance against time reparameterization. By integrating signature kernel feature layers—computed via either classical or quantum variational linear solvers—with a downstream Quantum Convolutional Neural Network (QCNN), the model effectively processes temporal data. The authors analyze the computational challenges of the VQLS components and empirically validate the approach on handwritten digit time series.

## Key Contributions

- Proposes a hybrid quantum-classical architecture that uses rough path signature kernels to achieve time reparameterization invariance in time series data.
- Integrates variational linear solvers (VQLS) with signature kernels for quantum-enhanced feature extraction.
- Evaluates the proposed framework on a time-series classification task of handwritten digits, demonstrating the feasibility of QCNN-based downstream learning.

## Open Questions & Future Work

- [[vqls-scalability-and-complexity]]

## Key Concepts

- [[rough-path-signature-kernels]]: A feature extraction method that computes kernels between time series paths using path signature mathematics, integrated into a hybrid quantum-classical pipeline.

## Archivist Review

The paper introduces a mathematically principled approach to time series representation via path signatures in a quantum-classical hybrid setting. I approved the concept for its reuse potential in time-series feature engineering and the open question for its substantial role in the advancement of variational quantum algorithms. No datasets were approved as the handwritten digit experiment is routine for time-series classification benchmarks.

### Approved Concepts
- Rough Path Signature Kernels: It enables the computation of signature-based kernels within a quantum circuit, providing time reparameterization invariance which is a critical problem in time series representation.

### Approved Open Questions
- VQLS scalability and complexity: Understanding VQLS scalability is critical for determining the feasibility of quantum hardware for complex linear algebraic operations in time series modeling.

## Links

- [Abstract](https://arxiv.org/abs/2607.07634)
- [PDF](https://arxiv.org/pdf/2607.07634)

