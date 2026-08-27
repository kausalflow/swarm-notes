---
created_at: '2026-08-27T15:58:17Z'
source_papers:
- '[[openalex-2608.23456-mutual-information-entropy-plane-a-new-quantifier-space-for]]'
title: Robust Parameter Selection for Information Planes
---

**Background:** Statistical quantifiers derived from time series, such as permutation entropy and mutual information, rely on probability distributions affected by preprocessing choices like window size, embedding dimension, and time delay.

**Question / Future Work:** Investigate and establish robust parameter selection criteria or normalization methods to mitigate the sensitivity of the mutual information-entropy plane quantifiers to time series preprocessing choices such as window length, embedding dimension, and time delay.

**Why It Matters:** Sensitivity to hyperparameters hinders automated or cross-study comparison without strict manual homogeneity.

**Evidence:** The values of entropy and mutual information depend sensitively on the discretization method, the embedding, and the window size used... Therefore, quantitative comparison between different time series is only valid if all the parameters involved are homogeneous