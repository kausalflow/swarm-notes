---
created_at: '2026-04-11T05:56:16Z'
source_papers:
- '[[openalex-2604.06602-umi-a-gpu-accelerated-asymmetric-robust-estimator-for-photom]]'
title: Asymmetric Detrending Bias Impact
---

**Background:** Exoplanet transit detection requires detrending photometric light curves to remove stellar variability, often using M-estimators like the Tukey bisquare. The introduction of asymmetric weight functions and one-sided scale estimators into these methods can introduce systematic flux biases that may affect the reliability of automated transit search pipelines.

**Question / Future Work:** Future work is required to systematically quantify the impact of the systematic flux bias introduced by asymmetric detrending estimators on the performance of downstream transit detection algorithms. Specifically, a rigorous false-positive analysis is necessary to ensure that constant-offset biases do not create or mask periodic signals.

**Why It Matters:** Understanding if and how detrending-induced biases impact downstream sensitivity is critical for ensuring the reliability of large-scale automated signal detection in non-stationary time series.