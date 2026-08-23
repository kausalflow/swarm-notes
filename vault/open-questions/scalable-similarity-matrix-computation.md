---
created_at: '2026-08-23T05:18:55Z'
source_papers:
- '[[openalex-2608.20025-clast-context-aware-contrastive-vae-for-probabilistic-time-s]]'
title: Scalable Similarity Matrix Computation
---

**Background:** Probabilistic multivariate time series forecasting models leverage latent-variable representations, but conventional training objectives often struggle with computational scaling and expressive power for high-dimensional sequences.

**Question / Future Work:** Investigate scaling and mitigating the computational complexity of full similarity-matrix construction, which currently exhibits quadratic scaling with respect to the sequence length.

**Why It Matters:** Quadratic complexity limits applicability to extremely long input sequences or very high-dimensional time series, making scalable similarity estimation an important direction for future research.

**Evidence:** The contextual similarity alignment loss incurs $\mathcal{O}(N^{2})$ complexity due to full similarity-matrix construction.