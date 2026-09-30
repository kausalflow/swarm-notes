---
created_at: '2026-09-30T10:49:08Z'
source_papers:
- '[[openalex-2609.34842-qiyao-m-multimodal-time-series-foundation-model-with-role-aw]]'
title: Asymmetric Modeling of Multimodal Time Series
---

**Background:** Existing multimodal time series foundation models adopt a role-agnostic approach by applying shared modeling mechanisms to heterogeneous modalities, ignoring the distinct forecasting characteristics and asymmetries between endogenous and exogenous data.

**Question / Future Work:** Investigate the development of fully unified or role-adaptive architectures that can dynamically reconcile or jointly optimize the asymmetric contributions of endogenous and exogenous modalities without relying on disjoint prediction pathways or proxy pretraining strategies.

**Why It Matters:** Crucial for building truly generalized multimodal foundation models that do not require specialized, decoupled pathways for internal versus external signals.

**Evidence:** Existing multimodal TSFMs incorporate both endogenous and exogenous modalities through largely shared multimodal mechanisms... overlooking a fundamental asymmetry in how endogenous and exogenous modalities relate to forecasting.