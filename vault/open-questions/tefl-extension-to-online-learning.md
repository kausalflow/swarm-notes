---
created_at: '2026-03-27T14:09:15Z'
source_papers:
- '[[openalex-2602.22520-tefl-prediction-residual-guided-rolling-forecasting-for-mult]]'
title: Extending Feedback to Online Learning
---

**Background:** Deep forecasting models are often optimized using standard batch training on sampled segments, creating a mismatch with real-world deployment where forecasts are made sequentially in a rolling manner, generating a stream of past prediction residuals.

**Question / Future Work:** The paper identifies the need to extend the error feedback mechanism to true online learning scenarios, where model parameters might be updated sequentially as new residuals become available, in contrast to the proposed fixed-model, batch-trained framework.