---
# CSL-compatible fields
title: "Time-Series Classification with Multivariate Statistical Dependence Features"
author:
  - literal: "Yao Sun"
  - literal: "Bo Hu"
  - literal: "Jose Principe"
issued:
  date-parts:
    - [2026, 4, 8]
url: "https://arxiv.org/abs/2604.06537"

# Custom fields
paper_id: "2604.06537"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "text-classification"
  - "speech-recognition"
  - "machine-translation"
  - "model-compression"
architectures:
  []
datasets:
  []
concept_slugs:
  - "cross-density-ratio-cdr"
  - "functional-maximal-correlation-algorithm-fmca"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-04-11T05:54:23Z"
created_at: "2026-04-11T05:54:23Z"
---

# Time-Series Classification with Multivariate Statistical Dependence Features

**Authors**: Yao Sun, Bo Hu, Jose Principe
**Date**: 2026-04-08
**Paper ID**: [openalex:2604.06537](https://arxiv.org/abs/2604.06537)

## Summary

This paper introduces a non-stationary time-series classification framework that replaces traditional correlation-based statistics with the Cross Density Ratio (CDR), a measure capturing statistical dependence in the joint density of input-target signals. By utilizing the Functional Maximal Correlation Algorithm (FMCA) to decompose the CDR's eigenspectrum, the method constructs a robust projection space for feature extraction. Evaluated on the TI-46 digit speech corpus, this lightweight approach outperforms hidden Markov models and spiking neural networks while maintaining a minimal storage footprint.

## Key Contributions

- Introduces the Cross Density Ratio (CDR) as a robust, order-independent measure for non-stationary time-series dependence.
- Proposes the Functional Maximal Correlation Algorithm (FMCA) to project time-series into an informative eigenspace.
- Achieves state-of-the-art classification accuracy on the TI-46 digit speech corpus using a lightweight architecture under 5 MB.

## Open Questions & Future Work

- [[complex-valued-fmca-extension]]

## Key Concepts

- [[cross-density-ratio-cdr]]: A measure of statistical dependence in the normalized joint density of input and target signals used to capture dependencies in time-series data.
- [[functional-maximal-correlation-algorithm-fmca]]: A feature extraction algorithm that constructs a projection space by decomposing the eigenspectrum of the Cross Density Ratio.

## Archivist Review

The approved concepts represent a novel, robust framework for time-series dependence estimation that avoids the pitfalls of standard correlation-based measures in non-stationary environments. The open question regarding complex-valued extensions identifies a clear architectural limitation that is technically significant for future spectral-focused time-series research. I have rejected the TI-46 dataset as it is a classical speech corpus that does not meet the criteria for a modern, reusable time-series benchmark dataset in this vault.

### Approved Concepts
- Cross Density Ratio (CDR): Provides a novel, sample-order-independent alternative to correlation-based statistics for capturing dependencies in non-stationary time-series.
- Functional Maximal Correlation Algorithm (FMCA): Central method for constructing the projection space from CDR for feature extraction.

### Approved Open Questions
- Extending FMCA to Complex-Valued Domains: Expanding to complex-valued processing allows for a more comprehensive utilization of signal information, which is critical for non-stationary signals where phase and spectral characteristics are fundamentally intertwined.

## Links

- [Abstract](https://arxiv.org/abs/2604.06537)
- [PDF](https://arxiv.org/pdf/2604.06537)

