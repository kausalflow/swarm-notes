---
created_at: '2026-08-08T05:34:56Z'
source_papers:
- '[[openalex-2608.04593-rethinking-reservoir-pruning-a-dynamical-perspective-for-ech]]'
title: Scalable Dynamic Reservoir Pruning
---

**Background:** Echo State Networks (ESNs) often suffer from over-parameterization and redundancy in their randomly initialized reservoirs, which can be mitigated via pruning. Existing pruning methods rely on static connectivity or activation statistics, overlooking how neurons contribute to input-driven temporal state transitions.

**Question / Future Work:** Investigate and develop scalable dynamical model reduction and online pruning techniques for Echo State Networks that avoid the heavy offline computational costs associated with dense Jacobian-Gramian construction and eigendecomposition.

**Why It Matters:** The cubic computational complexity with respect to reservoir size poses a significant bottleneck for scaling dynamical pruning methods to very large recurrent neural networks.

**Evidence:** A direct dense implementation of Algorithm 1 requires $\\mathcal{O}(TN^{3})$ time to form $J(t)^{\\top}J(t)$ across $T$ time steps, plus $\\mathcal{O}(N^{3})$ time for the eigendecomposition of the resulting Gramian... making the method less suitable for online pruning without approximation.