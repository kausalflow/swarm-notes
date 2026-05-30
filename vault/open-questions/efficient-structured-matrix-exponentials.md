---
created_at: '2026-05-30T07:35:06Z'
source_papers:
- '[[openalex-2605.28507-universal-time-series-generation-with-neural-controlled-diff]]'
title: Efficient Structured Matrix Exponentials
---

**Background:** In continuous-time neural networks based on linear ODEs or CDEs, computing the matrix exponential efficiently on GPU hardware is a significant computational bottleneck.

**Question / Future Work:** Developing high-performance GPU kernels for exact structured matrix exponentials is necessary to move beyond current first-order approximations, improving both the computational runtime and the mathematical accuracy of CDE-based models.

**Why It Matters:** The matrix exponential is a fundamental operation in structured differential equation models; its optimized implementation is essential for widespread adoption and scaling of these methods.

**Evidence:** efficient GPU kernels for structured matrix exponentials remain an important direction.