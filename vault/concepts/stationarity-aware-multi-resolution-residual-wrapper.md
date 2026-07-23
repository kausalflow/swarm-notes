---
title: "Stationarity-Aware Multi-Resolution Residual Wrapper"
slug: "stationarity-aware-multi-resolution-residual-wrapper"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2607.17511-lightweight-wrappers-for-adapting-time-series-foundation-mod]]"
processed_at: "2026-07-23T07:26:24Z"
created_at: "2026-07-23T07:26:24Z"
---

# Stationarity-Aware Multi-Resolution Residual Wrapper

> *Auto-generated stub. Edit this file to add more details.*

A stationarity-aware multi-resolution residual wrapper that adapts frozen time series foundation models at inference time via ensembling.


## Why It Matters

Provides a black-box, inference-time adaptation mechanism for time series foundation models that requires no backbone parameter updates.

## Evidence

> SMR^2 (Stationarity aware multi-resolution Residual), which decomposes the input into multi-resolution temporal views, learns stride specific residual corrections that capture regional dynamics, then adaptively ensembles them into a single forecast

## Related Papers

- [[openalex-2607.17511-lightweight-wrappers-for-adapting-time-series-foundation-mod]]
