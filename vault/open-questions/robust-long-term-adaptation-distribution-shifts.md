---
created_at: '2026-09-05T08:41:35Z'
source_papers:
- '[[openalex-2609.02093-compositional-spectral-prompts-for-llm-based-online-time-ser]]'
title: Robust Long-Term Adaptation under Distribution Shifts
---

**Background:** Existing online time series forecasting frameworks rely on memory buffers or associative retrieval, which suffer from capacity constraints, catastrophic forgetting during extended online phases, and poor generalization to previously unseen patterns or distribution shifts.

**Question / Future Work:** Develop advanced prompting or adaptation mechanisms that enable robust, long-term generalization to heavily evolving time-series patterns and complex distribution shifts without relying on capacity-constrained memory buffers or incurring high parameter-updating overhead during the online phase.

**Why It Matters:** Crucial for scaling online time series forecasting to highly non-stationary real-world environments where new, unprecedented regimes continually emerge.

**Evidence:** Despite the recent advancements, the buffer-based design of existing methods faces two fundamental challenges in practical OTSF scenarios. (1) Inadaptability to extended online phases... (2) Inadaptability to unseen patterns.