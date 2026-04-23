---
created_at: '2026-04-23T06:55:10Z'
source_papers:
- '[[openalex-2604.17998-causally-constrained-probabilistic-forecasting-for-time-seri]]'
title: Joint Causal Discovery and Detection
---

**Background:** Anomaly detection systems often utilize causal graph priors learned from historical data to interpret multivariate dependencies. These systems frequently fail to account for errors in the learned graph structure, such as those caused by noise, latent confounders, or non-stationary system dynamics.

**Question / Future Work:** There is an unresolved challenge in developing methods that jointly learn causal structures and anomaly detection models, rather than relying on sequential estimation. Further research is required to enable online adaptive updates of the causal structure to account for non-stationarity and structural drift during deployment.

**Why It Matters:** Addressing this bottleneck is critical for deploying causal anomaly detection in dynamic, real-world industrial environments where static causal priors quickly become obsolete or inaccurate.