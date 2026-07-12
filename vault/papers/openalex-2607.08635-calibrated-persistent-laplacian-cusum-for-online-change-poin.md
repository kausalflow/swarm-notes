---
# CSL-compatible fields
title: "Calibrated Persistent-Laplacian CUSUM for Online Change-Point Detection"
author:
  - literal: "Shiheng Nie"
  - literal: "Yunguang Yue"
issued:
  date-parts:
    - [2026, 7, 9]
url: "https://arxiv.org/abs/2607.08635"

# Custom fields
paper_id: "2607.08635"
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
  - "persistent-laplacian-cumulative-sum-pl-cusum"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-07-12T07:27:50Z"
created_at: "2026-07-12T07:27:50Z"
---

# Calibrated Persistent-Laplacian CUSUM for Online Change-Point Detection

**Authors**: Shiheng Nie, Yunguang Yue
**Date**: 2026-07-09
**Paper ID**: [openalex:2607.08635](https://arxiv.org/abs/2607.08635)

## Summary

This paper introduces the Persistent Laplacian Cumulative Sum (PL-CUSUM), an online change-point detection method for high-dimensional, nonlinear time series. By transforming sliding windows into point clouds and computing persistent Laplacian spectra, the method effectively captures complex geometric structures that traditional persistent homology approaches overlook. The authors provide theoretical guarantees for false-alarm control and detection delay, complemented by a calibrated Phase I/Phase II operational procedure. Empirical results demonstrate that PL-CUSUM achieves stable false-alarm control and competitive performance across various simulated and real-world systems.

## Key Contributions

- Proposed the Persistent Laplacian Cumulative Sum (PL-CUSUM) method to capture within-scale connectivity and geometric structure via persistent Laplacian spectra.
- Derived theoretical false-alarm-delay bounds for the oracle detector and demonstrated false-alarm control for the plug-in whitened score.
- Established a robust Phase I/Phase II procedure for parameter selection and control-limit calibration in online monitoring.

## Open Questions & Future Work

- [[persistent-laplacian-continuous-theory-extension]]
- [[phase-i-estimation-error-propagation]]

## Key Concepts

- [[persistent-laplacian-cumulative-sum-pl-cusum]]: An online change-point detection framework that integrates persistent Laplacian spectra into the Page cumulative sum recursion for nonlinear time series.

## Archivist Review

I have approved the core method, PL-CUSUM, as it introduces a distinct topological-spectral integration for change-point detection. The two open questions are approved because they address fundamental theoretical limitations—continuous distribution generalization and parameter estimation error propagation—that are critical for the reliability of online streaming change-point detection systems.

### Approved Concepts
- Persistent Laplacian Cumulative Sum (PL-CUSUM): It is the core contribution of the paper, providing a novel framework for online change-point detection that leverages topological and spectral geometric information.

### Approved Open Questions
- Continuous Theory for PL-CUSUM: The current reliance on finite-support models limits the theoretical applicability of the detector to practical scenarios where data generating processes are continuous and potentially high-dimensional. Generalizing this theory is essential for establishing performance bounds in more realistic, continuous-data regimes.
- Unified Phase I Estimation Theory: These estimation errors are primary sources of deviation between theoretical performance and empirical results in real-world deployments. Understanding these bottlenecks is necessary for building more robust and provably reliable online monitoring systems.

## Links

- [Abstract](https://arxiv.org/abs/2607.08635)
- [PDF](https://arxiv.org/pdf/2607.08635)

