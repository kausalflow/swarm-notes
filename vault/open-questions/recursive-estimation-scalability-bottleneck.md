---
created_at: '2026-06-25T08:19:39Z'
source_papers:
- '[[openalex-2606.23326-online-forecast-reconciliation-using-linear-models]]'
title: Recursive estimation scalability bottleneck
---

**Background:** In online recursive estimation, computational complexity arises when design and weight matrices grow with each new time observation. The matrices currently used for residuals in recursive linear models eventually reach a size that renders numerical updates infeasible for long-term online operation.

**Question / Future Work:** There is a need to develop recursive estimation methods that handle high-dimensional or long-term streaming data without requiring the storage and manipulation of matrices that grow linearly with the number of time steps. Research should investigate sparse or banded structures that can discard long-term correlations in residuals or parameter estimates to maintain computational efficiency in persistent online forecasting environments.

**Why It Matters:** This is a fundamental bottleneck for deploying adaptive, online linear forecasting models in real-world streaming data applications where the model must operate continuously.

**Evidence:** As new observations become available, the matrices increase in size, so that numerics eventually become infeasible. It may be useful to consider banded or sparse structures that discard long-term correlations in the residuals.