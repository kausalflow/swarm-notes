---
created_at: '2026-10-08T11:41:24Z'
source_papers:
- '[[openalex-2610.06355-latent-similarity-gaussian-processes-a-theory-grounded-appro]]'
title: PAC-Bayes Generalization Bound Model Selection
---

**Background:** Machine learning models for personalized clinical risk forecasting are often evaluated using standard log-likelihood metrics that can fail to prioritize task-specific within-patient dynamic discrimination under severe outcome class imbalance.

**Question / Future Work:** Investigate alternative training objectives and selection criteria that optimize PAC-Bayes generalization bounds rather than relying on marginal likelihoods or standard test log-likelihoods, which fail to properly differentiate uninformative base-rate models from predictive models on sparse longitudinal clinical datasets.

**Why It Matters:** Critical for ensuring that probabilistic models in healthcare are selected based on clinically meaningful metrics rather than uncalibrated marginal likelihoods under extreme class imbalance.

**Evidence:** Because LL fails to differentiate uninformative base-rate models from predictive models on the EMA data, we question its suitability for model selection and its impact on Bayesian inference. In future work, we plan to investigate alternative training objectives and selection criteria that optimize PAC-Bayes generalization bounds rather than relying on marginal likelihoods.