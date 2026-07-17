---
created_at: '2026-07-17T07:10:29Z'
source_papers:
- '[[openalex-2411.19572-canonical-correlation-analysis-of-stochastic-trends-via-func]]'
title: Improving long-run variance estimation
---

**Background:** The estimation of long-run variance matrices is critical for constructing asymptotically valid test statistics in nonstationary time series analysis.

**Question / Future Work:** Existing nonparametric estimators of the long-run variance matrix perform poorly in finite samples, leading to significant size distortions in hypothesis testing. Research is needed to develop more accurate, robust, or shrinkage-based estimators for canonical correlation analysis of stochastic trends.

**Why It Matters:** Imprecise long-run variance estimation is a persistent obstacle to the reliability of statistical inference in nonstationary systems.

**Evidence:** The main challenge in the implementation of the tests lies in the precise estimation of the LRV Omega_22.1... The tests are largely oversized in finite samples... suggesting that a major part of the size distortions are due to the imprecise LRV estimation.