---
created_at: '2026-06-11T09:06:46Z'
source_papers:
- '[[openalex-2606.08896-fame-forecastability-aware-mixture-of-experts-for-heterogene]]'
title: Automated Forecastability-Aware Expert Routing
---

**Background:** In large-scale industrial forecasting systems, the performance of models is sensitive to the data's inherent properties, such as sparsity, volatility, and lifecycle stage. Current approaches often rely on manual, rule-based expert selection or global model training, which fail to adapt optimally to the diverse and evolving regimes within such systems.

**Question / Future Work:** It remains an open challenge to develop automated, scalable methods that can learn to map arbitrary time series to appropriate forecasting experts in a way that is simultaneously accurate, cost-effective for large-scale production, and interpretable. Future work is needed to refine the router's robustness against noisy oracle-suitability labels, improve its stability across unseen or shifting data regimes, and optimize the trade-off between the inference cost of executing specialized experts and overall forecasting accuracy.

**Why It Matters:** The development of robust, cost-aware automated model routing is critical for managing heterogeneous, production-scale time series datasets where no single model architecture is optimal. Tracking this problem is essential for advancing beyond static heuristic model selection in automated forecasting pipelines.