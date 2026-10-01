---
created_at: '2026-10-01T11:14:54Z'
source_papers:
- '[[openalex-2609.37715-volatility-clustering-adaptation-for-financial-time-series]]'
title: Scaling Volatility-Clustering Adaptation
---

**Background:** Financial time-series foundation models are adapted to target markets using objectives that often fail to capture domain-specific temporal structures like volatility clustering.

**Question / Future Work:** Investigate how to scale and stabilize volatility-clustering adaptation objectives (such as the ACF2 loss) across diverse financial asset classes and different foundation model architectures without inducing severe volatility inflation or optimization instability.

**Why It Matters:** Understanding the scalability and cross-architecture robustness of domain-specific path-level losses is critical for reliable financial forecasting and bridging general-purpose time-series foundation models with domain-informed learning.

**Evidence:** First, VCA’s advantage appears conditional on a well-pre-trained backbone... Second, although VCA is strongest on average, its gains are not consistent across benchmarks, and the scaling trend remains unclear, leaving room for future work.