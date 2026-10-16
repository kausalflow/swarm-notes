---
created_at: '2026-10-16T09:22:55Z'
source_papers:
- '[[openalex-2610.17864-tstruct-learning-shared-temporal-structures-for-long-term-ti]]'
title: Resolution-Adaptive Temporal Structures
---

**Background:** Time series forecasting models often utilize fixed patch sizes to capture temporal dependencies, but the learned structures are fundamentally constrained to specific spatial-temporal resolutions.

**Question / Future Work:** Investigate how temporal dependency structures can be transferred, interpolated, or composed across different patch scales and resolutions without requiring fixed matrix dimensions.

**Why It Matters:** Crucial for building multi-scale and resolution-agnostic time series models that can seamlessly handle varying observation frequencies and input lengths.

**Evidence:** The learned temporal structures are tied to a specific patch resolution. Since each temporal dependency matrix is parameterized over N patch positions, changing the patch size or look-back length can alter the matrix dimensions or the temporal meaning of its coordinates... A promising direction is to develop resolution-adaptive temporal structures that can be transferred, interpolated, or composed across different patch scales.