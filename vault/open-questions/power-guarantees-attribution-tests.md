---
created_at: '2026-07-19T07:24:41Z'
source_papers:
- '[[openalex-2607.14814-post-hoc-inference-for-component-attribution-in-multivariate]]'
title: Power guarantees for attribution tests
---

**Background:** Post-selection inference, where a data-driven selection step influences the distribution of subsequent test statistics, complicates the validity of attribution in multivariate time series. Standard statistical tests lose Type I error control when applied to samples defined based on estimated change-points, creating a fundamental selection bias.

**Question / Future Work:** Establishing the theoretical power of attribution procedures (like grid-based two-sample tests or hold-out methods) remains an unresolved challenge. While Type I error control is often provable under specific localization assumptions, the statistical power of these attribution methods in general, high-dimensional settings lacks rigorous analytical bounds.

**Why It Matters:** Understanding the power of attribution methods is essential to ensure they do not produce excessive false negatives in decision-critical applications like process control or clinical monitoring.