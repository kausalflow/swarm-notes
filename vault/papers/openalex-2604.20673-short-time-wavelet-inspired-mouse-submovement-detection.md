---
# CSL-compatible fields
title: "Short-time, Wavelet-inspired Mouse Submovement Detection"
author:
  - literal: "Auejin Ham"
  - literal: "Ben Boudaoud"
issued:
  date-parts:
    - [2026, 4, 22]
url: "https://arxiv.org/abs/2604.20673"

# Custom fields
paper_id: "2604.20673"
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
  - "self-weighted-loss-refinement"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-25T06:16:19Z"
created_at: "2026-04-25T06:16:19Z"
---

# Short-time, Wavelet-inspired Mouse Submovement Detection

**Authors**: Auejin Ham, Ben Boudaoud
**Date**: 2026-04-22
**Paper ID**: [openalex:2604.20673](https://arxiv.org/abs/2604.20673)

## Summary

This paper introduces a wavelet-inspired framework to extract and analyze ballistic submovements from complex, overlapping 1D speed time series. The method addresses the challenge of accurately parameterizing these motions by implementing a self-weighted loss refinement step that specifically targets and corrects regions with poor quality of fit. Evaluated on ~6,400 synthetic mouse aim trials modeled after real-user data, the approach provides more accurate submovement detection compared to traditional thresholding and persistence-based segmentation methods.

## Key Contributions

- Proposes a wavelet-inspired method for detecting and parameterizing overlapping submovements in high-speed motion data.
- Introduces a self-weighted loss refinement mechanism to improve signal fit quality for non-stationary submovement patterns.
- Demonstrates superior performance over dual-threshold and persistence-based 1D segmentation techniques using a controlled synthetic dataset of ~6,400 mouse aim trials.

## Open Questions & Future Work

- [[robust-submovement-decomposition-refinement]]

## Key Concepts

- [[self-weighted-loss-refinement]]: A refinement technique that dynamically weights loss based on fit performance to improve wavelet-based signal decomposition.

## Archivist Review

I approved the self-weighted loss refinement concept because it provides a generally useful architectural pattern for improving wavelet-based decomposition in the presence of noise and overlap. The open question was approved for its focus on the critical bottleneck of termination criteria in iterative decomposition frameworks. The dataset was rejected for being a localized synthetic evaluation tool rather than a reusable benchmark.

### Approved Concepts
- Self-weighted loss refinement: It addresses a common limitation of fixed wavelet transforms in signal decomposition by dynamically adjusting based on local fit quality.

### Approved Open Questions
- Robust Submovement Decomposition Refinement: Establishing standardized, robust decomposition frameworks is vital for motor assessment and adaptive human-computer interaction applications.

### Rejected Candidates
- [dataset] Synthetic mouse aim dataset (`mouse-aim-data-trials`) - low_impact: This is a small, task-specific synthetic dataset rather than a benchmark-grade collection of broad interest.

## Links

- [Abstract](https://arxiv.org/abs/2604.20673)
- [PDF](https://arxiv.org/pdf/2604.20673)

