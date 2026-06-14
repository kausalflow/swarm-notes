---
created_at: '2026-06-14T08:37:18Z'
source_papers:
- '[[openalex-2606.13624-beyond-uniform-tokens-adaptive-compression-for-time-series-l]]'
title: Adaptive Asymmetric Token Compression
---

**Background:** Time series data and textual prompt data exhibit fundamentally different information structures, yet they are often processed using uniform token mechanisms in Large Language Models (LLMs).

**Question / Future Work:** A key unresolved question is how to optimize the computational efficiency of LLM-based time series analysis by simultaneously exploiting the frequency-domain spectral redundancy of time series and the layer-wise decay of prompt token influence. Future work is needed to determine the optimal adaptive merging granularity for spectral components and the ideal prompt compression schedules across diverse model architectures.

**Why It Matters:** This question addresses the fundamental efficiency bottleneck in cross-modal foundation models, particularly in balancing redundant numerical data with contextual linguistic prompts for resource-constrained inference.