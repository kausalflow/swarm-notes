---
created_at: '2026-09-26T09:37:17Z'
source_papers:
- '[[openalex-2609.27531-semiparametric-inference-for-dynamic-causal-effects-from-obs]]'
title: Nuisance Rate Transfer for Temporal Learners
---

**Background:** Estimating dynamic causal effects from observational time series via local projection instrumental variable methods requires nuisance estimators to satisfy specific rates, but bridging general time-series prediction guarantees to these required nuisance error rates under block cross-fitting and temporal dependence remains non-trivial.

**Question / Future Work:** The paper highlights that while rate transfer theorems can link population prediction rates to empirical rates on buffered validation blocks under temporal dependence, verifying such conditions for various off-the-shelf temporal machine learning learners (such as complex deep neural networks or advanced kernel methods) in high-dimensional time-series settings remains an open area for future investigation.

**Why It Matters:** Establishing rigorous data-driven learner verification bridges theoretical double/debiased machine learning and practical time-series forecasting models, guiding how complex nonparametric models can be safely deployed in causal dynamic settings.

**Evidence:** There is no existing result tailored to the block cross-fitting scheme in Algorithm 1 on how to verify such rates for an off-the-shelf temporal learner, and Theorem 3 provides a general recipe; see Section 5.