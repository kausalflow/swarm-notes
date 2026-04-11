---
# CSL-compatible fields
title: "Estimating varying parameters in dynamical systems: a modular framework using switch detection, optimization and sparse regression"
author:
  - literal: "Jamiree Harrison"
  - literal: "Enoch Yeung"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2412.16198"

# Custom fields
paper_id: "2412.16198"
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
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:55:57Z"
created_at: "2026-04-11T05:55:57Z"
---

# Estimating varying parameters in dynamical systems: a modular framework using switch detection, optimization and sparse regression

**Authors**: Jamiree Harrison, Enoch Yeung
**Date**: 2026-04-08
**Paper ID**: [openalex:2412.16198](https://arxiv.org/abs/2412.16198)

## Summary

This paper presents a modular framework for estimating time-varying and spatially varying parameters in dynamical systems, assuming prior knowledge of the system dynamics. The approach handles both discrete piecewise constant parameter switches—via binary segmentation and optimization—and continuously varying parameters through dictionary-based sparse regression. The framework is evaluated across diverse models, including gene expression networks and partial differential equations, demonstrating robustness to measurement noise and varying data resolution.

## Key Contributions

- A modular algorithmic framework for identifying time-varying and spatially varying parameters in dynamical systems by combining switch detection, optimization, and sparse regression.
- Implements binary segmentation for detecting discrete parameter switches alongside Nelder-Mead and Powell optimization for piecewise constant model fitting.
- Extends the approach to continuously varying parameter estimation through dictionary-based sparse regression using trigonometric and polynomial functions.

## Open Questions & Future Work

- [[robust-estimation-mixed-varying-parameters]]

## Archivist Review

I rejected the proposed framework and standard techniques (binary segmentation, sparse regression) as they are well-established methods rather than novel contributions. I approved the open question regarding mixed-varying parameters because it addresses a substantial bottleneck in modeling complex non-stationary systems that persists across many scientific domains. The approved open question was polished for conciseness and technical clarity.

### Approved Open Questions
- Robust Estimation of Mixed-Varying Parameters: This problem is fundamental to modeling and control of complex real-world dynamical systems (e.g., biological or physical processes), which rarely follow static parameter assumptions.

### Rejected Candidates
- [concept] Modular Framework for Parameter Estimation (`modular-framework-for-parameter-estimation`) - paper_local: The framework is a general system architecture rather than a specific, novel, and reusable technical concept.
- [concept] Dictionary-based Sparse Regression (`dictionary-based-sparse-regression`) - not_novel: This is an existing statistical technique and not a novel concept specific to this work.
- [concept] Binary Segmentation for Switch Detection (`binary-segmentation-for-switch-detection`) - not_novel: Binary segmentation is a well-established classical statistical technique for change-point detection.

## Links

- [Abstract](https://arxiv.org/abs/2412.16198)
- [PDF](https://arxiv.org/pdf/2412.16198)

