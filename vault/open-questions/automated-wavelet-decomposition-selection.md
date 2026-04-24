---
created_at: '2026-04-24T06:59:22Z'
source_papers:
- '[[openalex-2509.14640-dywpe-signal-aware-dynamic-wavelet-positional-encoding-for-t]]'
title: Automated Wavelet Decomposition Selection
---

**Background:** Positional encoding methods in transformer models generally derive information from static sequence indices rather than the input signal itself, often failing to account for non-stationary dynamics. While signal-aware frameworks can improve performance, the optimal configuration of temporal decomposition parameters remains highly dependent on signal characteristics.

**Question / Future Work:** Investigate methods to automatically select or meta-learn the optimal wavelet decomposition parameters, such as decomposition depth and wavelet family, to suit the inherent spectral complexity and hierarchy of different time series datasets without manual tuning.

**Why It Matters:** This addresses a key bottleneck in applying signal-aware architectures, as current methods often require task-specific manual tuning that limits generalizability.

**Evidence:** UniMiB-SHAR shows negative results (-1.0%), indicating that multi-scale decomposition benefits depend on signal complexity.