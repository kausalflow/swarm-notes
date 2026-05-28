---
created_at: '2026-05-28T08:38:17Z'
source_papers:
- '[[openalex-2605.25359-a-quasi-maximum-likelihood-estimation-method-for-bergomi-typ]]'
title: Instability of Joint Estimation in Bergomi Models
---

**Background:** Bergomi-type volatility models describe the dynamics of the forward variance curve using a kernel function that determines how shocks propagate across maturities. Statistical estimation of this kernel parameter from time-series option prices is complicated by the infinite-dimensional nature of the state process and the rank-degenerate structure of the observations.

**Question / Future Work:** The joint estimation of scale and shape parameters (e.g., in a shifted power-law kernel) remains empirically unstable, exhibiting sensitivity to the choice of the proxy distribution's regularization parameter. Further research is required to determine whether this instability is an inherent feature of identifying scale versus memory (shape) parameters from cumulative forward variance data or if more robust estimation procedures or alternative model parameterizations can decouple these effects.

**Why It Matters:** The joint estimation of memory parameters and volatility scale is critical for characterizing market dynamics correctly; persistent instability here suggests potential model misspecification or inherent identification issues that impact the reliability of risk pricing and volatility surface modeling.