---
created_at: '2026-03-27T15:44:13Z'
source_papers:
- '[[openalex-2603.22655-generalizing-dynamics-modeling-more-easily-from-representati]]'
title: Optimizing PDE-DER Pre-training Objectives
---

**Background:** The pre-training process for the generalized Pre-trained Dynamics EncoDER (PDE-DER) involves minimizing a combination of Lyapunov exponent, reconstruction, and forecasting objectives. The authors note that without the Lyapunov objective, performance suffers in some cases, but its absence surprisingly led to better short-term forecasting for specific systems (2D-CFD and Gene).

**Question / Future Work:** Explore how to optimally balance the three pre-training objectives (Lyapunov minimization, reconstruction, and forecasting) to achieve the best generalization and forecasting performance across all dynamic systems. Specifically, a systematic investigation is needed into when and why minimizing chaos (Lyapunov objective) might hinder short-term forecasting accuracy for certain dynamics, and how to adjust the weighting parameters ($\\rho_1, \\rho_2$) or the MLE objective itself to optimize the representation quality for all forecasting horizons and domains.

**Why It Matters:** The interplay between learning stable latent dynamics (via MLE) and preserving fine-grained local information (via reconstruction/forecasting) is a key architectural tuning problem for representation-based dynamics modeling.

**Evidence:** We also find that the ablative version pre-training without Lyapunov objective outperforms other settings in some of the short-term forecasting settings on 2D-CFD and Gene. These phenomena may indicate that reducing the chaos from embedded observations when pre-training are more likely to benefit long-term forecasting to some extent.