---
created_at: '2026-05-21T08:25:53Z'
source_papers:
- '[[openalex-2404.08472-tslanet-rethinking-transformers-for-time-series-representati]]'
title: CNN Long-Horizon Scaling Limitations
---

**Background:** Convolutional Neural Networks (CNNs) are effective at capturing local dependencies in time series data but often face limitations when modeling long-range temporal correlations compared to self-attention architectures.

**Question / Future Work:** Developing architectural strategies that allow efficient convolutional models to maintain local feature extraction capabilities while robustly scaling to diverse long-term dependency horizons remains a fundamental challenge. Current models often show performance degradation when applying fixed receptive field architectures to time series data with varying temporal sampling rates and spectral characteristics.

**Why It Matters:** Bridging the gap between the computational efficiency of CNNs and the global modeling capability of Transformers is critical for developing universal, lightweight forecasting frameworks.