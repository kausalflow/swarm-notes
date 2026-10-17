---
created_at: '2026-10-17T08:54:57Z'
source_papers:
- '[[openalex-2610.20243-retrieval-over-training-similarity-search-based-model-select]]'
title: Handling Neighbor Disagreement in Selection
---

**Background:** Retrieval-based time-series anomaly detector selection frameworks transfer model performance profiles from retrieved nearest-neighbor instances in a knowledge base.

**Question / Future Work:** Investigate whether averaging detector-performance profiles from retrieved neighbors remains robust when the retrieved neighbors disagree significantly in their individual best detector recommendations.

**Why It Matters:** Understanding the robustness boundaries of profile aggregation under neighbor disagreement is theoretically critical for improving non-parametric model selection reliability.

**Evidence:** We also observe (in preliminary experiments) that even when neighbours disagree, the averaged profile in RAMSAD still picks the right detector; we defer a detailed study to future work.