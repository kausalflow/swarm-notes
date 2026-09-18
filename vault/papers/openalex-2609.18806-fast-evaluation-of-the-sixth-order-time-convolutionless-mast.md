---
# CSL-compatible fields
title: "Fast Evaluation of the Sixth-Order Time-Convolutionless Master-Equation Generator and Beyond"
author:
  - literal: "Jiahao Chen"
  - literal: "Sirui Chen"
  - literal: "Dragomir Davidovic"
issued:
  date-parts:
    - [2026, 9, 16]
url: "https://arxiv.org/abs/2609.18806"

# Custom fields
paper_id: "2609.18806"
paper_source: "openalex"
domain: "time-series"
tags:
  - "time-series"
architectures:
  []
datasets:
  []
concept_slugs:
  []
dataset_slugs:
  []
skill: "TimeSeriesSkill"
processed_at: "2026-09-18T09:17:58Z"
created_at: "2026-09-18T09:17:58Z"
---

# Fast Evaluation of the Sixth-Order Time-Convolutionless Master-Equation Generator and Beyond

**Authors**: Jiahao Chen, Sirui Chen, Dragomir Davidovic
**Date**: 2026-09-16
**Paper ID**: [openalex:2609.18806](https://arxiv.org/abs/2609.18806)

## Summary

This paper presents an exact complexity reduction for evaluating higher-order time-convolutionless (TCL) master-equation generators for open quantum systems interacting with a stationary Gaussian bath. By separating operator coefficients from scalar bath kernels and reformulating the temporal dependencies into convolutions, cumulative sums, and dyadic recursions, the authors reduce the evaluation cost of the sixth-order TCL (TCL6) generator from $O(N_t^3)$ to $O(N_t\log^2 N_t)$. Furthermore, they generalize this approach to show that $\text{TCL}{2n}$ and finite Matsubara expansions can achieve log-linear or near-linear complexity scaling with respect to time steps.

## Key Contributions

- Derives an exact algorithmic reduction for the Hadamard-reduced sixth-order time-convolutionless (TCL6) generator, reducing evaluation complexity from $O(N_t^3)$ to $O(N_t\log^2 N_t)$ operations at fixed system dimension.
- Generalizes the complexity reduction to show that any $\text{TCL}{2n}$ expansion can be evaluated in $O(N_t\log^{n-1} N_t)$ time complexity.
- Demonstrates that using a fixed finite Matsubara expansion enables $O(N_t\log N_t)$ evaluation complexity for any arbitrary fixed TCL expansion order.

## Open Questions & Future Work

- [[higher-order-tcl-complexity-bounds-and-depth]]

## Archivist Review

I approved the open question regarding higher-order time-convolutionless (TCL) complexity bounds as it targets a specific theoretical bottleneck in evaluating non-Markovian open quantum systems. I rejected the concept candidate because it is highly domain-specific to quantum master equations rather than representing a general machine learning or forecasting methodology.

### Approved Open Questions
- Higher-Order TCL Complexity Bounds: Extending the fast evaluation framework from sixth order (TCL6) to arbitrary higher-order TCL expansions is crucial for understanding the computational complexity limits of high-order non-Markovian master equations.

### Rejected Candidates
- [concept] TCL6 Fast Evaluation Algorithm (`tcl6-fast-evaluation-algorithm`) - low_impact: The algorithmic complexity reduction for time-convolutionless master equations is a specialized physics/quantum dynamics method rather than a reusable machine learning or general time-series forecasting mechanism.

## Links

- [Abstract](https://arxiv.org/abs/2609.18806)
- [PDF](https://arxiv.org/pdf/2609.18806)

