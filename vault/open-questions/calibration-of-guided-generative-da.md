---
created_at: '2026-04-26T06:54:46Z'
source_papers:
- '[[openalex-2604.21180-uncertainty-aware-spatiotemporal-super-resolution-data-assim]]'
title: Calibration of Guided Generative DA
---

**Background:** Diffusion models generate posterior samples for data assimilation through a learned conditional score, which can be modified at inference time using observation-consistency guidance to incorporate sensor-layout shifts. This guidance approximates the posterior by augmenting the prior score with a likelihood-based correction derived from a masked residual.

**Question / Future Work:** Improving the calibration of guided diffusion models remains a significant challenge, as the current guidance mechanisms often rely on heuristic or stop-gradient likelihood approximations that may introduce bias or degrade the quality of the ensemble spread compared to retraining. Research is needed to develop schedule-aware guidance, better likelihood models, and more robust uncertainty quantification mechanisms that maintain predictive calibration without sacrificing the deployment-time flexibility offered by training-free guidance.

**Why It Matters:** Uncertainty quantification is central to data assimilation, and if deployment-time guidance destroys the statistical reliability of the ensemble, the method loses its primary scientific value for forecasting. Tracking progress in calibrating guided generative models is essential for reliable probabilistic DA.