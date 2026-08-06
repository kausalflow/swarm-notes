---
created_at: '2026-08-06T07:32:32Z'
source_papers:
- '[[openalex-2505.23535-robust-estimation-of-double-autoregressive-models-via-normal]]'
title: Optimal Component Selection in DAR Models
---

**Background:** The double autoregressive (DAR) model is frequently estimated using Gaussian quasi-maximum likelihood estimation (QMLE), which suffers from a loss of statistical efficiency when the true innovation distribution deviates significantly from normality. While normal mixture quasi-maximum likelihood estimation (NM-QMLE) effectively captures heavy tails and skewness, selecting the appropriate number of mixture components remains a challenging problem without universally established theoretical guidance for time series models.

**Question / Future Work:** The authors discuss the challenges in determining the optimal number of mixture components K in normal mixture QMLE for DAR models, noting that while information criteria like BIC and ICL are widely used, establishing formal order selection consistency and deriving the exact asymptotic distribution of order estimators in conditionally heteroskedastic time series frameworks remain open theoretical avenues. Further research is needed to develop fully data-driven, theoretically guaranteed procedures for component selection in mixture-based time series models.

**Why It Matters:** Determining the correct number of mixture components in time series mixture models directly impacts estimation consistency, finite-sample performance, and computational tractability.

**Evidence:** A critical contribution of this paper is addressing the often-overlooked challenge of selecting the appropriate number of mixture components, K, a key parameter that significantly impacts model performance.