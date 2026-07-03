---
created_at: '2026-07-03T07:55:02Z'
source_papers:
- '[[openalex-2606.31904-sequential-rc-tgan-generating-relational-time-series-with-sp]]'
title: Frequency Domain Relational Modeling
---

**Background:** Generative models for relational time series often struggle to capture long-range seasonality and cyclical structures, particularly when data contains categorical attributes that standard one-hot encoding fails to represent naturally.

**Question / Future Work:** Developing robust methods for integrating frequency-domain information into generative models for relational data is critical, specifically where categorical and continuous features exhibit intertwined temporal dynamics. Future work is needed to determine whether discretization methods like Gaussian Mixture Models (GMM) can be replaced by end-to-end differentiable alternatives that better preserve local variance while capturing global periodic patterns.

**Why It Matters:** Addressing these gaps is essential for scaling relational generative models to enterprise data, which often features complex, mixed-type, and non-stationary temporal relationships.