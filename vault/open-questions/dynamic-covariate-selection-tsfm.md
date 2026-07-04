---
created_at: '2026-07-04T07:36:08Z'
source_papers:
- '[[openalex-2607.01204-tirex-2-generalizing-tirex-to-multivariate-data-and-streamin]]'
title: Dynamic Covariate Selection in TSFMs
---

**Background:** Time series foundation models often struggle to balance the integration of external multivariate information with the need for computational efficiency during streaming inference.

**Question / Future Work:** Future research is needed to develop dynamic covariate selection mechanisms that adaptively prune irrelevant input variates during inference based on in-context estimates of covariate-target correlation, reducing computational cost at inference time.

**Why It Matters:** Efficiently handling high-dimensional covariate sets without increasing inference latency is a significant bottleneck for scaling time series foundation models.