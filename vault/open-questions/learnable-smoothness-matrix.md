---
created_at: '2026-05-07T07:38:11Z'
source_papers:
- '[[openalex-2605.02675-online-generalised-predictive-coding]]'
title: Learnable Smoothness Matrix
---

**Background:** Generalised predictive coding frameworks rely on a smoothness matrix to quantify the relationships between derivatives of noise processes in a state-space model, which is typically a fixed hyperparameter defining prior expectations about the smoothness of latent dynamics.

**Question / Future Work:** Developing a method to treat the smoothness matrix as a learnable parameter, rather than a fixed hyperparameter, is essential for improving model flexibility. This requires establishing how to incorporate the smoothness matrix elements into the variational update scheme for precision hyperparameters to allow the model to adaptively infer the smoothness of the underlying random fluctuations.

**Why It Matters:** Learning the smoothness matrix enables the model to automatically adapt to the temporal correlation properties of noise in the generative process, rather than relying on prior manual configuration.

**Evidence:** We will explore the effect of parametrising this matrix and making its elements learnable, which will directly influence the generalised precision terms Πx~ and Πy~.