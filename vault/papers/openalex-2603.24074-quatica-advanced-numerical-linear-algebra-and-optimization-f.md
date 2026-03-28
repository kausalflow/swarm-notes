---
# CSL-compatible fields
title: "QuatIca: Advanced Numerical Linear Algebra and Optimization for Quaternionic Matrices in Python"
author:
  - literal: "Valentin Leplat"
  - literal: "Salman Ahmadi-Asl"
  - literal: "Junjun Pan"
  - literal: "Henni Ouerdane"
  - literal: "Michael Ng"
issued:
  date-parts:
    - [2026, 3, 25]
url: "https://arxiv.org/abs/2603.24074"

# Custom fields
paper_id: "2603.24074"
paper_source: "openalex"
domain: "computer-vision"
tags:
  - "tool-use"
  - "optimization"
  - "computer-vision"
  - "multimodal"
architectures:
  []
datasets:
  []
concept_slugs:
  - "quatica-library"
  - "optiq-quaternion-sdp-solver"
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-03-28T05:30:03Z"
created_at: "2026-03-28T05:30:03Z"
---

# QuatIca: Advanced Numerical Linear Algebra and Optimization for Quaternionic Matrices in Python

**Authors**: Valentin Leplat, Salman Ahmadi-Asl, Junjun Pan, Henni Ouerdane, Michael Ng
**Date**: 2026-03-25
**Paper ID**: [openalex:2603.24074](https://arxiv.org/abs/2603.24074)

## Summary

This paper introduces QuatIca, an open-source Python library designed to provide robust and numerically reliable software support for quaternion-valued representations, which are useful for coupled multi-channel signals like imagery and vector fields. The library implements core linear algebra functions such as dense decompositions (QR, Q-SVD, Cholesky) and iterative solvers (quaternion GMRES). Furthermore, it includes OptiQ, a module that solves quaternion Hermitian semidefinite programs using specialized log-det barrier Newton methods. The authors detail design choices made to preserve the inherent quaternion structure and validate the library through applications like quaternion image deblurring and signal filtering.

## Key Contributions

- Development of QuatIca, an open-source Python library offering core numerical linear algebra routines (QR, LU, Q-SVD, Cholesky, etc.) for quaternion matrices.
- Implementation of iterative solvers, including quaternion GMRES with preconditioning and Newton-Schulz pseudoinverse schemes, tailored for quaternion data structures.
- Introduction of OptiQ, a solver for quaternion Hermitian semidefinite programs utilizing log-det barrier Newton methods with $\mu$-continuation.
- Demonstration of practical application across domains including quaternion image deblurring, Lorenz-attractor filtering, and image completion.

## Limitations

The abstract does not explicitly state limitations, but the focus on numerical linear algebra suggests potential performance bottlenecks compared to highly optimized real/complex libraries for very large-scale deep learning models.

## Key Concepts

- [[quatica-library]]: An open-source Python library providing core quaternion matrix operations, decompositions, iterative solvers, and optimization routines.
- [[optiq-quaternion-sdp-solver]]: A component within QuatIca that solves quaternion Hermitian semidefinite programs using log-det barrier Newton methods with $\\mu$-continuation.

## Archivist Review

The paper introduces QuatIca, a fundamental software library for quaternion linear algebra, making both the library itself and its specialized optimization component, OptiQ, core reusable concepts. Since the paper is a library release focused on specialized numerical methods for quaternions (which are used in multi-channel signal processing), these two candidates were approved as they represent reusable numerical primitives that will be essential for future ML work using this representation. No suitable open questions or datasets were identified.

### Approved Concepts
- QuatIca Library: It is the central software contribution, providing a comprehensive suite for quaternion matrix operations and optimization.
- OptiQ Solver: It introduces a specialized solver for a difficult class of optimization problems (quaternion Hermitian semidefinite programs) relevant to signal processing and potentially ML regularization.

## Links

- [Abstract](https://arxiv.org/abs/2603.24074)
- [PDF](https://arxiv.org/pdf/2603.24074)

