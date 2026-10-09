---
created_at: '2026-10-09T11:33:42Z'
source_papers:
- '[[openalex-2610.07834-retrieval-is-not-enough-refreshing-memory-for-frozen-time-se]]'
title: Query-Level Reference Trust in Forecasting
---

**Background:** Retrieval-augmented time-series forecasting frameworks typically construct their retrieval memory once from the training segment, leaving observations revealed after deployment unavailable and failing to calibrate retrieval influence on frozen forecasters.

**Question / Future Work:** Deciding query by query whether a retrieved historical reference can be trusted by a frozen forecaster remains an open problem, particularly when determining how to robustly handle shifts between validation and deployment or when mitigating the risk of the retrieval correction harming the base forecaster's accuracy.

**Why It Matters:** Understanding how to reliably evaluate and trust historical references query-by-query is fundamental to advancing retrieval-augmented forecasting without risking performance degradation.

**Evidence:** For a frozen forecaster, what retrieval can offer is the new observations it has never seen and the patterns it has not yet captured; deciding query by query whether a reference can be trusted remains an open problem.