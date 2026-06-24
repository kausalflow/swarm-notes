---
created_at: '2026-06-24T08:17:33Z'
source_papers:
- '[[openalex-2509.21711-multi-modal-bayesian-neural-network-surrogates-with-conjugat]]'
title: Multi-modal Bayesian Optimization Framework
---

**Background:** Multi-modal surrogate models leverage multiple data sources to predict a quantity of interest, but selecting optimal acquisition policies in a Bayesian Optimization loop when modalities have complex, non-linear dependencies remains a challenge.

**Question / Future Work:** Developing a multi-modal acquisition framework to guide the sequential selection of input locations and specific modalities to sample is identified as a necessary future extension to complete the Bayesian Optimization procedure. This framework must handle the non-linear, complex relationships between data modalities learned by Bayesian Neural Network surrogates and accommodate high-dimensional modalities.

**Why It Matters:** The effectiveness of surrogate models in Bayesian Optimization is fundamentally tied to their ability to guide sampling; without a corresponding acquisition function, the surrogate models are limited in their practical utility for optimization tasks.

**Evidence:** A multi-modal acquisition framework to complete the BO procedure using these multi-modal surrogate models is future work.