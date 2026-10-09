---
created_at: '2026-10-09T11:34:42Z'
source_papers:
- '[[openalex-2610.08118-attenuated-in-context-identification-in-time-series-foundati]]'
title: Preventing Catastrophic Forgetting in TSFMs
---

**Background:** Fine-tuning time-series foundation models to improve dynamic response and what-if reasoning capabilities frequently causes catastrophic forgetting on general univariate forecasting tasks.

**Question / Future Work:** Investigate and develop effective mitigation strategies for catastrophic forgetting when adapting time-series foundation models to specialised tasks such as system identification or what-if forecasting, ensuring that general univariate forecasting performance is preserved alongside improved dynamic reasoning.

**Evidence:** Replay therefore largely kept the what-if gains but did not prevent forgetting; it made univariate forecasting worse still (one run). Preventing forgetting remains open.