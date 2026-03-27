---
created_at: '2026-03-27T15:43:26Z'
source_papers:
- '[[openalex-2603.22719-a-frequency-domain-approach-for-integrating-multiple-functio]]'
title: Resolving Eigenfunction Non-Uniqueness
---

**Background:** The eigenfunctions used to represent the underlying stochastic process in spectral decompositions are not uniquely determined, but are unique only up to multiplication by a phase factor from the set $\\mathcal{M}$, which consists of functions on the complex unit circle with specific symmetry.

**Question / Future Work:** The non-uniqueness of the eigenfunctions $\\psi_k(\\cdot|\\omega)$ (up to a phase multiplier $\\nu_k(\\omega) \\in \\mathcal{M}$) can lead to redundant representations and potential degradation in forecasting accuracy for Multivariate Functional Time Series (MFTS) analysis. A method to select the unique optimal multiplier $\\tilde{\\nu}_k(\\cdot)$ is needed to ensure stable and optimal representation.

**Why It Matters:** Resolving non-uniqueness in basis representation is crucial for achieving stable and theoretically optimal dimension reduction methods in functional data analysis, directly impacting the reliability of downstream tasks like forecasting.

**Evidence:** This non-uniqueness issue may lead to redundant representations and degrade forecasting accuracy Guo et al., (2024). To avoid this issue, we extend the optimal functional filter criterion in (Guo et al., 2024) to the MFTS setting.