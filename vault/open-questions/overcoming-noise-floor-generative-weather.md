---
created_at: '2026-10-08T11:41:15Z'
source_papers:
- '[[openalex-2610.06509-xaurora-generative-weather-forecasting-with-denoising-stocha]]'
title: Overcoming Noise Floor in Generative Weather Forecasting
---

**Background:** Data-driven and deep learning-based weather forecasting models frequently exhibit a persistent high-frequency spectral deficit, termed the noise floor, which limits their spectral calibration and realism at fine spatial scales.

**Question / Future Work:** Investigate and overcome the persistent noise floor observed in spectral calibration analyses, which limits the high-frequency realism and power spectral density of generative weather forecasting models across varying lead times and network architectures.

**Why It Matters:** The noise floor is a fundamental limitation shared across modern data-driven and generative weather forecasting models, affecting how well small-scale atmospheric turbulence and mesoscale dynamics are represented in ensemble predictions.

**Evidence:** Though high frequencies are less important than large scales for operational weather forecasting, the persistent noise floor highlighted by our analysis is the main limitation of Xaurora. We identified the major influence of the noise model on the spectral properties of the forecasts, which inference-only interventions can only partially calibrate. Further research can focus on building random fields that are better suited to the spectral properties of the task.