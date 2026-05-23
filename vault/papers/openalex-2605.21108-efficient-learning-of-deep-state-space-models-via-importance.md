---
# CSL-compatible fields
title: "Efficient Learning of Deep State Space Models via Importance Smoothing"
author:
  - literal: "John-Joseph Brady"
  - literal: "Nikolas Nüsken"
  - literal: "Yunpeng Li"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.21108"

# Custom fields
paper_id: "2605.21108"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "state-space-model"
  - "ssm"
  - "generative-adversarial-network"
  - "forecasting"
architectures:
  []
datasets:
  []
concept_slugs:
  - "parallel-variational-monte-carlo-pvmc"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:26:00Z"
created_at: "2026-05-23T07:26:00Z"
---

# Efficient Learning of Deep State Space Models via Importance Smoothing

**Authors**: John-Joseph Brady, Nikolas Nüsken, Yunpeng Li
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.21108](https://arxiv.org/abs/2605.21108)

## Summary

This paper addresses the computational inefficiency of training deep state space models (DSSMs), which typically rely on either variational lower bound optimization or inherently sequential Monte Carlo algorithms. The authors introduce Parallel Variational Monte Carlo (PVMC), a training framework that bridges these two paradigms to allow for efficient, parallelized computation. Empirical evaluations show that PVMC delivers state-of-the-art performance across baseline tasks while providing a 10x speedup over existing SMC training methods.

## Key Contributions

- Introduces Parallel Variational Monte Carlo (PVMC) to decouple the sequential bottleneck of traditional SMC-based DSSM training.
- Demonstrates that PVMC enables training of deep state space models for both discriminative and generative tasks.
- Achieves a 10x speedup in training throughput compared to state-of-the-art sequential Monte Carlo baselines.

## Open Questions & Future Work

- [[parallel-differentiable-particle-smoothing]]

## Key Concepts

- [[parallel-variational-monte-carlo-pvmc]]: A training method for deep state space models that enables parallelized computation by bridging the gap between variational inference and sequential Monte Carlo.

## Archivist Review

I approved the Parallel Variational Monte Carlo (PVMC) concept as it provides a distinct, reusable paradigm for overcoming sequential bottlenecks in state space model training. The open question regarding parallel differentiable particle smoothing was approved for capturing a significant unresolved theoretical and computational bottleneck in time-series latent modeling. No datasets were approved as none were cited as central to the paper's contribution.

### Approved Concepts
- Parallel Variational Monte Carlo: It acts as a bridging method between variational auto-encoding and SMC-based training, improving both scalability and versatility for DSSMs.

### Approved Open Questions
- Parallel Differentiable Particle Smoothing: This is central to enabling scalable training of deep state space models (DSSMs) for supervised and semi-supervised tasks, where high-fidelity latent representations and efficient parallel processing are both required.

## Links

- [Abstract](https://arxiv.org/abs/2605.21108)
- [PDF](https://arxiv.org/pdf/2605.21108)

