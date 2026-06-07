---
created_at: '2026-06-07T08:19:21Z'
source_papers:
- '[[openalex-2606.06348-performance-evaluation-of-graphcast-for-medium-range-weather]]'
title: Bottlenecks in Extratropical MLWP Forecasting
---

**Background:** Autoregressive machine learning weather prediction models typically rely on training data discretized at relatively coarse temporal intervals, such as the 6-hour frequency common in reanalysis datasets like ERA5. In baroclinic environments, these models often exhibit distinct skill degradation in mid-to-upper tropospheric geopotential height forecasts while retaining accuracy in lower-tropospheric thermodynamic variables.

**Question / Future Work:** It remains unresolved whether the forecast degradation in mid-latitude winter regimes is caused by the undersampling of rapid baroclinic growth rates due to fixed temporal timesteps, or by insufficient modeling of vertical decoupling between upper-level synoptic flow and lower-level surface dynamics. Investigating the relative contribution of temporal sampling limitations versus vertical structure representation is essential for improving regional weather prediction fidelity.

**Why It Matters:** Understanding these failure modes is critical for the adaptation of global weather models to diverse regional climates, specifically to determine if architectural innovations like adaptive timestepping or better vertically-aware encoders are required.

**Evidence:** The 6 h temporal resolution of GraphCast operational... appears inadequate to resolve the growth and propagation of baroclinic systems... The vertical decoupling documented in this work... imposes a strong constraint on possible explanations.