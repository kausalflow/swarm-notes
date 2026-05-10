---
created_at: '2026-05-10T07:21:08Z'
source_papers:
- '[[openalex-2605.05725-detecting-time-series-anomalies-like-an-expert-a-multi-agent]]'
title: Multivariate Time Series Extension
---

**Background:** Most current LLM-based time series anomaly detection methodologies focus on univariate signals, whereas many real-world monitoring tasks involve complex inter-sensor dependencies.

**Question / Future Work:** The current multi-agent LLM framework is designed specifically for univariate time series anomaly diagnosis. Extending this framework to handle multivariate time series, where inter-sensor dependencies and complex joint anomaly patterns must be modeled, remains a significant unresolved challenge.

**Why It Matters:** Real-world systems are typically multivariate, and anomalies often emerge from relationships across sensors rather than just individual signal deviations.

**Evidence:** We focus on univariate TSAD as a first step toward structured and interpretable anomaly diagnosis, leaving multivariate extensions for future work.