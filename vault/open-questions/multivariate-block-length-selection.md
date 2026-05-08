---
created_at: '2026-05-08T06:27:14Z'
source_papers:
- '[[openalex-2605.03997-uncertainty-quantification-in-forecast-comparisons]]'
title: Multivariate block length selection
---

**Background:** The moving block bootstrap is a common resampling method for capturing temporal dependence in time series data, but its performance depends on the choice of the block length. In multivariate settings, data-driven methods for selecting this block length are not well-established.

**Question / Future Work:** Establishing principled, data-driven procedures for selecting the optimal block length in the moving block bootstrap for multivariate forecasting comparisons remains an open challenge. Currently, practitioners typically rely on ad-hoc rules of thumb, which may not be optimal for diverse forecasting applications.

**Why It Matters:** The accuracy of uncertainty quantification via the block bootstrap is highly sensitive to block length; an automatic selection procedure would remove a significant source of researcher subjectivity and potential bias.