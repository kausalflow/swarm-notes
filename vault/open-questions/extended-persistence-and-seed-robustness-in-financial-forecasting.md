---
created_at: '2026-10-09T11:35:38Z'
source_papers:
- '[[openalex-2610.09654-dstnet-dynamic-spectral-trajectory-network-for-causal-multi]]'
title: Extended Persistence and Seed Robustness
---

**Background:** Financial multi-horizon forecasting models evaluate performance primarily against historical equity indices and single non-equity probes under standard validation protocols.

**Question / Future Work:** Investigate extending the random-walk persistence comparison to longer forecast horizons beyond one day, evaluate rolling origins across broader asset classes and historical periods, rerun stochastic baselines and models across additional random seeds, and conduct un-gated decoder ablations to isolate the utility of horizon-specific gating.

**Why It Matters:** Crucial for establishing whether proposed multi-horizon deep learning architectures maintain statistical superiority over persistence benchmarks across diverse economic regimes and varied model initializations.

**Evidence:** The immediate next step is extending the persistence comparison to H ∈ {3, 5, 10}, which the stored per-origin errors already permit without retraining. Beyond that: rolling origins across more assets and periods, more seeds with the stochastic baselines rerun under the same set, an ungated-decoder ablation to test whether horizon gating earns its place...