---
# CSL-compatible fields
title: "Adaptive multi-line fitting for stable line-core intensity and Doppler velocity"
author:
  - literal: "Shahin Jafarzadeh"
  - literal: "David B. Jess"
  - literal: "M. Stangalini"
  - literal: "Peter H. Keys"
  - literal: "Glen Chambers"
  - literal: "Samuel D. T. Grant"
  - literal: "M. Berretti"
  - literal: "Timothy Duckenfield"
issued:
  date-parts:
    - [2026, 5, 20]
url: "https://arxiv.org/abs/2605.20861"

# Custom fields
paper_id: "2605.20861"
paper_source: "openalex"
domain: "speech"
tags:
  - "time-series"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "linefit"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-23T07:25:53Z"
created_at: "2026-05-23T07:25:53Z"
---

# Adaptive multi-line fitting for stable line-core intensity and Doppler velocity

**Authors**: Shahin Jafarzadeh, David B. Jess, M. Stangalini, Peter H. Keys, Glen Chambers, Samuel D. T. Grant, M. Berretti, Timothy Duckenfield
**Date**: 2026-05-20
**Paper ID**: [openalex:2605.20861](https://arxiv.org/abs/2605.20861)

## Summary

The paper introduces LineFit, a robust spectral analysis framework designed to handle the complexities of dense-window solar spectroscopy, such as line blending, asymmetry, and multi-lobed profiles. By employing bounded non-linear least-squares fitting with Voigt-family profiles and explicit split-core management, the method significantly improves the stability of line-core and Doppler velocity time series. Benchmarking shows LineFit outperforms common fast estimators in stress cases, resulting in more accurate downstream wave diagnostics. Additionally, the study showcases a hybrid emulation approach to accelerate the computationally demanding fitting process by three orders of magnitude.

## Key Contributions

- Introduces LineFit, a robust, adaptive multi-line spectral fitting method that reduces artifacts in line-core intensity and Doppler velocity estimations.
- Demonstrates LineFit's superior performance in tracking split-core spectral profiles and recovering accurate power spectra compared to standard fast estimation baselines.
- Provides a proof-of-concept for hybrid acceleration of the fitting algorithm through supervised emulation, achieving a 1000x speedup.

## Open Questions & Future Work

- [[hybrid-emulation-scalability]]

## Key Concepts

- [[linefit]]: An adaptive, multi-line spectral fitting approach that uses bounded non-linear least-squares with Voigt-family profiles and robust split-core handling for dense-window spectroscopy.

## Archivist Review

The proposed concept 'LineFit' is approved as it addresses a specific, non-trivial problem in spectral time-series extraction. The open question 'hybrid-emulation-scalability' is approved as it addresses the challenge of scaling physically-informed, compute-intensive fitting workflows, a bottleneck relevant across high-dimensional time-series domains. Other potential concepts were omitted to maintain the desired scarcity of the vault.

### Approved Concepts
- LineFit: It addresses the core problem of spectral line mis-tracking in complex solar observations, which introduces artifacts in wave and dynamics analysis.

### Approved Open Questions
- Scaling hybrid spectral emulation: Establishing robust hybrid emulation strategies is critical for handling the immense data volumes from next-generation instruments while preserving the diagnostic integrity required for MHD wave and dynamics research.

## Links

- [Abstract](https://arxiv.org/abs/2605.20861)
- [PDF](https://arxiv.org/pdf/2605.20861)

