---
created_at: '2026-11-04T12:39:53Z'
source_papers:
- '[[openalex-2611.02802-synforecast-controlled-synthetic-time-series-for-forecasting]]'
title: Corpus Size vs Mechanism Diversity
---

**Background:** Synthetic data generation methods vary widely in their assumptions, mechanism families, and coverage of complex temporal structures like daily cycles.

**Question / Future Work:** Investigate how varying corpus size while holding mechanism diversity fixed, and vice versa, affects forecasting pretraining performance to decouple whether synthetic priors are too small or have the wrong shape.

**Why It Matters:** Crucial for understanding the scaling laws and structural requirements of synthetic pretraining corpora in time series forecasting.

**Evidence:** Varying corpus size while holding mechanism diversity fixed, and vice versa, would separate two explanations our results leave confounded: that the prior is too small, or that it has the wrong shape.