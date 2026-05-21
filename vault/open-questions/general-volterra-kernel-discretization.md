---
created_at: '2026-05-21T08:40:13Z'
source_papers:
- '[[openalex-2605.18406-computational-aspects-of-the-volterra-signature]]'
title: General Volterra Kernel Computation
---

**Background:** The computation of Volterra signatures for arbitrary kernel functions lacks a universally efficient closed-form solution, particularly when kernels are not restricted to specific families like finite-state space or convolution kernels.

**Question / Future Work:** It remains unclear how to systematically derive computationally efficient algorithms for a broader class of kernels that do not possess a finite state-space representation or convolution structure, while maintaining sub-quadratic complexity in the number of time steps. While specific approximation schemes exist for fractional and exponential-polynomial kernels, finding a general-purpose, efficient discretization for arbitrary Volterra kernels remains an unresolved challenge in rough path analysis.

**Why It Matters:** Identifying broader classes of kernels with efficient computational representations is critical for expanding the applicability of Volterra signatures to more complex time-series modeling tasks.

**Evidence:** Indeed, since the convolution \oast operation is not purely arithmetic, even when x is discretized a tractable computation without resorting to quadratures on the kernel requires additional structure and understanding.