---
created_at: '2026-04-20T07:10:03Z'
source_papers:
- '[[openalex-2409.04090-estimation-of-service-value-parameters-for-a-queue-with-unob]]'
title: Extensions for Unobserved Balking Models
---

**Background:** Queueing systems with heterogeneous customers often exhibit unobserved balking behavior, making it difficult to estimate customer service valuation parameters and optimize admission prices. Existing literature on this topic generally requires strong assumptions or is limited to simple model variants.

**Question / Future Work:** Addressing the estimation of service value and waiting-cost parameters in systems where both are heterogeneous or follow unknown joint distributions remains an open challenge. Furthermore, extending the current parametric estimation framework to more complex non-parametric approaches or broader queueing models (e.g., M/M/s) requires further development.

**Why It Matters:** These directions are critical for moving beyond current restrictive model assumptions, allowing for more realistic and robust applications of statistical inference and revenue management in service systems.

**Evidence:** Another possibility is to relax another assumption of Naor’s model—the homogeneity of customers’ patience (C). A similar approach can be used to construct an MLE for a common joint distribution of R and C. . . The estimation procedure presented here can be taken a step further to a non-parametric approach where for each queue length qi a different state dependent arrival rate λi is estimated.