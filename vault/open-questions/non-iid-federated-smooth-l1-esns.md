---
created_at: '2026-10-18T09:12:55Z'
source_papers:
- '[[openalex-2610.21742-sparse-federated-echo-state-networks-for-time-series-classif]]'
title: Non-IID Federated Optimization
---

**Background:** Federated learning systems frequently encounter non-identically distributed (non-IID) data across clients, which introduces client drift during optimization.

**Question / Future Work:** Analyze how continuation schedules and shared global shrinkage thresholds interact with client-heterogeneous sparsity patterns in federated Smooth-L1 regularized Echo State Networks, and integrate Newton-type federated aggregation methods designed for statistical heterogeneity.

**Why It Matters:** Overcoming non-IID data challenges is crucial for deploying federated reservoir computing frameworks in real-world decentralized IoT environments where data distributions vary across devices.

**Evidence:** Two risks are specific to our scheme: under client drift, the local Gauss-Newton Hessians describe curvature around different local optima, so their plain sum can bias the global Newton direction, and a single global shrinkage threshold could prune directions that only minority clients rely on.