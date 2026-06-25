---
# CSL-compatible fields
title: "Time Series Classification through Diffeomorphic Time Warping (DiffTW)"
author:
  - literal: "Vicky Geneva Haney"
  - literal: "Kamel Lahouel"
  - literal: "Victor Rielly"
  - literal: "Bruno M. Jedynak"
issued:
  date-parts:
    - [2026, 6, 22]
url: "https://arxiv.org/abs/2606.23472"

# Custom fields
paper_id: "2606.23472"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "machine-translation"
  - "benchmark"
architectures:
  []
datasets:
  []
concept_slugs:
  - "diffeomorphic-time-warping-difftw"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-06-25T08:16:46Z"
created_at: "2026-06-25T08:16:46Z"
---

# Time Series Classification through Diffeomorphic Time Warping (DiffTW)

**Authors**: Vicky Geneva Haney, Kamel Lahouel, Victor Rielly, Bruno M. Jedynak
**Date**: 2026-06-22
**Paper ID**: [openalex:2606.23472](https://arxiv.org/abs/2606.23472)

## Summary

This paper introduces Diffeomorphic Time Warping (DiffTW), a theoretically grounded dissimilarity measure for time series classification that addresses the limitations of standard discrete Dynamic Time Warping (DTW). The method approximates diffeomorphic transformations between sequences by mapping them as flows of a linear transport equation, which is subsequently solved using ordinary differential equations. By leveraging reproducing kernel Hilbert spaces and optimal control, the framework enables expressive, flexible sequence alignment. Empirically, DiffTW achieves better classification accuracy than traditional DTW across a wide range of benchmark datasets.

## Key Contributions

- Introduced Diffeomorphic Time Warping (DiffTW), a framework for time series alignment based on learning diffeomorphic mappings between real-valued functions.
- Formulated the alignment problem as a linear transport equation solved through the method of characteristics to model system dynamics as ODEs.
- Demonstrated superior classification performance over traditional Dynamic Time Warping (DTW) on 60 out of 86 datasets when paired with a 1-nearest neighbor classifier.

## Open Questions & Future Work

- [[robust-continuous-time-warping-high-frequency]]

## Key Concepts

- [[diffeomorphic-time-warping-difftw]]: A framework for measuring time series similarity by learning diffeomorphic mappings between continuous functions via the method of characteristics and optimal control.

## Archivist Review

The DiffTW framework is approved as a novel alternative to DTW for continuous time series alignment. The open question regarding high-frequency noise robustness is approved as it addresses a fundamental limitation in applying dynamical systems-based alignment to real-world, non-idealized data. No datasets were approved as they were reported as a aggregate collection (86 datasets) rather than a single critical artifact.

### Approved Concepts
- Diffeomorphic Time Warping (DiffTW): DiffTW introduces a novel, theoretically-grounded dissimilarity measure for time series that moves beyond discrete point-matching limitations of traditional DTW by using diffeomorphic transformations.

### Approved Open Questions
- High-Frequency Noise Robustness: Understanding how to handle high-frequency components is critical for expanding the applicability of continuous dynamical systems models to a wider range of real-world signal processing tasks.

## Links

- [Abstract](https://arxiv.org/abs/2606.23472)
- [PDF](https://arxiv.org/pdf/2606.23472)

