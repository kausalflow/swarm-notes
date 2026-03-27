---
created_at: '2026-03-27T14:09:37Z'
source_papers:
- '[[openalex-2603.00636-retrodictive-forecasting-a-proof-of-concept-for-exploiting-t]]'
title: Decoder Likelihood Fidelity
---

**Background:** Assumptions made about the underlying data distribution affect model fidelity, particularly when the assumptions do not align with complex, real-world data generating processes.

**Question / Future Work:** The current decoder implementation assumes a diagonal Gaussian likelihood for past reconstruction pθ(𝒙|𝒚,𝒛), which imposes homogeneous reconstruction weights across all timesteps. This limitation is shown to cause decoupling between the retrodictive objective (RetroNLL) and predictive accuracy (RMSE) on certain geophysical datasets, suggesting that alternative likelihood models are needed.