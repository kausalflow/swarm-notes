---
# CSL-compatible fields
title: "Adaptive Runge-Kutta Dynamics for Spatiotemporal Prediction"
author:
  - literal: "Xuanle Zhao"
  - literal: "Yue Sun"
  - literal: "Ziyi Wang"
  - literal: "Bo Xu"
  - literal: "Tielin Zhang"
issued:
  date-parts:
    - [2026, 4, 21]
url: "https://arxiv.org/abs/2405.14504"

# Custom fields
paper_id: "2405.14504"
paper_source: "openalex"
domain: "nlp"
tags:
  - "transformer"
  - "time-series"
  - "vision-transformer"
architectures:
  []
datasets:
  []
concept_slugs:
  - "adaptive-runge-kutta-dynamics"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-24T06:59:47Z"
created_at: "2026-04-24T06:59:47Z"
---

# Adaptive Runge-Kutta Dynamics for Spatiotemporal Prediction

**Authors**: Xuanle Zhao, Yue Sun, Ziyi Wang, Bo Xu, Tielin Zhang
**Date**: 2026-04-21
**Paper ID**: [openalex:2405.14504](https://arxiv.org/abs/2405.14504)

## Summary

This paper addresses the challenge of accurately modeling complex spatiotemporal dynamics by integrating numerical physical priors into deep learning. The authors introduce a physics-guided neural network that employs an adaptive second-order Runge-Kutta method to improve state estimation and a frequency-enhanced Fourier module to capture dynamic patterns. Evaluations across spatiotemporal and video prediction tasks demonstrate superior performance and parameter efficiency compared to existing methods.

## Key Contributions

- Introduces a physics-guided neural network utilizing an adaptive second-order Runge-Kutta method to more precisely model the evolution of physical states.
- Proposes a frequency-enhanced Fourier module to improve the representation and estimation of complex spatiotemporal dynamics.
- Achieves state-of-the-art performance on spatiotemporal and video prediction benchmarks while maintaining a smaller parameter footprint compared to existing models.

## Open Questions & Future Work

- [[robust-pde-approximation-kernels]]

## Key Concepts

- [[adaptive-runge-kutta-dynamics]]: A physics-guided neural network architecture that integrates adaptive second-order Runge-Kutta methods to model spatiotemporal physical states.

## Archivist Review

I approved the 'Adaptive Runge-Kutta Dynamics' concept as it represents a robust, reusable design pattern for integrating numerical solvers into neural architectures. The open question on PDE approximation robustness was approved for its fundamental role in physics-informed ML. I rejected the 'Frequency-enhanced Fourier module' because it is a common architectural component that lacks sufficient novelty to justify a standalone, permanent vault entry compared to existing frequency-domain mechanisms.

### Approved Concepts
- Adaptive Runge-Kutta Dynamics: Provides a principled numerical integration scheme for modeling physical state evolution, addressing the limitation of previous black-box neural approaches to spatiotemporal dynamics.

### Approved Open Questions
- Robustness of Convolutional PDE Approximation: This is critical because the reliance on convolution-based PDE estimation is a primary limiting factor for generalization to unknown physical systems; if kernels fail to accurately represent higher-order derivatives, the resulting physical dynamics model will be inherently flawed.

## Links

- [Abstract](https://arxiv.org/abs/2405.14504)
- [PDF](https://arxiv.org/pdf/2405.14504)

