---
created_at: '2026-06-05T08:37:48Z'
source_papers:
- '[[openalex-2606.03828-network-time-series-models-for-multivariate-volatility-forec]]'
title: Dynamic Network Structure Selection
---

**Background:** Volatility forecasting models often rely on realized measures computed from high-frequency data, but their performance can be sensitive to the selection of graphical structures representing cross-asset spillover effects.

**Question / Future Work:** It remains unclear how to optimally define and adapt the underlying graphical structures (e.g., Granger-causal vs. connectedness-based networks) as financial regimes shift, particularly regarding the trade-off between network density, spillover interpretability, and the forecasting robustness of the resulting models. There is currently no consensus on an automated or data-driven mechanism to dynamically select the most appropriate network structure in real-time.

**Why It Matters:** Automated or adaptive network selection is critical for practical financial applications where manually choosing a graph for each rolling window is computationally expensive and prone to bias, limiting scalability and reliability.

**Evidence:** While the most suitable network order for predicting the RV depends naturally on the network used, we can still observe some interesting patterns across the networks.