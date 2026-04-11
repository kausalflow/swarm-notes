---
# CSL-compatible fields
title: "UMI: A GPU-Accelerated Asymmetric Robust Estimator for Photometric Detrending in Exoplanet Transit Searches"
author:
  - literal: "Omar Khan"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.06602"

# Custom fields
paper_id: "2604.06602"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "anomaly-detection"
architectures:
  []
datasets:
  []
concept_slugs:
  - "asymmetric-robust-detrending"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:56:16Z"
created_at: "2026-04-11T05:56:16Z"
---

# UMI: A GPU-Accelerated Asymmetric Robust Estimator for Photometric Detrending in Exoplanet Transit Searches

**Authors**: Omar Khan
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.06602](https://arxiv.org/abs/2604.06602)

## Summary

UMI is a novel, GPU-accelerated robust estimator designed for photometric detrending, specifically optimized for exoplanet transit detection. By employing an asymmetric weight function that targets downward dips and a modified upper-RMS scale estimator, it prevents transit signals from biasing noise estimation. Extensive validation on TESS and Kepler datasets shows that UMI significantly outperforms traditional methods like Savitzky-Golay and biweight in both computational speed and planet recovery accuracy.

## Key Contributions

- Introduces UMI (Unified Median Iterative), a robust location estimator for photometric detrending in exoplanet transit searches.
- Achieves 69x faster processing speeds compared to traditional biweight estimators via a fused HIP/CUDA GPU kernel.
- Demonstrates a 23% and 71% reduction in depth recovery error on TESS and Kepler datasets, respectively, compared to the standard biweight approach.

## Open Questions & Future Work

- [[asymmetric-detrending-bias-impact]]
- [[adaptive-asymmetry-selection]]

## Key Concepts

- [[asymmetric-robust-detrending]]: A robust estimation framework that uses asymmetric weighting to prevent signal-induced bias in noise-sensitive time-series detrending.

## Archivist Review

I approved 'Asymmetric Robust Detrending' because it provides a clear, reusable inductive bias for time-series preprocessing by constraining M-estimators based on physical signal properties. I also approved two research questions concerning the potential bias and parameter adaptation of this method, as these are critical concerns for any robust estimation framework applied to real-world time-series data. Other implementation details were rejected as they represent local acceleration techniques rather than algorithmic innovations.

### Approved Concepts
- Asymmetric Robust Detrending: Provides a domain-specific inductive bias for time-series detrending where signal-of-interest (e.g., dips) is strictly bounded by one side of the noise, a pattern recurring in anomaly detection and physical sensor monitoring.

### Approved Open Questions
- Asymmetric Detrending Bias Impact: Understanding if and how detrending-induced biases impact downstream sensitivity is critical for ensuring the reliability of large-scale automated signal detection in non-stationary time series.
- Adaptive Asymmetry Parameter Selection: Adaptive parameter selection enables a better balance between maximizing signal preservation and minimizing bias on a per-target basis, essential for heterogeneous time-series environments.

### Rejected Candidates
- [concept] Fused HIP/CUDA GPU Kernel (`fused-hip-cuda-kernel`) - paper_local: This is a specific implementation-level optimization rather than a generalizable algorithmic concept.

## Links

- [Abstract](https://arxiv.org/abs/2604.06602)
- [PDF](https://arxiv.org/pdf/2604.06602)

