---
created_at: '2026-07-03T07:54:48Z'
source_papers:
- '[[openalex-2410.00574-asymmetric-garch-modelling-without-moment-conditions]]'
title: Skewed stable GARCH modeling
---

**Background:** Financial time series often exhibit asymmetry and leverage effects, which can be modeled either through the conditional variance equation or by assuming skewed innovation distributions.

**Question / Future Work:** Extending asymmetric GARCH models to accommodate skewness in the underlying innovations (e.g., skew-stable distributions) poses significant theoretical and computational challenges. Specific issues include the lack of closed-form densities for skew-stable laws, numerical instability near boundary values of parameters like skewness, and the difficulty of ensuring parameter identifiability.

**Why It Matters:** Adding skewness to innovations could potentially better capture stylized financial features, but current estimation frameworks are limited by the computational complexity and non-identifiability concerns.

**Evidence:** Theoretically, extending to skew-stable GARCH(1,1) setting mainly requires: (i) the asymptotic behavior of partial derivatives of log f_{α,β} involving β, and (ii) the identifiability of the skewness parameter β. We leave this extension to future work.