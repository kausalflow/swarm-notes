---
created_at: '2026-05-23T07:25:41Z'
source_papers:
- '[[openalex-2605.21437-neural-negative-binomial-regression-for-weekly-seismicity-fo]]'
title: Modeling cross-cell spatial dependencies
---

**Background:** Count-based forecasting models often rely on marginal predictive factorizations where grid cells are assumed conditionally independent.

**Question / Future Work:** Investigate the limitations of marginal predictive factorization in seismicity forecasting and develop architectures (e.g., graph neural networks or spatial convolutions) capable of modeling explicit cross-cell spatial dependencies, such as stress transfer and seismic triggering, rather than relying on independent per-cell predictions.

**Why It Matters:** Models ignoring cross-cell interactions miss the core physical mechanism of earthquake triggering, which is essential for advancing beyond marginal predictors to full joint generative spatiotemporal models.

**Evidence:** The factorization below is a marginal predictive factorization, not a full generative model of the joint spatiotemporal field. Extension to an ETAS-like spatial convolution is left for future work.