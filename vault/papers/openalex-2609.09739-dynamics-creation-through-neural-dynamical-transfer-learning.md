---
# CSL-compatible fields
title: "Dynamics Creation through Neural Dynamical Transfer Learning"
author:
  - literal: "He Ma"
  - literal: "Qiyang Ge"
  - literal: "Yu Meng"
  - literal: "Celso Grebogi"
  - literal: "Wei Lin"
issued:
  date-parts:
    - [2026, 9, 9]
url: "https://arxiv.org/abs/2609.09739"

# Custom fields
paper_id: "2609.09739"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "reinforcement-learning"
architectures:
  []
datasets:
  []
concept_slugs:
  - "neural-dynamical-transfer-learning"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-12T08:55:47Z"
created_at: "2026-09-12T08:55:47Z"
---

# Dynamics Creation through Neural Dynamical Transfer Learning

**Authors**: He Ma, Qiyang Ge, Yu Meng, Celso Grebogi, Wei Lin
**Date**: 2026-09-09
**Paper ID**: [openalex:2609.09739](https://arxiv.org/abs/2609.09739)

## Summary

Data-driven machine learning has traditionally focused on reconstructing existing nonlinear dynamical systems rather than generating new ones. To address this, the authors introduce Neural Dynamical Transfer Learning (NDTL), a framework inspired by style transfer that creates new systems with prescribed dynamics from pairs of parent nonlinear dynamical systems. By evaluating key dynamical signatures like the Lyapunov spectrum and intrinsic dimension, NDTL is shown to successfully preserve inherited features while yielding novel dynamics across various applications including ecological modeling, epidemiology, and chaos-based image encryption.

## Key Contributions

- Introduces Neural Dynamical Transfer Learning (NDTL), a neural framework for generating new nonlinear dynamical systems with prescribed dynamics from parent systems.
- Demonstrates that NDTL preserves inherited features while generating novel dynamics, validated via fundamental dynamical signatures such as intrinsic dimension, Kaplan-Yorke dimension, invariant measure statistics, and the Lyapunov spectrum.
- Applies NDTL to induce a dynamics classification criterion, create stable oscillatory coexistence in the Hastings-Powell food chain model, produce interpretable epidemiological models, and provide a chaotic source for image encryption.

## Open Questions & Future Work

- [[physics-informed-layerwise-system-design]]

## Key Concepts

- [[neural-dynamical-transfer-learning]]: A neural network framework for generating new nonlinear dynamical systems with prescribed dynamics from parent dynamical systems.

## Archivist Review

Approved the central NDTL framework concept and its corresponding open question regarding layerwise physical interpretability and design, as they represent novel methodological contributions to dynamical systems machine learning. No named standalone datasets were present.

### Approved Concepts
- Neural Dynamical Transfer Learning: Central framework introduced in the paper for generative synthesis of new dynamical systems from pairs of parent nonlinear systems.

### Approved Open Questions
- Physics-Informed Layerwise System Design: Understanding the distinct physical roles of different network layers in dynamical system generation bridges deep learning representations with rigorous dynamical systems theory, enabling targeted control over system creation and modulation.

## Links

- [Abstract](https://arxiv.org/abs/2609.09739)
- [PDF](https://arxiv.org/pdf/2609.09739)

