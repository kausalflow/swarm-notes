---
created_at: '2026-10-04T10:48:18Z'
source_papers:
- '[[openalex-2610.02058-foundations-without-fundamentals-zero-shot-blind-spots-in-ti]]'
title: Inductive Biases for Leading Indicators
---

**Background:** Time series foundation models frequently struggle to effectively leverage exogenous leading indicators and past covariate signals, often defaulting to univariate patterns despite available predictive information.

**Question / Future Work:** Investigate whether current time series foundation model architectures fundamentally lack the necessary inductive biases to exploit exogenous leading indicators, or if this behavior is merely an artifact of pre-training data distributions and optimization objectives. Addressing this requires developing advanced synthetic data generation strategies with explicit lead-lag relationships and evaluating architectural modifications to better internalize multivariate dependencies.

**Why It Matters:** Understanding whether covariate underutilization stems from architectural bottlenecks or training limitations is critical for building general-purpose multivariate forecasting models that can reliably incorporate exogenous signals in high-stakes domains.

**Evidence:** While TSFMs demonstrate impressive zero-shot capabilities in many settings, our analysis reveals clear failure modes that warrant caution for industry practitioners in high-stakes environments. These findings suggest that current pre-training regimes might lack the necessary inductive biases to leverage exogenous leading indicators, often defaulting to univariate overreliance despite available predictive signals.