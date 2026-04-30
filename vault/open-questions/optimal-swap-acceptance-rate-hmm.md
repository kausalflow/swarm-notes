---
created_at: '2026-04-30T07:24:12Z'
source_papers:
- '[[openalex-2604.24587-bayesian-inference-for-hidden-markov-models-under-genuine-mu]]'
title: Optimal swap rate for HMMs
---

**Background:** The parallel tempering algorithm is commonly used for exploring multimodal distributions, but the determination of the optimal swap acceptance rate between tempered replicas in the specific context of hidden Markov models remains an unresolved research problem.

**Question / Future Work:** While an optimal constant swap acceptance rate of 0.234 has been established for parallel tempering under certain regularity conditions, it has not been theoretically verified that this specific rate remains optimal for hidden Markov models, leaving the exact optimal tuning parameter for these models as an open question.

**Why It Matters:** Efficient exploration of multimodal posteriors in HMMs is highly sensitive to the temperature schedule; establishing a theoretically grounded optimal swap rate would improve the consistency and computational efficiency of Bayesian inference for these models.

**Evidence:** While the optimal inverse temperature schedule conveys constant swap acceptance rates, it has not been verified theoretically that 0.234 is the correspond to the value for the optimal solution in the case of hidden Markov models.