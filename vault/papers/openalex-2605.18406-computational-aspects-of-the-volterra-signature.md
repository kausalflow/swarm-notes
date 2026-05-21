---
# CSL-compatible fields
title: "Computational aspects of the Volterra Signature"
author:
  - literal: "Paul P. Hager"
  - literal: "Fabian N. Harang"
  - literal: "Luca Pelizzari"
  - literal: "Samy Tindel"
issued:
  date-parts:
    - [2026, 5, 18]
url: "https://arxiv.org/abs/2605.18406"

# Custom fields
paper_id: "2605.18406"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
  - "embedding"
architectures:
  []
datasets:
  []
concept_slugs:
  - "volterra-signature"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-05-21T08:40:13Z"
created_at: "2026-05-21T08:40:13Z"
---

# Computational aspects of the Volterra Signature

**Authors**: Paul P. Hager, Fabian N. Harang, Luca Pelizzari, Samy Tindel
**Date**: 2026-05-18
**Paper ID**: [openalex:2605.18406](https://arxiv.org/abs/2605.18406)

## Summary

This paper addresses the computational complexity of the Volterra signature, an extension of the classical path signature that incorporates matrix-valued kernels for flexible memory modeling in time series. The authors decompose the Chen-type convolution relation to enable efficient computation and propose three algorithms: a general quadratic scheme, an FFT-based acceleration for uniform grids, and a state-space recursive approach. These methods significantly improve tractability, with complexity scaling efficiently relative to the number of time steps and kernel representation dimensions.

## Key Contributions

- Introduced efficient algorithms for computing the Volterra signature with quadratic O(J^2) complexity.
- Developed an FFT-based acceleration achieving O(J log J) complexity for convolution kernels on uniform grids.
- Formulated an exact O(JR^2) recursive algorithm for kernels with a state-space representation of dimension R.
- Implemented the proposed methodology in the open-source JAX-based library 'tensordev'.

## Open Questions & Future Work

- [[general-volterra-kernel-discretization]]

## Key Concepts

- [[volterra-signature]]: A path signature extension that incorporates matrix-valued kernels to model memory-dependent dynamics in time series.

## Archivist Review

The Volterra signature is a significant, theoretically rigorous extension of the path signature, meriting a standalone note for its potential in memory-aware time-series representation. The identified open question addresses a fundamental limitation in the computational tractability of these signatures, providing a clear path for future research in rough path analysis and time-series modeling. Other algorithmic contributions are treated as subcomponents of the overarching Volterra signature framework.

### Approved Concepts
- Volterra Signature: It provides a novel, memory-aware extension to the path signature for time-series analysis, overcoming the limitations of standard iterated integrals.

### Approved Open Questions
- General Volterra Kernel Computation: Identifying broader classes of kernels with efficient computational representations is critical for expanding the applicability of Volterra signatures to more complex time-series modeling tasks.

## Links

- [Abstract](https://arxiv.org/abs/2605.18406)
- [PDF](https://arxiv.org/pdf/2605.18406)

