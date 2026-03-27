---
created_at: '2026-03-27T14:08:58Z'
source_papers:
- '[[openalex-2603.15452-unlocking-the-value-of-text-event-driven-reasoning-and-multi]]'
title: ETA Alternative Decomposition Strategies
---

**Background:** The model integrates representations via Endogenous Text Alignment (ETA) which decomposes the time series into trend and seasonal components before applying contrastive learning with corresponding text embeddings.

**Question / Future Work:** Future work could explore if the explicit decomposition into trend and seasonality within Endogenous Text Alignment (ETA) is the optimal way to align textual and temporal features, or if alternative decomposition strategies (e.g., periodic/non-periodic, or using feature representations learned directly by the LLM without explicit spectral decomposition) might offer richer alignment for certain time series characteristics.