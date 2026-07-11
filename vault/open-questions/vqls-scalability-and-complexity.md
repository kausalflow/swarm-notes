---
created_at: '2026-07-11T07:05:40Z'
source_papers:
- '[[openalex-2607.07634-qcnn-with-rough-path-signature-kernels]]'
title: VQLS scalability and complexity
---

**Background:** The Variational Quantum Linear Solver (VQLS) is a hybrid quantum-classical algorithm used to solve linear systems on near-term quantum hardware. Its rigorous computational complexity and scaling behavior remain central theoretical challenges in quantum machine learning.

**Question / Future Work:** The VQLS algorithm faces significant scalability bottlenecks when applied to systems derived from high-dimensional data, such as signature kernel matrices, where matrix condition numbers grow rapidly and the optimization landscape becomes highly non-convex. Further research is required to determine formal scaling limits and develop more robust ansatzes or initialization techniques for large-scale systems.

**Why It Matters:** Understanding VQLS scalability is critical for determining the feasibility of quantum hardware for complex linear algebraic operations in time series modeling.

**Evidence:** Future research should investigate strategies to improve VQLS trainability on large-scale systems, such as employing QAOA-based ansatzes or leveraging the inherent structure of the linear systems.