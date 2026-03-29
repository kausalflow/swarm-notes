---
created_at: '2026-03-29T06:09:13Z'
source_papers:
- '[[openalex-2603.25670-uncertainty-guided-label-rebalancing-for-cps-safety-monitori]]'
title: Investigate alternative uncertainty estimation
---

**Background:** The effectiveness of the uncertainty-guided label rebalancing mechanism depends on the quality and nature of the uncertainty estimates provided by the initial predictor model.

**Question / Future Work:** Investigate how different uncertainty estimation techniques, such as Monte Carlo Dropout (MC Dropout) or Deep Ensembles, influence the performance and effectiveness of the uncertainty-guided label rebalancing (uLNR) mechanism in safety prediction.

**Why It Matters:** Understanding the relationship between the fidelity of uncertainty estimation methods (like MC Dropout or Deep Ensembles) and the resulting data rebalancing effectiveness is important for optimizing the overall system pipeline, especially since the core contribution relies on high-quality uncertainty scores.

**Evidence:** We also plan to investigate alternative uncertainty estimation techniques, such as MC Dropout and Deep Ensembles, to better understand how the accuracy of the uncertainty estimates influences the effectiveness of rebalancing.