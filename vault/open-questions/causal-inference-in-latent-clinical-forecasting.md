---
created_at: '2026-05-24T07:48:23Z'
source_papers:
- '[[openalex-2605.21963-chronomedicalworld-a-medical-world-model-for-learning-patien]]'
title: Causal Inference in Clinical Forecasting
---

**Background:** Clinical simulation requires accounting for time-dependent confounding, where both states and intervention choices are influenced by historical patient data. Predictive world models often prioritize accuracy over causal identification, potentially confounding correlation with intervention effect.

**Question / Future Work:** The challenge remains to integrate rigorous causal estimation into latent world model frameworks to ensure that simulated trajectories accurately reflect the effect of interventions rather than observational correlation.

**Why It Matters:** Distinguishing causal impact from correlation is required for any clinical forecasting system intended to guide, rather than merely track, patient outcomes.

**Evidence:** CMWM is not a causal estimator, and comparison with methods that explicitly adjust for time-dependent confounding [5, 27] is left to future work.