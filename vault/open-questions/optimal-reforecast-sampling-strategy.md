---
created_at: '2026-10-03T10:09:35Z'
source_papers:
- '[[openalex-2609.40133-regraf-a-global-mpas-reforecast-data-set-with-convection-all]]'
title: Optimal Reforecast Sampling Strategy
---

**Background:** Deep-learning numerical weather prediction models are increasingly trained on convection-permitting datasets, but the scarcity of high-resolution training data at these scales remains a major constraint.

**Question / Future Work:** Investigate how different initial condition sampling strategies (such as targeted high-impact weather sampling versus regular continuous reforecast sampling) impact the generalization capability and skill of deep-learning weather prediction models trained on convection-permitting data.

**Why It Matters:** Determining the optimal reforecast sampling strategy is critical for balancing computational constraints with the training efficiency and generalization of AI weather models.

**Evidence:** This strategy, we hope, will allow us to train deep learning models focused on precipitation and achieve acceptable accuracy with a smaller number of cases than might be necessary with a regular sampling strategy.