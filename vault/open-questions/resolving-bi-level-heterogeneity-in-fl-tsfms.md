---
created_at: '2026-04-11T05:54:12Z'
source_papers:
- '[[openalex-2604.06727-bi-level-heterogeneous-learning-for-time-series-foundation-m]]'
title: Resolving Bi-level Heterogeneity in FL-TSFMs
---

**Background:** Federated learning often encounters performance degradation when applied to non-IID time series data due to significant temporal dynamics variation across domains.

**Question / Future Work:** Developing methods to effectively balance local domain specialization with global feature alignment under simultaneous inter-domain covariate shifts and intra-domain temporal concept drift remains a significant challenge for TSFM training.

**Why It Matters:** This is critical because existing FL methods for time series often ignore intra-domain variability or assume local homogeneity, leading to incoherent local embeddings and misaligned global models.

**Evidence:** The open question is how to design a FL paradigm that can simultaneously resolve bi-level heterogeneity