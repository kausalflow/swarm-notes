---
created_at: '2026-06-17T09:26:05Z'
source_papers:
- '[[openalex-2606.15917-reinforcement-learning-for-llm-based-event-forecasting]]'
title: Scaling Context in Forecasting
---

**Background:** In reinforcement learning for LLM-based forecasting, the use of limited or noisy context often acts as a performance ceiling for scaling improvements.

**Question / Future Work:** There is a need to determine the optimal relationship between model parameter count, context length, and forecasting accuracy, particularly when models are constrained by the quality or volume of retrieved information.

**Why It Matters:** Identifying whether predictive performance is constrained by model scale versus information density is critical for optimizing future LLM-based forecasting systems.

**Evidence:** The lack of a scaling effect for the small context regime seems to imply that when the model is presented with limited information, the information available acts as a bottleneck on performance.