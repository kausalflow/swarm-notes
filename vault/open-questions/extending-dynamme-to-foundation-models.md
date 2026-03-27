---
created_at: '2026-03-27T14:09:18Z'
source_papers:
- '[[openalex-2603.09062-dynamic-multi-period-experts-for-online-time-series-forecast]]'
title: Extend DynaME to Foundation Models
---

**Background:** Online Time Series Forecasting (OTSF) requires models to adapt to concept drift, where the underlying data pattern evolves over time. DynaME, a hybrid framework, addresses this by using a committee of specialized experts for recurring patterns and a stable, generalized expert for emergent patterns.

**Question / Future Work:** The paper proposes DynaME to handle both Recurring Drift (reappearing historical patterns) and Emergent Drift (entirely new patterns). The framework is validated on existing benchmark datasets and backbone architectures. Future work could involve extending the DynaME framework to more complex and expressive base models, such as large pre-trained foundation models, to further improve adaptability and generalization across a wider range of real-world time series scenarios.