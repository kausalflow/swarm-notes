---
created_at: '2026-06-20T08:17:25Z'
source_papers:
- '[[openalex-2606.18686-forecastbench-sim-a-simulated-world-forecasting-benchmark]]'
title: Brier vs. CRPS Performance Divergence
---

**Background:** In forecasting tasks, performance rankings can differ significantly depending on whether binary event outcomes (scored by Brier score) or continuous probability distributions (scored by CRPS) are used as the primary metric.

**Question / Future Work:** Investigate the fundamental differences between Brier score and CRPS metrics in the context of LLM-based forecasting to determine if they capture distinct aspects of probabilistic reasoning versus uncertainty estimation. This is necessary to avoid incomplete or misleading evaluations in AI forecasting benchmarks.

**Why It Matters:** Understanding the divergence between these two common metrics is essential for interpreting forecasting benchmarks correctly.