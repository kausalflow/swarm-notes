---
created_at: '2026-03-27T14:08:58Z'
source_papers:
- '[[openalex-2603.15452-unlocking-the-value-of-text-event-driven-reasoning-and-multi]]'
title: HIC Robustness to Extreme Text Noise
---

**Background:** While current methods utilize LLMs for feature extraction or reasoning in time series forecasting, challenges remain in fully unlocking the textual context available for prediction.

**Question / Future Work:** Investigating the scalability and robustness of the Historical In-Context Learning (HIC) mechanism in scenarios with extremely sparse or highly noisy exogenous text data remains an open question, as current tests only cover moderate degradation (10-20% masking/noise). Further work should explore the limits where performance decline becomes significant and develop mitigation strategies beyond simple quality flagging.