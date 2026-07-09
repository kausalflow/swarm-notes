---
created_at: '2026-07-09T08:17:59Z'
source_papers:
- '[[openalex-2607.04919-when-do-foundation-models-pay-off-a-break-even-analysis-of-p]]'
title: Predicting Time Series Break-Even Thresholds
---

**Background:** The effectiveness of time series foundation models varies significantly based on dataset characteristics, making the decision between foundation models and classical baselines a complex optimization problem.

**Question / Future Work:** Reliable automated prediction of break-even points—the data volume or regime at which classical forecasting methods outperform foundation models—remains an open research challenge. Scaling this analysis to larger, more diverse datasets is necessary to establish robust, generalized heuristics for model selection beyond existing benchmark observations.

**Why It Matters:** Establishing reliable predictive tools for model selection is critical for practitioners to avoid inefficient infrastructure deployment, such as the unnecessary use of GPU-intensive foundation models when classical methods would suffice.

**Evidence:** Four dataset features motivate mechanistic hypotheses for the remaining cases, though reliable automated prediction at this benchmark scale remains an open problem.