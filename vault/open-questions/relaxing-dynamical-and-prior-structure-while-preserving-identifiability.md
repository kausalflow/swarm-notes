---
created_at: '2026-03-27T15:43:34Z'
source_papers:
- '[[openalex-2603.22886-conditionally-identifiable-latent-representation-for-multiva]]'
title: Relax structural constraints while preserving identifiability
---

**Background:** Learning latent representations from multivariate time series often suffers from non-identifiability due to rotational or reparameterization ambiguities, which hinders causal interpretation.

**Question / Future Work:** Investigate methods to relax the structural constraints on the dynamics (e.g., moving beyond linear, diagonal dynamics) or the innovation prior distribution (e.g., moving beyond conditional exponential families) while successfully maintaining the guarantees of identifiability up to permutation and component-wise affine transformations.

**Why It Matters:** Relaxing structural constraints while preserving identifiability is key to achieving better predictive performance on complex, real-world time series without sacrificing the interpretability benefits of the factor representation.

**Evidence:** Further research may explore other conditional contexts (e.g., learned or task-specific embeddings), relax the dynamical or prior structure while preserving identifiability, and extend the approach to other modalities such as language or image sequences.