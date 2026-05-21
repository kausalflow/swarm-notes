---
created_at: '2026-05-21T08:30:22Z'
source_papers:
- '[[openalex-2605.18534-xctformer-leveraging-cross-channel-and-cross-time-dependenci]]'
title: Modeling Cross-Channel Time Dependencies
---

**Background:** Multivariate time-series analysis models are classified as either channel-independent (CI), which ignore inter-variable dependencies, or channel-dependent (CD), which explicitly model them. Current CD models often use indirect modeling strategies, which can overlook meaningful cross-channel and cross-time dependencies.

**Question / Future Work:** There is a need to identify the optimal strategy for modeling sequential cross-channel information to realize the potential of channel-dependent models in time-series analysis, particularly balancing explicit capture of dependencies without prohibitive computational costs.

**Why It Matters:** This addresses the paradoxical finding that simpler CI models often outperform more complex CD models in many forecasting benchmarks.

**Evidence:** recent findings show that channel-independent (CI) models, which assume no inter-variable dependencies, often outperform channel-dependent (CD) models that explicitly model such relationships.