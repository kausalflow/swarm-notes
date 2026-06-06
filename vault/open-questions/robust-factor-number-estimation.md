---
created_at: '2026-06-06T07:40:05Z'
source_papers:
- '[[openalex-2501.13614-determining-the-number-of-factors-in-two-way-factor-model-of]]'
title: Robust Factor Number Estimation
---

**Background:** Factor models for matrix-variate time series rely on determining the correct number of row and column factors to achieve valid dimension reduction. Current methods often struggle with empirical parameter selection and robustness in the presence of weak factors or serial correlation.

**Question / Future Work:** The challenge involves developing an automated and robust framework for determining the number of factors in high-dimensional matrix-variate models that does not rely on heuristic thresholds or fixed upper bounds, especially in the presence of weak serial dependencies.

**Why It Matters:** This is a central limitation in applying factor models to real-world high-dimensional time series, where misspecification of factor counts directly compromises predictive accuracy.