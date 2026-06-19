---
created_at: '2026-06-19T09:24:27Z'
source_papers:
- '[[openalex-2606.17435-morphstrata-layer-specific-perturbations-for-generating-morp]]'
title: Temporal-Structure-Aware MTD Scaling
---

**Background:** Moving target defense (MTD) in time-series forecasting involves generating heterogeneous model instances to degrade the effectiveness of adversarial attacks. The efficacy of these ensembles often depends on the specific temporal structure of the underlying dataset, such as its spectral entropy and autocorrelation decay.

**Question / Future Work:** There is a need to systematically investigate how perturbation scaling—adjusting the noise injection strategy based on the specific temporal characteristics (e.g., spectral entropy, memory decay) of the dataset—can optimize the robustness-cost trade-off. This involves moving beyond static layer-specific masking to dynamic mechanisms that adapt to the signal's periodicity and volatility.

**Why It Matters:** The effectiveness of MTD is highly dataset-dependent and tied to temporal properties; finding a systematic way to adapt to these properties is the logical next step for robust defense design.