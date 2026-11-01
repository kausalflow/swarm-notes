---
created_at: '2026-11-01T11:33:04Z'
source_papers:
- '[[openalex-2610.39246-imrouter-imbalance-aware-temporal-pattern-routing-for-llm-ba]]'
title: Temporal Pattern Imbalance in LLMs
---

**Background:** Large language model-based time series forecasting methods optimize an overall forecasting objective while overlooking temporal pattern imbalance, where different temporal patterns occur at highly unequal frequencies.

**Question / Future Work:** Investigate how temporal pattern imbalance affects the generalization and adaptation of large language models across diverse, non-uniformly distributed real-world time series regimes, and develop automated, label-free balancing techniques that do not rely on heuristic cluster boundaries or predefined temporal categories.

**Why It Matters:** Temporal pattern imbalance is a pervasive issue in real-world time series data that severely degrades predictive performance on underrepresented regimes, making robust and label-free balancing mechanisms crucial for reliable deployment in safety-critical web and industrial applications.

**Evidence:** However, existing LLM-based TSF methods largely optimize the overall forecasting objective while overlooking temporal pattern imbalance (TPI), where different temporal patterns occur at highly unequal frequencies.