---
created_at: '2026-05-02T06:56:13Z'
source_papers:
- '[[openalex-2604.26762-exploring-the-potential-of-probabilistic-transformer-for-tim]]'
title: Scaling Structural Prior Injection
---

**Background:** Structural priors, such as periodicity, trend, and lag, can be injected into the Spatio-Temporal Probabilistic Transformer (ST-PT) factor graph to mitigate data scarcity and improve noise robustness. However, the marginal contribution of these priors on real-world datasets remains inconsistent.

**Question / Future Work:** Further research is required to determine how to effectively combine multiple structural priors and scale their benefits to large-scale, real-world forecasting benchmarks. This includes resolving how to disentangle prior knowledge contributions from data-driven representation learning and defining a robust, model-agnostic injection interface.

**Why It Matters:** This is a fundamental bottleneck for bridging symbolic domain knowledge with deep learning for time-series forecasting, especially in data-scarce settings.

**Evidence:** The overall gain from prior modelling on real data is currently not pronounced... A fuller scoping of RQ1 would therefore need to combine multiple priors and to control each of these factors more carefully than the present study does.