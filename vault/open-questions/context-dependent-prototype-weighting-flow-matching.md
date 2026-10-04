---
created_at: '2026-10-04T10:48:01Z'
source_papers:
- '[[openalex-2610.01320-protoflow-prototype-guided-flow-matching-for-multivariate-ti]]'
title: Context-Dependent Prototype Prior Adaptation
---

**Background:** Prototype-prior flow matching frameworks for multivariate time series forecasting use static global training statistics to construct source priors for latent generation.

**Question / Future Work:** Develop context-dependent prototype weighting mechanisms for prototype-prior flow matching frameworks, enabling the initialization source distribution to dynamically adapt to individual historical forecasting contexts while preserving the computational efficiency of few-step ODE sampling.

**Why It Matters:** Addressing static prior initialization can bridge the gap between global codebook representations and localized temporal uncertainties, potentially improving probabilistic forecasting quality across diverse and non-stationary regimes.

**Evidence:** Although the learned transport is conditioned on historical observations, the source prior does not adapt its probability allocation to individual forecasting contexts. A promising direction is to develop context-dependent prototype weighting, allowing initialization to reflect the current temporal regime while retaining the efficiency of few-step generation. We leave this direction for our future work.