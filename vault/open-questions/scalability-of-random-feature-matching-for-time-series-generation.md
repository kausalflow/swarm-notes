---
created_at: '2026-06-06T07:39:44Z'
source_papers:
- '[[openalex-2606.05138-generating-financial-time-series-by-matching-random-convolut]]'
title: Scalability of Random Feature Matching
---

**Background:** Financial time series generation frequently relies on models trained on a single historical path, which presents risks of overfitting and requires effective techniques to learn the underlying dynamics from scarce data.

**Question / Future Work:** The scalability of random convolutional feature-matching generative models remains unclear, specifically whether this approach remains competitive compared to learned discriminators or diffusion models when data availability is high and the sample size is not limited to a single historical path.

**Why It Matters:** Understanding the performance limits of non-adversarial feature matching compared to learned discriminators is crucial for the adoption of these methods in broader financial time series generation tasks.