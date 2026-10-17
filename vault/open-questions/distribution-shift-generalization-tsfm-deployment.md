---
created_at: '2026-10-17T08:54:33Z'
source_papers:
- '[[openalex-2610.19725-timersi-towards-self-improved-agentic-deployment-for-time-se]]'
title: Generalization under Distribution Shift
---

**Background:** Time-series forecasting models often experience performance degradation when deployed in real-world environments due to underlying shifts between historical training distributions and future deployment conditions.

**Question / Future Work:** Investigate how performance improvements achieved on historical validation and adaptation windows can be reliably guaranteed to generalize to unseen future deployment contexts under severe distribution shifts.

**Why It Matters:** Addressing distribution shift is critical for ensuring that self-improving agentic deployment pipelines do not overfit to historical backtests and maintain robustness during actual real-world deployment.

**Evidence:** Besides, gains on historical windows do not guarantee gains on future forecasts. This highlights the open problem, i.e., distribution shift, in time-series forecasting.