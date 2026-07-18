---
created_at: '2026-07-18T06:52:13Z'
source_papers:
- '[[openalex-2607.13651-from-surface-forecasting-to-observability-forecasting-a-late]]'
title: OOD robustness for EO observability
---

**Background:** Observability forecasting, defined as predicting the usability of future Earth Observation data under cloud cover, remains significantly affected by distribution shifts in operational environments.

**Question / Future Work:** The performance of latent world models for observability forecasting currently degrades under Out-of-Distribution (OOD) conditions, indicating a lack of robustness in handling diverse geographic, seasonal, and weather regimes. Future research is required to improve generalization capabilities and develop techniques that maintain predictive accuracy when data distributions shift.

**Why It Matters:** Robustness to distribution shift is critical for the practical, reliable deployment of Earth Observation observability models in real-world, global monitoring systems.

**Evidence:** OOD is the one split where LeWM falls behind more consistently. The latent distribution itself shifts away from the train-like regime.