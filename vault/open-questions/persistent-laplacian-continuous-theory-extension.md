---
created_at: '2026-07-12T07:27:50Z'
source_papers:
- '[[openalex-2607.08635-calibrated-persistent-laplacian-cusum-for-online-change-poin]]'
title: Continuous Theory for PL-CUSUM
---

**Background:** The persistent Laplacian provides a spectral representation of complex point clouds by capturing within-scale connectivity beyond standard homological persistence summaries. While this spectral information has proven informative for data analysis, its rigorous integration into online, sequential change-point detection frameworks with finite-horizon false-alarm and delay guarantees remains an emerging area of study.

**Question / Future Work:** A formal extension of the existing local minimax theory and finite-horizon detection bounds is required to accommodate continuous weighting or non-finite spectral coordinates. The current analysis relies on a finite-support exponential-tilting model, and replacing this with conditions such as the existence of a moment-generating function in a neighborhood of the origin would generalize the theoretical performance guarantees to broader classes of continuous distributions.

**Why It Matters:** The current reliance on finite-support models limits the theoretical applicability of the detector to practical scenarios where data generating processes are continuous and potentially high-dimensional. Generalizing this theory is essential for establishing performance bounds in more realistic, continuous-data regimes.

**Evidence:** To extend the detection bounds to continuous weights or continuous spectral coordinates, the finite-support assumption may be replaced by conditions such as finiteness of the moment-generating function under P0 in a neighbourhood of the origin...