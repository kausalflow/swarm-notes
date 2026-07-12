---
created_at: '2026-07-12T07:23:57Z'
source_papers:
- '[[openalex-2607.00154-evots-evolutionary-transformer-search-for-time-series-foreca]]'
title: Multi-stage architectural search expansion
---

**Background:** Time-series forecasting models are typically constrained by single-stage designs where tokenization is applied only at the input layer, limiting the hierarchical representation capacity of current Transformer architectures.

**Question / Future Work:** Future research should investigate the integration of multi-stage architectures that allow for intermediate retokenization within a model, enabling dynamic transitions between variable-wise, patch-based, and cross-variable token spaces.

**Why It Matters:** It addresses the structural rigidity of current time-series Transformers which often fail to exploit hierarchical multiscale temporal structures.

**Evidence:** Multistage architectures with intermediate retokenization are not included in the current search space and are left for future work.