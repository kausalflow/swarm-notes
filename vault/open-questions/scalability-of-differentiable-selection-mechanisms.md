---
created_at: '2026-07-04T07:37:39Z'
source_papers:
- '[[openalex-2607.00581-decision-focused-sparse-tangent-portfolio-optimization]]'
title: Scalability of Differentiable Selection
---

**Background:** Decision-focused learning relies on differentiating through optimization solvers, which often incurs significant computational costs as problem dimensions increase.

**Question / Future Work:** Designing more efficient, scalable differentiable operators for sparse selection and downstream convex optimization is essential to support the transition from small asset universes to the large-scale portfolios typical of real-world financial markets.

**Why It Matters:** Computational efficiency is a primary bottleneck for scaling end-to-end learning frameworks to high-dimensional financial datasets.

**Evidence:** differentiating through the sparse selection module, especially the soft top-k operator, introduces computational overhead as the asset universe or the sparsity budget grows.