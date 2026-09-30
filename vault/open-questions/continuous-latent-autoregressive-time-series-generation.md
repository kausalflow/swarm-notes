---
created_at: '2026-09-30T10:50:26Z'
source_papers:
- '[[openalex-2609.34511-halo-enhancing-time-series-generation-via-hyperspherical-lat]]'
title: Continuous Latent Time Series Generation
---

**Background:** Most time series generative models follow a two-stage paradigm combining discrete tokenization with autoregressive next-token prediction, which introduces quantization information loss and sequential error accumulation.

**Question / Future Work:** Investigate and develop generative frameworks that operate fully in continuous latent spaces while avoiding the trade-offs between parallel decoding efficiency and rigorous temporal correlation modeling.

**Why It Matters:** Overcoming the limitations of discrete codebooks versus continuous latent representations is crucial for improving fine-grained temporal fidelity and generation stability in time series foundation models.

**Evidence:** To address these key limitations, we aim to perform generative modeling in a continuous latent space with a more efficient autoregressive framework, thereby mitigating information loss and improving generation stability and efficiency.