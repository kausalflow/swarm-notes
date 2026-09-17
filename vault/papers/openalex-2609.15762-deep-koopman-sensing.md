---
# CSL-compatible fields
title: "Deep Koopman Sensing"
author:
  - literal: "Nithin Somasekharan"
  - literal: "Yadi Cao"
  - literal: "Shaowu Pan"
issued:
  date-parts:
    - [2026, 9, 14]
url: "https://arxiv.org/abs/2609.15762"

# Custom fields
paper_id: "2609.15762"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "deep-koopman-sensing"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-17T09:45:10Z"
created_at: "2026-09-17T09:45:10Z"
---

# Deep Koopman Sensing

**Authors**: Nithin Somasekharan, Yadi Cao, Shaowu Pan
**Date**: 2026-09-14
**Paper ID**: [openalex:2609.15762](https://arxiv.org/abs/2609.15762)

## Summary

Real-time fluid flow reconstruction from sparse sensor measurements is critical for flow control, yet standard reduced-order models are typically optimized for forward forecasting rather than state estimation. The authors propose Deep Koopman Sensing, a data-driven framework combining a nonlinear autoencoder with parameter-conditioned linear latent dynamics approximating the Koopman operator. Evaluated across four fluid dynamics benchmarks (1D Burgers, 2D cylinder flow, 2D dambreak, 3D sphere flow) using extended Kalman and ensemble filters, the approach achieves superior assimilation performance compared to pDMD, MLPs, and xLSTM, proving that latent dynamics should be explicitly tailored for downstream data assimilation rather than open-loop forecast accuracy.

## Key Contributions

- Introduces Deep Koopman Sensing, a data-driven reduced-order data assimilation framework combining a nonlinear autoencoder with parameter-conditioned linear latent dynamics approximating the Koopman operator.
- Demonstrates across 1D viscous Burgers, 2D flow past a cylinder, 2D dambreak, and 3D flow past a sphere that open-loop forecasting accuracy does not reliably predict state estimation performance.
- Shows that incorporating sparse sensor measurements with an extended Kalman filter or ensemble filtering enables Deep Koopman Sensing to achieve the lowest assimilation error across all four benchmarks.

## Open Questions & Future Work

- [[latent-dynamics-for-closed-loop-data-assimilation]]

## Key Concepts

- [[deep-koopman-sensing]]: A data-driven reduced-order data assimilation framework that combines a nonlinear autoencoder with parameter-conditioned linear latent dynamics approximating the Koopman operator.

## Archivist Review

Approved the core framework 'Deep Koopman Sensing' as a reusable concept for data assimilation and state reconstruction using Koopman operators, along with its central open question on aligning latent dynamics for closed-loop assimilation. All constraints, strict counts, and schema requirements were strictly followed.

### Approved Concepts
- Deep Koopman Sensing: Central framework introduced in the paper for real-time flow reconstruction from sparse sensor measurements.

### Approved Open Questions
- Latent Dynamics for Closed-Loop Assimilation: Bridging the gap between open-loop forecasting accuracy and closed-loop data assimilation performance is critical for reliable real-time sensing and control in fluid dynamics.

## Links

- [Abstract](https://arxiv.org/abs/2609.15762)
- [PDF](https://arxiv.org/pdf/2609.15762)

