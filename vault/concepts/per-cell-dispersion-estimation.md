---
title: "Per-cell Dispersion Estimation"
slug: "per-cell-dispersion-estimation"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2605.21437-neural-negative-binomial-regression-for-weekly-seismicity-fo]]"
processed_at: "2026-05-23T07:25:41Z"
created_at: "2026-05-23T07:25:41Z"
---

# Per-cell Dispersion Estimation

> *Auto-generated stub. Edit this file to add more details.*

A technique for count-based spatiotemporal forecasting that uses a neural network to learn an endogenous, per-cell overdispersion parameter instead of assuming global homogeneity.


## Why It Matters

It replaces the common assumption of global overdispersion in count forecasting with a flexible, data-driven per-cell mechanism that accounts for spatial heterogeneity.

## Evidence

> the EarthquakeNet architecture, which provides an endogenous per-cell estimate of the overdispersion parameter alpha via a neural network (spatial embeddings + MLP), without explicit spatial covariance specification.

## Related Papers

- [[openalex-2605.21437-neural-negative-binomial-regression-for-weekly-seismicity-fo]]
