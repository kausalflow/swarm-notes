---
created_at: '2026-08-27T15:58:00Z'
source_papers:
- '[[openalex-2608.23221-which-histories-matter-for-time-series-forecasting-learning]]'
title: Alternative and Jointly Learned Candidate Generators
---

**Background:** Historical retrieval methods for time-series forecasting traditionally treat past similarity as a proxy for utility, but similarity is only an imperfect proxy for final predictive relevance under nonstationarity and regime shifts.

**Question / Future Work:** Investigate and develop alternative or jointly learned candidate generators that can recover relevant historical examples falling outside the initial similarity-based candidate pool (such as the Pattern Top-M pool), given that current rerankers are strictly bounded by the coarse candidate generation step.

**Why It Matters:** Crucial for overcoming the performance bottleneck where rerankers are constrained by initial retrieval pools, enabling more robust end-to-end historical retrieval architectures.