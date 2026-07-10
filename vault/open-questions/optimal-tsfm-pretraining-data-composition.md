---
created_at: '2026-07-10T08:14:58Z'
source_papers:
- '[[openalex-2607.06504-rmisc-a-large-scale-real-world-multivariate-corpus-for-time]]'
title: Optimal TSFM Pretraining Composition
---

**Background:** Time series foundation models have historically been pretrained using large-scale synthetic datasets due to their scalability. However, it remains unclear whether and to what extent real-world multivariate data provides superior generalization capabilities for these models compared to synthetic alternatives.

**Question / Future Work:** Research is required to quantify the optimal data composition strategies for training multivariate time series foundation models, specifically comparing the relative contributions of real-world univariate, synthetic multivariate, and real-world multivariate data to maximize zero-shot generalization.

**Why It Matters:** Identifying the ideal balance of synthetic and real-world data is essential for the efficient scaling and performance optimization of foundation models, especially given data privacy and cross-domain imbalance constraints.

**Evidence:** This raises a key question: Whether and to what extent do the leading TSFMs trained with the real-world corpus perform better than those trained with synthetic data?