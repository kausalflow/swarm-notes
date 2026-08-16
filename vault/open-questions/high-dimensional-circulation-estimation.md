---
created_at: '2026-08-16T05:17:39Z'
source_papers:
- '[[openalex-2608.13431-measuring-the-arrow-of-time-identification-estimation-and-in]]'
title: High-Dimensional Circulation and Entropy Estimation
---

**Background:** The standard empirical analysis of coupled time series often relies on contemporaneous correlation matrices, distance measures, or network centralities that are mathematically invariant to time-reversal transformations and therefore cannot identify directional structure.

**Question / Future Work:** Developing regularised estimators and associated inference procedures for the circulation matrix and entropy production rate when the dimensionality $n$ is large relative to the sample size $T$ (i.e., when $n^2/T$ exceeds operational thresholds without regularization).

**Why It Matters:** High-dimensional panels frequently arise in economics, neuroscience, and climate science where standard sample-moment estimators of circulation break down due to curse of dimensionality and noise accumulation.

**Evidence:** High dimension. At n^2/T above one, no estimator here is reliable. Regularised versions of the quadratic functional, along the lines developed for covariance estimation, would extend the reach considerably, and the cross-fitting structure is already the right one to build on.