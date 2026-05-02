---
created_at: '2026-05-02T06:57:05Z'
source_papers:
- '[[openalex-2604.26535-arma-approximation-of-a-non-separable-spatio-temporal-model]]'
title: Spatial resolution sensitivity analysis
---

**Background:** The proposed approach for discretizing non-separable spatio-temporal models exhibits performance sensitivity to spatial grid density, with parameter inference stability appearing linked to resolution.

**Question / Future Work:** The mechanism driving the performance degradation—specifically the tendency for parameter inference to drift toward extreme values in the temporal range as the spatial basis count increases—remains poorly understood. Future work is needed to determine the conditions for robustness and whether this behavior stems from numerical instability, overfitting, or misspecification.

**Why It Matters:** This is a critical stability issue for the practical application of spatiotemporal models in high-resolution settings, potentially limiting their reliability in climate and environmental forecasting.

**Evidence:** The source of this effect is not clear and further study is needed in future work. ... We conjecture that this effect is caused, at least to some degree, by misspecification in the spatial model.