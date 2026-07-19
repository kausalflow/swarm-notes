---
created_at: '2026-07-19T07:24:55Z'
source_papers:
- '[[openalex-2607.14886-reachability-aware-pretraining-for-efficient-target-oriented]]'
title: Scalability of Reachability Labeling
---

**Background:** Reachability-aware pretraining introduces a preprocessing overhead to identify reachable nodes, which often involves exhaustive search or costly label generation in large graphs.

**Question / Future Work:** Investigating methods to compute or approximate reachability information efficiently, potentially through learned surrogates or graph sketching, to overcome the scalability limits of current labeling procedures on massive temporal knowledge graphs.

**Why It Matters:** As graphs scale, the preprocessing burden threatens the practical utility of reachability-based training methods, necessitating more efficient labeling alternatives.