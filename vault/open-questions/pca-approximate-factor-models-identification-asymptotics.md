---
created_at: '2026-09-30T10:48:06Z'
source_papers:
- '[[openalex-2211.01921-principal-component-analysis-for-highdimensional-approximate]]'
title: PCA for Approximate Factor Models
---

**Background:** Principal Component Analysis (PCA) is widely used to estimate high-dimensional approximate factor models in time series, yet its asymptotic properties, identification restrictions, and the precise relation between equivalent estimation formulations remain heavily studied.

**Question / Future Work:** Provide a comprehensive clarification and unification of alternative PCA formulations (such as approaches A1, B1, A2, and B2) and their precise finite-sample and asymptotic relationships, addressing how different identifying constraints (e.g., orthonormal factors versus orthonormal loadings) impact the rates of convergence and the validity of downstream statistical inference and central limit theorems.

**Why It Matters:** Clarifying the precise equivalence and asymptotic behavior across various PCA formulations and identifying restrictions is crucial for valid hypothesis testing, confidence interval construction, and inference in high-dimensional factor models.

**Evidence:** The approximate factor model is then characterized by an eigengap in the population covariance matrix that widens as n -> infinity. Conversely, if the population covariance exhibits a widening eigengap as n -> infinity, the data can be said to follow an approximate factor model...