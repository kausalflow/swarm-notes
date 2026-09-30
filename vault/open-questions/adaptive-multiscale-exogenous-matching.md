---
created_at: '2026-09-30T10:48:55Z'
source_papers:
- '[[openalex-2609.34939-xmatch-enhancing-covariate-aware-time-series-forecasting-thr]]'
title: Adaptive Multi-Scale Exogenous Matching
---

**Background:** Covariate-aware time series forecasting models typically rely on a fixed exogenous variable order or a single temporal scale, which may not fully capture joint multi-variable interactions or adapt to varying forecasting horizons.

**Question / Future Work:** Investigate adaptive, query-dependent variable ordering and multi-scale prototype trees to better capture joint multi-variable contributions and diverse temporal patterns without relying on fixed information-gain rankings or single-scale patch lengths.

**Why It Matters:** Addressing the fixed variable ordering and single patch scale limitations can improve the generalization and robustness of tree-structured exogenous matching models across complex real-world multi-covariate datasets.

**Evidence:** Exploring tree construction based on conditional information gain, or dynamically adapting variable selection and matching order to each query, is a direction for future work... Developing a multi-scale ProtoTree or adaptively selecting patch lengths based on the data is another direction for future work.