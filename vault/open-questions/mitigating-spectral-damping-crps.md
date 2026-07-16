---
created_at: '2026-07-16T07:14:27Z'
source_papers:
- '[[openalex-2607.11457-hourglass-a-probabilistic-data-driven-temporal-downscaler-fo]]'
title: Mitigating spectral damping in CRPS
---

**Background:** Probabilistic models trained with the Continuous Ranked Probability Score (CRPS) can exhibit damping at certain spatial scales, impacting physical fidelity.

**Question / Future Work:** Investigate whether multiscale CRPS formulations or other spectral-aware loss adjustments can mitigate the spectral damping artifacts often observed in probabilistic meteorological forecasting.

**Why It Matters:** Spectral fidelity is critical for the physical consistency of weather forecasts, particularly for high-resolution variables like precipitation.

**Evidence:** A possible mitigation would be to adopt the multiscale CRPS formulation proposed by Lang et al. [17]; we leave this investigation to future work.