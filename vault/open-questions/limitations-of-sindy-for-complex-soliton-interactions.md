---
created_at: '2026-07-04T07:37:18Z'
source_papers:
- '[[openalex-2510.13566-data-driven-soliton-manifold-approximations-for-dark-and-bri]]'
title: SINDy for Complex Soliton Interactions
---

**Background:** Sparse identification of nonlinear dynamics (SINDy) is a data-driven method for discovering governing ordinary differential equations from time-series data. Current applications of this method to complex multi-degree-of-freedom systems, such as interacting solitons, often encounter significant deviations from analytical models.

**Question / Future Work:** Identifying high-dimensional dynamical models for complex interactions, specifically accounting for higher-order effects, phase dynamics, and force reciprocity between solitons, remains a challenge for SINDy. Future work is required to develop tools that integrate physical constraints directly into the regression framework to ensure fidelity to the underlying manifold dynamics.

**Why It Matters:** Addresses the fundamental limitations of using sparse regression for discovering governing physics in complex, high-dimensional nonlinear wave systems.

**Evidence:** It is worthwhile to note that unfortunately, in this more complex, multi-degree case example, SINDy fails to yield a prediction which closely aligns with the corresponding approximated dynamics... The incorporation of physical attributes of the dynamics (such as the potential force reciprocity etc.) may enable further refinement of the dynamics identified.