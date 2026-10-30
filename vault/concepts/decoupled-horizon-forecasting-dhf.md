---
title: "Decoupled Horizon Forecasting"
slug: "decoupled-horizon-forecasting-dhf"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2610.37585-timestral]]"
processed_at: "2026-10-30T11:05:04Z"
created_at: "2026-10-30T11:05:04Z"
---

# Decoupled Horizon Forecasting

> *Auto-generated stub. Edit this file to add more details.*

A forecasting architecture that separates prediction tokens from causally encoded context, enabling multi-step forecasting without masking context tokens.


## Why It Matters

Addresses the fundamental limitation in autoregressive or sequence-to-sequence forecasting where long horizons require masking context or lose sequential feedback.

## Evidence

> Decoupled Horizon Forecasting (DHF), which separates prediction tokens from the causally encoded context, so that longer horizons are trained without masking context...

## Related Papers

- [[openalex-2610.37585-timestral]]
