---
created_at: '2026-06-26T08:25:22Z'
source_papers:
- '[[openalex-2606.24604-uncertainty-aware-longitudinal-forecasting-of-alzheimers-dis]]'
title: Mitigating Time-to-Conversion Bias
---

**Background:** Alzheimer’s disease progression modelling often suffers from recruitment bias and an over-representation of specific disease stages in datasets, leading to potential biases in predictive models.

**Question / Future Work:** Investigate techniques to mitigate time-to-conversion bias introduced by sliding-window sequence construction, such as temporal-position weighting or patient-level reweighting to ensure training data reflects the full longitudinal timeline.

**Why It Matters:** Addressing this bias is critical for the clinical reliability of longitudinal models, preventing overestimation of disease progression speeds.

**Evidence:** This discrepancy suggests that the generator may overestimate the speed of conversion for some MCI patients. The most likely explanation is a selection bias introduced by the sliding-window construction of training sequences.