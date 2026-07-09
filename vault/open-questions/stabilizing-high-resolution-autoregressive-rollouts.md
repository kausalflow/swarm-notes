---
created_at: '2026-07-09T08:18:10Z'
source_papers:
- '[[openalex-2607.05100-aifs-subs-extending-data-driven-forecasting-to-sub-seasonal]]'
title: Stabilizing high-resolution autoregressive rollouts
---

**Background:** Data-driven forecasting models often struggle with the trade-off between temporal resolution and the numerical stability of long-range autoregressive rollouts.

**Question / Future Work:** Research is needed to develop methods that allow data-driven models to operate with higher temporal resolution (e.g., 6h) over long autoregressive forecasts without suffering from the error accumulation that currently necessitates larger time steps. This involves identifying ways to either stabilize the rollout or predict daily averages while retaining sub-daily information.

**Why It Matters:** Improving temporal resolution is vital for accurately resolving the diurnal cycle and reducing discretization errors in numerical forecasting.

**Evidence:** The 24 h time step limits error accumulation over the long autoregressive rollout, but it comes at a cost: the model sees only instantaneous fields at a single time of day and cannot resolve the diurnal cycle. In future work we aim to stabilise error accumulation so that we can return to a 6 h time step, or alternatively predict daily means rather than instantaneous snapshots.