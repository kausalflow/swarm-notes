---
created_at: '2026-04-11T05:54:01Z'
source_papers:
- '[[openalex-2604.07018-time-series-gaussian-chain-graph-models]]'
title: Non-Gaussian and Non-stationary Extensions
---

**Background:** Time series chain graph models represent multivariate temporal dependencies by partitioning variables into blocks, distinguishing between contemporaneous/lagged causal relations and within-block conditional dependencies. Most current estimation procedures for these models assume Gaussian distributions and strict stationarity.

**Question / Future Work:** Extend time series chain graph models to handle non-Gaussian distributions (e.g., heavy-tailed data) and non-stationary processes, which are common in real-world time series such as financial and biological data. This requires developing new identifiability criteria and estimation methods that relax the current reliance on Gaussian error processes and stationarity assumptions.

**Why It Matters:** Generalizing beyond Gaussian and stationary assumptions is essential for applying these graphical models to complex, real-world temporal data that frequently exhibit non-normality and structural shifts.