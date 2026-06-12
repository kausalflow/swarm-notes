---
created_at: '2026-06-12T08:54:23Z'
source_papers:
- '[[openalex-2606.10596-embedding-hybrid-systems-into-continuous-latent-vector-field]]'
title: Refining continuous latent embeddings
---

**Background:** Hybrid systems, which combine continuous-time dynamics with discrete state resets, often present discontinuities that are ill-posed for standard differentiable optimization techniques. Although it has been established that such systems can be embedded into higher-dimensional continuous latent manifolds, the general conditions for the existence of a continuous latent vector field on these embeddings remain a critical area of investigation.

**Question / Future Work:** The paper identifies a need to characterize the conditions and techniques for establishing continuous latent vector fields for hybrid systems beyond the provided existence proof. Specific challenges include exploring the boundary case m = 2n to eliminate discrete singular points and addressing the handling of piecewise smooth guard surfaces with potential degeneracies at corners.

**Why It Matters:** Establishing the robustness of the latent embedding across the full range of dimensions (including the critical m=2n case) and for more complex, piecewise-defined guard geometries is essential for the practical applicability of these models.

**Evidence:** To explore Theorem ˜6 when m = 2n, we need to eliminate these discrete points with additional techniques... In case that S is piecewise smooth, we need to discuss the transversality condition on the intersection of different pieces... we consider this an interesting future extension.