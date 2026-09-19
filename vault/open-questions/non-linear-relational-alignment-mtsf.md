---
created_at: '2026-09-19T09:02:55Z'
source_papers:
- '[[openalex-2609.19670-core-coherence-and-relational-alignment-for-multivariate-tim]]'
title: Non-linear Relational Graph Alignment
---

**Background:** Multivariate time-series forecasting relies heavily on linear PCA-based subspaces to capture cross-variable relational alignment during training supervision.

**Question / Future Work:** Investigate extending the relational alignment term beyond a linear low-rank subspace (such as standard PCA) to capture more complex, non-linear cross-variable dependencies in multivariate time-series forecasting.

**Why It Matters:** Linear low-rank projections may fail to capture highly non-linear interactions among variables in complex real-world multivariate systems, making non-linear extensions crucial for improving relational graph losses.

**Evidence:** Extending the relational term beyond a linear low-rank basis is a natural next step.