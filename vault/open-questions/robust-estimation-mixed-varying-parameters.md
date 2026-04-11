---
created_at: '2026-04-11T05:55:57Z'
source_papers:
- '[[openalex-2412.16198-estimating-varying-parameters-in-dynamical-systems-a-modular]]'
title: Robust Estimation of Mixed-Varying Parameters
---

**Background:** Parameter-varying systems can exhibit parameters that evolve continuously over time or undergo discrete switches. The identification of both the switch locations and the functional forms of these varying parameters from noisy observed data remains a significant computational and theoretical challenge.

**Question / Future Work:** Future work is required to develop frameworks that simultaneously estimate discrete switch locations and continuously varying parameters within the same dynamical system. Current limitations include cascading error propagation between switch detection and parameter regression, as well as the non-convexity of the underlying optimization problems. Improving robustness to measurement noise and developing globally optimal, computationally efficient algorithms for these mixed-dynamics systems are critical open research areas.

**Why It Matters:** This problem is fundamental to modeling and control of complex real-world dynamical systems (e.g., biological or physical processes), which rarely follow static parameter assumptions.

**Evidence:** Working with parameters that are combinations of both discretely switching and continuously varying is successful up to the following extent: we can approximate these parameters/inputs reasonably well by sufficiently segmenting the data, but we cannot estimate the switch locations during this process.