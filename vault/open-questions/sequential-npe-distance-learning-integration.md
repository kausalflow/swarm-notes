---
created_at: '2026-06-25T08:19:45Z'
source_papers:
- '[[openalex-2606.22981-learning-the-distance-for-abc-and-localized-neural-posterior]]'
title: Distance learning in sequential NPE
---

**Background:** Sequential neural posterior estimation (NPE) improves simulation efficiency by adaptively focusing simulation budgets on regions of high posterior support.

**Question / Future Work:** Integrating adaptive distance learning into sequential NPE frameworks remains an open challenge, particularly when reconciling weight optimization with adaptive prior truncation under model misspecification.

**Why It Matters:** Sequential methods are crucial for scaling likelihood-free inference; solving this integration would enable robust, computationally efficient Bayesian forecasting for complex misspecified models.

**Evidence:** We do not consider the sequential approach here, since it is not obvious how to combine this with distance learning under misspecification, but this is an interesting future research direction.