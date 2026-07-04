---
title: "SIGReg"
slug: "sigreg"
type: concept
generated_stub: true
source_papers:
  - "[[openalex-2607.00958-lenepa-no-augmentation-next-latent-prediction-for-time-serie]]"
processed_at: "2026-07-04T07:35:45Z"
created_at: "2026-07-04T07:35:45Z"
---

# SIGReg

> *Auto-generated stub. Edit this file to add more details.*

An isotropy regularization technique used to stabilize neural latent space training without requiring stop-gradients or exponential moving averages.


## Why It Matters

This regularization method is the core stability mechanism enabling LeNEPA's no-augmentation objective, serving as a functional replacement for common but complex stabilization heuristics like EMA.

## Evidence

> LeNEPA replaces the stop-gradient/EMA stabilization used by vanilla NEPA with SIGReg-based isotropy regularization

## Related Papers

- [[openalex-2607.00958-lenepa-no-augmentation-next-latent-prediction-for-time-serie]]
