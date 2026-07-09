---
created_at: '2026-07-09T08:17:52Z'
source_papers:
- '[[openalex-2607.05291-forecasting-realized-volatility-with-time-series-foundation]]'
title: TSFM vs. Econometric Volatility Forecasting
---

**Background:** Time series foundation models (TSFMs) are typically evaluated in zero-shot settings, where models pretrained on diverse external corpora are applied to new time series without domain-specific fine-tuning. It remains unclear whether these general-purpose architectures can consistently outperform established, task-specific econometric benchmarks in specialized domains like financial realized volatility forecasting.

**Question / Future Work:** Future research is required to evaluate whether zero-shot TSFMs provide a robust informational advantage in volatility dynamics or if performance gains are artifacts of scale/level bias. Furthermore, it is unknown if domain-specific parameter-efficient fine-tuning can consistently bridge the performance gap between these zero-shot models and traditional benchmarks like the Log-HAR model.

**Why It Matters:** Establishing whether the performance edge of TSFMs in finance is a robust informational gain versus a fragile calibration artifact is critical for deciding whether to integrate these models into existing risk management frameworks.