---
# CSL-compatible fields
title: "Curriculum Multiple Shooting for Robust Training of Neural and Universal Differential Equations"
author:
  - literal: "Sebastian Persson"
  - literal: "Giacomo Fabrini"
  - literal: "Branwen Snelling"
  - literal: "Fabian Fröhlich"
issued:
  date-parts:
    - [2026, 8, 6]
url: "https://arxiv.org/abs/2608.05777"

# Custom fields
paper_id: "2608.05777"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "forecasting"
  - "robustness"
architectures:
  []
datasets:
  []
concept_slugs:
  - "curriculum-multiple-shooting"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-08-09T05:40:55Z"
created_at: "2026-08-09T05:40:55Z"
---

# Curriculum Multiple Shooting for Robust Training of Neural and Universal Differential Equations

**Authors**: Sebastian Persson, Giacomo Fabrini, Branwen Snelling, Fabian Fröhlich
**Date**: 2026-08-06
**Paper ID**: [openalex:2608.05777](https://arxiv.org/abs/2608.05777)

## Summary

Neural ordinary differential equations (NODEs) and universal differential equations (UDEs) struggle with robust training on sparse and noisy time-series data. To resolve this, the authors introduce curriculum multiple shooting (CMS), a training strategy combining curriculum learning with multiple shooting. Evaluated across twelve benchmarks covering NODEs, UDEs, and mechanistic ODEs, CMS accelerates convergence, improves generalisation, and outperforms current state-of-the-art methods.

## Key Contributions

- Introduces Curriculum Multiple Shooting (CMS), a general-purpose training strategy that integrates curriculum learning with multiple shooting for neural and universal differential equations.
- Demonstrates that CMS accelerates and stabilises training convergence across twelve simulated and real-world benchmarks spanning NODEs, UDEs, and mechanistic ODEs.
- Outperforms existing state-of-the-art training strategies and ranks among top methods in generalisation on sparse and noisy time-series data.

## Open Questions & Future Work

- [[scaling-cms-high-dimensional-odes]]

## Key Concepts

- [[curriculum-multiple-shooting]]: A general-purpose training strategy for fitting ODE models to time-series data by integrating curriculum learning with multiple shooting.

## Archivist Review

Approved the core methodological concept 'Curriculum Multiple Shooting' and the open question regarding its scaling to high-dimensional ODEs. Applied strict selectivity criteria; no other candidates met the thresholds.

### Approved Concepts
- Curriculum Multiple Shooting: It is the core methodological contribution of the paper, combining curriculum learning with multiple shooting for robust training of neural and universal differential equations.

### Approved Open Questions
- Scaling Curriculum Multiple Shooting: High-dimensional dynamical systems modeling is critical for applications like single-cell genomics and systems biology, yet existing ODE training strategies often break down or become computationally intractable as state and parameter dimensions grow.

## Links

- [Abstract](https://arxiv.org/abs/2608.05777)
- [PDF](https://arxiv.org/pdf/2608.05777)

