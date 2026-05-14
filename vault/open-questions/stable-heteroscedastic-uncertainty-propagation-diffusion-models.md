---
created_at: '2026-05-14T07:39:02Z'
source_papers:
- '[[openalex-2605.10717-heteroscedastic-diffusion-for-multi-agent-trajectory-modelin]]'
title: Stable uncertainty propagation in diffusion
---

**Background:** Multi-agent trajectory modeling in complex dynamic environments often uses generative diffusion models to capture stochastic human behaviors. Current frameworks frequently struggle to produce stable, calibrated, heteroscedastic uncertainty estimates that accurately reflect state-wise variance in multi-agent scenarios.

**Question / Future Work:** There is a need for theoretically grounded and computationally efficient methods to propagate heteroscedastic uncertainty from latent generative spaces to real-world state spaces, particularly when avoiding numerical instabilities or high-cost Monte Carlo approximations in complex multi-agent scenes.

**Why It Matters:** Calibrated uncertainty is essential for the reliability of generative models in safety-critical robotics and decision-making applications.

**Evidence:** the full Jacobian can be ill-conditioned or contain large off-diagonal elements, introducing numerical instabilities that result in non-positive-definite covariance estimates.