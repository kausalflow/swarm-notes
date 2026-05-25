---
created_at: '2026-05-25T08:50:01Z'
source_papers:
- '[[openalex-2506.01945-stock-market-telepathy-graph-neural-networks-predicting-the]]'
title: Predictive vs Causal Graphs in GNNs
---

**Background:** Graph neural networks (GNNs) are increasingly used to capture spatio-temporal dependencies in multivariate time series data for financial forecasting. While these models effectively learn interdependencies between nodes, the resulting graph structures are optimized for predictive loss and do not inherently represent underlying economic causal relationships.

**Question / Future Work:** There is an unresolved challenge in distinguishing between purely predictive correlations and true causal mechanisms within the graph structures learned by spatio-temporal GNNs. Determining whether the extracted connections represent actual economic influence or merely statistical artifacts remains a significant bottleneck for policy-making and strategic interpretation.

**Why It Matters:** Crucial for validating the reliability of deep learning models in high-stakes environments like economic policy and portfolio management, as predictive performance alone does not ensure the robustness required for structural decision-making.