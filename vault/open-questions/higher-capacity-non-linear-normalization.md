---
created_at: '2026-05-14T07:36:49Z'
source_papers:
- '[[openalex-2605.10823-norin-backbone-adaptive-reversible-normalization-for-time-se]]'
title: Higher-capacity non-linear normalization families
---

**Background:** Time-series forecasting often utilizes reversible normalization techniques to handle non-stationary data, but these methods traditionally rely on affine transformations that cannot reshape complex, heavy-tailed, or skewed probability distributions. While non-linear transformations offer the potential to address these shortcomings, they face a degeneration problem where end-to-end gradient-based training causes the model to collapse back to linear regimes.

**Question / Future Work:** Future research should investigate if higher-capacity, non-linear shape families—such as full four-parameter Johnson distributions or advanced normalizing flows—can provide superior performance for highly complex data, such as intraday financial series. This includes developing frameworks that can effectively navigate the search complexity of these higher-dimensional normalization parameter spaces without falling into the degeneration trap.

**Why It Matters:** Determining the limits of current parameterization and whether increased model capacity is necessary for complex temporal dynamics is crucial for advancing time-series normalization techniques.