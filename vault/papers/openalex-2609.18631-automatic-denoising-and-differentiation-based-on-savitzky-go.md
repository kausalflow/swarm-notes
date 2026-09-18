---
# CSL-compatible fields
title: "Automatic denoising and differentiation based on Savitzky-Golay filtering and Homogeneous Differentiators for attractor reconstruction via differential embedding"
author:
  - literal: "Uros Sutulovic"
  - literal: "Daniele Proverbio"
  - literal: "Rami Katz"
  - literal: "Giulia Giordano"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18631"

# Custom fields
paper_id: "2609.18631"
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
  - "shaded"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:18:16Z"
created_at: "2026-09-18T09:18:16Z"
---

# Automatic denoising and differentiation based on Savitzky-Golay filtering and Homogeneous Differentiators for attractor reconstruction via differential embedding

**Authors**: Uros Sutulovic, Daniele Proverbio, Rami Katz, Giulia Giordano
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18631](https://arxiv.org/abs/2609.18631)

## Summary

The paper introduces SHADED, an automated methodology for denoising and high-order numerical differentiation of noisy time series that integrates Homogeneous Differentiators with Savitzky-Golay filtering. SHADED automatically determines all necessary parameters from data without manual tuning, enabling robust attractor reconstruction via differential embedding. The method is validated on computational neuroscience models, chaotic electronic circuits, and biomedical recordings such as photoplethysmography and arterial blood pressure.

## Key Contributions

- Introduces SHADED, a fully automated methodology combining Homogeneous Differentiators and Savitzky-Golay filtering for numerical differentiation and denoising of noisy time series.
- Automatically extracts all required parameters for HD and SG filtering from data without manual tuning.
- Demonstrates accurate attractor reconstruction via differential embedding across computational neuroscience models, electronic circuits, and biomedical recordings (PPG and ABP).

## Open Questions & Future Work

- [[system-specific-cost-functions-for-differential-embedding]]
- [[adaptive-staircase-depth-selection]]

## Key Concepts

- [[shaded]]: A methodology combining Homogeneous Differentiators and Savitzky-Golay filtering for automatic denoising and derivative estimation to enable attractor reconstruction from noisy time series.

## Archivist Review

The SHADED framework is approved as a distinctive, reusable methodology for automatic denoising and high-order numerical differentiation in differential embedding. The open questions regarding system-specific cost functions and adaptive staircase depth selection are approved as they address persistent challenges in automated phase space reconstruction. No datasets met the criteria for permanent vault notes.

### Approved Concepts
- SHADED: It is the core methodological contribution of the paper, enabling automatic denoising and numerical differentiation for differential embedding.

### Approved Open Questions
- System-Specific Cost Functions for Differential Embedding: Optimizing parameter selection costs for differential embedding and denoising remains an open problem across nonlinear dynamics and signal processing applications.
- Adaptive Staircase Depth Selection: Automating the determination of embedding dimension and differentiation depth prevents error accumulation and unnecessary computational overhead.

## Links

- [Abstract](https://arxiv.org/abs/2609.18631)
- [PDF](https://arxiv.org/pdf/2609.18631)

